from rest_framework import serializers
from .models import (
    Client, Domain, CustomUser, UserProfile, Team, Project, Category, Tag, Metric,
    MetricMetadata, MetricTarget, Correlation, Connection, HistoricalData,
    Experiment, Forecast, Anomaly, Trend, Dashboard, Report, ActionRemark,
    Strategy, TacticalSolution, DataQualityScore, TimeDimension
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

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'tenant']
        read_only_fields = ['tenant', 'created_at', 'updated_at']

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
    position = serializers.SerializerMethodField()

    class Meta:
        model = Metric
        fields = ['id', 'name', 'type', 'value_type', 'rhythm', 'category', 'description', 'hypothesis', 'tags', 'technical_description', 'last_updated', 'source', 'position', 'tenant']
        read_only_fields = ['tenant', 'last_updated']

    def get_position(self, obj):
        return {"x": obj.position_x, "y": obj.position_y}

    def validate_type(self, value):
        if value not in Metric.Type.values:
            raise serializers.ValidationError(f"Invalid metric type: {value}")
        return value

    def validate_value_type(self, value):
        if value not in Metric.ValueType.values:
            raise serializers.ValidationError(f"Invalid value type: {value}")
        return value

    def validate_rhythm(self, value):
        if value not in Metric.Rhythm.values:
            raise serializers.ValidationError(f"Invalid rhythm: {value}")
        return value

class MetricMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricMetadata
        fields = ['id', 'metric', 'data_source', 'source_url', 'rhythm', 'last_updated', 'data_quality_score', 'team', 'technical_description', 'description', 'artifacts_url', 'hypothesis', 'confidence', 'position_x', 'position_y', 'tenant']
        read_only_fields = ['tenant', 'last_updated']

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

class HistoricalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalData
        fields = ['id', 'metric', 'date', 'value', 'forecasted_value', 'anomaly_detected', 'trend_component', 'tenant']
        read_only_fields = ['tenant']

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'status', 'results', 'metrics', 'tenant']
        read_only_fields = ['tenant']

    def validate_status(self, value):
        if value not in Experiment.ExperimentStatus.values:
            raise serializers.ValidationError(f"Invalid experiment status: {value}")
        return value

class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ['id', 'metric', 'forecast_date', 'forecast_value', 'model_used', 'accuracy', 'confidence_interval', 'variance', 'tenant']
        read_only_fields = ['tenant']

class AnomalySerializer(serializers.ModelSerializer):
    class Meta:
        model = Anomaly
        fields = ['id', 'metric', 'detection_date', 'anomaly_value', 'anomaly_score', 'notes', 'anomaly_type', 'quality', 'tenant']
        read_only_fields = ['tenant']

    def validate_anomaly_type(self, value):
        if value not in Anomaly.AnomalyType.values:
            raise serializers.ValidationError(f"Invalid anomaly type: {value}")
        return value

    def validate_quality(self, value):
        if value not in Anomaly.QualityType.values:
            raise serializers.ValidationError(f"Invalid quality type: {value}")
        return value

class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ['id', 'metric', 'trend_type', 'start_date', 'end_date', 'trend_value', 'notes', 'tenant']
        read_only_fields = ['tenant']

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = ['id', 'name', 'layout', 'tenant']
        read_only_fields = ['tenant']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'name', 'configuration', 'tenant']
        read_only_fields = ['tenant']

class ActionRemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionRemark
        fields = ['id', 'metric', 'title', 'date', 'summary', 'impact', 'importance', 'tenant']
        read_only_fields = ['tenant']

    def validate_impact(self, value):
        if value not in ActionRemark.Impact.values:
            raise serializers.ValidationError(f"Invalid impact: {value}")
        return value

    def validate_importance(self, value):
        if value not in ActionRemark.Importance.values:
            raise serializers.ValidationError(f"Invalid importance: {value}")
        return value

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

class DataQualityScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataQualityScore
        fields = ['id', 'data_entry', 'completeness_score', 'accuracy_score', 'consistency_score', 'timeliness_score', 'overall_score', 'tenant']
        read_only_fields = ['tenant']

class TimeDimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeDimension
        fields = ['id', 'date', 'day', 'day_of_week', 'day_name', 'week', 'month', 'month_name', 'quarter', 'year', 'is_weekend', 'is_holiday', 'tenant']
        read_only_fields = ['tenant']