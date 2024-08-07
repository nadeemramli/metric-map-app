from django.test import TestCase
from django.utils import timezone
from django_tenants.test.cases import TenantTestCase
from django_tenants.utils import tenant_context, schema_context
from django.db import connection
from ...models import (
    Client, Domain, CustomUser, UserProfile, Team, Project, Category, Tag, Metric,
    MetricMetadata, MetricTarget, Correlation, Connection, HistoricalData,
    Experiment, Forecast, Anomaly, Trend, Dashboard, Report, ActionRemark,
    Strategy, TacticalSolution, DataQualityScore, TimeDimension, ValueType, MetricType,
    Rhythm, ExperimentStatus, Impact, Importance, AnomalyType, QualityType, Confidence,
    Insight, MovingAverage, TechnicalIndicator, ImpactAnalysis, SeasonalityResult,
    TrendChangePoint, NetworkAnalysisResult, ComputationStatus, Notification, PendingComputation
)
from ...serializers import (
    ClientSerializer, DomainSerializer, CustomUserSerializer, UserProfileSerializer,
    TeamSerializer, ProjectSerializer, CategorySerializer, TagSerializer, MetricSerializer,
    MetricMetadataSerializer, ExperimentSerializer, ReportSerializer, ActionRemarkSerializer,
    AnomalySerializer, InsightSerializer, TechnicalIndicatorSerializer, ImpactAnalysisSerializer,
    MovingAverageSerializer, SeasonalityResultSerializer, TrendChangePointSerializer,
    NetworkAnalysisResultSerializer, ComputationStatusSerializer, NotificationSerializer,
    PendingComputationSerializer, MetricTargetSerializer, CorrelationSerializer, ConnectionSerializer,
    HistoricalDataSerializer, ForecastSerializer, TrendSerializer,
    DashboardSerializer, StrategySerializer, TacticalSolutionSerializer,
    DataQualityScoreSerializer, TimeDimensionSerializer
)

class SerializerTestCase(TenantTestCase):
    def setUp(self):
        super().setUp()
        
        with schema_context('public'):
            self.tenant = Client.objects.create(
                name="Test Tenant",
                schema_name="test_tenant",
            )
            
            self.domain = Domain.objects.create(
                domain="test.localhost",
                tenant=self.tenant,
                is_primary=True
            )
        
        connection.set_tenant(self.tenant)
        
        # Create a team
        self.team = Team.objects.create(name="Test Team", description="Test Description")

        # Create a custom user
        self.user = CustomUser.objects.create(username="testuser", email="test@example.com", team=self.team)

        # Create a user profile
        self.user_profile = UserProfile.objects.create(user=self.user)

        # Create a project
        self.project = Project.objects.create(name="Test Project")

        # Create a category
        self.category = Category.objects.create(name="Test Category")

        # Create a tag
        self.tag = Tag.objects.create(name="Test Tag", project=self.project)

        # Create a metric
        self.metric = Metric.objects.create(
            name="Test Metric",
            type=MetricType.KPI.name,
            value_type=ValueType.COUNT.name,
            category=self.category,
            project=self.project
            )
        self.metric.tags.add(self.tag)

        # Create metric metadata
        self.metric_metadata = MetricMetadata.objects.create(
            metric=self.metric,
            data_source="Test Source",
            source_url="http://test.com",
            rhythm=Rhythm.DAILY.name,
            team=self.team,
            technical_description="Test Technical Description",
            description="Test Description",
            artifacts_url="http://artifacts.com",
            hypothesis="Test Hypothesis",
            confidence=Confidence.ON_TRACK.name,
            position_x=1.0,
            position_y=2.0
        )
        
        # Create a data quality score
        self.data_quality_score = DataQualityScore.objects.create(
            metric=self.metric,
            project=self.project,
            data_entry="Test Data Entry",
            completeness_score=0.95,
            accuracy_score=0.95,
            consistency_score=0.95,
            timeliness_score=0.95,
            overall_score=0.95
        )
        
        # Create a metric target
        self.metric_target = MetricTarget.objects.create(
            metric=self.metric,
            target_value=100.0,
            target_date=timezone.now() + timezone.timedelta(days=30)
        )

        # Create an experiment
        self.experiment = Experiment.objects.create(
            name="Test Experiment",
            description="Test Description",
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=30),
            status=ExperimentStatus.PLANNED.name
        )
        self.experiment.metrics.add(self.metric)

        # Create a report
        self.report = Report.objects.create(
            metric=self.metric,
            name="Test Report",
            configuration={"test": "config"},
            analysis_result={
                "trend": {"trend_type": "increasing", "start_date": "2023-01-01", "end_date": "2023-12-31", "trend_value": 10.5, "slope": 0.5},
                "technical_indicators": [{"date": "2023-12-31", "stochastic_value": 75.5, "rsi_value": 60.2, "percent_change": 2.5, "moving_average": 105.3}]
            },
            forecast_result={"sarima": [{"date": "2024-01-01", "value": 110.5, "lower_bound": 105.2, "upper_bound": 115.8, "confidence_interval": 0.95}]},
            anomaly_result={"anomalies": [{"date": "2023-06-15", "value": 150.0, "score": 0.95, "type": "SPIKE"}]},
            relationship_result={"correlations": [{"metric_id": 2, "pearson": 0.85, "spearman": 0.82}]},
            report="# Test Report\n\nThis is a test report."
        )

        # Create an action remark
        self.action_remark = ActionRemark.objects.create(
            metric=self.metric,
            title="Test Action",
            date=timezone.now(),
            summary="Test Summary",
            impact=Impact.POSITIVE.name,
            importance=Importance.MAJOR.name
        )

        # Create an anomaly
        self.anomaly = Anomaly.objects.create(
            metric=self.metric,
            detection_date=timezone.now(),
            anomaly_value=100.0,
            anomaly_score=0.95,
            notes="Test Notes",
            anomaly_type=AnomalyType.OPPORTUNITY.name,
            quality=QualityType.HIGH.name
        )

        # Create an insight
        self.insight = Insight.objects.create(
            metric=self.metric,
            user=self.user,
            date=timezone.now(),
            title="Test Insight",
            content="Test Content"
        )

        # Create a technical indicator
        self.technical_indicator = TechnicalIndicator.objects.create(
            metric=self.metric,
            date=timezone.now(),
            stochastic_value=75.5,
            rsi_value=60.2,
            percent_change=2.5,
            moving_average=105.3
        )

        # Create an impact analysis
        self.impact_analysis = ImpactAnalysis.objects.create(
            experiment=self.experiment,
            metric=self.metric,
            before_value=100.0,
            after_value=110.0,
            percentage_change=10.0,
            confidence=0.95,
            artifact_link="http://artifact.com"
        )

        # Create a moving average
        self.moving_average = MovingAverage.objects.create(
            metric=self.metric,
            date=timezone.now(),
            ma_type="SMA",
            period=7,
            value=105.3
        )

        # Create a seasonality result
        self.seasonality_result = SeasonalityResult.objects.create(
            metric=self.metric,
            seasonality_type="WEEKLY",
            strength=0.8,
            period=7
        )

        # Create a trend change point
        self.trend_change_point = TrendChangePoint.objects.create(
            metric=self.metric,
            date=timezone.now(),
            direction="INCREASING",
            significance=0.95
        )

        # Create a network analysis result
        self.network_analysis_result = NetworkAnalysisResult.objects.create(
            metric=self.metric,
            analysis_type="CENTRALITY",
            result={"centrality": 0.8}
        )

        # Create a computation status
        self.computation_status = ComputationStatus.objects.create(
            status="COMPLETED",
            error_message=""
        )

        # Create a notification
        self.notification = Notification.objects.create(
            message="Test Notification",
            is_read=False
        )

        # Create a pending computation
        self.pending_computation = PendingComputation.objects.create(
            metric=self.metric
        )

        # Create a correlation
        self.correlation = Correlation.objects.create(
            metric1=self.metric,
            metric2=self.metric,
            lag=2,
            pearson_correlation=0.85,
            spearman_correlation=0.82
        )

        # Create a connection
        self.connection = Connection.objects.create(
            from_metric=self.metric,
            to_metric=self.metric,
            relationship="CAUSAL",
            strength=0.7
        )

        # Create historical data
        self.historical_data = HistoricalData.objects.create(
            metric=self.metric,
            date=timezone.now(),
            value=95.5
        )

        # Create a forecast
        self.forecast = Forecast.objects.create(
            metric=self.metric,
            forecast_date=timezone.now() + timezone.timedelta(days=7),
            forecast_value=105.0,
            lower_bound=100.0,
            upper_bound=110.0,
            model_used="ARIMA",
            accuracy=0.95,
            confidence_interval={"lower": 100.0, "upper": 110.0},
            variance=0.05
        )

        # Create a trend
        self.trend = Trend.objects.create(
            metric=self.metric,
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=30),
            trend_type="INCREASING",
            trend_value=0.5
        )

        # Create a dashboard
        self.dashboard = Dashboard.objects.create(name="Test Dashboard")
        self.dashboard.metrics.add(self.metric)

        # Create a strategy
        self.strategy = Strategy.objects.create(
            title = "Test Strategy",
            description = "Test Strategy Description",
            team = self.team,
            estimated_time = timezone.timedelta(days=7),
            artifacts_url = "http://artifact.com",
            created_at = timezone.now(),
            updated_at = timezone.now()
        )

        # Create a tactical solution
        self.tactical_solution = TacticalSolution.objects.create(
            name="Test Tactical Solution",
            description="Test Tactical Solution Description",
            strategy=self.strategy
        )

        # Create a data quality score
        self.data_quality_score = DataQualityScore.objects.create(
            metric=self.metric,
            score=0.95,
            date=timezone.now()
        )

        # Create a time dimension
        self.time_dimension = TimeDimension.objects.create(
            name="Test Time Dimension",
            dimension_type="MONTH"
        )

    def tearDown(self):
        connection.set_schema_to_public()
        with schema_context('public'):
            self.tenant.delete()
        super().tearDown()
        
    def test_domain_serializer(self):
        serializer = DomainSerializer(instance=self.domain)
        self.assertEqual(serializer.data['domain'], "test.localhost")

    def test_custom_user_serializer(self):
        serializer = CustomUserSerializer(instance=self.user)
        self.assertEqual(serializer.data['username'], "testuser")

    def test_user_profile_serializer(self):
        serializer = UserProfileSerializer(instance=self.user_profile)
        self.assertEqual(serializer.data['user'], self.user.id)

    def test_team_serializer(self):
        serializer = TeamSerializer(instance=self.team)
        self.assertEqual(serializer.data['name'], "Test Team")

    def test_project_serializer(self):
        serializer = ProjectSerializer(instance=self.project)
        self.assertEqual(serializer.data['name'], "Test Project")

    def test_category_serializer(self):
        serializer = CategorySerializer(instance=self.category)
        self.assertEqual(serializer.data['name'], "Test Category")

    def test_tag_serializer(self):
        serializer = TagSerializer(instance=self.tag)
        self.assertEqual(serializer.data['name'], "Test Tag")

    def test_metric_serializer(self):
        serializer = MetricSerializer(instance=self.metric)
        self.assertEqual(serializer.data['name'], "Test Metric")
        self.assertEqual(serializer.data['type'], MetricType.KPI.value)
        self.assertEqual(serializer.data['value_type'], ValueType.COUNT.value)

    def test_metric_metadata_serializer(self):
        serializer = MetricMetadataSerializer(instance=self.metric_metadata)
        self.assertEqual(serializer.data['data_source'], "Test Source")
        self.assertEqual(serializer.data['rhythm'], Rhythm.DAILY.value)
        self.assertEqual(serializer.data['confidence'], Confidence.ON_TRACK.value)

    def test_experiment_serializer(self):
        serializer = ExperimentSerializer(instance=self.experiment)
        self.assertEqual(serializer.data['name'], "Test Experiment")
        self.assertEqual(serializer.data['status'], ExperimentStatus.PLANNED.value)

    def test_report_serializer(self):
        serializer = ReportSerializer(instance=self.report)
        self.assertEqual(serializer.data['name'], "Test Report")
        self.assertIn('trend', serializer.data['analysis_result'])
        self.assertIn('sarima', serializer.data['forecast_result'])
        self.assertIn('anomalies', serializer.data['anomaly_result'])
        self.assertIn('correlations', serializer.data['relationship_result'])

    def test_action_remark_serializer(self):
        serializer = ActionRemarkSerializer(instance=self.action_remark)
        self.assertEqual(serializer.data['title'], "Test Action")
        self.assertEqual(serializer.data['impact'], Impact.POSITIVE.value)
        self.assertEqual(serializer.data['importance'], Importance.MAJOR.value)

    def test_anomaly_serializer(self):
        serializer = AnomalySerializer(instance=self.anomaly)
        self.assertEqual(serializer.data['anomaly_value'], 100.0)
        self.assertEqual(serializer.data['anomaly_type'], AnomalyType.OPPORTUNITY.value)
        self.assertEqual(serializer.data['quality'], QualityType.HIGH.value)

    def test_insight_serializer(self):
        serializer = InsightSerializer(instance=self.insight)
        self.assertEqual(serializer.data['title'], "Test Insight")

    def test_technical_indicator_serializer(self):
        serializer = TechnicalIndicatorSerializer(instance=self.technical_indicator)
        self.assertEqual(serializer.data['stochastic_value'], 75.5)
        self.assertEqual(serializer.data['rsi_value'], 60.2)

    def test_impact_analysis_serializer(self):
        serializer = ImpactAnalysisSerializer(instance=self.impact_analysis)
        self.assertEqual(serializer.data['before_value'], 100.0)
        self.assertEqual(serializer.data['after_value'], 110.0)

    def test_moving_average_serializer(self):
        serializer = MovingAverageSerializer(instance=self.moving_average)
        self.assertEqual(serializer.data['ma_type'], "SMA")
        self.assertEqual(serializer.data['period'], 7)

    def test_seasonality_result_serializer(self):
        serializer = SeasonalityResultSerializer(instance=self.seasonality_result)
        self.assertEqual(serializer.data['seasonality_type'], "WEEKLY")
        self.assertEqual(serializer.data['strength'], 0.8)

    def test_trend_change_point_serializer(self):
        serializer = TrendChangePointSerializer(instance=self.trend_change_point)
        self.assertEqual(serializer.data['direction'], "INCREASING")
        self.assertEqual(serializer.data['significance'], 0.95)

    def test_network_analysis_result_serializer(self):
        serializer = NetworkAnalysisResultSerializer(instance=self.network_analysis_result)
        self.assertEqual(serializer.data['analysis_type'], "CENTRALITY")
        self.assertEqual(serializer.data['result'], {"centrality": 0.8})

    def test_computation_status_serializer(self):
        serializer = ComputationStatusSerializer(instance=self.computation_status)
        self.assertEqual(serializer.data['status'], "COMPLETED")

    def test_notification_serializer(self):
        serializer = NotificationSerializer(instance=self.notification)
        self.assertEqual(serializer.data['message'], "Test Notification")
        self.assertEqual(serializer.data['is_read'], False)

    def test_pending_computation_serializer(self):
        serializer = PendingComputationSerializer(instance=self.pending_computation)
        self.assertEqual(serializer.data['metric'], self.metric.id)

    def test_metric_target_serializer(self):
        serializer = MetricTargetSerializer(instance=self.metric_target)
        self.assertEqual(serializer.data['target_value'], 100.0)

    def test_correlation_serializer(self):
        serializer = CorrelationSerializer(instance=self.correlation)
        self.assertEqual(serializer.data['pearson_correlation'], 0.85)
        self.assertEqual(serializer.data['spearman_correlation'], 0.82)
        self.assertEqual(serializer.data['lag'], 2)

    def test_connection_serializer(self):
        serializer = ConnectionSerializer(instance=self.connection)
        self.assertEqual(serializer.data['relationship'], "CAUSAL")
        self.assertEqual(serializer.data['strength'], 0.7)
        self.assertEqual(serializer.data['from_metric'], self.metric.id)
        self.assertEqual(serializer.data['to_metric'], self.metric.id)

    def test_historical_data_serializer(self):
        serializer = HistoricalDataSerializer(instance=self.historical_data)
        self.assertEqual(serializer.data['value'], 95.5)

    def test_forecast_serializer(self):
        serializer = ForecastSerializer(instance=self.forecast)
        self.assertEqual(serializer.data['value'], 105.0)
        self.assertEqual(serializer.data['lower_bound'], 100.0)
        self.assertEqual(serializer.data['upper_bound'], 110.0)

    def test_trend_serializer(self):
        serializer = TrendSerializer(instance=self.trend)
        self.assertEqual(serializer.data['trend_type'], "INCREASING")
        self.assertEqual(serializer.data['trend_value'], 0.5)

    def test_dashboard_serializer(self):
        serializer = DashboardSerializer(instance=self.dashboard)
        self.assertEqual(serializer.data['name'], "Test Dashboard")
        self.assertIn(self.metric.id, serializer.data['metrics'])

    def test_strategy_serializer(self):
        serializer = StrategySerializer(instance=self.strategy)
        self.assertEqual(serializer.data['name'], "Test Strategy")

    def test_tactical_solution_serializer(self):
        serializer = TacticalSolutionSerializer(instance=self.tactical_solution)
        self.assertEqual(serializer.data['name'], "Test Tactical Solution")
        self.assertEqual(serializer.data['strategy'], self.strategy.id)

    def test_data_quality_score_serializer(self):
        serializer = DataQualityScoreSerializer(instance=self.data_quality_score)
        self.assertEqual(serializer.data['score'], 0.95)

    def test_time_dimension_serializer(self):
        serializer = TimeDimensionSerializer(instance=self.time_dimension)
        self.assertEqual(serializer.data['name'], "Test Time Dimension")

    def test_metric_deserialization(self):
        data = {
            'name': 'New Metric',
            'type': MetricType.KPI.name,
            'value_type': ValueType.COUNT.name,
            'category': self.category.id,
            'description': 'New Description',
            'hypothesis': 'New Hypothesis',
            'technical_description': 'New Technical Description',
            'source': 'New Source',
            'tenant': self.client.id
        }
        serializer = MetricSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertEqual(instance.name, 'New Metric')
        self.assertEqual(instance.type, MetricType.KPI.name)

    def test_metric_validation(self):
        invalid_data = {
            'name': 'Invalid Metric',
            'type': 'INVALID_TYPE',
            'value_type': ValueType.COUNT.name,
            'category': self.category.id,
            'tenant': self.client.id
        }
        serializer = MetricSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('type', serializer.errors)

    def test_metric_edge_cases(self):
        # Test with empty string
        data = {
            'name': '',
            'type': MetricType.KPI.name,
            'value_type': ValueType.COUNT.name,
            'category': self.category.id,
            'tenant': self.client.id
        }
        serializer = MetricSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

        # Test with null value
        data['name'] = None
        serializer = MetricSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

        # Test maximum length
        data['name'] = 'a' * 256  # Assuming max_length is 255
        serializer = MetricSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

    def test_bulk_create_metrics(self):
        data = [
            {
                'name': 'Bulk Metric 1',
                'type': MetricType.KPI.name,
                'value_type': ValueType.COUNT.name,
                'category': self.category.id,
                'tenant': self.client.id
            },
            {
                'name': 'Bulk Metric 2',
                'type': MetricType.NORTH_STAR.name,
                'value_type': ValueType.PERCENTAGE.name,
                'category': self.category.id,
                'tenant': self.client.id
            }
        ]
        serializer = MetricSerializer(data=data, many=True)
        self.assertTrue(serializer.is_valid())
        instances = serializer.save()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].name, 'Bulk Metric 1')
        self.assertEqual(instances[1].name, 'Bulk Metric 2')

    def test_metric_error_handling(self):
        # Test missing required field
        data = {
            'name': 'Error Metric',
            'type': MetricType.KPI.name,
            # 'value_type' is missing
            'category': self.category.id,
            'tenant': self.client.id
        }
        serializer = MetricSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('value_type', serializer.errors)

        # Test invalid foreign key
        data['value_type'] = ValueType.COUNT.name
        data['category'] = 9999  # Assuming this ID doesn't exist
        serializer = MetricSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('category', serializer.errors)

    def test_report_complex_field_validation(self):
        invalid_data = {
            'metric': self.metric.id,
            'tenant': self.client.id,
            'name': 'Invalid Report',
            'analysis_result': {'invalid_key': 'value'}
        }
        serializer = ReportSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('analysis_result', serializer.errors)

        # Test with valid complex field data
        valid_data = {
            'metric': self.metric.id,
            'tenant': self.client.id,
            'name': 'Valid Report',
            'analysis_result': {
                'trend': {
                    'trend_type': 'increasing',
                    'start_date': '2023-01-01',
                    'end_date': '2023-12-31',
                    'trend_value': 10.5,
                    'slope': 0.5
                },
                'technical_indicators': [{
                    'date': '2023-12-31',
                    'stochastic_value': 75.5,
                    'rsi_value': 60.2,
                    'percent_change': 2.5,
                    'moving_average': 105.3
                }]
            }
        }
        serializer = ReportSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

    def test_experiment_nested_serializer(self):
        # Test nested MetricSerializer in ExperimentSerializer
        serializer = ExperimentSerializer(instance=self.experiment)
        data = serializer.data
        self.assertIn('metrics', data)
        self.assertTrue(isinstance(data['metrics'], list))
        self.assertEqual(len(data['metrics']), 1)
        self.assertEqual(data['metrics'][0]['name'], self.metric.name)

    def test_experiment_deserialization(self):
        data = {
            'name': 'New Experiment',
            'description': 'Test Description',
            'start_date': timezone.now().isoformat(),
            'end_date': (timezone.now() + timezone.timedelta(days=30)).isoformat(),
            'status': ExperimentStatus.PLANNED.name,
            'results': {'key': 'value'},
            'tenant': self.client.id
        }
        serializer = ExperimentSerializer(data=data, context={'metrics': [self.metric.id]})
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertEqual(instance.name, 'New Experiment')
        self.assertEqual(instance.status, ExperimentStatus.PLANNED.name)
        self.assertEqual(instance.metrics.count(), 1)

    def test_experiment_validation(self):
        invalid_data = {
            'name': 'Invalid Experiment',
            'status': 'INVALID_STATUS',
            'tenant': self.client.id
        }
        serializer = ExperimentSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('status', serializer.errors)

    def test_experiment_read_only_fields(self):
        data = {
            'name': 'Read Only Test',
            'tenant': 999  # This should be ignored as it's read-only
        }
        serializer = ExperimentSerializer(data=data, context={'metrics': []})
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertEqual(instance.tenant, self.client)  # Should use the tenant from context, not from data

    def test_report_complex_field_serialization(self):
        serializer = ReportSerializer(instance=self.report)
        data = serializer.data
        self.assertIn('analysis_result', data)
        self.assertIn('trend', data['analysis_result'])
        self.assertIn('technical_indicators', data['analysis_result'])

    def test_report_complex_field_deserialization(self):
        data = {
            'metric': self.metric.id,
            'name': 'New Report',
            'analysis_result': {
                'trend': {
                    'trend_type': 'increasing',
                    'start_date': '2023-01-01',
                    'end_date': '2023-12-31',
                    'trend_value': 10.5,
                    'slope': 0.5
                },
                'technical_indicators': [{
                    'date': '2023-12-31',
                    'stochastic_value': 75.5,
                    'rsi_value': 60.2,
                    'percent_change': 2.5,
                    'moving_average': 105.3
                }]
            },
            'tenant': self.client.id
        }
        serializer = ReportSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertEqual(instance.name, 'New Report')
        self.assertEqual(instance.analysis_result['trend']['trend_type'], 'increasing')

    def test_report_complex_field_validation(self):
        invalid_data = {
            'metric': self.metric.id,
            'name': 'Invalid Report',
            'analysis_result': {'invalid_key': 'value'},
            'tenant': self.client.id
        }
        serializer = ReportSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('analysis_result', serializer.errors)

    def test_date_time_field_handling(self):
        now = timezone.now()
        data = {
            'name': 'DateTime Test',
            'start_date': now.isoformat(),
            'end_date': (now + timezone.timedelta(days=30)).isoformat(),
            'status': ExperimentStatus.PLANNED.name,
            'tenant': self.client.id
        }
        serializer = ExperimentSerializer(data=data, context={'metrics': []})
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertEqual(instance.start_date.isoformat(), data['start_date'])
        self.assertEqual(instance.end_date.isoformat(), data['end_date'])

    def test_custom_method_to_representation(self):
        serializer = ExperimentSerializer(instance=self.experiment)
        data = serializer.data
        self.assertEqual(data['status'], ExperimentStatus[self.experiment.status].value)

    def test_many_to_many_relationship(self):
        # Test creating an experiment with multiple metrics
        metric2 = Metric.objects.create(name="Second Metric", type=MetricType.KPI.name, value_type=ValueType.COUNT.name, category=self.category, tenant=self.client)
        data = {
            'name': 'Multi-Metric Experiment',
            'status': ExperimentStatus.PLANNED.name,
            'tenant': self.client.id
        }
        serializer = ExperimentSerializer(data=data, context={'metrics': [self.metric.id, metric2.id]})
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertEqual(instance.metrics.count(), 2)
        self.assertIn(self.metric, instance.metrics.all())
        self.assertIn(metric2, instance.metrics.all())

    def test_write_only_field(self):
        with schema_context('test_tenant'):
            # Assuming MetricSerializer has a write-only field called 'secret_key'
            data = {
                'name': 'Write Only Test',
                'type': MetricType.KPI.name,
                'value_type': ValueType.COUNT.name,
                'category': self.category.id,
                'project': self.project.id,
                'secret_key': 'top_secret'
            }
            serializer = MetricSerializer(data=data)
            self.assertTrue(serializer.is_valid())
            instance = serializer.save()
            
            # Check that the instance was created with the secret_key
            self.assertEqual(instance.secret_key, 'top_secret')
            
            # Serialize the instance and check that secret_key is not in the output
            serialized_data = MetricSerializer(instance).data
            self.assertNotIn('secret_key', serialized_data)

    def test_experiment_edge_cases(self):
        # Test with empty string for name
        data = {
            'name': '',
            'status': ExperimentStatus.PLANNED.name,
            'tenant': self.client.id
        }
        serializer = ExperimentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

        # Test with null value for start_date
        data = {
            'name': 'Test Experiment',
            'status': ExperimentStatus.PLANNED.name,
            'start_date': None,
            'tenant': self.client.id
        }
        serializer = ExperimentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('start_date', serializer.errors)

        # Test with end_date before start_date
        data = {
            'name': 'Test Experiment',
            'status': ExperimentStatus.PLANNED.name,
            'start_date': '2023-01-02',
            'end_date': '2023-01-01',
            'tenant': self.client.id
        }
        serializer = ExperimentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('end_date', serializer.errors)

    def test_report_edge_cases(self):
        # Test with empty analysis_result
        data = {
            'metric': self.metric.id,
            'name': 'Test Report',
            'analysis_result': {},
            'tenant': self.client.id
        }
        serializer = ReportSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('analysis_result', serializer.errors)

        # Test with invalid JSON in configuration
        data = {
            'metric': self.metric.id,
            'name': 'Test Report',
            'configuration': 'invalid json',
            'tenant': self.client.id
        }
        serializer = ReportSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('configuration', serializer.errors)

    def test_experiment_metric_relationship(self):
        # Test creating an experiment with no metrics
        data = {
            'name': 'No Metrics Experiment',
            'status': ExperimentStatus.PLANNED.name,
            'tenant': self.client.id
        }
        serializer = ExperimentSerializer(data=data, context={'metrics': []})
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertEqual(instance.metrics.count(), 0)

        # Test creating an experiment with multiple metrics
        metric2 = Metric.objects.create(name="Second Metric", type=MetricType.KPI.name, value_type=ValueType.COUNT.name, category=self.category, tenant=self.client)
        data = {
            'name': 'Multi-Metric Experiment',
            'status': ExperimentStatus.PLANNED.name,
            'tenant': self.client.id
        }
        serializer = ExperimentSerializer(data=data, context={'metrics': [self.metric.id, metric2.id]})
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertEqual(instance.metrics.count(), 2)
        self.assertIn(self.metric, instance.metrics.all())
        self.assertIn(metric2, instance.metrics.all())

        # Test updating experiment metrics
        data = {
            'name': 'Updated Experiment',
            'status': ExperimentStatus.IN_PROGRESS.name,
        }
        serializer = ExperimentSerializer(instance=instance, data=data, partial=True, context={'metrics': [self.metric.id]})
        self.assertTrue(serializer.is_valid())
        updated_instance = serializer.save()
        self.assertEqual(updated_instance.metrics.count(), 1)
        self.assertIn(self.metric, updated_instance.metrics.all())
        self.assertNotIn(metric2, updated_instance.metrics.all())

    def test_report_metric_relationship(self):
        # Test creating a report with a valid metric
        data = {
            'metric': self.metric.id,
            'name': 'Test Report',
            'tenant': self.client.id
        }
        serializer = ReportSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertEqual(instance.metric, self.metric)
        
        # Test creating a report with an invalid metric
        data['metric'] = 9999  # Assuming this ID doesn't exist
        serializer = ReportSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('metric', serializer.errors)

        # Test updating report's metric
        metric2 = Metric.objects.create(name="Second Metric", type=MetricType.KPI.name, value_type=ValueType.COUNT.name, category=self.category, tenant=self.client)
        data = {
            'metric': metric2.id,
        }
        serializer = ReportSerializer(instance=instance, data=data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_instance = serializer.save()
        self.assertEqual(updated_instance.metric, metric2)
        
