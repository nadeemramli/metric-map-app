from django.urls import path, include
from rest_framework_nested import routers
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
project_router.register(r'categories', CategoryViewSet, basename='project-categories')
project_router.register(r'tags', TagViewSet, basename='project-tags')
project_router.register(r'dashboards', DashboardViewSet, basename='project-dashboards')
project_router.register(r'experiments', ExperimentViewSet, basename='project-experiments')
project_router.register(r'reports', ReportViewSet, basename='project-reports')
project_router.register(r'strategies', StrategyViewSet, basename='project-strategies')
project_router.register(r'action-remarks', ActionRemarkViewSet, basename='project-action-remarks')
project_router.register(r'tactical-solutions', TacticalSolutionViewSet, basename='project-tactical-solutions')
project_router.register(r'time-dimensions', TimeDimensionViewSet, basename='project-time-dimensions')


# Nested router for metric-related entities
metric_router = routers.NestedSimpleRouter(project_router, r'metrics', lookup='metric')
metric_router.register(r'historical-data', HistoricalDataViewSet, basename='metric-historical-data')
metric_router.register(r'metadata', MetricMetadataViewSet, basename='metric-metadata')
metric_router.register(r'targets', MetricTargetViewSet, basename='metric-targets')
metric_router.register(r'forecast', ForecastViewSet, basename='metric-forecast')
metric_router.register(r'anomaly', AnomalyViewSet, basename='metric-anomaly')
metric_router.register(r'trend', TrendViewSet, basename='metric-trend')
metric_router.register(r'correlations', CorrelationViewSet, basename='metric-correlations')
metric_router.register(r'connections', ConnectionViewSet, basename='metric-connections')
metric_router.register(r'data-quality-scores', DataQualityScoreViewSet, basename='metric-data-quality-scores')


# Router for non-nested viewsets
router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'user-profiles', UserProfileViewSet, basename='user-profiles')
router.register(r'teams', TeamViewSet, basename='teams')

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
   
   Project-related entities:
   - Categories: /clients/{client_pk}/projects/{project_pk}/categories/
   - Tags: /clients/{client_pk}/projects/{project_pk}/tags/
   - Dashboards: /clients/{client_pk}/projects/{project_pk}/dashboards/
   - Experiments: /clients/{client_pk}/projects/{project_pk}/experiments/
   - Reports: /clients/{client_pk}/projects/{project_pk}/reports/
   - Strategies: /clients/{client_pk}/projects/{project_pk}/strategies/
   - Action Remarks: /clients/{client_pk}/projects/{project_pk}/action-remarks/
   - Tactical Solutions: /clients/{client_pk}/projects/{project_pk}/tactical-solutions/
   - Time Dimensions: /clients/{client_pk}/projects/{project_pk}/time-dimensions/

3. Metric Level:
   - List/Create: /clients/{client_pk}/projects/{project_pk}/metrics/
   - Retrieve/Update/Delete: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/
   
   Metric-related entities:
   - Historical Data: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/historical-data/
   - Metadata: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/metadata/
   - Targets: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/targets/
   - Forecast: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/forecast/
   - Anomaly: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/anomaly/
   - Trend: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/trend/
   - Correlations: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/correlations/
   - Connections: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/connections/
   - Data Quality Scores: /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/data-quality-scores/

4. Non-nested entities:
   - Users: /users/
   - User Profiles: /user-profiles/
   - Teams: /teams/

5. Home:
   - Public Home: /
"""
