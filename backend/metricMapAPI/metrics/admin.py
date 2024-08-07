from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django_tenants.utils import get_public_schema_name
from django_tenants.admin import TenantAdminMixin
from django.utils.html import format_html
from django.db import connection
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.offline as opy
from .models import (
    Client, CustomUser, UserProfile, Team, Project, Category, Tag, Metric,
    MetricMetadata, MetricTarget, Correlation, Connection, HistoricalData,
    Experiment, Forecast, Anomaly, Trend, Dashboard, Report, ActionRemark,
    Strategy, TacticalSolution, DataQualityScore, TimeDimension, ComputationStatus,
    Notification, PendingComputation, TechnicalIndicator, ImpactAnalysis,
    MovingAverage, SeasonalityResult, TrendChangePoint, Insight, NetworkAnalysisResult, Domain
)
import logging
from rest_framework.authtoken.models import Token

logger = logging.getLogger(__name__)

class MetricMapAdminSite(admin.AdminSite):
    def each_context(self, request):
        context = super().each_context(request)
        schema_name = connection.schema_name
        if schema_name == get_public_schema_name():
            tenant_name = 'Public'
        else:
            tenant_name = getattr(request.tenant, 'name', 'Unknown')
        
        context.update({
            'site_header': _('Metric Map Administration - {}'.format(tenant_name)),
            'site_title': _('Metric Map Admin - {}'.format(tenant_name)),
            'index_title': _('Welcome to Metric Map - {}'.format(tenant_name)),
        })
        return context

    def get_app_list(self, request, app_label=None):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request, app_label)
        
        if connection.schema_name == get_public_schema_name():
            # Customized app_list for public schema
            app_list = [
                {
                    'name': _('Tenant Management'),
                    'app_label': 'tenant_management',
                    'models': [
                        {
                            'name': _('Clients'),
                            'object_name': 'Client',
                            'admin_url': '/admin/metrics/client/',
                            'add_url': '/admin/metrics/client/add/',
                        },
                        {
                            'name': _('Domains'),
                            'object_name': 'Domain',
                            'admin_url': '/admin/metrics/domain/',
                            'add_url': '/admin/metrics/domain/add/',
                        },
                    ],
                },
                {
                    'name': _('User Management'),
                    'app_label': 'auth',
                    'models': [
                        {
                            'name': _('Users'),
                            'object_name': 'CustomUser',
                            'admin_url': '/admin/metrics/customuser/',
                            'add_url': '/admin/metrics/customuser/add/',
                        },
                        {
                            'name': _('Groups'),
                            'object_name': 'Group',
                            'admin_url': '/admin/auth/group/',
                            'add_url': '/admin/auth/group/add/',
                        },
                    ],
                },
            ]
        else:
            # Customized app_list for tenant schemas
            app_list = [
                {
                    'name': _('Project Nested Configuration'),
                    'app_label': 'project_config',
                    'models': [
                        {'name': _('Projects'), 'object_name': 'Project', 'admin_url': '/admin/metrics/project/'},
                        {'name': _('Categories'), 'object_name': 'Category', 'admin_url': '/admin/metrics/category/'},
                        {'name': _('Dashboards'), 'object_name': 'Dashboard', 'admin_url': '/admin/metrics/dashboard/'},
                        {'name': _('Reports'), 'object_name': 'Report', 'admin_url': '/admin/metrics/report/'},
                        {'name': _('Tags'), 'object_name': 'Tag', 'admin_url': '/admin/metrics/tag/'},
                        {'name': _('Time Dimensions'), 'object_name': 'TimeDimension', 'admin_url': '/admin/metrics/timedimension/'},
                    ]
                },
                {
                    'name': _('Manage Metrics'),
                    'app_label': 'manage_metrics',
                    'models': [
                        {'name': _('Metrics'), 'object_name': 'Metric', 'admin_url': '/admin/metrics/metric/'},
                        {'name': _('Metric Targets'), 'object_name': 'MetricTarget', 'admin_url': '/admin/metrics/metrictarget/'},
                        {'name': _('Historical Data'), 'object_name': 'HistoricalData', 'admin_url': '/admin/metrics/historicaldata/'},
                        {'name': _('Data Quality Scores'), 'object_name': 'DataQualityScore', 'admin_url': '/admin/metrics/dataqualityscore/'},
                    ]
                },
                {
                    'name': _('Manage Strategy'),
                    'app_label': 'manage_strategy',
                    'models': [
                        {'name': _('Forecasts'), 'object_name': 'Forecast', 'admin_url': '/admin/metrics/forecast/'},
                    ]
                },
                {
                    'name': _('Manage Technical Indicator'),
                    'app_label': 'manage_technical_indicator',
                    'models': [
                        {'name': _('Technical Indicators'), 'object_name': 'TechnicalIndicator', 'admin_url': '/admin/metrics/technicalindicator/'},
                        {'name': _('Anomalies'), 'object_name': 'Anomaly', 'admin_url': '/admin/metrics/anomaly/'},
                        {'name': _('Impact Analyses'), 'object_name': 'ImpactAnalysis', 'admin_url': '/admin/metrics/impactanalysis/'},
                        {'name': _('Trends'), 'object_name': 'Trend', 'admin_url': '/admin/metrics/trend/'},
                        {'name': _('Moving Averages'), 'object_name': 'MovingAverage', 'admin_url': '/admin/metrics/movingaverage/'},
                        {'name': _('Seasonality Results'), 'object_name': 'SeasonalityResult', 'admin_url': '/admin/metrics/seasonalityresult/'},
                        {'name': _('Trend Change Points'), 'object_name': 'TrendChangePoint', 'admin_url': '/admin/metrics/trendchangepoint/'},
                    ]
                },
                {
                    'name': _('Manage Execution'),
                    'app_label': 'manage_execution',
                    'models': [
                        {'name': _('Experiments'), 'object_name': 'Experiment', 'admin_url': '/admin/metrics/experiment/'},
                        {'name': _('Action Remarks'), 'object_name': 'ActionRemark', 'admin_url': '/admin/metrics/actionremark/'},
                        {'name': _('Insights'), 'object_name': 'Insight', 'admin_url': '/admin/metrics/insight/'},
                        {'name': _('Strategies'), 'object_name': 'Strategy', 'admin_url': '/admin/metrics/strategy/'},
                        {'name': _('Tactical Solutions'), 'object_name': 'TacticalSolution', 'admin_url': '/admin/metrics/tacticalsolution/'},
                    ]
                },
                {
                    'name': _('Manage Relationships'),
                    'app_label': 'manage_relationships',
                    'models': [
                        {'name': _('Correlations'), 'object_name': 'Correlation', 'admin_url': '/admin/metrics/correlation/'},
                        {'name': _('Connections'), 'object_name': 'Connection', 'admin_url': '/admin/metrics/connection/'},
                        {'name': _('Network Analysis Results'), 'object_name': 'NetworkAnalysisResult', 'admin_url': '/admin/metrics/networkanalysisresult/'},
                    ]
                },
                {
                    'name': _('Manage System Utils'),
                    'app_label': 'manage_system_utils',
                    'models': [
                        {'name': _('Computation Statuses'), 'object_name': 'ComputationStatus', 'admin_url': '/admin/metrics/computationstatus/'},
                        {'name': _('Notifications'), 'object_name': 'Notification', 'admin_url': '/admin/metrics/notification/'},
                        {'name': _('Pending Computations'), 'object_name': 'PendingComputation', 'admin_url': '/admin/metrics/pendingcomputation/'},
                    ]
                },
            ]
        return app_list

admin_site = MetricMapAdminSite(name='metricmap_admin')

@admin.register(Client, site=admin_site)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'created_on']
    search_fields = ['name']
    
@admin.register(Domain, site=admin_site)
class DomainAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['domain', 'tenant', 'is_primary']
    search_fields = ['domain', 'tenant__name']

@admin.register(CustomUser, site=admin_site)
class CustomUserAdmin(TenantAdminMixin, UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'tenant']
    list_filter = ['is_staff', 'is_superuser', 'tenant']
    fieldsets = UserAdmin.fieldsets + (
        ('Tenant Information', {'fields': ('tenant',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Tenant Information', {'fields': ('tenant',)}),
    )

@admin.register(UserProfile, site=admin_site)
class UserProfileAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['user', 'tenant']
    search_fields = ['user__username', 'user__email', 'tenant__name']

@admin.register(Team, site=admin_site)
class TeamAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'description', 'tenant']
    search_fields = ['name', 'description', 'tenant__name']

@admin.register(Project, site=admin_site)
class ProjectAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'created_on', 'tenant']
    list_filter = ['tenant']
    search_fields = ['name', 'tenant__name']

@admin.register(Category, site=admin_site)
class CategoryAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'tenant']
    list_filter = ['tenant']
    search_fields = ['name', 'tenant__name']

@admin.register(Dashboard, site=admin_site)
class DashboardAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'tenant']
    list_filter = ['tenant']
    search_fields = ['name', 'tenant__name']

@admin.register(Report, site=admin_site)
class ReportAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'metric', 'tenant', 'created_at', 'updated_at']
    list_filter = ['tenant', 'created_at', 'updated_at']
    search_fields = ['name', 'metric__name', 'tenant__name']

@admin.register(Tag, site=admin_site)
class TagAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'project', 'tenant']
    list_filter = ['project', 'tenant']
    search_fields = ['name', 'project__name', 'tenant__name']

@admin.register(TimeDimension, site=admin_site)
class TimeDimensionAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['date', 'day', 'month', 'year', 'is_weekend', 'is_holiday', 'tenant']
    list_filter = ['is_weekend', 'is_holiday', 'tenant']
    search_fields = ['date', 'tenant__name']

class MetricMetadataInline(admin.StackedInline):
    model = MetricMetadata
    extra = 1

@admin.register(Metric, site=admin_site)
class MetricAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'type', 'value_type', 'category', 'tenant']
    list_filter = ['type', 'value_type', 'category', 'tenant']
    search_fields = ['name', 'description', 'tenant__name']
    inlines = [MetricMetadataInline]

    def chart_view(self, obj):
        historical_data = HistoricalData.objects.filter(metric=obj).order_by('date')
        forecasts = Forecast.objects.filter(metric=obj).order_by('forecast_date')

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(
            go.Scatter(x=[hd.date for hd in historical_data], y=[hd.value for hd in historical_data], name="Actual"),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(x=[f.forecast_date for f in forecasts], y=[f.forecast_value for f in forecasts], name="Forecast"),
            secondary_y=True,
        )

        fig.update_layout(title_text=f"Actual vs Forecast for {obj.name}")
        fig.update_xaxes(title_text="Date")
        fig.update_yaxes(title_text="Value", secondary_y=False)
        fig.update_yaxes(title_text="Forecast", secondary_y=True)

        div = opy.plot(fig, auto_open=False, output_type='div')
        return format_html(div)

    chart_view.short_description = 'Chart View'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        obj = self.get_object(request, object_id)
        if obj:
            extra_context['chart_view'] = self.chart_view(obj)
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

@admin.register(MetricTarget, site=admin_site)
class MetricTargetAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'target_value', 'target_date', 'tenant']
    list_filter = ['metric', 'tenant']
    search_fields = ['metric__name', 'tenant__name']

@admin.register(HistoricalData, site=admin_site)
class HistoricalDataAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'date', 'value', 'tenant']
    list_filter = ['metric', 'tenant']
    search_fields = ['metric__name', 'tenant__name']
    date_hierarchy = 'date'

@admin.register(DataQualityScore, site=admin_site)
class DataQualityScoreAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'overall_score', 'data_entry', 'tenant']
    list_filter = ['metric', 'tenant']
    search_fields = ['metric__name', 'tenant__name']

@admin.register(Forecast, site=admin_site)
class ForecastAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'forecast_date', 'forecast_value', 'tenant']
    list_filter = ['metric', 'tenant']
    search_fields = ['metric__name', 'tenant__name']
    date_hierarchy = 'forecast_date'

@admin.register(TechnicalIndicator, site=admin_site)
class TechnicalIndicatorAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'date', 'stochastic_value', 'rsi_value', 'percent_change', 'moving_average', 'tenant']
    list_filter = ['metric', 'date', 'tenant']
    search_fields = ['metric__name', 'tenant__name']
    date_hierarchy = 'date'

@admin.register(Anomaly, site=admin_site)
class AnomalyAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'anomaly_type', 'quality', 'tenant']
    list_filter = ['metric', 'anomaly_type', 'quality', 'tenant']
    search_fields = ['metric__name', 'tenant__name']

@admin.register(ImpactAnalysis, site=admin_site)
class ImpactAnalysisAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'experiment', 'tenant']
    list_filter = ['metric', 'experiment', 'tenant']
    search_fields = ['metric__name', 'experiment__name', 'tenant__name']

@admin.register(Trend, site=admin_site)
class TrendAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'start_date', 'end_date', 'trend_type', 'tenant']
    list_filter = ['metric', 'trend_type', 'tenant']
    search_fields = ['metric__name', 'tenant__name']
    date_hierarchy = 'start_date'

@admin.register(MovingAverage, site=admin_site)
class MovingAverageAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'date', 'value', 'tenant']
    list_filter = ['metric', 'tenant']
    search_fields = ['metric__name', 'tenant__name']
    date_hierarchy = 'date'

@admin.register(SeasonalityResult, site=admin_site)
class SeasonalityResultAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'get_tenant']
    list_filter = ['metric']
    search_fields = ['metric__name', 'metric__tenant__name']
    
    def get_tenant(self, obj):
        return obj.metric.tenant
    get_tenant.short_description = 'Tenant'

@admin.register(TrendChangePoint, site=admin_site)
class TrendChangePointAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'get_tenant']
    list_filter = ['metric']
    search_fields = ['metric__name', 'metric__tenant__name']
    
    def get_tenant(self, obj):
        return obj.metric.tenant
    get_tenant.short_description = 'Tenant'

@admin.register(Experiment, site=admin_site)
class ExperimentAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'status', 'tenant']
    list_filter = ['status', 'tenant']
    search_fields = ['name', 'description', 'tenant__name']
    filter_horizontal = ['metrics']
    date_hierarchy = 'start_date'

@admin.register(ActionRemark, site=admin_site)
class ActionRemarkAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'date', 'title', 'impact', 'importance', 'tenant']
    list_filter = ['impact', 'importance', 'tenant']
    search_fields = ['metric__name', 'title', 'summary', 'tenant__name']
    date_hierarchy = 'date'

@admin.register(Insight, site=admin_site)
class InsightAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'user', 'date', 'title', 'tenant']
    list_filter = ['metric', 'user', 'tenant']
    search_fields = ['metric__name', 'user__username', 'title', 'content', 'tenant__name']
    date_hierarchy = 'date'

@admin.register(Strategy, site=admin_site)
class StrategyAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'team', 'estimated_time', 'tenant']
    list_filter = ['team', 'tenant']
    search_fields = ['title', 'description', 'team__name', 'tenant__name']

@admin.register(TacticalSolution, site=admin_site)
class TacticalSolutionAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'title', 'tenant']
    list_filter = ['metric', 'tenant']
    search_fields = ['title', 'description', 'metric__name', 'tenant__name']

@admin.register(Correlation, site=admin_site)
class CorrelationAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric1', 'metric2', 'tenant']
    list_filter = ['tenant']
    search_fields = ['metric1__name', 'metric2__name', 'tenant__name']

@admin.register(Connection, site=admin_site)
class ConnectionAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['from_metric', 'to_metric', 'strength', 'tenant']
    list_filter = ['tenant']
    search_fields = ['from_metric__name', 'to_metric__name', 'tenant__name']

@admin.register(NetworkAnalysisResult, site=admin_site)
class NetworkAnalysisResultAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'analysis_type', 'tenant']
    list_filter = ['analysis_type', 'tenant']
    search_fields = ['metric__name', 'analysis_type', 'tenant__name']

@admin.register(ComputationStatus, site=admin_site)
class ComputationStatusAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['status', 'created_at', 'updated_at', 'tenant']
    list_filter = ['status', 'tenant']
    search_fields = ['error_message', 'tenant__name']
    date_hierarchy = 'created_at'

@admin.register(Notification, site=admin_site)
class NotificationAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['message', 'created_at', 'is_read', 'tenant']
    list_filter = ['is_read', 'tenant']
    search_fields = ['message', 'tenant__name']
    date_hierarchy = 'created_at'

@admin.register(PendingComputation, site=admin_site)
class PendingComputationAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['metric', 'created_at', 'tenant']
    list_filter = ['tenant']
    search_fields = ['metric__name', 'tenant__name']
    date_hierarchy = 'created_at'

# Register Group model
admin_site.register(Group)

# Override the default admin site
admin.site = admin_site
admin.sites.site = admin_site

# Register Token model for token authentication
admin_site.register(Token)