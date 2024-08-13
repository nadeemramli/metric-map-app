from rest_framework import serializers
from .models import *

# Client nested serializers
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'tenant']
        read_only_fields = ['tenant', 'created_at', 'updated_at']

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'team', 'tenant']  # include other fields
        read_only_fields = ['id']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'tenant']
        read_only_fields = ['tenant']

# Project nested serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'project', 'name', 'tenant']
        read_only_fields = ['tenant']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'project', 'tenant']
        read_only_fields = ['tenant']

class ActionRemarkSerializer(serializers.ModelSerializer):
    impact = serializers.ChoiceField(choices=[(impact.name, impact.value) for impact in Impact])
    importance = serializers.ChoiceField(choices=[(importance.name, importance.value) for importance in Importance])

    class Meta:
        model = ActionRemark
        fields = ['id', 'project', 'title', 'date', 'summary', 'impact', 'importance', 'tenant']
        read_only_fields = ['tenant']

    def validate_impact(self, value):
        try:
            return Impact[value].name
        except KeyError:
            raise serializers.ValidationError(f"Invalid impact: {value}")

    def validate_importance(self, value):
        try:
            return Importance[value].name
        except KeyError:
            raise serializers.ValidationError(f"Invalid importance: {value}")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['impact'] = Impact[instance.impact].value
        representation['importance'] = Importance[instance.importance].value
        return representation

class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ['id', 'project', 'title', 'description', 'team', 'estimated_time', 'artifacts_url', 'created_at', 'updated_at', 'tenant']
        read_only_fields = ['tenant', 'created_at', 'updated_at']

class TacticalSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TacticalSolution
        fields = ['id', 'project', 'title', 'description', 'artifact_url', 'created_at', 'updated_at', 'tenant']
        read_only_fields = ['tenant', 'created_at', 'updated_at']

class TimeDimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeDimension
        fields = ['id', 'project', 'date', 'day', 'day_of_week', 'day_name', 'week', 'month', 'month_name', 'quarter', 'year', 'is_weekend', 'is_holiday', 'tenant']
        read_only_fields = ['tenant']
      
class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = ['id', 'project', 'name', 'layout', 'tenant']
        read_only_fields = ['tenant']

class NetworkAnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkAnalysisResult
        fields = ['id', 'project', 'metric', 'analysis_type', 'result', 'tenant']
        read_only_fields = ['tenant']

class ComputationStatusSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=ComputationStatus.STATUS_CHOICES)

    class Meta:
        model = ComputationStatus
        fields = ['id', 'project', 'status', 'created_at', 'updated_at', 'error_message', 'tenant']
        read_only_fields = ['tenant', 'created_at', 'updated_at']

    def validate_status(self, value):
        if value not in dict(ComputationStatus.STATUS_CHOICES):
            raise serializers.ValidationError(f"Invalid status: {value}")
        return value

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'project', 'message', 'created_at', 'is_read', 'tenant']
        read_only_fields = ['tenant', 'created_at']

class PendingComputationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingComputation
        fields = ['id', 'project', 'metric', 'created_at', 'tenant']
        read_only_fields = ['tenant', 'created_at']

# Metric nested serializers
class DataQualityScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataQualityScore
        fields = ['id', 'data_entry', 'completeness_score', 'accuracy_score', 'consistency_score', 'timeliness_score', 'overall_score', 'tenant']
        read_only_fields = ['tenant']

class MetricMetadataSerializer(serializers.ModelSerializer):
    rhythm = serializers.ChoiceField(choices=[(r.name, r.value) for r in Rhythm])
    confidence = serializers.ChoiceField(choices=[(c.name, c.value) for c in Confidence])

    class Meta:
        model = MetricMetadata
        fields = ['id', 'metric', 'data_source', 'source_url', 'rhythm', 'last_updated', 
                  'data_quality_score', 'team', 'technical_description', 'description', 
                  'artifacts_url', 'hypothesis', 'confidence', 'position_x', 'position_y', 'tenant']
        read_only_fields = ['tenant', 'last_updated']

    def validate_rhythm(self, value):
        try:
            return Rhythm[value].name
        except KeyError:
            raise serializers.ValidationError(f"Invalid rhythm: {value}")

    def validate_confidence(self, value):
        try:
            return Confidence[value].name
        except KeyError:
            raise serializers.ValidationError(f"Invalid confidence: {value}")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['rhythm'] = Rhythm[instance.rhythm].value
        representation['confidence'] = Confidence[instance.confidence].value
        return representation

class MetricTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricTarget
        fields = ['id', 'metric', 'target_kpi', 'target_remarks', 'target_date', 'target_value', 'tenant']
        read_only_fields = ['tenant']

class CorrelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correlation
        fields = ['id','metric1', 'metric2', 'lag', 'pearson_correlation', 'spearman_correlation', 'tenant']
        read_only_fields = ['tenant']

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['id', 'from_metric', 'to_metric', 'relationship', 'tenant']
        read_only_fields = ['tenant']

class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = ['id', 'metric', 'user', 'date', 'title', 'content', 'created_at', 'updated_at', 'tenant']
        read_only_fields = ['tenant', 'created_at', 'updated_at']

class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ['id', 'metric', 'forecast_date', 'forecast_value', 'model_used', 'accuracy', 'confidence_interval', 'variance', 'tenant']
        read_only_fields = ['tenant']

class TechnicalIndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalIndicator
        fields = ['id', 'metric', 'date', 'stochastic_value', 'rsi_value', 'percent_change', 'moving_average', 'tenant']
        read_only_fields = ['tenant']

class AnomalySerializer(serializers.ModelSerializer):
    anomaly_type = serializers.ChoiceField(choices=[(t.name, t.value) for t in AnomalyType])
    quality = serializers.ChoiceField(choices=[(q.name, q.value) for q in QualityType])

    class Meta:
        model = Anomaly
        fields = ['id', 'metric', 'detection_date', 'anomaly_value', 'anomaly_score', 'notes', 'anomaly_type', 'quality', 'tenant']
        read_only_fields = ['tenant']

    def validate_anomaly_type(self, value):
        try:
            return AnomalyType[value].name
        except KeyError:
            raise serializers.ValidationError(f"Invalid anomaly type: {value}")

    def validate_quality(self, value):
        try:
            return QualityType[value].name
        except KeyError:
            raise serializers.ValidationError(f"Invalid quality type: {value}")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['anomaly_type'] = AnomalyType[instance.anomaly_type].value
        representation['quality'] = QualityType[instance.quality].value
        return representation

class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ['id', 'metric', 'trend_type', 'start_date', 'end_date', 'trend_value', 'notes', 'tenant']
        read_only_fields = ['tenant']

class MovingAverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovingAverage
        fields = ['id', 'metric', 'date', 'ma_type', 'period', 'value', 'tenant']
        read_only_fields = ['tenant']

class SeasonalityResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonalityResult
        fields = ['id', 'metric', 'seasonality_type', 'strength', 'period', 'created_at']
        read_only_fields = ['created_at']

class TrendChangePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendChangePoint
        fields = ['id', 'metric', 'date', 'direction', 'significance', 'tenant']
        read_only_fields = ['tenant']

class HistoricalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalData
        fields = ['id', 'metric', 'date', 'value', 'tenant']
        read_only_fields = ['tenant']

class ReportSerializer(serializers.ModelSerializer):
    configuration = serializers.JSONField(required=False)
    analysis_result = serializers.JSONField(required=False)
    forecast_result = serializers.JSONField(required=False)
    anomaly_result = serializers.JSONField(required=False)
    relationship_result = serializers.JSONField(required=False)

    class Meta:
        model = Report
        fields = ['id', 'project', 'metric', 'tenant', 'name', 'configuration', 'analysis_result', 
                  'forecast_result', 'anomaly_result', 'relationship_result', 'report', 
                  'created_at', 'updated_at']
        read_only_fields = ['tenant', 'created_at', 'updated_at']

    def validate_configuration(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Configuration must be a JSON object")
        return value

    def validate_analysis_result(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Analysis result must be a JSON object")
        
        required_keys = ['trend', 'technical_indicators']
        for key in required_keys:
            if key not in value:
                raise serializers.ValidationError(f"Analysis result must contain '{key}'")
        
        trend = value['trend']
        trend_keys = ['trend_type', 'start_date', 'end_date', 'trend_value', 'slope']
        for key in trend_keys:
            if key not in trend:
                raise serializers.ValidationError(f"Trend must contain '{key}'")
        
        indicators = value['technical_indicators']
        if not isinstance(indicators, list):
            raise serializers.ValidationError("Technical indicators must be a list")
        for indicator in indicators:
            indicator_keys = ['date', 'stochastic_value', 'rsi_value', 'percent_change', 'moving_average']
            for key in indicator_keys:
                if key not in indicator:
                    raise serializers.ValidationError(f"Each technical indicator must contain '{key}'")
        
        return value

    def validate_forecast_result(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Forecast result must be a JSON object")
        
        for model, forecasts in value.items():
            if not isinstance(forecasts, list):
                raise serializers.ValidationError(f"Forecasts for model '{model}' must be a list")
            for forecast in forecasts:
                required_keys = ['date', 'value', 'lower_bound', 'upper_bound', 'confidence_interval']
                for key in required_keys:
                    if key not in forecast:
                        raise serializers.ValidationError(f"Each forecast must contain '{key}'")
        
        return value

    def validate_anomaly_result(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Anomaly result must be a JSON object")
        
        if 'anomalies' not in value:
            raise serializers.ValidationError("Anomaly result must contain 'anomalies'")
        
        anomalies = value['anomalies']
        if not isinstance(anomalies, list):
            raise serializers.ValidationError("Anomalies must be a list")
        
        for anomaly in anomalies:
            required_keys = ['date', 'value', 'score', 'type']
            for key in required_keys:
                if key not in anomaly:
                    raise serializers.ValidationError(f"Each anomaly must contain '{key}'")
        
        return value

    def validate_relationship_result(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Relationship result must be a JSON object")
        
        if 'correlations' not in value:
            raise serializers.ValidationError("Relationship result must contain 'correlations'")
        
        correlations = value['correlations']
        if not isinstance(correlations, list):
            raise serializers.ValidationError("Correlations must be a list")
        
        for correlation in correlations:
            required_keys = ['metric_id', 'pearson', 'spearman']
            for key in required_keys:
                if key not in correlation:
                    raise serializers.ValidationError(f"Each correlation must contain '{key}'")
        
        return value
        
# Experiment nested serializers
class ImpactAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpactAnalysis
        fields = ['id', 'experiment', 'metric', 'before_value', 'after_value', 'percentage_change', 'confidence', 'artifact_link', 'tenant']
        read_only_fields = ['tenant']

class MetricSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    metadata = MetricMetadataSerializer(read_only=True)
    targets = MetricTargetSerializer(many=True, read_only=True)
    historical_data = HistoricalDataSerializer(many=True, read_only=True)
    forecast = ForecastSerializer(many=True, read_only=True)
    anomaly = AnomalySerializer(many=True, read_only=True)
    trend = TrendSerializer(many=True, read_only=True)
    correlations = CorrelationSerializer(many=True, read_only=True)
    connections = ConnectionSerializer(many=True, read_only=True)
    data_quality_scores = DataQualityScoreSerializer(many=True, read_only=True)
    insights = InsightSerializer(many=True, read_only=True)
    technical_indicators = TechnicalIndicatorSerializer(many=True, read_only=True)
    moving_averages = MovingAverageSerializer(many=True, read_only=True)
    seasonality_results = SeasonalityResultSerializer(many=True, read_only=True)
    trend_change_points = TrendChangePointSerializer(many=True, read_only=True)

    class Meta:
        model = Metric
        fields = ['id', 'name', 'project', 'type', 'value_type', 'category', 'tags', 'tenant',
                  'metadata', 'targets', 'historical_data', 'forecast', 'anomaly', 'trend',
                  'correlations', 'connections', 'data_quality_scores', 'insights',
                  'technical_indicators', 'moving_averages', 'seasonality_results',
                  'trend_change_points']
        read_only_fields = ['tenant', 'last_updated']
        depth = 3  # This will serialize the first level of nested objects (projects)

    def validate_type(self, value):
        try:
            return MetricType[value].name
        except KeyError:
            raise serializers.ValidationError(f"Invalid metric type: {value}")

    def validate_value_type(self, value):
        try:
            return ValueType[value].name
        except KeyError:
            raise serializers.ValidationError(f"Invalid value type: {value}")

    def validate_rhythm(self, value):
        try:
            return Rhythm[value].name
        except KeyError:
            raise serializers.ValidationError(f"Invalid rhythm: {value}")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['type'] = MetricType[instance.type].value
        representation['value_type'] = ValueType[instance.value_type].value
        representation['rhythm'] = Rhythm[instance.rhythm].value
        return representation

    def create(self, validated_data):
        tags_data = self.context.get('tags', [])
        category_data = self.context.get('category')
        metadata_data = self.context.get('metadata', {})
        
        metric = Metric.objects.create(**validated_data)
        
        if category_data:
            category, _ = Category.objects.get_or_create(**category_data)
            metric.category = category
        
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            metric.tags.add(tag)
        
        if metadata_data:
            MetricMetadata.objects.create(metric=metric, **metadata_data)
        
        metric.save()
        return metric

    def update(self, instance, validated_data):
        tags_data = self.context.get('tags', [])
        category_data = self.context.get('category')
        metadata_data = self.context.get('metadata', {})
        
        instance = super().update(instance, validated_data)
        
        if category_data:
            category, _ = Category.objects.get_or_create(**category_data)
            instance.category = category
        
        instance.tags.clear()
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)
        
        if metadata_data:
            MetricMetadata.objects.update_or_create(
                metric=instance,
                defaults=metadata_data
            )
        
        instance.save()
        return instance

class ExperimentSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=[(status.name, status.value) for status in ExperimentStatus])
    metrics = MetricSerializer(many=True, read_only=True)
    results = serializers.JSONField(required=False)
    impact_analysis = ImpactAnalysisSerializer(many=True, read_only=True)

    class Meta:
        model = Experiment
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'status', 'results', 'metrics', 'tenant', 'impact_analysis']
        read_only_fields = ['tenant']
        depth = 3  # This will serialize the first level of nested objects (projects)

    def validate_status(self, value):
        try:
            return ExperimentStatus[value].name
        except KeyError:
            raise serializers.ValidationError(f"Invalid experiment status: {value}")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['status'] = ExperimentStatus[instance.status].value
        return representation

    def create(self, validated_data):
        metrics_data = self.context.get('metrics', [])
        experiment = Experiment.objects.create(**validated_data)
        experiment.metrics.set(metrics_data)
        return experiment

    def update(self, instance, validated_data):
        metrics_data = self.context.get('metrics', [])
        instance = super().update(instance, validated_data)
        instance.metrics.set(metrics_data)
        return instance

class ProjectSerializer(serializers.ModelSerializer):
    metrics = MetricSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    dashboards = DashboardSerializer(many=True, read_only=True)
    experiments = ExperimentSerializer(many=True, read_only=True)
    reports = ReportSerializer(many=True, read_only=True)
    strategies = StrategySerializer(many=True, read_only=True)
    action_remarks = ActionRemarkSerializer(many=True, read_only=True)
    tactical_solutions = TacticalSolutionSerializer(many=True, read_only=True)
    time_dimensions = TimeDimensionSerializer(many=True, read_only=True)
    network_analysis_results = NetworkAnalysisResultSerializer(many=True, read_only=True)
    computation_status = ComputationStatusSerializer(many=True, read_only=True)
    notifications = NotificationSerializer(many=True, read_only=True)
    pending_computations = PendingComputationSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'created_on', 'tenant', 'metrics', 'categories', 'tags', 'dashboards', 
                  'experiments', 'reports', 'strategies', 'action_remarks', 'tactical_solutions', 
                  'time_dimensions', 'network_analysis_results', 'computation_status', 'notifications', 
                  'pending_computations']
        read_only_fields = ['tenant', 'created_on']
        depth = 2  # This will serialize the first level of nested objects (projects)
    
    def create(self, validated_data):
        metrics_data = validated_data.pop('metrics', [])
        categories_data = validated_data.pop('categories', [])
        tags_data = validated_data.pop('tags', [])
        dashboards_data = validated_data.pop('dashboards', [])
        experiments_data = validated_data.pop('experiments', [])
        reports_data = validated_data.pop('reports', [])
        strategies_data = validated_data.pop('strategies', [])
        action_remarks_data = validated_data.pop('action_remarks', [])
        tactical_solutions_data = validated_data.pop('tactical_solutions', [])
        time_dimensions_data = validated_data.pop('time_dimensions', [])
        network_analysis_results_data = validated_data.pop('network_analysis_results', [])
        computation_status_data = validated_data.pop('computation_status', [])
        notifications_data = validated_data.pop('notifications', [])
        pending_computations_data = validated_data.pop('pending_computations', [])

        project = Project.objects.create(**validated_data)

        for metric_data in metrics_data:
            Metric.objects.create(project=project, **metric_data)
        for category_data in categories_data:
            Category.objects.create(project=project, **category_data)
        for tag_data in tags_data:
            Tag.objects.create(project=project, **tag_data)
        for dashboard_data in dashboards_data:
            Dashboard.objects.create(project=project, **dashboard_data)
        for experiment_data in experiments_data:
            Experiment.objects.create(project=project, **experiment_data)
        for report_data in reports_data:
            Report.objects.create(project=project, **report_data)
        for strategy_data in strategies_data:
            Strategy.objects.create(project=project, **strategy_data)
        for action_remark_data in action_remarks_data:
            ActionRemark.objects.create(project=project, **action_remark_data)
        for tactical_solution_data in tactical_solutions_data:
            TacticalSolution.objects.create(project=project, **tactical_solution_data)
        for time_dimension_data in time_dimensions_data:
            TimeDimension.objects.create(project=project, **time_dimension_data)
        for network_analysis_result_data in network_analysis_results_data:
            NetworkAnalysisResult.objects.create(project=project, **network_analysis_result_data)
        for computation_status_item in computation_status_data:
            ComputationStatus.objects.create(project=project, **computation_status_item)
        for notification_data in notifications_data:
            Notification.objects.create(project=project, **notification_data)
        for pending_computation_data in pending_computations_data:
            PendingComputation.objects.create(project=project, **pending_computation_data)

        return project

    def update(self, instance, validated_data):
        metrics_data = validated_data.pop('metrics', [])
        categories_data = validated_data.pop('categories', [])
        tags_data = validated_data.pop('tags', [])
        dashboards_data = validated_data.pop('dashboards', [])
        experiments_data = validated_data.pop('experiments', [])
        reports_data = validated_data.pop('reports', [])
        strategies_data = validated_data.pop('strategies', [])
        action_remarks_data = validated_data.pop('action_remarks', [])
        tactical_solutions_data = validated_data.pop('tactical_solutions', [])
        time_dimensions_data = validated_data.pop('time_dimensions', [])
        network_analysis_results_data = validated_data.pop('network_analysis_results', [])
        computation_status_data = validated_data.pop('computation_status', [])
        notifications_data = validated_data.pop('notifications', [])
        pending_computations_data = validated_data.pop('pending_computations', [])

        # Update project fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update or create nested objects
        self.update_nested_objects(instance.metrics, metrics_data, Metric)
        self.update_nested_objects(instance.categories, categories_data, Category)
        self.update_nested_objects(instance.tags, tags_data, Tag)
        self.update_nested_objects(instance.dashboards, dashboards_data, Dashboard)
        self.update_nested_objects(instance.experiments, experiments_data, Experiment)
        self.update_nested_objects(instance.reports, reports_data, Report)
        self.update_nested_objects(instance.strategies, strategies_data, Strategy)
        self.update_nested_objects(instance.action_remarks, action_remarks_data, ActionRemark)
        self.update_nested_objects(instance.tactical_solutions, tactical_solutions_data, TacticalSolution)
        self.update_nested_objects(instance.time_dimensions, time_dimensions_data, TimeDimension)
        self.update_nested_objects(instance.network_analysis_results, network_analysis_results_data, NetworkAnalysisResult)
        self.update_nested_objects(instance.computation_status, computation_status_data, ComputationStatus)
        self.update_nested_objects(instance.notifications, notifications_data, Notification)
        self.update_nested_objects(instance.pending_computations, pending_computations_data, PendingComputation)

        return instance

    def update_nested_objects(self, queryset, data_list, model):
        existing_ids = set(queryset.values_list('id', flat=True))
        for item_data in data_list:
            item_id = item_data.get('id')
            if item_id in existing_ids:
                item = queryset.get(id=item_id)
                for attr, value in item_data.items():
                    setattr(item, attr, value)
                item.save()
                existing_ids.remove(item_id)
            else:
                model.objects.create(**item_data)
        queryset.filter(id__in=existing_ids).delete()

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'created_on', 'schema_name', 'domain_url', 'projects']
        read_only_fields = ['schema_name', 'created_on']
        depth = 1  # This will serialize the first level of nested objects (projects)

    def get_projects(self, obj):
        return ProjectSerializer(obj.projects.all(), many=True, context=self.context).data

class TenantCreationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    domain_url = serializers.CharField(max_length=253)
    email = serializers.EmailField()

    def validate_domain(self, value):
        if Client.objects.filter(schema_name=value).exists():
            raise serializers.ValidationError("This domain is already in use.")
        return value

class ProjectCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description']

class TeamCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'description']

class TeamMemberAssignmentSerializer(serializers.Serializer):
    team_id = serializers.IntegerField()
    user_ids = serializers.ListField(child=serializers.IntegerField())