from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import (
    Client, CustomUser, UserProfile, Team, Project, Category, Tag, Metric,
    MetricMetadata, MetricTarget, Correlation, Connection, HistoricalData,
    Experiment, Forecast, Anomaly, Trend, Dashboard, Report, ActionRemark,
    Strategy, TacticalSolution, DataQualityScore, TimeDimension
)

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'created_on', 'schema_name']
    search_fields = ['name', 'schema_name']

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'team', 'tenant']
    list_filter = ['team', 'tenant']
    search_fields = ['username', 'email', 'team__name', 'tenant__name']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'tenant']
    search_fields = ['user__username', 'user__email', 'tenant__name']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'tenant']
    search_fields = ['name', 'description', 'tenant__name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_on', 'tenant']
    list_filter = ['tenant']
    search_fields = ['name', 'tenant__name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'tenant']
    list_filter = ['tenant']
    search_fields = ['name', 'tenant__name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'tenant']
    list_filter = ['project', 'tenant']
    search_fields = ['name', 'project__name', 'tenant__name']

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'value_type', 'category', 'tenant']
    list_filter = ['type', 'value_type', 'category', 'tenant']
    search_fields = ['name', 'description', 'tenant__name']
    filter_horizontal = ['tags']

@admin.register(MetricMetadata)
class MetricMetadataAdmin(admin.ModelAdmin):
    list_display = ['metric', 'data_source', 'rhythm', 'last_updated', 'tenant']
    list_filter = ['rhythm', 'tenant']
    search_fields = ['metric__name', 'data_source', 'tenant__name']
    date_hierarchy = 'last_updated'

@admin.register(MetricTarget)
class MetricTargetAdmin(admin.ModelAdmin):
    list_display = ['metric', 'target_kpi', 'target_date', 'target_value', 'tenant']
    list_filter = ['metric', 'tenant']
    search_fields = ['metric__name', 'target_kpi', 'tenant__name']
    date_hierarchy = 'target_date'

@admin.register(Correlation)
class CorrelationAdmin(admin.ModelAdmin):
    list_display = ['metric1', 'metric2', 'lag', 'pearson_correlation', 'spearman_correlation', 'tenant']
    list_filter = ['tenant']
    search_fields = ['metric1__name', 'metric2__name', 'tenant__name']

@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ['from_metric', 'to_metric', 'relationship', 'tenant']
    list_filter = ['tenant']
    search_fields = ['from_metric__name', 'to_metric__name', 'relationship', 'tenant__name']

@admin.register(HistoricalData)
class HistoricalDataAdmin(admin.ModelAdmin):
    list_display = ['metric', 'date', 'value', 'tenant']
    list_filter = ['metric', 'tenant']
    search_fields = ['metric__name', 'tenant__name']
    date_hierarchy = 'date'

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'status', 'tenant']
    list_filter = ['status', 'tenant']
    search_fields = ['name', 'description', 'tenant__name']
    filter_horizontal = ['metrics']
    date_hierarchy = 'start_date'

@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ['metric', 'forecast_date', 'forecast_value', 'model_used', 'accuracy', 'tenant']
    list_filter = ['metric', 'model_used', 'tenant']
    search_fields = ['metric__name', 'model_used', 'tenant__name']
    date_hierarchy = 'forecast_date'

@admin.register(Anomaly)
class AnomalyAdmin(admin.ModelAdmin):
    list_display = ['metric', 'detection_date', 'anomaly_value', 'anomaly_score', 'tenant']
    list_filter = ['metric', 'tenant']
    search_fields = ['metric__name', 'notes', 'tenant__name']
    date_hierarchy = 'detection_date'

@admin.register(Trend)
class TrendAdmin(admin.ModelAdmin):
    list_display = ['metric', 'trend_type', 'start_date', 'end_date', 'trend_value', 'tenant']
    list_filter = ['metric', 'trend_type', 'tenant']
    search_fields = ['metric__name', 'trend_type', 'notes', 'tenant__name']
    date_hierarchy = 'start_date'

@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ['name', 'tenant']
    list_filter = ['tenant']
    search_fields = ['name', 'tenant__name']

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['name', 'tenant']
    list_filter = ['tenant']
    search_fields = ['name', 'tenant__name']

@admin.register(ActionRemark)
class ActionRemarkAdmin(admin.ModelAdmin):
    list_display = ['metric', 'date', 'impact', 'importance', 'tenant']
    list_filter = ['impact', 'importance', 'tenant']
    search_fields = ['metric__name', 'title', 'summary', 'tenant__name']
    date_hierarchy = 'date'

@admin.register(Strategy)
class StrategyAdmin(admin.ModelAdmin):
    list_display = ['title', 'team', 'estimated_time', 'tenant']
    list_filter = ['team', 'tenant']
    search_fields = ['title', 'description', 'team__name', 'tenant__name']

@admin.register(TacticalSolution)
class TacticalSolutionAdmin(admin.ModelAdmin):
    list_display = ['metric', 'title', 'tenant']
    list_filter = ['metric', 'tenant']
    search_fields = ['title', 'description', 'metric__name', 'tenant__name']

@admin.register(DataQualityScore)
class DataQualityScoreAdmin(admin.ModelAdmin):
    list_display = ['data_entry', 'completeness_score', 'accuracy_score', 'consistency_score', 'timeliness_score', 'overall_score', 'tenant']
    list_filter = ['tenant']
    search_fields = ['data_entry', 'tenant__name']

@admin.register(TimeDimension)
class TimeDimensionAdmin(admin.ModelAdmin):
    list_display = ['date', 'day', 'month', 'year', 'is_weekend', 'is_holiday', 'tenant']
    list_filter = ['is_weekend', 'is_holiday', 'tenant']
    search_fields = ['date', 'tenant__name']
    date_hierarchy = 'date'