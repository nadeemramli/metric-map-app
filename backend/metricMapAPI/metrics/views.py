
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, throttle_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db import models, transaction
from django_tenants.utils import tenant_context
from rest_framework.exceptions import NotFound, ValidationError
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from celery.result import AsyncResult
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Client, Domain, CustomUser, UserProfile, Team, Project, Category, Tag, Metric,
    MetricMetadata, MetricTarget, Correlation, Connection, HistoricalData,
    Experiment, Forecast, Anomaly, Trend, Dashboard, Report, ActionRemark,
    Strategy, TacticalSolution, DataQualityScore, TimeDimension, ComputationStatus, Notification, PendingComputation
)
from .serializers import (
    ClientSerializer, DomainSerializer, CustomUserSerializer, UserProfileSerializer,
    TeamSerializer, ProjectSerializer, CategorySerializer, TagSerializer, MetricSerializer,
    MetricMetadataSerializer, MetricTargetSerializer, CorrelationSerializer,
    ConnectionSerializer, HistoricalDataSerializer, ExperimentSerializer,
    ForecastSerializer, AnomalySerializer, TrendSerializer, DashboardSerializer,
    ReportSerializer, ActionRemarkSerializer, StrategySerializer,
    TacticalSolutionSerializer, DataQualityScoreSerializer, TimeDimensionSerializer,
    TenantCreationSerializer, ProjectCreationSerializer, TeamCreationSerializer, TeamMemberAssignmentSerializer
)
from .tasks import run_computations
from .throttles import ComputationTriggerThrottle
from .interim.dashboard_computations import generate_automated_suggestions, performance_dashboard
from .interim.performance_analysis import forecast_vs_actual_comparison, probability_analysis, process_progress_tracking
from .interim.statistical_analysis import calculate_advanced_stats, calculate_aggregated_views, calculate_basic_stats
from .interim.experiment_analysis import ab_test_analysis, difference_in_differences
from .interim.data_export import bulk_export_data, prepare_data_for_bulk_import
from .tasks import run_long_computation

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
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return self.queryset.filter(tenant=self.request.tenant)

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.tenant)

class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        # Add logging
        print(f"User {self.request.user} is fetching clients")
        queryset = Client.objects.all()
        print(f"Found {queryset.count()} clients")
        return queryset

class DomainViewSet(TenantViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    filterset_fields = ['domain', 'is_primary']

class CustomUserViewSet(TenantViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filterset_fields = ['username', 'email', 'team']

class UserProfileViewSet(TenantViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filterset_fields = ['user']

class TeamViewSet(TenantViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_fields = ['name']

class ProjectViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    basename='client-projects'
    filterset_fields = ['name']

    def get_queryset(self):
        return Project.objects.filter(tenant=self.request.tenant)

class CategoryViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name']
    basename='project-categories'

    def get_queryset(self):
        return Category.objects.filter(tenant=self.request.tenant)

class TagViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filterset_fields = ['name', 'project']
    basename='project-tags'
    
    def get_queryset(self):
        return Tag.objects.filter(tenant=self.request.tenant)

class MetricViewSet(TenantViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    filterset_fields = ['name', 'type', 'value_type', 'rhythm', 'category', 'tags']

    @action(detail=True, methods=['post'])
    def set_position(self, request, pk=None):
        metric = self.get_object()
        x = request.data.get('x')
        y = request.data.get('y')
        if x is not None and y is not None:
            metric.set_position(x, y)
            return Response({'status': 'position updated'})
        return Response({'error': 'Invalid position data'}, status=status.HTTP_400_BAD_REQUEST)

class MetricMetadataViewSet(TenantViewSet):
    queryset = MetricMetadata.objects.all()
    serializer_class = MetricMetadataSerializer
    filterset_fields = ['metric', 'rhythm', 'team']

'''
class MetricViewSet(viewsets.ModelViewSet):
    serializer_class = MetricSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    basename = 'project-metrics'

    def get_queryset(self):
        client_pk = self.kwargs.get('client_pk')
        project_pk = self.kwargs.get('project_pk')
        logger.info(f"Fetching metrics for client {client_pk} and project {project_pk}")
        
        queryset = Metric.objects.filter(
            tenant_id=client_pk,
            project_id=project_pk
        ).select_related('category', 'project').prefetch_related('tags')
        
        logger.info(f"Found {queryset.count()} metrics")
        print(f"Query: {queryset.query}")  # This will print the SQL query
        print(f"Count: {queryset.count()}")
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            logger.info(f"Serialized {len(serializer.data)} metrics")
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        logger.info(f"Serialized {len(serializer.data)} metrics (unpaginated)")
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        logger.info(f"Retrieving metric. kwargs: {kwargs}")
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        logger.info(f"Creating metric. Data: {request.data}")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        logger.info(f"Updating metric. Data: {request.data}, kwargs: {kwargs}")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        logger.info(f"Deleting metric. kwargs: {kwargs}")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        client_pk = self.kwargs.get('client_pk')
        project_pk = self.kwargs.get('project_pk')
        project = Project.objects.get(tenant_id=client_pk, id=project_pk)
        logger.info(f"Creating new metric for project {project_pk}")
        serializer.save(tenant_id=client_pk, project=project)

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
    def connections(self, request, pk=None, client_pk=None, project_pk=None):
        try:
            metric = self.get_object()
            connections = Connection.objects.filter(
                (models.Q(from_metric=metric) | models.Q(to_metric=metric)) &
                models.Q(from_metric__project__tenant_id=client_pk, from_metric__project_id=project_pk)
            )
            serializer = ConnectionSerializer(connections, many=True)
            logger.info(f"Retrieved {connections.count()} connections for metric {pk}")
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error retrieving connections for metric {pk}: {str(e)}")
            return Response({"error": "An error occurred while retrieving connections"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'client_pk': self.kwargs.get('client_pk'),
            'project_pk': self.kwargs.get('project_pk'),
        })
        return context

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
'''

class MetricTargetViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MetricTarget.objects.all()
    serializer_class = MetricTargetSerializer
    filterset_fields = ['metric', 'target_date']
    basename='project-targets'

    def get_queryset(self):
        return MetricTarget.objects.filter(tenant=self.request.tenant)

class CorrelationViewSet(TenantViewSet):
    queryset = Correlation.objects.all()
    serializer_class = CorrelationSerializer
    filterset_fields = ['metric1', 'metric2']

class ConnectionViewSet(TenantViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    filterset_fields = ['from_metric', 'to_metric']
    basename = 'metric-connections'

    def get_queryset(self):
        return Connection.objects.filter(tenant=self.request.tenant)

'''
    def get_queryset(self):
        client_pk = self.kwargs.get('client_pk')
        project_pk = self.kwargs.get('project_pk')
        metric_pk = self.kwargs.get('metric_pk')
        
        logger.info(f"Attempting to fetch connections. kwargs: {self.kwargs}")
        
        if not all([client_pk, project_pk, metric_pk]):
            logger.error(f"Missing parameters in URL. client_pk: {client_pk}, project_pk: {project_pk}, metric_pk: {metric_pk}")
            raise ValidationError("Missing parameters in URL")

        queryset = Connection.objects.filter(
            models.Q(from_metric_id=metric_pk) | models.Q(to_metric_id=metric_pk),
            from_metric__project_id=project_pk,
            from_metric__tenant_id=client_pk
        ).select_related('from_metric', 'to_metric')

        logger.info(f"Queryset count: {queryset.count()}")
        return queryset

    def perform_create(self, serializer):
        client_pk = self.kwargs.get('client_pk')
        project_pk = self.kwargs.get('project_pk')
        metric_pk = self.kwargs.get('metric_pk')
        from_metric = Metric.objects.get(id=metric_pk, project_id=project_pk, tenant_id=client_pk)
        to_metric_id = self.request.data.get('to_metric')
        to_metric = Metric.objects.get(id=to_metric_id, project_id=project_pk, tenant_id=client_pk)
        serializer.save(from_metric=from_metric, to_metric=to_metric, tenant_id=client_pk)

    def list(self, request, *args, **kwargs):
        logger.info(f"Listing connections. Request: {request.GET}, kwargs: {kwargs}")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        logger.info(f"Creating connection. Data: {request.data}")
        return super().create(request, *args, **kwargs)
'''

class HistoricalDataViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HistoricalData.objects.all()
    serializer_class = HistoricalDataSerializer
    filterset_fields = ['metric', 'date', 'anomaly_detected']
    pagination_class = StandardResultsSetPagination
    basename = 'metric-historical-data'

    def get_queryset(self):
        return HistoricalData.objects.filter(tenant=self.request.tenant)

'''
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
'''

class ExperimentViewSet(TenantViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    filterset_fields = ['name', 'status', 'start_date', 'end_date']
    permission_classes = [IsAuthenticated]
    basename='project-experiments'

    def get_queryset(self):
        return Experiment.objects.filter(tenant=self.request.tenant)

'''
    @action(detail=True, methods=['post'])
    def run_experiment(self, request):
        experiment = self.get_object()
        experiment_type = request.data.get('experiment_type')
        params = request.data.get('params', {})

        with tenant_context(self.request.tenant):
            task = ExperimentManager.run_analysis.delay(experiment.id, experiment_type, **params)
        return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)
'''

class ForecastViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    filterset_fields = ['metric', 'forecast_date', 'model_used']
    basename='metric-forecast'

    def get_queryset(self):
        return Forecast.objects.filter(tenant=self.request.tenant)

class AnomalyViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer
    filterset_fields = ['metric', 'detection_date', 'anomaly_type', 'quality']
    basename='metric-anomaly'

    def get_queryset(self):
        return Anomaly.objects.filter(tenant=self.request.tenant)

class TrendViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Trend.objects.all()
    serializer_class = TrendSerializer
    filterset_fields = ['metric', 'trend_type', 'start_date', 'end_date']
    basename='metric-trend'

    def get_queryset(self):
        return Trend.objects.filter(tenant=self.request.tenant)

class DashboardViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    filterset_fields = ['name']
    basename='project-dashboards'

'''
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
'''

class ReportViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filterset_fields = ['name']
    basename='project-reports'

    def get_queryset(self):
        return Report.objects.filter(tenant=self.request.tenant)

class ActionRemarkViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ActionRemark.objects.all()
    serializer_class = ActionRemarkSerializer
    filterset_fields = ['metric', 'date', 'impact', 'importance']
    basename='metric-action-remarks'

    def get_queryset(self):
        return ActionRemark.objects.filter(tenant=self.request.tenant)

'''
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
'''

class StrategyViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Strategy.objects.all()
    serializer_class = StrategySerializer
    filterset_fields = ['title', 'team']
    basename='project-strategies'

    def get_queryset(self):
        return Strategy.objects.filter(tenant=self.request.tenant)

class TacticalSolutionViewSet(TenantViewSet):
    queryset = TacticalSolution.objects.all()
    serializer_class = TacticalSolutionSerializer
    filterset_fields = ['metric', 'title']
    basename='metric-tactical-solutions'

    def get_queryset(self):
        return TacticalSolution.objects.filter(tenant=self.request.tenant)

class DataQualityScoreViewSet(TenantViewSet):
    queryset = DataQualityScore.objects.all()
    serializer_class = DataQualityScoreSerializer
    filterset_fields = ['data_entry']
    basename='metric-data-quality-scores'

    def get_queryset(self):
        return DataQualityScore.objects.filter(tenant=self.request.tenant)

class TimeDimensionViewSet(TenantViewSet):
    queryset = TimeDimension.objects.all()
    serializer_class = TimeDimensionSerializer
    filterset_fields = ['date', 'year', 'month', 'is_weekend', 'is_holiday']
    basename='metric-time-dimensions'

    def get_queryset(self):
        return TimeDimension.objects.filter(tenant=self.request.tenant)

@api_view(['POST'])
@throttle_classes([ComputationTriggerThrottle])
@permission_classes([IsAuthenticated])
def trigger_computations(request):
    tenant = request.tenant
    pending_computations = PendingComputation.objects.filter(tenant=tenant)
    metric_ids = list(pending_computations.values_list('metric_id', flat=True))
    
    if metric_ids:
        run_computations.delay(tenant.id, metric_ids)
        pending_computations.delete()
        return Response({"message": "Computations queued successfully"})
    else:
        return Response({"message": "No pending computations"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_computation_status(request):
    tenant = request.tenant
    latest_status = ComputationStatus.objects.filter(tenant=tenant).first()
    if latest_status:
        return Response({
            "status": latest_status.status,
            "updated_at": latest_status.updated_at
        })
    else:
        return Response({"message": "No computation status found"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    tenant = request.tenant
    notifications = Notification.objects.filter(tenant=tenant, is_read=False)
    return Response({
        "notifications": [
            {"id": n.id, "message": n.message, "created_at": n.created_at}
            for n in notifications
        ]
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def prepare_bulk_import(request, metric_id):
    sheet_url = request.data.get('sheet_url')
    if not sheet_url:
        return Response({"error": "Google Sheet URL is required"}, status=400)
    
    result = data_export.prepare_data_for_bulk_import(sheet_url)
    return Response(result)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def import_historical_data(request, metric_id):
    data = request.data.get('data')
    if not data:
        return Response({"error": "No data provided for import"}, status=400)
    
    try:
        metric = Metric.objects.get(id=metric_id)
    except Metric.DoesNotExist:
        return Response({"error": "Metric not found"}, status=404)
    
    try:
        with transaction.atomic():
            for item in data:
                HistoricalData.objects.create(
                    metric=metric,
                    date=item['date'],
                    value=item['value'],
                    tenant=request.tenant  # Assuming you're using multi-tenancy
                )
        return Response({"message": f"Successfully imported {len(data)} data points"})
    except Exception as e:
        return Response({"error": f"Error during import: {str(e)}"}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_statistical_analysis(request, metric_id):
    analysis_type = request.query_params.get('type', 'basic')
    if analysis_type == 'basic':
        stats = statistical_analysis.calculate_basic_stats(metric_id)
    elif analysis_type == 'advanced':
        stats = statistical_analysis.calculate_advanced_stats(metric_id)
    elif analysis_type == 'aggregated':
        stats = statistical_analysis.calculate_aggregated_views(metric_id)
    else:
        return Response({"error": "Invalid analysis type"}, status=400)
    return Response(stats)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_performance_analysis(request, metric_id):
    analysis_type = request.query_params.get('type')
    if analysis_type == 'forecast_comparison':
        result = performance_analysis.forecast_vs_actual_comparison(metric_id)
    elif analysis_type == 'probability':
        result = performance_analysis.probability_analysis(metric_id)
    elif analysis_type == 'progress_tracking':
        result = performance_analysis.process_progress_tracking(metric_id)
    else:
        return Response({"error": "Invalid analysis type"}, status=400)
    return Response(result)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def run_experiment_analysis(request, metric_id):
    analysis_type = request.data.get('type')
    if analysis_type == 'ab_test':
        result = experiment_analysis.ab_test_analysis(
            metric_id,
            request.data.get('control_group'),
            request.data.get('treatment_group')
        )
    elif analysis_type == 'difference_in_differences':
        result = experiment_analysis.difference_in_differences(
            metric_id,
            request.data.get('pre_period'),
            request.data.get('post_period'),
            request.data.get('control_group'),
            request.data.get('treatment_group')
        )
    else:
        return Response({"error": "Invalid analysis type"}, status=400)
    return Response(result)

@api_view(['POST'])
def mark_notification_read(request, notification_id):
    tenant = request.user.tenant
    try:
        notification = Notification.objects.get(id=notification_id, tenant=tenant)
        notification.is_read = True
        notification.save()
        return Response({"message": "Notification marked as read"})
    except Notification.DoesNotExist:
        return Response({"error": "Notification not found"}, status=404)
    
@permission_classes([IsAuthenticated])
def trigger_long_computation(request, metric_id):
    computation_type = request.data.get('computation_type')
    task = run_long_computation.delay(metric_id, computation_type)
    return Response({'task_id': task.id})

@permission_classes([IsAuthenticated])
def get_automated_suggestions(request, metric_id):
    suggestions = dashboard_computations.generate_automated_suggestions(metric_id)
    return Response(suggestions)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_performance_dashboard(request, metric_id):
    current_date = request.query_params.get('current_date')
    dashboard = dashboard_computations.performance_dashboard(metric_id, current_date)
    return Response(dashboard)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def export_data(request, metric_id):
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')
    data_type = request.query_params.get('data_type', 'raw')
    data = bulk_export_data(metric_id, start_date, end_date, data_type)
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_tenant(request):
    serializer = TenantCreationSerializer(data=request.data)
    if serializer.is_valid():
        with transaction.atomic():
            # Create the tenant
            tenant = Client(
                schema_name=serializer.validated_data['domain'],
                name=serializer.validated_data['name']
            )
            tenant.save()

            # Add domain for the tenant
            domain = Domain()
            domain.domain = f"{serializer.validated_data['domain']}.example.com"  # replace with your actual domain
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()

            # Create a user profile for the tenant
            with tenant_context(tenant):
                UserProfile.objects.create(user=request.user, tenant=tenant)

        return Response({"message": "Tenant created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    serializer = ProjectCreationSerializer(data=request.data)
    if serializer.is_valid():
        project = serializer.save(tenant=request.tenant)
        return Response({"message": "Project created successfully", "id": project.id}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_team(request):
    serializer = TeamCreationSerializer(data=request.data)
    if serializer.is_valid():
        team = serializer.save(tenant=request.tenant)
        return Response({"message": "Team created successfully", "id": team.id}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_team_members(request):
    serializer = TeamMemberAssignmentSerializer(data=request.data)
    if serializer.is_valid():
        team_id = serializer.validated_data['team_id']
        user_ids = serializer.validated_data['user_ids']
        
        try:
            team = Team.objects.get(id=team_id, tenant=request.tenant)
        except Team.DoesNotExist:
            return Response({"error": "Team not found"}, status=status.HTTP_404_NOT_FOUND)
        
        users = CustomUser.objects.filter(id__in=user_ids, tenant=request.tenant)
        team.members.add(*users)
        
        return Response({"message": "Team members assigned successfully"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)