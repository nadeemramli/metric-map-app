from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

# Main router for tenants (clients) 
router = routers.SimpleRouter()
router.register(r'clients', ClientViewSet, basename='client')

# Nested router for projects within a client
client_router = routers.NestedSimpleRouter(router, r'clients', lookup='client')
client_router.register(r'projects', ProjectViewSet, basename='client-projects')

# Nested router for entities within a project
project_router = routers.NestedSimpleRouter(client_router, r'projects', lookup='project')
project_router.register(r'metrics', MetricViewSet, basename='project-metrics')
project_router.register(r'dashboards', DashboardViewSet, basename='project-dashboards')
project_router.register(r'experiments', ExperimentViewSet, basename='project-experiments')
project_router.register(r'categories', CategoryViewSet, basename='project-categories')
project_router.register(r'tags', TagViewSet, basename='project-tags')
project_router.register(r'connections', ConnectionViewSet, basename='project-connections')
project_router.register(r'targets', TargetViewSet, basename='project-targets')
project_router.register(r'reports', ReportViewSet, basename='project-reports')

# Nested router for historical data within a metric
metric_router = routers.NestedSimpleRouter(project_router, r'metrics', lookup='metric')
metric_router.register(r'historical-data', HistoricalDataViewSet,  basename='metric-historical-data')
metric_router.register(r'forecast', ForecastViewSet,  basename='metric-forecast')
metric_router.register(r'anomaly', AnomalyViewSet,  basename='metric-anomaly')
metric_router.register(r'trend', TrendViewSet,  basename='metric-trend')
metric_router.register(r'action-remarks', ActionRemarkViewSet, basename='metric-action-remarks')

urlpatterns = [
    # Router URLs
    path('', include(router.urls)),
    path('', include(client_router.urls)),
    path('', include(project_router.urls)),
    path('', include(metric_router.urls)),
]


# Documentation for URL patterns
"""
URL Patterns:

1. Client (Tenant) Level:
   - List/Create: /clients/
   - Retrieve/Update/Delete: /clients/{client_pk}/

2. Project Level:
   - List/Create: /clients/{client_pk}/projects/
   - Retrieve/Update/Delete: /clients/{client_pk}/projects/{project_pk}/

3. Metric Level:
   - List/Create: /clients/{client_pk}/projects/{project_pk}/metrics/
   - Retrieve/Update/Delete: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/
   
   Metric Actions:
   - Analyze: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/analyze/
   - Historical Data: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/historical-data/
   - Preprocess: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/preprocess/
   - Manage Data: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/manage_data/
   - Connections: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/connections/
   - Action Remarks: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/action_remarks/
   - Targets: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/targets/
   - Reports: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/reports/
   - Feedback: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/feedback/
   - Visualization: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/visualization/
   - Progress Tracking: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/progress_tracking/

4. Dashboard Level:
   - List/Create: /clients/{client_pk}/projects/{project_pk}/dashboards/
   - Retrieve/Update/Delete: /clients/{client_pk}/projects/{project_pk}/dashboards/{dashboard_pk}/
   
   Dashboard Actions:
   - Performance: /clients/{client_pk}/projects/{project_pk}/dashboards/performance/
   - Decision Support: /clients/{client_pk}/projects/{project_pk}/dashboards/decision_support/

5. Experiment Level:
   - List/Create: /clients/{client_pk}/projects/{project_pk}/experiments/
   - Retrieve/Update/Delete: /clients/{client_pk}/projects/{project_pk}/experiments/{experiment_pk}/
   
   Experiment Actions:
   - Run Experiment: /clients/{client_pk}/projects/{project_pk}/experiments/{experiment_pk}/run_experiment/

6. Other Project-level Entities:
   - Categories: /clients/{client_pk}/projects/{project_pk}/categories/
   - Tags: /clients/{client_pk}/projects/{project_pk}/tags/
   - Connections: /clients/{client_pk}/projects/{project_pk}/connections/
   - Targets: /clients/{client_pk}/projects/{project_pk}/targets/
   - Reports: /clients/{client_pk}/projects/{project_pk}/reports/

7. Historical Data:
   - List/Create: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/historical-data/
   - Retrieve/Update/Delete: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/historical-data/{id}/
   
   Historical Data Actions:
   - Bulk Import: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/historical-data/bulk_import/
   - Aggregated Views: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/historical-data/aggregated_views/
   - Advanced Statistics: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/historical-data/advanced_statistics/

8. Authentication:
   - Obtain Token: /token/
   - Refresh Token: /token/refresh/

9. Health Check:
   - Health Check: /health-check/
   
10. Forecast
11. Anomaly
12. Trends
"""