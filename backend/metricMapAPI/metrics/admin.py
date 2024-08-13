from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django_tenants.admin import TenantAdminMixin
from django_tenants.utils import get_public_schema_name
from django.db import connection
from .models import *
from metrics import logger

class TenantAwareAdmin(TenantAdminMixin, admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not isinstance(self.model, Client):
            qs = qs.filter(tenant=request.tenant)
        return qs
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        logger.debug(f"[TenantAwareAdmin: change_view] Current schema: {connection.schema_name}")
        logger.debug(f"[TenantAwareAdmin: change_view] Request tenant: {request.tenant.schema_name if hasattr(request, 'tenant') else 'N/A'}")
        logger.debug(f"[TenantAwareAdmin: change_view] Object ID: {object_id}")
        
        try:
            obj = self.get_object(request, object_id)
            if obj:
                logger.debug(f"[TenantAwareAdmin: change_view] Object tenant: {obj.tenant.schema_name if hasattr(obj, 'tenant') else 'N/A'}")
        except Exception as e:
            logger.error(f"[TenantAwareAdmin: change_view] Error getting object: {str(e)}")

        return super().change_view(request, object_id, form_url, extra_context)

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        return [field for field in list_display if field != 'tenant']

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        return [field for field in fields if field != 'tenant']

    def save_model(self, request, obj, form, change):
        logger.debug(f"TenantAwareAdmin save_model - Current schema: {connection.schema_name}, Object schema: {obj.tenant.schema_name if hasattr(obj, 'tenant') else 'N/A'}")
        if not change:  # Only set tenant for new objects
            obj.tenant = request.tenant
        with schema_context(request.tenant.schema_name):
            logger.debug(f"TenantAwareAdmin save_model - Inside schema_context: {connection.schema_name}")
            super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        with schema_context(request.tenant.schema_name):
            super().delete_model(request, obj)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if not change:
                instance.tenant = request.tenant
        with schema_context(request.tenant.schema_name):
            formset.save()

class MetricMapAdminSite(admin.AdminSite):
    def each_context(self, request):
        context = super().each_context(request)
        tenant = getattr(request, 'tenant', None)
        tenant_name = getattr(tenant, 'name', 'Unknown')
        
        context.update({
            'site_header': _('Metric Map Administration - {}'.format(tenant_name)),
            'site_title': _('Metric Map Admin - {}'.format(tenant_name)),
            'index_title': _('Welcome to Metric Map - {}'.format(tenant_name)),
            'tenant': tenant,
        })
        return context

admin_site = MetricMapAdminSite(name='metricmap_admin')

# Only register ClientAdmin if we're in the public schema
@admin.register(Client, site=admin_site)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'schema_name', 'domain_url', 'created_on']

    def has_module_permission(self, request):
        return connection.schema_name == get_public_schema_name()

@admin.register(CustomUser, site=admin_site)
class CustomUserAdmin(TenantAwareAdmin, UserAdmin):
    list_display = ['username', 'email', 'is_staff', 'tenant']
    fieldsets = UserAdmin.fieldsets + (
        ('Tenant Information', {'fields': ('tenant',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Tenant Information', {'fields': ('tenant',)}),
    )

@admin.register(Team, site=admin_site)
class TeamAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']

@admin.register(UserProfile, site=admin_site)
class UserProfileAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['user']

@admin.register(Project, site=admin_site)
class ProjectAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['name', 'created_on']

@admin.register(Category, site=admin_site)
class CategoryAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['name', 'project']

@admin.register(Tag, site=admin_site)
class TagAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['name', 'project']

@admin.register(Metric, site=admin_site)
class MetricAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['name', 'project', 'type', 'value_type', 'category']

@admin.register(DataQualityScore, site=admin_site)
class DataQualityScoreAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['metric', 'overall_score']

@admin.register(MetricMetadata, site=admin_site)
class MetricMetadataAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['metric', 'data_source', 'rhythm', 'last_updated']

@admin.register(MetricTarget, site=admin_site)
class MetricTargetAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['metric', 'target_kpi', 'target_date', 'target_value']

@admin.register(Correlation, site=admin_site)
class CorrelationAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['metric1', 'metric2', 'lag', 'pearson_correlation', 'spearman_correlation']

@admin.register(Connection, site=admin_site)
class ConnectionAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['from_metric', 'to_metric', 'relationship', 'strength']

@admin.register(Experiment, site=admin_site)
class ExperimentAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['name', 'project', 'start_date', 'end_date', 'status']

@admin.register(ActionRemark, site=admin_site)
class ActionRemarkAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['project', 'title', 'date', 'impact', 'importance']

@admin.register(Insight, site=admin_site)
class InsightAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['metric', 'user', 'date', 'title']

@admin.register(Strategy, site=admin_site)
class StrategyAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['project', 'title', 'team', 'estimated_time']

@admin.register(TacticalSolution, site=admin_site)
class TacticalSolutionAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['project', 'title', 'created_at']

@admin.register(Forecast, site=admin_site)
class ForecastAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['metric', 'forecast_date', 'forecast_value', 'model_used']

@admin.register(TechnicalIndicator, site=admin_site)
class TechnicalIndicatorAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['metric', 'date', 'stochastic_value', 'rsi_value', 'percent_change', 'moving_average']

@admin.register(Anomaly, site=admin_site)
class AnomalyAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['metric', 'detection_date', 'anomaly_value', 'anomaly_score', 'anomaly_type']

@admin.register(ImpactAnalysis, site=admin_site)
class ImpactAnalysisAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['experiment', 'metric', 'before_value', 'after_value', 'percentage_change']

@admin.register(Trend, site=admin_site)
class TrendAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['metric', 'trend_type', 'start_date', 'end_date', 'trend_value']

@admin.register(MovingAverage, site=admin_site)
class MovingAverageAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['metric', 'date', 'ma_type', 'period', 'value']

@admin.register(SeasonalityResult, site=admin_site)
class SeasonalityResultAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['metric', 'seasonality_type', 'strength', 'period']

@admin.register(TrendChangePoint, site=admin_site)
class TrendChangePointAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['metric', 'date', 'direction', 'significance']

@admin.register(NetworkAnalysisResult, site=admin_site)
class NetworkAnalysisResultAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['project', 'metric', 'analysis_type']

@admin.register(HistoricalData, site=admin_site)
class HistoricalDataAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['metric', 'date', 'value']

@admin.register(TimeDimension, site=admin_site)
class TimeDimensionAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['project', 'date', 'day', 'month', 'year']

@admin.register(Dashboard, site=admin_site)
class DashboardAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['project', 'name']

@admin.register(Report, site=admin_site)
class ReportAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['project', 'metric', 'name', 'created_at']

@admin.register(ComputationStatus, site=admin_site)
class ComputationStatusAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['project', 'status', 'created_at', 'updated_at']

@admin.register(Notification, site=admin_site)
class NotificationAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['project', 'message', 'created_at', 'is_read']

@admin.register(PendingComputation, site=admin_site)
class PendingComputationAdmin(TenantAwareAdmin, admin.ModelAdmin):
    list_display = ['project', 'metric', 'created_at']

# Override the default admin site
admin.site = admin_site
admin.sites.site = admin_site