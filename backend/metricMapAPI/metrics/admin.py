from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import (
    Client, Domain, Project, Category, Tag, Metric, Connection,
    HistoricalData, Target, ActionRemark, Dashboard, Report,
    Experiment, Forecast, Anomaly, Trend
)

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'created_on', 'schema_name']
    search_fields = ['name', 'schema_name']

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ['domain', 'tenant', 'is_primary']
    list_filter = ['is_primary', 'tenant']
    search_fields = ['domain', 'tenant__name']

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
    list_display = ['name', 'type', 'value_type', 'rhythm', 'category', 'tenant']
    list_filter = ['type', 'value_type', 'rhythm', 'category', 'tenant']
    search_fields = ['name', 'description', 'tenant__name']
    filter_horizontal = ['tags']

@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ['from_metric', 'to_metric', 'relationship', 'correlation_coefficient', 'tenant']
    list_filter = ['tenant']
    search_fields = ['from_metric__name', 'to_metric__name', 'relationship', 'tenant__name']

@admin.register(HistoricalData)
class HistoricalDataAdmin(admin.ModelAdmin):
    list_display = ['metric', 'date', 'value', 'forecasted_value', 'anomaly_detected', 'tenant']
    list_filter = ['metric', 'anomaly_detected', 'tenant']
    search_fields = ['metric__name', 'tenant__name']
    date_hierarchy = 'date'

@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ['metric', 'target_kpi', 'target_date', 'target_value', 'tenant']
    list_filter = ['metric', 'tenant']
    search_fields = ['metric__name', 'target_kpi', 'tenant__name']
    date_hierarchy = 'target_date'

@admin.register(ActionRemark)
class ActionRemarkAdmin(admin.ModelAdmin):
    list_display = ['metric', 'date', 'description', 'impact', 'tenant']
    list_filter = ['metric', 'tenant']
    search_fields = ['metric__name', 'description', 'impact', 'tenant__name']
    date_hierarchy = 'date'

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