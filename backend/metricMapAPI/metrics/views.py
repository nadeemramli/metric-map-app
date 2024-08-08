
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, throttle_classes, permission_classes
from rest_framework.response import Response
from django.core.management import call_command
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db import models, transaction
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
    ProjectCreationSerializer, TeamCreationSerializer, TeamMemberAssignmentSerializer
)
from .tasks import run_computations, run_long_computation
from .throttles import ComputationTriggerThrottle
from .interim.data_export import prepare_data_for_bulk_import

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

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error in list view of {self.__class__.__name__}: {str(e)}")
            return Response({"error": "An error occurred while fetching the list."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error in create view of {self.__class__.__name__}: {str(e)}")
            return Response({"error": "An error occurred while creating the object."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except models.ObjectDoesNotExist:
            return Response({"error": "Object not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error in retrieve view of {self.__class__.__name__}: {str(e)}")
            return Response({"error": "An error occurred while fetching the object."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

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

class CategoryViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name']
    basename='project-categories'

class TagViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filterset_fields = ['name', 'project']
    basename='project-tags'
    
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

class MetricTargetViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MetricTarget.objects.all()
    serializer_class = MetricTargetSerializer
    filterset_fields = ['metric', 'target_date']
    basename='project-targets'

class CorrelationViewSet(TenantViewSet):
    queryset = Correlation.objects.all()
    serializer_class = CorrelationSerializer
    filterset_fields = ['metric1', 'metric2']

class ConnectionViewSet(TenantViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    filterset_fields = ['from_metric', 'to_metric']
    basename = 'metric-connections'

class HistoricalDataViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HistoricalData.objects.all()
    serializer_class = HistoricalDataSerializer
    filterset_fields = ['metric', 'date', 'anomaly_detected']
    pagination_class = StandardResultsSetPagination
    basename = 'metric-historical-data'

class ExperimentViewSet(TenantViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    filterset_fields = ['name', 'status', 'start_date', 'end_date']
    permission_classes = [IsAuthenticated]
    basename='project-experiments'

class ForecastViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    filterset_fields = ['metric', 'forecast_date', 'model_used']
    basename='metric-forecast'

class AnomalyViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer
    filterset_fields = ['metric', 'detection_date', 'anomaly_type', 'quality']
    basename='metric-anomaly'

class TrendViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Trend.objects.all()
    serializer_class = TrendSerializer
    filterset_fields = ['metric', 'trend_type', 'start_date', 'end_date']
    basename='metric-trend'

class DashboardViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    filterset_fields = ['name']
    basename='project-dashboards'

class ReportViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filterset_fields = ['name']
    basename='project-reports'

class ActionRemarkViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ActionRemark.objects.all()
    serializer_class = ActionRemarkSerializer
    filterset_fields = ['metric', 'date', 'impact', 'importance']
    basename='metric-action-remarks'

class StrategyViewSet(TenantViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Strategy.objects.all()
    serializer_class = StrategySerializer
    filterset_fields = ['title', 'team']
    basename='project-strategies'

class TacticalSolutionViewSet(TenantViewSet):
    queryset = TacticalSolution.objects.all()
    serializer_class = TacticalSolutionSerializer
    filterset_fields = ['metric', 'title']
    basename='metric-tactical-solutions'

class DataQualityScoreViewSet(TenantViewSet):
    queryset = DataQualityScore.objects.all()
    serializer_class = DataQualityScoreSerializer
    filterset_fields = ['data_entry']
    basename='metric-data-quality-scores'

class TimeDimensionViewSet(TenantViewSet):
    queryset = TimeDimension.objects.all()
    serializer_class = TimeDimensionSerializer
    filterset_fields = ['date', 'year', 'month', 'is_weekend', 'is_holiday']
    basename='metric-time-dimensions'


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
    subdomain = request.data.get('subdomain')
    domain = request.data.get('domain', 'localhost')

    if not name or not subdomain:
        return Response({'error': 'Name and subdomain are required'}, status=400)

    try:
        # Call the create_tenant command
        call_command('manage_tenants', 'create', name=name, subdomain=subdomain, domain=domain)
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