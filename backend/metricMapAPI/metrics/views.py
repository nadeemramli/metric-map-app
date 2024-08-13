
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, throttle_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.management import call_command
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db import models, transaction
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from celery.result import AsyncResult
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from .tasks import run_computations, run_long_computation
from .utils.throttles import ComputationTriggerThrottle
from .interim.data_export import prepare_data_for_bulk_import
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from rest_framework.exceptions import NotFound
from metrics import logger
from django_tenants.utils import schema_context
from .utils.permissions import IsTenantUser
from .utils.filters import *

def public_home(request):
    return render(request, 'home.html')

def debug_view(request):
       return HttpResponse("Debug view is working!")

class CustomTokenObtainPairView(TokenObtainPairView):
    pass

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class TenantAwareViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsTenantUser]
    pagination_class = StandardResultsSetPagination
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    
    def check_tenant(self):
        if not hasattr(self.request, 'tenant') or not self.request.tenant:
            raise NotFound("Tenant not found.")
        return self.request.tenant
    
    def check_permissions(self, request):
        if not isinstance(request.user, CustomUser):
            raise PermissionDenied("Invalid user type")
        super().check_permissions(request)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not hasattr(self.request, 'tenant') or not self.request.tenant:
            return queryset.none()
        if hasattr(queryset.model, 'tenant'):
            queryset = queryset.filter(tenant=self.request.tenant)
        if hasattr(self, 'filterset_class') and self.request.query_params:
            return self.filterset_class(self.request.query_params, queryset=queryset).qs
        return queryset

    def perform_create(self, serializer):
        tenant = self.check_tenant()
        with schema_context(tenant.schema_name):
            serializer.save(tenant=self.request.tenant)

    @method_decorator(cache_page(60 * 15))  # Cache the response for 15 minutes
    def list(self, request, *args, **kwargs):
        logger.info(f"List view called for {self.__class__.__name__}")
        logger.debug(f"Request data: {request.data}")
        logger.debug(f"Request user: {request.user}")
        logger.debug(f"Request tenant: {getattr(request, 'tenant', None)}")
        try:
            with schema_context(request.tenant.schema_name):
                queryset = self.get_queryset()
                logger.debug(f"Queryset in list view: {queryset}")
                serializer = self.get_serializer(queryset, many=True)
                logger.debug(f"Serialized data: {serializer.data}")
            return Response(serializer.data)
        except Exception as e:
            logger.exception(f"Error in list view of {self.__class__.__name__}: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error in create view of {self.__class__.__name__}: {str(e)}")
            return Response({"error": "An error occurred while creating the object."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def retrieve(self, request, *args, **kwargs):
        logger.info(f"Retrieve view called for {self.__class__.__name__}")
        logger.debug(f"Request user: {request.user}")
        logger.debug(f"Request tenant: {getattr(request, 'tenant', None)}")
        logger.debug(f"Args: {args}")
        logger.debug(f"Kwargs: {kwargs}")
        
        try:
            instance = self.get_object()
            logger.debug(f"Retrieved object: {instance}")
            serializer = self.get_serializer(instance)
            logger.debug(f"Serialized data: {serializer.data}")
            return Response(serializer.data)
        except models.ObjectDoesNotExist as e:
            logger.warning(f"Object not found in retrieve view of {self.__class__.__name__}: {str(e)}")
            logger.debug(f"Query parameters: {request.query_params}")
            return Response({"error": "Object not found.", "details": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error in retrieve view of {self.__class__.__name__}: {str(e)}", exc_info=True)
            return Response({"error": "An error occurred while fetching the object.", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except models.ObjectDoesNotExist:
            return Response({"error": "Object not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error in update view of {self.__class__.__name__}: {str(e)}")
            return Response({"error": "An error occurred while updating the object."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except models.ObjectDoesNotExist:
            return Response({"error": "Object not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error in destroy view of {self.__class__.__name__}: {str(e)}")
            return Response({"error": "An error occurred while deleting the object."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ClientViewSet(TenantAwareViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CustomUserViewSet(TenantAwareViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filterset_class = CustomUserFilter

class UserProfileViewSet(TenantAwareViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filterset_class = UserProfileFilter

class TeamViewSet(TenantAwareViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_class = TeamFilter

class ProjectViewSet(TenantAwareViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter
    basename='client-projects'
    
    def get_queryset(self):
        return super().get_queryset().filter(tenant=self.request.tenant)

# Nested viewset for project-related entities
class CategoryViewSet(TenantAwareViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    basename='project-categories'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)

# Nested viewset for project-related entities
class TagViewSet(TenantAwareViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filterset_class = TagFilter
    basename='project-tags'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)

# Nested viewset for project-related entities  
class MetricViewSet(TenantAwareViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    filterset_class = MetricFilter
    basename='project-metrics'
    lookup_field = 'id'
    lookup_url_kwarg = 'metric_pk'
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)

    @action(detail=True, methods=['post'])
    def set_position(self, request, pk=None):
        metric = self.get_object()
        x = request.data.get('x')
        y = request.data.get('y')
        if x is not None and y is not None:
            metric.set_position(x, y)
            return Response({'status': 'position updated'})
        return Response({'error': 'Invalid position data'}, status=status.HTTP_400_BAD_REQUEST)

# Nested viewset for metric-related entities
class MetricMetadataViewSet(TenantAwareViewSet):
    queryset = MetricMetadata.objects.all()
    serializer_class = MetricMetadataSerializer
    filterset_class = MetricMetadataFilter
    basename='metric-metadata'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        metric_pk = self.kwargs.get('metric_pk')
        if metric_pk:
            return queryset.filter(metric__id=metric_pk)
        return queryset

# Nested viewset for metric-related entities
class MetricTargetViewSet(TenantAwareViewSet):
    queryset = MetricTarget.objects.all()
    serializer_class = MetricTargetSerializer
    filterset_class = MetricTargetFilter
    basename='metric-targets'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        metric_pk = self.kwargs.get('metric_pk')
        if metric_pk:
            return queryset.filter(metric__id=metric_pk)
        return queryset

# Nested viewset for metric-related entities
class CorrelationViewSet(TenantAwareViewSet):
    queryset = Correlation.objects.all()
    serializer_class = CorrelationSerializer
    filterset_class = CorrelationFilter
    basename='metric-correlations'
    lookup_field = 'metric1__id'
    lookup_url_kwarg = 'metric1_pk'
    
    def get_queryset(self):
        return Correlation.objects.filter(
            metric1__id=self.kwargs.get('metric1_pk'),
            metric2__id=self.kwargs.get('metric2_pk')
        )

# Nested viewset for metric-related entities
class ConnectionViewSet(TenantAwareViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    filterset_class = ConnectionFilter
    basename = 'metric-connections'
    lookup_field = 'metric1__id'
    lookup_url_kwarg = 'metric1_pk'

    def get_queryset(self):
        return Connection.objects.filter(
            metric1__id=self.kwargs.get('metric1_pk'),
            metric2__id=self.kwargs.get('metric2_pk')
        )

# Nested viewset for metric-related entities
class HistoricalDataViewSet(TenantAwareViewSet):
    queryset = HistoricalData.objects.all()
    serializer_class = HistoricalDataSerializer
    filterset_class = HistoricalDataFilter
    pagination_class = StandardResultsSetPagination
    basename = 'metric-historical-data'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        metric_pk = self.kwargs.get('metric_pk')
        if metric_pk:
            return queryset.filter(metric__id=metric_pk)
        return queryset

# Based on this code, the URL pattern for this view would likely look like:
# /api/clients/{client_id}/projects/{project_id}/metrics/{metric_id}/historical-data/
#
# This pattern is derived from:
# 1. The use of TenantAwareViewSet as the base class, which implies a client-level scope
# 2. The 'project_pk' in the get_queryset method, indicating a project-level scope
# 3. The 'metric_pk' used as the lookup_url_kwarg, suggesting a metric-level scope
# 4. The basename 'metric-historical-data', which would form the final part of the URL
#
# The view supports standard CRUD operations on HistoricalData objects, filtered by tenant, project, and metric.
# It uses authentication, pagination, and allows filtering on 'metric', 'date', and 'anomaly_detected' fields.

# Nested viewset for project-related entities  
class ExperimentViewSet(TenantAwareViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    filterset_class = ExperimentFilter
    basename='project-experiments'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)

# Nested viewset for metric-related entities
class ForecastViewSet(TenantAwareViewSet):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    filterset_class = ForecastFilter
    basename='metric-forecast'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        metric_pk = self.kwargs.get('metric_pk')
        if metric_pk:
            return queryset.filter(metric__id=metric_pk)
        return queryset

# Nested viewset for metric-related entities
class AnomalyViewSet(TenantAwareViewSet):
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer
    filterset_class = AnomalyFilter
    basename='metric-anomaly'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        metric_pk = self.kwargs.get('metric_pk')
        if metric_pk:
            return queryset.filter(metric__id=metric_pk)
        return queryset

# Nested viewset for metric-related entities
class TrendViewSet(TenantAwareViewSet):
    queryset = Trend.objects.all()
    serializer_class = TrendSerializer
    filterset_class = TrendFilter
    basename='metric-trend'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        metric_pk = self.kwargs.get('metric_pk')
        if metric_pk:
            return queryset.filter(metric__id=metric_pk)
        return queryset

# Nested viewset for project-related entities 
class DashboardViewSet(TenantAwareViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    filterset_class = DashboardFilter
    basename='project-dashboards'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)

# Nested viewset for project-related entities 
class ReportViewSet(TenantAwareViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filterset_class = ReportFilter
    basename='project-reports'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)

# Nested viewset for project-related entities 
class ActionRemarkViewSet(TenantAwareViewSet):
    queryset = ActionRemark.objects.all()
    serializer_class = ActionRemarkSerializer
    filterset_class = ActionRemarkFilter
    basename='project-action-remarks'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)

# Nested viewset for project-related entities 
class StrategyViewSet(TenantAwareViewSet):
    queryset = Strategy.objects.all()
    serializer_class = StrategySerializer
    filterset_class = StrategyFilter
    basename='project-strategies'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)

# Nested viewset for project-related entities 
class TacticalSolutionViewSet(TenantAwareViewSet):
    queryset = TacticalSolution.objects.all()
    serializer_class = TacticalSolutionSerializer
    filterset_class = TacticalSolutionFilter
    basename='project-tactical-solutions'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)

# Nested viewset for metric-related entities
class DataQualityScoreViewSet(TenantAwareViewSet):
    queryset = DataQualityScore.objects.all()
    serializer_class = DataQualityScoreSerializer
    filterset_class = DataQualityScoreFilter
    basename='metric-data-quality-scores'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        metric_pk = self.kwargs.get('metric_pk')
        if metric_pk:
            return queryset.filter(metric__id=metric_pk)
        return queryset

# Nested viewset for project-related entities 
class TimeDimensionViewSet(TenantAwareViewSet):
    queryset = TimeDimension.objects.all()
    serializer_class = TimeDimensionSerializer
    filterset_class = TimeDimensionFilter
    basename='project-time-dimensions'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)

# Nested viewset for project-related entities
class InsightViewSet(TenantAwareViewSet):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer
    filterset_class = InsightFilter
    basename = 'metric-insights'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        project_id = self.kwargs.get('project_pk')
        metric_pk = self.kwargs.get('metric_pk')
        if project_id:
            queryset = queryset.filter(metric__project_id=project_id)
        if metric_pk:
            queryset = queryset.filter(metric_id=metric_pk)
        return queryset

# Nested viewset for metric-related entities
class TechnicalIndicatorViewSet(TenantAwareViewSet):
    queryset = TechnicalIndicator.objects.all()
    serializer_class = TechnicalIndicatorSerializer
    filterset_class = TechnicalIndicatorFilter
    basename = 'metric-technical-indicators'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        metric_pk = self.kwargs.get('metric_pk')
        if metric_pk:
            return queryset.filter(metric__id=metric_pk)
        return queryset

# Nested viewset for metric-related entities
class ImpactAnalysisViewSet(TenantAwareViewSet):
    queryset = ImpactAnalysis.objects.all()
    serializer_class = ImpactAnalysisSerializer
    filterset_class = ImpactAnalysisFilter
    basename = 'experiment-impact-analysis'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        metric_pk = self.kwargs.get('metric_pk')
        if metric_pk:
            return queryset.filter(metric__id=metric_pk)
        return queryset

# Nested viewset for metric-related entities
class MovingAverageViewSet(TenantAwareViewSet):
    queryset = MovingAverage.objects.all()
    serializer_class = MovingAverageSerializer
    filterset_class = MovingAverageFilter
    basename = 'metric-moving-averages'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        metric_pk = self.kwargs.get('metric_pk')
        if metric_pk:
            return queryset.filter(metric__id=metric_pk)
        return queryset

# Nested viewset for metric-related entities
class SeasonalityResultViewSet(TenantAwareViewSet):
    queryset = SeasonalityResult.objects.all()
    serializer_class = SeasonalityResultSerializer
    filterset_class = SeasonalityResultFilter
    basename = 'metric-seasonality-results'
    lookup_field = 'id'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        metric_pk = self.kwargs.get('metric_pk')
        if metric_pk:
            return queryset.filter(metric__id=metric_pk)
        return queryset

# Nested viewset for metric-related entities
class TrendChangePointViewSet(TenantAwareViewSet):
    queryset = TrendChangePoint.objects.all()
    serializer_class = TrendChangePointSerializer
    filterset_class = TrendChangePointFilter
    basename = 'metric-trend-change-points'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        return TrendChangePoint.objects.filter(
            metric__id=self.kwargs.get('metric_pk')
        )

# Nested viewset for project-related entities 
class NetworkAnalysisResultViewSet(TenantAwareViewSet):
    queryset = NetworkAnalysisResult.objects.all()
    serializer_class = NetworkAnalysisResultSerializer
    filterset_class = NetworkAnalysisResultFilter
    basename = 'project-network-analysis-results'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)

# Nested viewset for project-related entities 
class ComputationStatusViewSet(TenantAwareViewSet):
    queryset = ComputationStatus.objects.all()
    serializer_class = ComputationStatusSerializer
    filterset_class = ComputationStatusFilter
    basename = 'project-computation-status'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)

# Nested viewset for project-related entities 
class NotificationViewSet(TenantAwareViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filterset_class = NotificationFilter
    basename = 'project-notifications'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk' 
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)

# Nested viewset for project-related entities 
class PendingComputationViewSet(TenantAwareViewSet):
    queryset = PendingComputation.objects.all()
    serializer_class = PendingComputationSerializer
    filterset_class = PendingComputationFilter
    basename = 'project-pending-computations'
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return super().get_queryset().filter(project_id=project_id)


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
    
    result = prepare_data_for_bulk_import(sheet_url)
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
@method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
def get_statistical_analysis(request, metric_id):
    analysis_type = request.query_params.get('type', 'basic')
    task = run_long_computation.delay(metric_id, f'{analysis_type}_stats')
    return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
def get_performance_analysis(request, metric_id):
    analysis_type = request.query_params.get('type')
    task = run_long_computation.delay(metric_id, analysis_type)
    return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
def run_experiment_analysis(request, metric_id):
    analysis_type = request.data.get('type')
    kwargs = {
        'control_group': request.data.get('control_group'),
        'treatment_group': request.data.get('treatment_group')
    }
    if analysis_type == 'difference_in_differences':
        kwargs.update({
            'pre_period': request.data.get('pre_period'),
            'post_period': request.data.get('post_period')
        })
    task = run_long_computation.delay(metric_id, analysis_type, **kwargs)
    return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
def get_automated_suggestions(request, metric_id):
    task = run_long_computation.delay(metric_id, 'automated_suggestions')
    return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
def get_performance_dashboard(request, metric_id):
    current_date = request.query_params.get('current_date')
    task = run_long_computation.delay(metric_id, 'performance_dashboard', current_date=current_date)
    return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def export_data(request, metric_id):
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')
    data_type = request.query_params.get('data_type', 'raw')
    task = run_long_computation.delay(metric_id, 'bulk_export', start_date=start_date, end_date=end_date, data_type=data_type)
    return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task_status(request, task_id):
    task_result = AsyncResult(task_id)
    if task_result.ready():
        return Response({"status": "completed", "result": task_result.result})
    else:
        return Response({"status": "pending"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_tenant(request):
    name = request.data.get('name')
    domain_url = request.data.get('domain_url')

    if not name or not domain_url:
        return Response({'error': 'Name and domain_url are required'}, status=400)

    try:
        # Call the create_tenant command
        call_command('manage_tenants', 'create', name=name, domain_url=domain_url)
        return Response({'message': f'Tenant {name} created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

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

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(tenant=request.tenant)
            return Response(CustomUserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)