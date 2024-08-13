from django.urls import path, include
from rest_framework_nested import routers
from .views import *
from .interim.dashboard_computations import generate_automated_suggestions, performance_dashboard
from .interim.performance_analysis import forecast_vs_actual_comparison, probability_analysis, process_progress_tracking
from .interim.statistical_analysis import calculate_advanced_stats, calculate_aggregated_views, calculate_basic_stats
from .interim.experiment_analysis import ab_test_analysis, difference_in_differences
from .interim.data_export import bulk_export_data, prepare_data_for_bulk_import

# Main router for tenants (clients) 
router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')

# Nested router for projects within a client
client_router = routers.NestedDefaultRouter(router, r'clients', lookup='client')
client_router.register(r'projects', ProjectViewSet, basename='client-projects')
client_router.register(r'users', CustomUserViewSet, basename='client-users')
client_router.register(r'user-profiles', UserProfileViewSet, basename='client-user-profiles')
client_router.register(r'teams', TeamViewSet, basename='client-teams')

# Nested router for entities within a project
project_router = routers.NestedDefaultRouter(client_router, r'projects', lookup='project')
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
project_router.register(r'network-analysis-results', NetworkAnalysisResultViewSet, basename='project-network-analysis-results')
project_router.register(r'computation-status', ComputationStatusViewSet, basename='project-computation-status')
project_router.register(r'notifications', NotificationViewSet, basename='project-notifications')
project_router.register(r'pending-computations', PendingComputationViewSet, basename='project-pending-computations')

# Nested router for metric-related entities
metric_router = routers.NestedDefaultRouter(project_router, r'metrics', lookup='metric')
metric_router.register(r'historical-data', HistoricalDataViewSet, basename='metric-historical-data')
metric_router.register(r'metadata', MetricMetadataViewSet, basename='metric-metadata')
metric_router.register(r'targets', MetricTargetViewSet, basename='metric-targets')
metric_router.register(r'forecast', ForecastViewSet, basename='metric-forecast')
metric_router.register(r'anomaly', AnomalyViewSet, basename='metric-anomaly')
metric_router.register(r'trend', TrendViewSet, basename='metric-trend')
metric_router.register(r'correlations', CorrelationViewSet, basename='metric-correlations')
metric_router.register(r'connections', ConnectionViewSet, basename='metric-connections')
metric_router.register(r'data-quality-scores', DataQualityScoreViewSet, basename='metric-data-quality-scores')
metric_router.register(r'insights', InsightViewSet, basename='metric-insights')
metric_router.register(r'technical-indicators', TechnicalIndicatorViewSet, basename='metric-technical-indicators')
metric_router.register(r'moving-averages', MovingAverageViewSet, basename='metric-moving-averages')
metric_router.register(r'seasonality-results', SeasonalityResultViewSet, basename='metric-seasonality-results')
metric_router.register(r'trend-change-points', TrendChangePointViewSet, basename='metric-trend-change-points')

# Nested router for experiment within a project
experiment_router = routers.NestedDefaultRouter(project_router, r'experiments', lookup='experiment')
experiment_router.register(r'impact-analysis', ImpactAnalysisViewSet, basename='experiment-impact-analysis')

# Interim computation routes
interim_routes = [
    path('suggestions/', generate_automated_suggestions, name='get_automated_suggestions'),
    path('performance-dashboard/', performance_dashboard, name='get_performance_dashboard'),
    path('export/', bulk_export_data, name='export_data'),
    path('import/', bulk_export_data, name='import_historical_data'),
    path('statistical-analysis/', calculate_advanced_stats, name='get_statistical_analysis'),
    path('performance-analysis/', process_progress_tracking, name='get_performance_analysis'),
    path('experiment-analysis/', ab_test_analysis, name='run_experiment_analysis'),
    path('prepare-import/', prepare_data_for_bulk_import, name='prepare_bulk_import'),
    path('forecast-vs-actual/', forecast_vs_actual_comparison, name='forecast_vs_actual'),
    path('probability-analysis/', probability_analysis, name='probability_analysis'),
    path('aggregated-views/', calculate_aggregated_views, name='aggregated_views'),
    path('basic-stats/', calculate_basic_stats, name='basic_stats'),
    path('difference-in-differences/', difference_in_differences, name='difference_in_differences'),
]

# Tenant and project creation flow routes
creation_flow_routes = [
    path('create-tenant/', create_tenant, name='create-tenant'),
    path('create-project/', create_project, name='create-project'),
    path('create-team/', create_team, name='create-team'),
    path('assign-team-members/', assign_team_members, name='assign-team-members'),
]

urlpatterns = [
    # Router URLs
    path('', include(router.urls)),
    path('', include(client_router.urls)),
    path('', include(project_router.urls)),
    path('', include(metric_router.urls)),
    path('', include(experiment_router.urls)),
    path('debug/', debug_view, name='debug_view'),
    
    # Interim computation routes
    path('metrics/<int:metric_id>/', include(interim_routes)),
    
    # Tenant and project creation flow routes
    path('', include(creation_flow_routes)),
]

# Documentation for URL patterns
"""
URL Patterns:

1. Client (Tenant) Level:
   - List/Create: 
     GET, POST /clients/
     Output: 
     [
       {
         "id": 1,
         "name": "Client Name",
         "created_at": "2023-05-20T10:30:00Z",
         "updated_at": "2023-05-20T10:30:00Z"
       },
       ...
     ]
   - Retrieve/Update/Delete: 
     GET, PUT, PATCH, DELETE /clients/{client_pk}/
     Output: 
     {
       "id": 1,
       "name": "Client Name",
       "created_at": "2023-05-20T10:30:00Z",
       "updated_at": "2023-05-20T10:30:00Z"
     }

2. Project Level:
   - List/Create: 
     GET, POST /clients/{client_pk}/projects/
     Output: 
     [
       {
         "id": 1,
         "name": "Project Name",
         "client": client_pk,
         "description": "Project description",
         "start_date": "2023-05-01",
         "end_date": "2023-12-31",
         "status": "active",
         "created_at": "2023-05-01T09:00:00Z",
         "updated_at": "2023-05-01T09:00:00Z"
       },
       ...
     ]
   - Retrieve/Update/Delete: 
     GET, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/
     Output: 
     {
       "id": 1,
       "name": "Project Name",
       "client": client_pk,
       "description": "Project description",
       "start_date": "2023-05-01",
       "end_date": "2023-12-31",
       "status": "active",
       "created_at": "2023-05-01T09:00:00Z",
       "updated_at": "2023-05-01T09:00:00Z"
     }
   
   Project-related entities:
   - Categories: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/categories/
     Output: 
     [
       {
         "id": 1,
         "name": "Category Name",
         "project": project_pk,
         "description": "Category description",
         "created_at": "2023-05-02T10:00:00Z",
         "updated_at": "2023-05-02T10:00:00Z"
       },
       ...
     ]
   - Tags: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/tags/
     Output: 
     [
       {
         "id": 1,
         "name": "Tag Name",
         "project": project_pk,
         "created_at": "2023-05-02T11:00:00Z",
         "updated_at": "2023-05-02T11:00:00Z"
       },
       ...
     ]
   - Dashboards: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/dashboards/
     Output: 
     [
       {
         "id": 1,
         "name": "Dashboard Name",
         "project": project_pk,
         "layout": {...},
         "created_at": "2023-05-03T09:00:00Z",
         "updated_at": "2023-05-03T09:00:00Z"
       },
       ...
     ]
      - Experiments: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/experiments/
     Output: 
     [
       {
         "id": 1,
         "name": "Experiment Name",
         "project": project_pk,
         "description": "Experiment description",
         "start_date": "2023-06-01",
         "end_date": "2023-06-30",
         "status": "running",
         "created_at": "2023-06-01T09:00:00Z",
         "updated_at": "2023-06-01T09:00:00Z"
       },
       ...
     ]
   - Reports: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/reports/
     Output: 
     [
       {
         "id": 1,
         "name": "Report Name",
         "project": project_pk,
         "content": "Report content",
         "created_at": "2023-06-02T10:00:00Z",
         "updated_at": "2023-06-02T10:00:00Z"
       },
       ...
     ]
   - Strategies: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/strategies/
     Output: 
     [
       {
         "id": 1,
         "name": "Strategy Name",
         "project": project_pk,
         "description": "Strategy description",
         "status": "active",
         "created_at": "2023-06-03T11:00:00Z",
         "updated_at": "2023-06-03T11:00:00Z"
       },
       ...
     ]
   - Action Remarks: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/action-remarks/
     Output: 
     [
       {
         "id": 1,
         "content": "Action Remark Content",
         "project": project_pk,
         "author": 1,
         "created_at": "2023-06-04T12:00:00Z",
         "updated_at": "2023-06-04T12:00:00Z"
       },
       ...
     ]
   - Tactical Solutions: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/tactical-solutions/
     Output: 
     [
       {
         "id": 1,
         "name": "Tactical Solution Name",
         "project": project_pk,
         "description": "Tactical solution description",
         "status": "implemented",
         "created_at": "2023-06-05T13:00:00Z",
         "updated_at": "2023-06-05T13:00:00Z"
       },
       ...
     ]
   - Time Dimensions: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/time-dimensions/
     Output: 
     [
       {
         "id": 1,
         "name": "Time Dimension Name",
         "project": project_pk,
         "type": "daily",
         "start_date": "2023-01-01",
         "end_date": "2023-12-31",
         "created_at": "2023-06-06T14:00:00Z",
         "updated_at": "2023-06-06T14:00:00Z"
       },                     
       ...
     ]
   - Network Analysis Results:
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/network-analysis-results/
     Output: 
     [
       {
         "id": 1,
         "project": project_pk,
         "result_data": {...},
         "created_at": "2023-06-08T15:00:00Z",
         "updated_at": "2023-06-08T15:00:00Z"
       },
       ...
     ]
   - Computation Status:
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/computation-status/
     Output: 
     [
       {
         "id": 1,
         "project": project_pk,
         "computation_type": "forecast",
         "status": "completed",
         "created_at": "2023-06-08T16:00:00Z",
         "updated_at": "2023-06-08T16:00:00Z"
       },
       ...
     ]
   - Notifications:
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/notifications/
     Output: 
     [
       {
         "id": 1,
         "project": project_pk,
         "message": "Notification message",
         "is_read": false,
         "created_at": "2023-06-08T17:00:00Z",
         "updated_at": "2023-06-08T17:00:00Z"
       },
       ...
     ]
   - Pending Computations:
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/pending-computations/
     Output: 
     [
       {
         "id": 1,
         "project": project_pk,
         "computation_type": "trend_analysis",
         "status": "pending",
         "created_at": "2023-06-08T18:00:00Z",
         "updated_at": "2023-06-08T18:00:00Z"
       },
       ...
     ]

3. Metric Level:
   - List/Create: 
     GET, POST /clients/{client_pk}/projects/{project_pk}/metrics/
     Output: 
     [
       {
         "id": 1,
         "name": "Metric Name",
         "project": project_pk,
         "type": "KPI",
         "value_type": "numeric",
         "description": "Metric description",
         "created_at": "2023-06-07T09:00:00Z",
         "updated_at": "2023-06-07T09:00:00Z"
       },
       ...
     ]
   - Retrieve/Update/Delete: 
     GET, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/
     Output: 
     {
       "id": 1,
       "name": "Metric Name",
       "project": project_pk,
       "type": "KPI",
       "value_type": "numeric",
       "description": "Metric description",
       "created_at": "2023-06-07T09:00:00Z",
       "updated_at": "2023-06-07T09:00:00Z"
     }
   
   Metric-related entities:
   - Historical Data: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/historical-data/
     Output: 
     [
       {
         "id": 1,
         "date": "2023-05-20",
         "value": 100,
         "metric": metric_pk,
         "created_at": "2023-06-07T10:00:00Z",
         "updated_at": "2023-06-07T10:00:00Z"
       },
       ...
     ]
   - Metadata: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/metadata/
     Output: 
     {
       "id": 1,
       "key": "metadata_key",
       "value": "metadata_value",
       "metric": metric_pk,
       "created_at": "2023-06-07T11:00:00Z",
       "updated_at": "2023-06-07T11:00:00Z"
     }
   - Targets: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/targets/
     Output: 
     [
       {
         "id": 1,
         "target_value": 1000,
         "target_date": "2023-12-31",
         "metric": metric_pk,
         "created_at": "2023-06-07T12:00:00Z",
         "updated_at": "2023-06-07T12:00:00Z"
       },
       ...
     ]
   - Forecast: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/forecast/
     Output: 
     [
       {
         "id": 1,
         "forecast_date": "2023-06-01",
         "forecast_value": 150,
         "metric": metric_pk,
         "created_at": "2023-06-07T13:00:00Z",
         "updated_at": "2023-06-07T13:00:00Z"
       },
       ...
     ]
   - Anomaly: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/anomaly/
     Output: 
     [
       {
         "id": 1,
         "date": "2023-05-25",
         "value": 200,
         "is_anomaly": true,
         "metric": metric_pk,
         "created_at": "2023-06-07T14:00:00Z",
         "updated_at": "2023-06-07T14:00:00Z"
       },
       ...
     ]
   - Trend: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/trend/
     Output: 
     [
       {
         "id": 1,
         "start_date": "2023-05-01",
         "end_date": "2023-05-31",
         "trend_value": 0.05,
         "metric": metric_pk,
         "created_at": "2023-06-07T15:00:00Z",
         "updated_at": "2023-06-07T15:00:00Z"
       },
       ...
     ]
   - Correlations: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/correlations/
     Output: 
     [
       {
         "id": 1,
         "correlated_metric": 2,
         "correlation_coefficient": 0.75,
         "metric": metric_pk,
         "created_at": "2023-06-07T16:00:00Z",
         "updated_at": "2023-06-07T16:00:00Z"
       },
       ...
     ]
   - Connections: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/connections/
     Output: 
     [
       {
         "id": 1,
         "connected_metric": 3,
         "connection_type": "causal",
         "metric": metric_pk,
         "created_at": "2023-06-07T17:00:00Z",
         "updated_at": "2023-06-07T17:00:00Z"
       },
       ...
     ]
   - Data Quality Scores: 
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/data-quality-scores/
     Output: 
     [
       {
         "id": 1,
         "score": 0.95,
         "date": "2023-05-20",
         "metric": metric_pk,
         "created_at": "2023-06-07T18:00:00Z",
         "updated_at": "2023-06-07T18:00:00Z"
       },
       ...
     ]
   - Insights:
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/insights/
     Output: 
     [
       {
         "id": 1,
         "metric": metric_pk,
         "content": "Insight content",
         "created_at": "2023-06-08T09:00:00Z",
         "updated_at": "2023-06-08T09:00:00Z"
       },
       ...
     ]
   - Technical Indicators:
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/technical-indicators/
     Output: 
     [
       {
         "id": 1,
         "metric": metric_pk,
         "indicator_type": "RSI",
         "value": 70,
         "date": "2023-06-08",
         "created_at": "2023-06-08T10:00:00Z",
         "updated_at": "2023-06-08T10:00:00Z"
       },
       ...
     ]
   - Moving Averages:
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/moving-averages/
     Output: 
     [
       {
         "id": 1,
         "metric": metric_pk,
         "window_size": 7,
         "value": 105.5,
         "date": "2023-06-08",
         "created_at": "2023-06-08T12:00:00Z",
         "updated_at": "2023-06-08T12:00:00Z"
       },
       ...
     ]
   - Seasonality Results:
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/seasonality-results/
     Output: 
     [
       {
         "id": 1,
         "metric": metric_pk,
         "seasonality_type": "weekly",
         "strength": 0.6,
         "created_at": "2023-06-08T13:00:00Z",
         "updated_at": "2023-06-08T13:00:00Z"
       },
       ...
     ]
   - Trend Change Points:
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/metrics/{metric_pk}/trend-change-points/
     Output: 
     [
       {
         "id": 1,
         "metric": metric_pk,
         "change_date": "2023-06-01",
         "change_magnitude": 0.15,
         "created_at": "2023-06-08T14:00:00Z",
         "updated_at": "2023-06-08T14:00:00Z"
       },
       ...
     ]

4. Experiment Analysis:
   - Impact Analysis:
     GET, POST, PUT, PATCH, DELETE /clients/{client_pk}/projects/{project_pk}/experiments/{experiment_pk}/impact-analysis/
     Output: 
     [
       {
         "id": 1,
         "metric": metric_pk,
         "impact_value": 0.15,
         "created_at": "2023-06-08T15:00:00Z",
         "updated_at": "2023-06-08T15:00:00Z"
       },
       ...
     ]

5. Non-nested entities:
   - Users: 
     GET, POST, PUT, PATCH, DELETE /users/
     Output: 
     [
       {
         "id": 1,
         "username": "johndoe",
         "email": "john@example.com",
         "first_name": "John",
         "last_name": "Doe",
         "is_active": true,
         "date_joined": "2023-06-01T10:00:00Z"
       },
       ...
     ]
   - User Profiles: 
     GET, POST, PUT, PATCH, DELETE /user-profiles/
     Output: 
     [
       {
         "id": 1,
         "user": 1,
         "bio": "A short bio",
         "location": "New York",
         "birth_date": "1990-01-01",
         "created_at": "2023-06-01T10:00:00Z",
         "updated_at": "2023-06-01T10:00:00Z"
       },
       ...
     ]
   - Teams: 
     GET, POST, PUT, PATCH, DELETE /teams/
     Output: 
     [
       {
         "id": 1,
         "name": "Team Alpha",
         "description": "A team description",
         "created_at": "2023-06-01T10:00:00Z",
         "updated_at": "2023-06-01T10:00:00Z",
         "members": [1, 2, 3]
       },
       ...
     ]

6. Interim Computation Routes:
   - Statistical Analysis: 
     GET /metrics/{metric_id}/statistical-analysis/
     Input: ?type=basic (or advanced, aggregated)
     Output: {"task_id": "12345-abcde-67890"}

   - Performance Analysis: 
     GET /metrics/{metric_id}/performance-analysis/
     Input: ?type=forecast_vs_actual (or probability_analysis, process_progress_tracking)
     Output: {"task_id": "12345-abcde-67890"}

   - Experiment Analysis: 
     POST /metrics/{metric_id}/experiment-analysis/
     Input: 
     {
       "type": "ab_test",
       "control_group": "A",
       "treatment_group": "B"
     }
     Output: {"task_id": "12345-abcde-67890"}

   - Automated Suggestions: 
     GET /metrics/{metric_id}/automated-suggestions/
     Output: {"task_id": "12345-abcde-67890"}

   - Performance Dashboard: 
     GET /metrics/{metric_id}/performance-dashboard/
     Input: ?current_date=2023-06-01
     Output: {"task_id": "12345-abcde-67890"}

   - Export Data: 
     GET /metrics/{metric_id}/export-data/
     Input: ?start_date=2023-01-01&end_date=2023-06-01&data_type=raw
     Output: {"task_id": "12345-abcde-67890"}

   - Task Status: 
     GET /task-status/{task_id}/
     Output: 
     {
       "status": "completed",
       "result": {
         // Task-specific result data
       }
     }

   - Prepare Bulk Import: 
     POST /metrics/{metric_id}/prepare-import/
     Input: {"sheet_url": "https://docs.google.com/spreadsheets/d/..."}
     Output: 
     {
       "preview": [
         {"date": "2023-05-20", "value": 100},
         ...
       ],
       "column_mapping": {...}
     }

   - Import Historical Data: 
     POST /metrics/{metric_id}/import-historical-data/
     Input: 
     {
       "data": [
         {"date": "2023-05-20", "value": 100},
         ...
       ]
     }
     Output: {"message": "Successfully imported 100 data points"}
  
      - Forecast vs Actual Comparison:
     GET /metrics/{metric_id}/forecast-vs-actual/
     Output: 
     [
       {
         "date": "2023-06-01",
         "forecast": 100,
         "actual": 105,
         "difference": 5
       },
       ...
     ]

   - Probability Analysis:
     GET /metrics/{metric_id}/probability-analysis/
     Output: 
     {
       "target_value": 1000,
       "target_date": "2023-12-31",
       "probability_of_achieving": 0.75
     }

   - Advanced Stats:
     GET /metrics/{metric_id}/advanced-stats/
     Output: 
     {
       "skewness": 0.5,
       "kurtosis": 3.2,
       "autocorrelation": 0.7,
       "stationarity": 0.01
     }

   - Aggregated Views:
     GET /metrics/{metric_id}/aggregated-views/
     Output: 
     {
       "daily": {"2023-06-01": 100, "2023-06-02": 105, ...},
       "weekly": {"2023-W22": 102, "2023-W23": 107, ...},
       "monthly": {"2023-06": 105, "2023-07": 110, ...}
     }

   - Basic Stats:
     GET /metrics/{metric_id}/basic-stats/
     Output: 
     {
       "mean": 100,
       "median": 98,
       "std": 10,
       "min": 80,
       "max": 120
     }
      - Difference in Differences Analysis:
     POST /metrics/{metric_id}/difference-in-differences/
     Input: 
     {
       "control_group": "A",
       "treatment_group": "B",
       "pre_period": "2023-04-01",
       "post_period": "2023-05-01"
     }
     Output: 
     {
       "diff_in_diff": 0.15,
       "p_value": 0.03,
       "standard_error": 0.05,
       "confidence_interval": [0.05, 0.25]
     }

6. Tenant and project creation flow routes:
   - Create Tenant: 
     POST /create-tenant/
     Input: {"name": "New Tenant", "subdomain": "new-tenant"}
     Output: {"message": "Tenant New Tenant created successfully"}

   - Create Project: 
     POST /create-project/
     Input: {"name": "New Project", "client": 1}
     Output: {"message": "Project created successfully", "id": 1}

   - Create Team: 
     POST /create-team/
     Input: {"name": "New Team", "members": [1, 2, 3]}
     Output: {"message": "Team created successfully", "id": 1}

   - Assign Team Members: 
     POST /assign-team-members/
     Input: {"team": 1, "members": [4, 5, 6]}
     Output: {"message": "Team members assigned successfully"}
"""