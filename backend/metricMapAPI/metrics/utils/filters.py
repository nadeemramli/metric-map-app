from django_filters import rest_framework as filters
from ..models import *

# Tenant related filters
class TenantAwareFilterSet(filters.FilterSet):
    tenant = filters.NumberFilter(field_name='tenant__id')

class ProjectFilter(TenantAwareFilterSet):
    class Meta:
        model = Project
        fields = ['tenant', 'name']

class CustomUserFilter(TenantAwareFilterSet):
    class Meta:
        model = CustomUser
        fields = ['tenant', 'username', 'email', 'team']

class UserProfileFilter(TenantAwareFilterSet):
    class Meta:
        model = UserProfile
        fields = ['tenant', 'user']

class TeamFilter(TenantAwareFilterSet):
    class Meta:
        model = Team
        fields = ['tenant', 'name']

# Project related filters
class ProjectRelatedFilterSet(filters.FilterSet):
    project = filters.NumberFilter(field_name='project__id')

class MetricFilter(ProjectRelatedFilterSet):
    class Meta:
        model = Metric
        fields = ['project', 'name', 'type', 'value_type', 'category', 'tags']

class CategoryFilter(ProjectRelatedFilterSet):
    class Meta:
        model = Category
        fields = ['project', 'name']

class TagFilter(ProjectRelatedFilterSet):
    class Meta:
        model = Tag
        fields = ['project', 'name']

class DashboardFilter(ProjectRelatedFilterSet):
    class Meta:
        model = Dashboard
        fields = ['project', 'name']

class ExperimentFilter(ProjectRelatedFilterSet):
    class Meta:
        model = Experiment
        fields = ['project', 'name', 'status', 'start_date', 'end_date']

class ReportFilter(ProjectRelatedFilterSet):
    class Meta:
        model = Report
        fields = ['project', 'name']

class StrategyFilter(ProjectRelatedFilterSet):
    class Meta:
        model = Strategy
        fields = ['project', 'title', 'team']

class ActionRemarkFilter(ProjectRelatedFilterSet):
    class Meta:
        model = ActionRemark
        fields = ['project', 'date', 'impact', 'importance']

class TacticalSolutionFilter(ProjectRelatedFilterSet):
    class Meta:
        model = TacticalSolution
        fields = ['project', 'title']

class TimeDimensionFilter(ProjectRelatedFilterSet):
    class Meta:
        model = TimeDimension
        fields = ['project', 'date', 'year', 'month', 'is_weekend', 'is_holiday']

class NetworkAnalysisResultFilter(ProjectRelatedFilterSet):
    class Meta:
        model = NetworkAnalysisResult
        fields = ['project', 'metric']

class ComputationStatusFilter(ProjectRelatedFilterSet):
    class Meta:
        model = ComputationStatus
        fields = ['project', 'status']

class NotificationFilter(ProjectRelatedFilterSet):
    class Meta:
        model = Notification
        fields = ['project', 'is_read']

class PendingComputationFilter(ProjectRelatedFilterSet):
    class Meta:
        model = PendingComputation
        fields = ['project']

# Metric related filters
class MetricRelatedFilterSet(filters.FilterSet):
    metric = filters.NumberFilter(field_name='metric__id')

class MetricMetadataFilter(MetricRelatedFilterSet):
    class Meta:
        model = MetricMetadata
        fields = ['metric', 'data_quality_score', 'team', 'confidence']

class MetricTargetFilter(MetricRelatedFilterSet):
    class Meta:
        model = MetricTarget
        fields = ['metric', 'target_date']

class TechnicalIndicatorFilter(MetricRelatedFilterSet):
    class Meta:
        model = TechnicalIndicator
        fields = ['metric', 'date']

class MovingAverageFilter(MetricRelatedFilterSet):
    class Meta:
        model = MovingAverage
        fields = ['metric', 'ma_type']

class SeasonalityResultFilter(MetricRelatedFilterSet):
    class Meta:
        model = SeasonalityResult
        fields = ['metric', 'seasonality_type']

class TrendChangePointFilter(MetricRelatedFilterSet):
    class Meta:
        model = TrendChangePoint
        fields = ['metric']

class HistoricalDataFilter(MetricRelatedFilterSet):
    class Meta:
        model = HistoricalData
        fields = ['metric', 'date']

class ForecastFilter(MetricRelatedFilterSet):
    class Meta:
        model = Forecast
        fields = ['metric', 'forecast_date', 'model_used']

class AnomalyFilter(MetricRelatedFilterSet):
    class Meta:
        model = Anomaly
        fields = ['metric', 'detection_date', 'anomaly_type', 'quality']

class TrendFilter(MetricRelatedFilterSet):
    class Meta:
        model = Trend
        fields = ['metric', 'trend_type', 'start_date', 'end_date']

class InsightFilter(MetricRelatedFilterSet):
    class Meta:
        model = Insight
        fields = ['metric']

class CorrelationFilter(MetricRelatedFilterSet):
    class Meta:
        model = Correlation
        fields = ['metric1', 'metric2']

class ConnectionFilter(MetricRelatedFilterSet):
    class Meta:
        model = Connection
        fields = ['from_metric', 'to_metric']

class DataQualityScoreFilter(MetricRelatedFilterSet):
    class Meta:
        model = DataQualityScore
        fields = ['metric', 'data_entry']

class InsightFilter(MetricRelatedFilterSet):
    class Meta:
        model = Insight
        fields = ['metric']

# Experiment related filters
class ExperimentRelatedFilterSet(filters.FilterSet):
    experiment = filters.NumberFilter(field_name='experiment__id')
    
class ImpactAnalysisFilter(ExperimentRelatedFilterSet):
    impacted_metric = filters.NumberFilter(field_name='impacted_metric__id')
    class Meta:
        model = ImpactAnalysis
        fields = ['experiment']