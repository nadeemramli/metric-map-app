from rest_framework import serializers
from .models import Project, Client, Category, Tag, Metric, Connection, HistoricalData, Target, ActionRemark, Dashboard, Report, Experiment, Trend, Anomaly, Forecast

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'created_on']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'created_on','tenant']
        read_only_fields = ['tenant']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'tenant']
        read_only_fields = ['tenant']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'tenant']
        read_only_fields = ['tenant']

class MetricSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False, allow_null=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), required=False)  
    
    connections = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    
    position = serializers.SerializerMethodField()
    
    class Meta:
        model = Metric
        fields = ['id', 'name', 'type', 'confidence', 'value_type', 'rhythm', 'category', 
                  'description', 'hypothesis', 'tags', 'technical_description', 'last_updated', 
                  'source', 'position', 'connections', 'tenant']
        read_only_fields = ['tenant', 'last_updated']

    def get_position(self, obj):
        return obj.position

    def update(self, instance, validated_data):
        position = validated_data.pop('position', None)
        if position:
            instance.set_position(position['x'], position['y'])
        return super().update(instance, validated_data)
    
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
    
    def validate_confidence(self, value):
        if value not in Metric.Confidence.values:
            raise serializers.ValidationError(f"Invalid confidence level: {value}")
        return value

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        connections_data = validated_data.pop('connections', [])
        tenant = self.context['request'].tenant
        metric = Metric.objects.create(tenant=tenant, **validated_data)
        metric.tags.set(tags_data)
        
        for connection_id in connections_data:
            try:
                to_metric = Metric.objects.get(id=connection_id)
                Connection.objects.create(from_metric=metric, to_metric=to_metric)
            except Metric.DoesNotExist:
                pass
        
        return metric

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['id', 'from_metric', 'to_metric', 'relationship', 'correlation_coefficient', 'tenant']
        read_only_fields = ['tenant']

class HistoricalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalData
        fields = ['id', 'metric', 'date', 'value', 'forecasted_value', 'tenant']
        read_only_fields = ['tenant']

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'metric', 'remarks', 'target_kpi', 'target_date', 'target_value', 'tenant']
        read_only_fields = ['tenant']

class ActionRemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionRemark
        fields = ['id', 'metric', 'date', 'description', 'impact', 'tenant']
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

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'status', 'results', 'metrics', 'tenant']
        read_only_fields = ['tenant']

class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ['id', 'metric', 'forecast_date', 'forecast_value', 'model_used', 'accuracy', 'confidence_interval', 'tenant']
        read_only_fields = ['tenant']

class AnomalySerializer(serializers.ModelSerializer):
    class Meta:
        model = Anomaly
        fields = ['id', 'metric', 'detection_date', 'anomaly_value', 'anomaly_score', 'notes', 'tenant']
        read_only_fields = ['tenant']

class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ['id', 'metric', 'trend_type', 'start_date', 'end_date', 'trend_value', 'notes', 'tenant']
        read_only_fields = ['tenant']

class AnalysisResultSerializer(serializers.Serializer):
    task_id = serializers.CharField()
    analysis_type = serializers.CharField()
    result = serializers.JSONField()

class DataPreprocessResultSerializer(serializers.Serializer):
    task_id = serializers.CharField()
    process_type = serializers.CharField()
    result = serializers.JSONField()

class DataManagementResultSerializer(serializers.Serializer):
    task_id = serializers.CharField()
    operation_type = serializers.CharField()
    result = serializers.JSONField()

class MetricFeedbackSerializer(serializers.Serializer):
    metric_id = serializers.IntegerField()
    feedback = serializers.CharField()

class MetricPlaygroundSerializer(serializers.Serializer):
    scenario_data = serializers.DictField()
    simulation_results = serializers.DictField()