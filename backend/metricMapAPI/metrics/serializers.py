from rest_framework import serializers
from .models import (
    Client, Domain, CustomUser, UserProfile, Team, Project, Category, Tag, Metric,
    MetricMetadata, MetricTarget, Correlation, Connection, HistoricalData,
    Experiment, Forecast, Anomaly, Trend, Dashboard, Report, ActionRemark,
    Strategy, TacticalSolution, DataQualityScore, TimeDimension, ValueType, MetricType,
    Rhythm, ExperimentStatus, Impact, Importance, AnomalyType, QualityType, Confidence,
    Insight, Trend, MovingAverage, TechnicalIndicator, ImpactAnalysis, SeasonalityResult,
    TrendChangePoint, NetworkAnalysisResult, ComputationStatus, Notification, PendingComputation
)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'created_on', 'schema_name']
        read_only_fields = ['schema_name']

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ['id', 'domain', 'tenant', 'is_primary']
        read_only_fields = ['tenant']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'tenant']
        read_only_fields = ['tenant', 'created_at', 'updated_at']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'team', 'tenant']
        read_only_fields = ['tenant']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'tenant']
        read_only_fields = ['tenant']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'created_on', 'tenant']
        read_only_fields = ['tenant', 'created_on']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'tenant']
        read_only_fields = ['tenant']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'project', 'tenant']
        read_only_fields = ['tenant']

class MetricSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    type = serializers.ChoiceField(choices=[(t.name, t.value) for t in MetricType])
    value_type = serializers.ChoiceField(choices=[(vt.name, vt.value) for vt in ValueType])
    rhythm = serializers.ChoiceField(choices=[(r.name, r.value) for r in Rhythm])

    class Meta:
        model = Metric
        fields = ['id', 'name', 'type', 'value_type', 'category', 'tags', 'description', 
                  'hypothesis', 'technical_description', 'last_updated', 'source', 'tenant']
        read_only_fields = ['tenant', 'last_updated']

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
        fields = ['id', 'metric1', 'metric2', 'lag', 'pearson_correlation', 'spearman_correlation', 'tenant']
        read_only_fields = ['tenant']

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['id', 'from_metric', 'to_metric', 'relationship', 'tenant']
        read_only_fields = ['tenant']

class ExperimentSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=[(status.name, status.value) for status in ExperimentStatus])
    metrics = MetricSerializer(many=True, read_only=True)
    results = serializers.JSONField(required=False)

    class Meta:
        model = Experiment
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'status', 'results', 'metrics', 'tenant']
        read_only_fields = ['tenant']

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

class ActionRemarkSerializer(serializers.ModelSerializer):
    impact = serializers.ChoiceField(choices=[(impact.name, impact.value) for impact in Impact])
    importance = serializers.ChoiceField(choices=[(importance.name, importance.value) for importance in Importance])

    class Meta:
        model = ActionRemark
        fields = ['id', 'metric', 'title', 'date', 'summary', 'impact', 'importance', 'tenant']
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

class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = ['id', 'metric', 'user', 'date', 'title', 'content', 'created_at', 'updated_at', 'tenant']
        read_only_fields = ['tenant', 'created_at', 'updated_at']

class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ['id', 'title', 'description', 'team', 'estimated_time', 'artifacts_url', 'created_at', 'updated_at', 'tenant']
        read_only_fields = ['tenant', 'created_at', 'updated_at']

class TacticalSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TacticalSolution
        fields = ['id', 'metric', 'title', 'description', 'artifact_url', 'created_at', 'updated_at', 'tenant']
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

class ImpactAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpactAnalysis
        fields = ['id', 'experiment', 'metric', 'before_value', 'after_value', 'percentage_change', 'confidence', 'artifact_link', 'tenant']
        read_only_fields = ['tenant']

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

class NetworkAnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkAnalysisResult
        fields = ['id', 'metric', 'analysis_type', 'result', 'tenant']
        read_only_fields = ['tenant']

class HistoricalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalData
        fields = ['id', 'metric', 'date', 'value', 'forecasted_value', 'anomaly_detected', 'trend_component', 'tenant']
        read_only_fields = ['tenant']

class TimeDimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeDimension
        fields = ['id', 'date', 'day', 'day_of_week', 'day_name', 'week', 'month', 'month_name', 'quarter', 'year', 'is_weekend', 'is_holiday', 'tenant']
        read_only_fields = ['tenant']
      
class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = ['id', 'name', 'layout', 'tenant']
        read_only_fields = ['tenant']
  
class ReportSerializer(serializers.ModelSerializer):
    configuration = serializers.JSONField(required=False)
    analysis_result = serializers.JSONField(required=False)
    forecast_result = serializers.JSONField(required=False)
    anomaly_result = serializers.JSONField(required=False)
    relationship_result = serializers.JSONField(required=False)

    class Meta:
        model = Report
        fields = ['id', 'metric', 'tenant', 'name', 'configuration', 'analysis_result', 
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
        
class ComputationStatusSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=ComputationStatus.STATUS_CHOICES)

    class Meta:
        model = ComputationStatus
        fields = ['id', 'status', 'created_at', 'updated_at', 'error_message', 'tenant']
        read_only_fields = ['tenant', 'created_at', 'updated_at']

    def validate_status(self, value):
        if value not in dict(ComputationStatus.STATUS_CHOICES):
            raise serializers.ValidationError(f"Invalid status: {value}")
        return value

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'message', 'created_at', 'is_read', 'tenant']
        read_only_fields = ['tenant', 'created_at']

class PendingComputationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingComputation
        fields = ['id', 'metric', 'created_at', 'tenant']
        read_only_fields = ['tenant', 'created_at']

class TenantCreationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=253)
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