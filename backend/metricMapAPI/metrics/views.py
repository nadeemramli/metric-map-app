# views.py
from django.db import models
from django_tenants.utils import tenant_context
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import NotFound
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from celery.result import AsyncResult
from django.shortcuts import render

from .models import (
    Metric, HistoricalData, Connection, ActionRemark, Target, Report,
    Dashboard, Experiment, Project, Client, Category, Tag, Forecast, Anomaly, Trend
)
from .serializers import (
    MetricSerializer, HistoricalDataSerializer, ConnectionSerializer,
    ActionRemarkSerializer, TargetSerializer, ReportSerializer,
    DashboardSerializer, ExperimentSerializer, ProjectSerializer,
    ClientSerializer, CategorySerializer, TagSerializer, ForecastSerializer,
    TrendSerializer, AnomalySerializer
)
from .computations import (
    TimeSeriesManager, ExperimentManager, ImpactAnalyzer,
    RelationshipAnalyzer, StatisticsAnalyzer, DashboardManager,
    DataPreprocessor, DataManager
)

import logging

logger = logging.getLogger(__name__)

def public_home(request):
    return render(request, 'home.html')

class CustomTokenObtainPairView(TokenObtainPairView):
    pass

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class TenantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(tenant=self.request.tenant)

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.tenant)

class ClientViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def get_queryset(self):
        # Add logging
        print(f"User {self.request.user} is fetching clients")
        queryset = Client.objects.all()
        print(f"Found {queryset.count()} clients")
        return queryset

class ProjectViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    basename='client-projects'
    
    def get_queryset(self):
        return Project.objects.filter(tenant=self.request.tenant)

class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    basename = 'project-metrics'

    def get_queryset(self):
        return super().get_queryset().select_related('category').prefetch_related('tags')

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.tenant)

    def perform_update(self, serializer):
        instance = serializer.instance
        new_type = serializer.validated_data.get('type')
        
        if new_type and new_type != instance.type:
            if new_type == Metric.Type.KPI:
                # Perform actions specific to changing to KPI type
                pass
            elif new_type == Metric.Type.NORTH_STAR:
                # Perform actions specific to changing to North Star type
                pass
            # Add more conditions for other types as needed

        serializer.save()

    @action(detail=True, methods=['get'])
    @method_decorator(cache_page(60*60))
    def historical_data(self, request, pk=None):
        metric = self.get_object()
        queryset = HistoricalData.objects.filter(metric=metric, tenant=self.request.tenant).order_by('date')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = HistoricalDataSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = HistoricalDataSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def add_tag(self, request, pk=None):
        metric = self.get_object()
        tag_id = request.data.get('tag_id')
        if not tag_id:
            return Response({"error": "tag_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            tag = Tag.objects.get(id=tag_id, tenant=request.tenant)
            metric.tags.add(tag)
            return Response({"message": "Tag added successfully"}, status=status.HTTP_200_OK)
        except Tag.DoesNotExist:
            return Response({"error": "Tag not found"}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['post'])
    def analyze(self, request, pk=None):
        metric = self.get_object()
        analysis_type = request.data.get('analysis_type')
        params = request.data.get('params', {})

        if analysis_type in ['forecasting', 'performance', 'experiment', 'impact', 'relationship', 'statistics']:
            task = self.run_analysis_task(metric.id, analysis_type, params)
            return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': 'Invalid analysis type'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def analysis_result(self, request, pk=None):
        task_id = request.query_params.get('task_id')
        if not task_id:
            return Response({'error': 'task_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        task = AsyncResult(task_id)
        if task.ready():
            return Response(task.result)
        else:
            return Response({'status': 'pending'}, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=['post'])
    def preprocess(self, request, pk=None):
        metric = self.get_object()
        process_type = request.data.get('process_type')
        params = request.data.get('params', {})

        with tenant_context(self.request.tenant):
            task = DataPreprocessor.run_process.delay(metric.id, process_type, **params)
        return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=['post'])
    def manage_data(self, request, pk=None):
        metric = self.get_object()
        operation_type = request.data.get('operation_type')
        params = request.data.get('params', {})

        with tenant_context(self.request.tenant):
            task = DataManager.run_operation.delay(metric.id, operation_type, **params)
        return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=['get'])
    def connections(self, request, pk=None):
        metric = self.get_object()
        connections = Connection.objects.filter(
            (models.Q(from_metric=metric) | models.Q(to_metric=metric)) &
            models.Q(tenant=self.request.tenant)
        )
        serializer = ConnectionSerializer(connections, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get', 'post'])
    def action_remarks(self, request, pk=None):
        metric = self.get_object()
        if request.method == 'GET':
            remarks = ActionRemark.objects.filter(metric=metric, tenant=self.request.tenant).order_by('date')
            serializer = ActionRemarkSerializer(remarks, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = ActionRemarkSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(metric=metric, tenant=self.request.tenant)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def targets(self, request, pk=None):
        metric = self.get_object()
        targets = Target.objects.filter(metric=metric, tenant=self.request.tenant).order_by('-target_date')
        serializer = TargetSerializer(targets, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def reports(self, request, pk=None):
        metric = self.get_object()
        reports = Report.objects.filter(metrics=metric, tenant=self.request.tenant)
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def feedback(self, request, pk=None):
        metric = self.get_object()
        feedback_data = request.data
        
        with tenant_context(self.request.tenant):
            task = DashboardManager.run_analysis.delay('generate_suggestions', {'metric_id': metric.id, 'feedback': feedback_data})
        return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=['get'])
    def visualization(self, request, pk=None):
        metric = self.get_object()
        with tenant_context(self.request.tenant):
            task = DashboardManager.run_analysis.delay('generate_visualization', {'metric_id': metric.id})
        return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=['get'])
    def progress_tracking(self, request, pk=None):
        metric = self.get_object()
        with tenant_context(self.request.tenant):
            task = DashboardManager.run_analysis.delay('track_progress', {'metric_id': metric.id})
        return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)
    
    @action(detail=True, methods=['patch'])
    def update_position(self, request, pk=None):
        metric = self.get_object()
        x = request.data.get('x')
        y = request.data.get('y')
        
        if x is not None and y is not None:
            metric.set_position(x, y)
            return Response({'status': 'position updated'})
        return Response({'status': 'failed', 'message': 'Invalid position data'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def change_rhythm(self, request, pk=None):
        metric = self.get_object()
        new_rhythm = request.data.get('rhythm')
        
        if new_rhythm not in Metric.Rhythm.values:
            return Response({'error': 'Invalid rhythm value'}, status=status.HTTP_400_BAD_REQUEST)
        
        metric.rhythm = new_rhythm
        metric.save()
        
        # Perform any additional actions based on rhythm change
        if new_rhythm == Metric.Rhythm.DAILY:
            # Handle daily rhythm specifics
            pass
        elif new_rhythm == Metric.Rhythm.WEEKLY:
            # Handle weekly rhythm specifics
            pass
        # Add more conditions for other rhythms as needed
        
        return Response({'status': 'rhythm updated'})

    def run_analysis_task(self, metric_id, analysis_type, params):
        metric = Metric.objects.get(id=metric_id)
        
        if metric.type == Metric.Type.KPI:
            # Specific analysis for KPI metrics
            pass
        elif metric.type == Metric.Type.NORTH_STAR:
            # Specific analysis for North Star metrics
            pass
        
        with tenant_context(self.request.tenant):
            if analysis_type in ['trend', 'anomaly', 'correlation', 'probability']:
                return StatisticsAnalyzer.run_analysis.delay(metric_id, analysis_type, **params)
            elif analysis_type in ['forecasting', 'comparative', 'forecast_vs_actual', 'scenario_modeling', 'predictive_goal', 'daily_forecast']:
                return TimeSeriesManager.run_analysis.delay(metric_id, analysis_type, **params)
            elif analysis_type == 'performance':
                return ImpactAnalyzer.run_analysis.delay(metric_id, params.get('performance_type'), **params)
            elif analysis_type == 'experiment':
                return ExperimentManager.run_analysis.delay(metric_id, params.get('experiment_type'), **params)
            elif analysis_type == 'impact':
                return ImpactAnalyzer.run_analysis.delay(metric_id, params.get('impact_type'), **params)
            elif analysis_type == 'relationship':
                return RelationshipAnalyzer.run_analysis.delay(metric_id, params.get('relationship_type'), **params)

class HistoricalDataViewSet(TenantViewSet):
    queryset = HistoricalData.objects.all()
    serializer_class = HistoricalDataSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    basename = 'metric-historical-data'

    def get_queryset(self):
        return super().get_queryset().select_related('metric')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            metric = Metric.objects.get(
                tenant=self.request.tenant,
                id=self.kwargs['metric_pk']
            )
        except Metric.DoesNotExist:
            raise NotFound('Metric not found')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(metric=metric, tenant=self.request.tenant)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def bulk_import(self, request):
        try:
            metric = Metric.objects.get(
                metric__tenant=self.request.tenant,
                metric_id=self.kwargs['metric_pk']
            )
        except Metric.DoesNotExist:
            raise NotFound('Metric not found')

        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer, metric)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_bulk_create(self, serializer, metric):
        HistoricalData.objects.bulk_create([
            HistoricalData(metric=metric, **item) for item in serializer.validated_data
        ])

    @action(detail=False, methods=['get'])
    def aggregated_views(self, request):
        historical_data = self.get_queryset().order_by('date').values('date', 'value')
        
        with tenant_context(self.request.tenant):
            task = StatisticsAnalyzer.run_analysis.delay(
                self.kwargs['metric_pk'], 'aggregated_views', {'historical_data': list(historical_data)}
            )
        return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['get'])
    def advanced_statistics(self, request):
        historical_data = self.get_queryset().order_by('date').values('date', 'value')
        
        with tenant_context(self.request.tenant):
            task = StatisticsAnalyzer.run_analysis.delay(
                self.kwargs['metric_pk'], 'advanced_statistics', {'historical_data': list(historical_data)}
            )
        return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)

class DashboardViewSet(TenantViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = [IsAuthenticated]
    basename='project-dashboards'

    def get_queryset(self):
        return Dashboard.objects.filter(tenant=self.request.tenant)

    @action(detail=False, methods=['get'])
    def performance(self, request):
        with tenant_context(self.request.tenant):
            task = DashboardManager.run_analysis.delay('performance_dashboard', {})
        return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['get'])
    def decision_support(self, request):
        with tenant_context(self.request.tenant):
            task = DashboardManager.run_analysis.delay('decision_support_dashboard', {})
        return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)

class ExperimentViewSet(TenantViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    permission_classes = [IsAuthenticated]
    basename='project-experiments'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('metrics')

    @action(detail=True, methods=['post'])
    def run_experiment(self, request):
        experiment = self.get_object()
        experiment_type = request.data.get('experiment_type')
        params = request.data.get('params', {})

        with tenant_context(self.request.tenant):
            task = ExperimentManager.run_analysis.delay(experiment.id, experiment_type, **params)
        return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)

class CategoryViewSet(TenantViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    basename='project-categories'

    def get_queryset(self):
        return Category.objects.filter(tenant=self.request.tenant)

class TagViewSet(TenantViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    basename='project-tags'

    def get_queryset(self):
        return Tag.objects.filter(tenant=self.request.tenant)

class ConnectionViewSet(TenantViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    permission_classes = [IsAuthenticated]
    basename='project-connections'

    def get_queryset(self):
        return super().get_queryset().select_related('cause', 'effect')

class ActionRemarkViewSet(TenantViewSet):
    queryset = ActionRemark.objects.all()
    serializer_class = ActionRemarkSerializer
    permission_classes = [IsAuthenticated]
    basename='metric-action-remarks'

    def get_queryset(self):
        return ActionRemark.objects.filter(tenant=self.request.tenant)

    def perform_create(self, serializer):
        metric_id = self.kwargs.get('metric_pk')
        metric = Metric.objects.get(id=metric_id, tenant=self.request.tenant)
        serializer.save(metric=metric, tenant=self.request.tenant)

    def list(self, request, *args, **kwargs):
        metric_id = self.kwargs.get('metric_pk')
        queryset = self.get_queryset().filter(metric_id=metric_id).order_by('date')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Update and Delete methods are already handled by ModelViewSet

class TargetViewSet(TenantViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    permission_classes = [IsAuthenticated]
    basename='project-targets'

    def get_queryset(self):
        return Target.objects.filter(tenant=self.request.tenant)

class ReportViewSet(TenantViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    basename='project-reports'

    def get_queryset(self):
        return Report.objects.filter(tenant=self.request.tenant)

class ForecastViewSet(TenantViewSet):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    basename='metric-forecast'

    def get_queryset(self):
        return super().get_queryset().select_related('metric')

class AnomalyViewSet(TenantViewSet):
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer
    basename='metric-anomaly'

    def get_queryset(self):
        return super().get_queryset().select_related('metric')

class TrendViewSet(TenantViewSet):
    queryset = Trend.objects.all()
    serializer_class = TrendSerializer
    basename='metric-trend'

    def get_queryset(self):
        return super().get_queryset().select_related('metric')