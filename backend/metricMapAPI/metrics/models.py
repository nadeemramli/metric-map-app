from django.db import models
from enum import Enum
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django_tenants.models import TenantMixin, DomainMixin
from .computations.permanent_computations import PermanentComputations
from django.db.models import Manager

''' 
Tenant, Organization and User Management: Setting Up
     1. Client: Represents a tenant in a multi-tenant system.
     2. Domain: Handles domain management for tenants.
     3. CustomUser: An extension of Django's AbstractUser with tenant awareness.
     4. UserProfile: Linked to CustomUser for additional profile information.
     5. Team: Represents groups within a tenant's organization.
     6. Project: Represents projects within a tenant.
'''
class Client(TenantMixin):
    name = models.CharField(max_length=100, db_index=True)
    created_on = models.DateField(auto_now_add=True)
    
    auto_create_schema = True

    def __str__(self):
        return self.name
    
    def generate_schema_name(self):
        return slugify(self.name).replace("-", "_")
    '''
        Represents a tenant in the multi-tenant system.
        - `name`: The name of the client (tenant).
        - `created_on`: The date when the client was created.
        - `auto_create_schema`: Automatically creates a database schema for each tenant.
    '''

class Domain(DomainMixin):
    pass

    '''
        Handles domain management for tenants. Inherits all fields from DomainMixin.
    '''

class TenantAwareMixin(models.Model):
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='tenant_%(class)ss')

    class Meta:
        abstract = True
    
    '''
        A mixin to make models tenant-aware.
            - `tenant`: A foreign key to the Client model, establishing the tenant relationship.
    '''

class Team(TenantAwareMixin):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    '''
        Represents groups within a tenant's organization.
        - `name`: The name of the team.
        - `description`: A description of the team's purpose or role.
        - `created_at`: Timestamp of when the team was created.
        - `updated_at`: Timestamp of the last update to the team.
    '''

class CustomUser(AbstractUser, TenantAwareMixin):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
    
    def __str__(self):
        return self.username
    
    '''
        An extension of Django's AbstractUser with tenant awareness.
        - `team`: The team to which the user belongs (optional).
    '''

class UserProfile(TenantAwareMixin):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    
    '''
        Linked to CustomUser for additional profile information.
        - `user`: One-to-one relationship with CustomUser.
    '''

class Project(TenantAwareMixin):
    name = models.CharField(max_length=100, db_index=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    '''
        Represents projects within a tenant.
        - `name`: The name of the project.
        - `created_on`: The date when the project was created.
    '''

'''
Utils for Metrics - This allow user to identify the instrumentation phase of analysis.
'''
class ValueType(Enum):
    COUNT = 'Count'
    PERCENTAGE = 'Percentage'
    CURRENCY = 'Currency'
    RATIO = 'Ratio'

class MetricType(Enum):
    KPI = 'Key Performance Indicator'
    NORTH_STAR = 'North Star Metric'
    INPUT = 'Input Metric'
    DIAGNOSIS = 'Diagnosis Metric'
    OUTPUT = 'Output Metric'

class Rhythm(Enum):
    DAILY = 'Daily'
    WEEKLY = 'Weekly'
    BI_WEEKLY = 'Bi-Weekly'
    MONTHLY = 'Monthly'
    QUARTERLY = 'Quarterly'
    YEARLY = 'Yearly'

class ExperimentStatus(Enum):
    PLANNED = 'Planned'
    IN_PROGRESS = 'In-Progress'
    COMPLETED = 'Completed'
    ON_HOLD = 'On-Hold'
    CANCELLED = 'Cancelled'
    ARCHIVED = 'Archived'

class Impact(Enum):
    NO_IMPACT = 'No-Impact'
    POSITIVE = 'Positive'
    NEGATIVE = 'Negative'

class Importance(Enum):
    MINOR = 'Minor'
    MEDIUM = 'Medium'
    MAJOR = 'Major'

class AnomalyType(Enum):
    IGNORE = 'Ignore/Noise'
    ANOMALY = 'Anomaly'
    OPPORTUNITY = 'Opportunity'

class QualityType(Enum):
    HIGH = 'High-Quality'
    LOW = 'Low-Quality'

class Confidence(Enum):
    NONE = 'None'
    ON_TRACK = 'On-track'
    AT_RISK = 'At-risk'
    OFF_TRACK = 'Off-track'

''' 
Core Business Logic:
    1. Category: For categorizing metrics.
    2. Tag: For tagging metrics, linked to projects.
    3. Metric: The central model for storing various types of metrics.
    4. MetricMetadata: Stores additional information about metrics.
    5. MetricTarget: Defines targets for metrics.
    6. Correlation Analysis: Stores correlation data between metrics.
    7. Connection: Represents relationships between metrics.
'''
class Category(TenantAwareMixin):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    
    '''
        For categorizing metrics.
        - `name`: The name of the category.
    '''

class Tag(TenantAwareMixin):
    name = models.CharField(max_length=100, db_index=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tags')

    class Meta:
        unique_together = ('name', 'project')
        indexes = [
            models.Index(fields=['name', 'project']),
        ]

    def __str__(self):
        return self.name
    
    '''
        For tagging metrics, linked to projects.
        - `name`: The name of the tag.
        - `project`: The project to which the tag belongs.
    '''
class MetricManager(Manager):
    def bulk_create(self, objs, **kwargs):
        result = super().bulk_create(objs, **kwargs)
        client = objs[0].client if objs else None
        if client:
            metric_ids = [obj.id for obj in result]
            PermanentComputations(metric_ids, client).run_all_computations()
        return result

class Metric(TenantAwareMixin):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='metrics')
    name = models.CharField(max_length=100, db_index=True)
    type = models.CharField(
        max_length=50,
        choices=[(t.name, t.value) for t in MetricType],
        default=MetricType.KPI.name,
        db_index=True
    )
    value_type = models.CharField(
        max_length=20,
        choices=[(t.name, t.value) for t in ValueType],
        default=ValueType.COUNT.name
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='metrics')
    tags = models.ManyToManyField(Tag, related_name='metrics')
    
    class Meta:
        unique_together = ('tenant', 'project', 'name')

    def clean(self):
        super().clean()
        if Metric.objects.filter(tenant=self.tenant, project=self.project, name=self.name).exclude(pk=self.pk).exists():
            raise ValidationError("A metric with this name already exists for this project and tenant.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    '''
        The central model for storing various types of metrics.
        - `project`: The project to which the metric belongs.
        - `name`: The name of the metric.
        - `type`: The type of metric (e.g., KPI, North Star, etc.).
        - `value_type`: The type of value for the metric (e.g., Count, Percentage, etc.).
        - `category`: The category of the metric (optional).
        - `tags`: Tags associated with the metric.
    '''

class DataQualityScore(TenantAwareMixin):
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name='data_quality_scores')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='data_quality_scores')
    data_entry = models.CharField(max_length=255)
    completeness_score = models.FloatField()
    accuracy_score = models.FloatField()
    consistency_score = models.FloatField()
    timeliness_score = models.FloatField()
    overall_score = models.FloatField()

    def __str__(self):
        return f"Data Quality Score for {self.metric.name} in {self.project.name}"
    
    class Meta:
        unique_together = ('tenant', 'metric', 'project')
    
    '''
        Stores data quality scores for metrics.
        - `data_entry`: Identifier for the data entry being scored.
        - `completeness_score`: Score for data completeness.
        - `accuracy_score`: Score for data accuracy.
        - `consistency_score`: Score for data consistency.
        - `timeliness_score`: Score for data timeliness.
        - `overall_score`: Overall data quality score.
    '''
  
class MetricMetadata(TenantAwareMixin):
    metric = models.OneToOneField('Metric', on_delete=models.CASCADE)
    data_source = models.CharField(max_length=100, blank=True)
    source_url = models.URLField(blank=True)
    rhythm = models.CharField(
        max_length=20,
        choices=[(r.name, r.value) for r in Rhythm],
        default=Rhythm.MONTHLY.name
    )
    last_updated = models.DateTimeField(auto_now=True, db_index=True)
    data_quality_score = models.OneToOneField(DataQualityScore, on_delete=models.CASCADE, null=True, blank=True, related_name='data_quality_score')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='metric_metadata_set')
    technical_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    artifacts_url = models.URLField(blank=True)
    hypothesis = models.TextField(blank=True)
    confidence = models.CharField(
        max_length=20,
        choices=[(c.name, c.value) for c in Confidence],
        default=Confidence.NONE.name
    )
    position_x = models.FloatField(default=0)
    position_y = models.FloatField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['last_updated']),
        ]

    def __str__(self):
        return f"Metadata for: {self.metric}"

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y
        self.save()

    @property
    def position(self):
        return {"x": self.position_x, "y": self.position_y}
    
    '''
        Stores additional information about metrics.
        - `metric`: One-to-one relationship with the Metric model.
        - `data_source`: The source of the metric data.
        - `source_url`: URL of the data source.
        - `rhythm`: Frequency of data updates.
        - `last_updated`: Timestamp of the last update.
        - `data_quality_score`: Associated data quality score.
        - `team`: Team responsible for the metric.
        - `technical_description`: Technical details about the metric.
        - `description`: General description of the metric.
        - `artifacts_url`: URL for any related artifacts.
        - `hypothesis`: Hypothesis related to the metric.
        - `confidence`: Confidence level in the metric.
        - `position_x` and `position_y`: Coordinates for visual representation.
    '''

class MetricTarget(TenantAwareMixin):
    metric = models.ForeignKey(Metric, related_name='targets', on_delete=models.CASCADE)
    target_kpi = models.CharField(max_length=100)
    target_remarks = models.TextField(blank=True)
    target_date = models.DateField(null=True, blank=True, db_index=True)
    target_value = models.FloatField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['metric', 'target_date']),
        ]
    
    def __str__(self):
        return f"Target for {self.metric.name}: {self.target_kpi}"
    
    def clean(self):
        super().clean()
        if self.target_date and self.target_date < timezone.now().date():
            raise ValidationError("Target date cannot be in the past.")
    
    '''
        Defines targets for metrics.
        - `metric`: The metric for which the target is set.
        - `target_kpi`: The target KPI value.
        - `target_remarks`: Any remarks about the target.
        - `target_date`: The date by which the target should be achieved.
        - `target_value`: The numerical target value.
    '''

class Correlation(TenantAwareMixin):
    metric1 = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name='correlations_from')
    metric2 = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name='correlations_to')
    lag = models.IntegerField()
    pearson_correlation = models.FloatField()
    spearman_correlation = models.FloatField()

    class Meta:
        unique_together = ('tenant', 'metric1', 'metric2', 'lag')
    
    def __str__(self):
        return f"Correlation between {self.metric1} and {self.metric2} with lag {self.lag}"
    
    '''
        Stores correlation data between metrics.
        - `metric1` and `metric2`: The two metrics being correlated.
        - `lag`: The time lag for the correlation.
        - `pearson_correlation`: Pearson correlation coefficient.
        - `spearman_correlation`: Spearman correlation coefficient.
    '''
class Connection(TenantAwareMixin):
    from_metric = models.ForeignKey(Metric, related_name='outgoing_connections', on_delete=models.CASCADE)
    to_metric = models.ForeignKey(Metric, related_name='incoming_connections', on_delete=models.CASCADE)
    relationship = models.CharField(max_length=100, blank=True)
    strength = models.FloatField()

    class Meta:
        unique_together = ('tenant', 'from_metric', 'to_metric')

    def __str__(self):
        return f"Connection from {self.from_metric} to {self.to_metric}"

    def get_correlations(self):
        return Correlation.objects.filter(
            metric1=self.from_metric, metric2=self.to_metric
        )

    def get_pearson_correlation(self):
        correlation = self.get_correlations().first()
        if correlation:
            return correlation.pearson_correlation
        return None

    def get_spearman_correlation(self):
        correlation = self.get_correlations().first()
        if correlation:
            return correlation.spearman_correlation
        return None
    
    def clean(self):
        super().clean()
        if self.from_metric == self.to_metric:
            raise ValidationError("A metric cannot be connected to itself.")
    
    '''
        Represents relationships between metrics.
        - `from_metric`: The source metric of the connection.
        - `to_metric`: The target metric of the connection.
        - `relationship`: Description of the relationship between the metrics.
    '''

class ConnectionManager(Manager):
    def bulk_create(self, objs, **kwargs):
        result = super().bulk_create(objs, **kwargs)
        affected_metric_ids = set()
        for obj in objs:
            affected_metric_ids.add(obj.from_metric_id)
            affected_metric_ids.add(obj.to_metric_id)
        client = objs[0].client if objs else None
        if client:
            PermanentComputations(list(affected_metric_ids), client).run_all_computations()
        return result

    def bulk_update(self, objs, fields, **kwargs):
        result = super().bulk_update(objs, fields, **kwargs)
        affected_metric_ids = set()
        for obj in objs:
            affected_metric_ids.add(obj.from_metric_id)
            affected_metric_ids.add(obj.to_metric_id)
        client = objs[0].client if objs else None
        if client:
            PermanentComputations(list(affected_metric_ids), client).run_all_computations()
        return result

''' 
Execution and Qualitative Data:
     1. Experiment: Represents experiments conducted on metrics.
     2. ActionRemark: Stores remarks or actions related to metrics.
     3. Insight: Captures user insights about metrics.
     4. Strategy: Represents strategic plans.
     5. TacticalSolution: Represents tactical solutions for metrics.
'''
class Experiment(TenantAwareMixin):
    name = models.CharField(max_length=100, db_index=True)
    title = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='experiment_set')
    description = models.TextField(blank=True)
    objective = models.TextField(blank=True)
    start_date = models.DateField(db_index=True)
    end_date = models.DateField(null=True, blank=True, db_index=True)
    status = models.CharField(
        max_length=20,
        choices=[(s.name, s.value) for s in ExperimentStatus],
        default=ExperimentStatus.PLANNED.name
    )
    metrics = models.ManyToManyField(Metric, related_name='experiments')
    
    result_summary = models.TextField(blank=True)
    result_value = models.FloatField(null=True, blank=True)
    result_date = models.DateField(null=True, blank=True)
    impact_description = models.TextField(blank=True)
    result_files = models.FileField(upload_to='experiment_results/', null=True, blank=True)


    class Meta:
        indexes = [
            models.Index(fields=['start_date', 'end_date']),
        ]

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        if self.end_date and self.start_date and self.end_date < self.start_date:
            raise ValidationError("End date must be after the start date.")
        
        if self.status == ExperimentStatus.COMPLETED.name and not self.result_summary:
            raise ValidationError("Completed experiments must have a result summary.")
        
        if self.start_date and self.start_date > timezone.now().date():
            raise ValidationError("Experiment start date cannot be in the future.")
    
    '''
        Represents experiments conducted on metrics.
        - `name` and `title`: Identifiers for the experiment.
        - `team`: The team conducting the experiment.
        - `description` and `objective`: Details about the experiment.
        - `start_date` and `end_date`: Duration of the experiment.
        - `status`: Current status of the experiment.
        - `metrics`: Metrics involved in the experiment.
        - `result_summary`, `result_value`, `result_date`: Experiment results.
        - `impact_description`: Description of the experiment's impact.
        - `result_files`: Uploaded files related to the experiment results.
    '''

class ActionRemark(TenantAwareMixin):
    metric = models.ForeignKey(Metric, related_name='action_remarks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True, db_index=True)
    summary = models.TextField()
    impact = models.CharField(
        max_length=20,
        choices=[(i.name, i.value) for i in Impact],
        default=Impact.NO_IMPACT.name
    )
    importance = models.CharField(
        max_length=20,
        choices=[(i.name, i.value) for i in Importance],
        default=Importance.MEDIUM.name
    )

    class Meta:
        indexes = [
            models.Index(fields=['metric', 'date']),
        ]
    
    def __str__(self):
        return self.title
    
    '''
        Stores remarks or actions related to metrics.
        - `metric`: The metric to which the remark is related.
        - `title`: Title of the action or remark.
        - `date`: Date of the action or remark.
        - `summary`: Detailed summary of the action or remark.
        - `impact`: The impact of the action (e.g., Positive, Negative).
        - `importance`: The importance of the action or remark.
    '''

class Insight(TenantAwareMixin):
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name='insights')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='insights')
    date = models.DateField(db_index=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['metric', 'date']),
            models.Index(fields=['user', 'date']),
        ]

    def __str__(self):
        return f"Insight for {self.metric.name} on {self.date}"
    
    '''
        Captures user insights about metrics.
        - `metric`: The metric the insight is about.
        - `user`: The user who provided the insight.
        - `date`: Date of the insight.
        - `title`: Title of the insight.
        - `content`: Detailed content of the insight.
        - `created_at` and `updated_at`: Timestamps for creation and last update.
    '''

class Strategy(TenantAwareMixin):
    title = models.CharField(max_length=200)
    description = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='strategies')
    estimated_time = models.DurationField(help_text="Estimated time for strategy completion")
    artifacts_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def clean(self):
        super().clean()
        if self.estimated_time.total_seconds() <= 0:
            raise ValidationError("Estimated time must be positive.")
    
    '''
        Represents strategic plans.
        - `title`: Title of the strategy.
        - `description`: Detailed description of the strategy.
        - `team`: The team responsible for the strategy.
        - `estimated_time`: Estimated duration for strategy completion.
        - `artifacts_url`: URL for any related artifacts.
        - `created_at` and `updated_at`: Timestamps for creation and last update.
    '''

class TacticalSolution(TenantAwareMixin):
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name='solutions')
    title = models.CharField(max_length=200)
    description = models.TextField()
    artifact_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    '''
        Represents tactical solutions for metrics.
        - `metric`: The metric the solution is for.
        - `title`: Title of the tactical solution.
        - `description`: Detailed description of the solution.
        - `artifact_url`: URL for any related artifacts.
        - `created_at` and `updated_at`: Timestamps for creation and last update.
    '''

''' 
Analytics and Computation:
    1. Forecast: Stores forecast data for metrics.
    2. TechnicalIndicator: Stores various technical indicators for metrics.
    3. Anomaly: Represents detected anomalies in metric data.
    4. ImpactAnalysis: Analyzes the impact of experiments on metrics.
    5. Trend: Represents trend information for metrics.
'''
class Forecast(TenantAwareMixin):
    metric = models.ForeignKey(Metric, related_name='forecasts', on_delete=models.CASCADE)
    forecast_date = models.DateField(db_index=True)
    forecast_value = models.FloatField()
    model_used = models.CharField(max_length=100)
    accuracy = models.FloatField(null=True, blank=True)
    lower_bound = models.FloatField()
    upper_bound = models.FloatField()
    confidence_interval = models.JSONField(default=dict, blank=True)
    variance = models.FloatField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['metric', 'forecast_date']),
        ]

    def __str__(self):
        return f"{self.metric.name} forecast on {self.forecast_date}"
    
    '''
        Stores forecast data for metrics.

        metric: The metric being forecasted.
        forecast_date: The date for which the forecast is made.
        forecast_value: The predicted value.
        model_used: The forecasting model used.
        accuracy: The accuracy of the forecast.
        confidence_interval: JSON field for storing confidence interval data.
        variance: The variance of the forecast.
    '''

class TechnicalIndicator(TenantAwareMixin):
    metric = models.ForeignKey('Metric', on_delete=models.CASCADE)
    date = models.DateField()
    stochastic_value = models.FloatField()
    rsi_value = models.FloatField()
    percent_change = models.FloatField()
    moving_average = models.FloatField()
    
    def __str__(self):
        return f"{self.metric} values for Stochastic:{self.stochastic_value}, RSI: {self.rsi_value}, % Change: {self.percent_change} and Moving Average: {self.moving_average}. "
    
    def clean(self):
        super().clean()
        if self.rsi_value < 0 or self.rsi_value > 100:
            raise ValidationError("RSI value must be between 0 and 100.")
        
        if self.stochastic_value < 0 or self.stochastic_value > 100:
            raise ValidationError("Stochastic value must be between 0 and 100.")
    
    '''
        Stores various technical indicators for metrics.

        metric: The metric for which indicators are calculated.
        date: The date of the indicator values.
        stochastic_value: The stochastic oscillator value.
        rsi_value: The Relative Strength Index value.
        percent_change: The percentage change.
        moving_average: The moving average value.
    '''

class Anomaly(TenantAwareMixin):
    metric = models.ForeignKey(Metric, related_name='anomalies', on_delete=models.CASCADE)
    detection_date = models.DateField(db_index=True)
    anomaly_value = models.FloatField()
    anomaly_score = models.FloatField()
    notes = models.TextField(blank=True)
    anomaly_type = models.CharField(
        max_length=20,
        choices=[(t.name, t.value) for t in AnomalyType],
        default=AnomalyType.IGNORE.name
    )
    quality = models.CharField(
        max_length=20,
        choices=[(q.name, q.value) for q in QualityType],
        default=QualityType.LOW.name
    )

    class Meta:
        indexes = [
            models.Index(fields=['metric', 'detection_date']),
        ]

    def __str__(self):
        return f"Anomaly in {self.metric.name} on {self.detection_date}"
    
    def clean(self):
        super().clean()
        if self.detection_date > timezone.now().date():
            raise ValidationError("Anomaly detection date cannot be in the future.")
        
        if self.anomaly_score < 0 or self.anomaly_score > 1:
            raise ValidationError("Anomaly score must be between 0 and 1.")
    
    '''
        Represents detected anomalies in metric data.

        metric: The metric in which the anomaly was detected.
        detection_date: The date the anomaly was detected.
        anomaly_value: The value that was flagged as anomalous.
        anomaly_score: A score indicating the severity of the anomaly.
        notes: Additional notes about the anomaly.
        anomaly_type: The type of anomaly (e.g., Ignore, Anomaly, Opportunity).
        quality: The quality of the anomaly detection (High or Low).
    '''

class ImpactAnalysis(TenantAwareMixin):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, related_name='impact_analyses')
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name='impact_analyses')
    before_value = models.FloatField()
    after_value = models.FloatField()
    percentage_change = models.FloatField()
    confidence = models.FloatField()
    artifact_link = models.URLField(blank=True)
    
    def clean(self):
        super().clean()
        if self.confidence < 0 or self.confidence > 1:
            raise ValidationError("Confidence must be between 0 and 1.")
        
        if self.experiment.start_date > timezone.now().date():
            raise ValidationError("Cannot perform impact analysis on future experiments.")
    
    '''
        Analyzes the impact of experiments on metrics.

        experiment: The experiment being analyzed.
        metric: The metric being impacted.
        before_value: The metric value before the experiment.
        after_value: The metric value after the experiment.
        percentage_change: The percentage change in the metric.
        confidence: The confidence level of the impact analysis.
        artifact_link: Link to any related artifacts.
    '''

class Trend(TenantAwareMixin):
    metric = models.ForeignKey(Metric, related_name='trends', on_delete=models.CASCADE)
    trend_type = models.CharField(max_length=50)
    start_date = models.DateField(db_index=True)
    end_date = models.DateField(null=True, blank=True, db_index=True)
    trend_value = models.FloatField()
    notes = models.TextField(blank=True)
    slope = models.FloatField()

    class Meta:
        indexes = [
            models.Index(fields=['metric', 'start_date', 'end_date']),
        ]

    def __str__(self):
        return f"Trend in {self.metric.name} from {self.start_date} to {self.end_date}"
    
    '''
        Represents trend information for metrics.

        metric: The metric for which the trend is identified.
        trend_type: The type of trend observed.
        start_date and end_date: The period over which the trend is observed.
        trend_value: A numerical representation of the trend.
        notes: Additional notes about the trend.
    '''

class MovingAverage(TenantAwareMixin):
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name='moving_averages')
    date = models.DateTimeField()
    ma_type = models.CharField(max_length=10)  # 'SMA', 'EMA', or 'WMA'
    period = models.IntegerField()
    value = models.FloatField()
    
    '''
    Stores calculated moving averages for metrics.

    metric: The metric for which the moving average is calculated.
    date: The date and time for which the moving average is calculated.
    ma_type: The type of moving average (e.g., 'SMA', 'EMA', 'WMA').
    period: The number of data points used in calculating the moving average.
    value: The calculated moving average value.

    This model allows for storing different types of moving averages (Simple,
    Exponential, Weighted) with various periods. It's useful for trend analysis,
    smoothing out short-term fluctuations, and highlighting longer-term trends
    or cycles in the data.
    '''

class SeasonalityResult(TenantAwareMixin):  # Remove TenantAwareMixin
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name='seasonality_results')
    seasonality_type = models.CharField(max_length=20)  # e.g., 'daily', 'weekly', 'yearly'
    strength = models.FloatField()
    period = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('metric', 'seasonality_type')  # Changed from ('tenant', 'metric')
        get_latest_by = 'created_at'

    def __str__(self):
        return f"Seasonality for {self.metric.name}: {self.seasonality_type}"
    
    '''
    Stores the results of seasonality analysis for metrics.

    metric: The metric for which seasonality is analyzed.
    seasonality_type: The type of seasonality detected (e.g., 'daily', 'weekly', 'yearly').
    strength: A value between 0 and 1 indicating the strength of the seasonal pattern.
    period: The number of time units (e.g., days) in one seasonal cycle.
    last_updated: The date and time when this seasonality result was last updated.

    This model captures the seasonal patterns detected in a metric's time series data.
    Seasonality refers to regular and predictable patterns that repeat over a fixed
    period. Understanding seasonality is crucial for:

    1. Forecasting: Accounting for seasonal variations can improve prediction accuracy.
    2. Trend Analysis: Separating seasonal effects from underlying trends.
    3. Anomaly Detection: Identifying deviations from expected seasonal patterns.
    4. Resource Planning: Anticipating cyclical changes in metrics for better resource allocation.

    The 'strength' field indicates how pronounced the seasonal pattern is, with values
    closer to 1 indicating stronger seasonality. The 'period' field helps in understanding
    the cycle length of the seasonal pattern.

    This information can be used to adjust other analyses (like trend detection or
    forecasting) to account for seasonal effects, leading to more accurate insights
    and predictions.
    '''

class TrendChangePoint(TenantAwareMixin):
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name='trend_change_points')
    date = models.DateTimeField()
    direction = models.CharField(max_length=20)  # e.g., 'upward', 'downward'
    significance = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"Trend change for {self.metric.name} on {self.date}: {self.direction}"

    @property
    def tenant(self):
        return self.metric.tenant

    '''
    Represents detected significant changes in the trend of a metric.

    metric: The metric for which the trend change is detected.
    date: The date and time when the trend change occurred.
    change_type: The type of change (e.g., 'upward', 'downward').
    significance: A value indicating the statistical significance of the change (0 to 1).

    This model is useful for identifying important shifts in metric behavior,
    which can be crucial for decision-making and understanding the impact of
    various factors on the metric's performance over time.
    '''

class NetworkAnalysisResult(TenantAwareMixin):
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name='network_analysis_results')
    analysis_type = models.CharField(max_length=20)  # e.g., 'PageRank', 'community'
    result = models.JSONField()  # Store complex results as JSON
    
    '''
    Stores results of network analysis performed on metric relationships.

    metric: The focal metric for the analysis, if applicable. Can be null for global network analyses.
    analysis_type: The type of network analysis performed (e.g., 'PageRank', 'community').
    result: A JSON field storing the complex results of the network analysis.
    timestamp: The date and time when the analysis was performed.

    This model is used to store results from advanced network analyses on the
    relationships between metrics. It can include results such as PageRank scores,
    which indicate the relative importance of metrics in the network, and
    community detection results, which group closely related metrics together.

    The results stored in this model can provide insights into the structure of
    metric relationships, helping to identify key performance indicators and
    understand how different metric groups interact with each other.

    Note: The 'metric' field can be null, allowing for storage of global network
    analyses that don't focus on a specific metric.
    '''

''' 
Utilities
    1. HistoricalData: Stores historical data points for metrics.
    2. TimeDimension: A utility model for time-based operations. We can forecast a year of time using this.
    3. Dashboard and Report: Stores Data For creating customizable dashboards and reports.
'''
class HistoricalDataManager(Manager):
    def bulk_create(self, objs, **kwargs):
        result = super().bulk_create(objs, **kwargs)
        affected_metric_ids = set(obj.metric_id for obj in objs)
        client = objs[0].client if objs else None
        if client:
            PermanentComputations(list(affected_metric_ids), client).run_all_computations()
        return result

    def bulk_update(self, objs, fields, **kwargs):
        result = super().bulk_update(objs, fields, **kwargs)
        affected_metric_ids = set(obj.metric_id for obj in objs)
        client = objs[0].client if objs else None
        if client:
            PermanentComputations(list(affected_metric_ids), client).run_all_computations()
        return result

class HistoricalData(TenantAwareMixin):
    metric = models.ForeignKey(Metric, related_name='historical_data', on_delete=models.CASCADE)
    date = models.DateField(db_index=True)
    value = models.FloatField(null=True, blank=True)
    forecast = models.ForeignKey(Forecast, related_name='historical_data', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['metric', 'date']),
        ]
    
    def clean(self):
        super().clean()
        if self.metric.value_type == ValueType.PERCENTAGE.name:
            if self.value < 0 or self.value > 100:
                raise ValidationError(f"Percentage values must be between 0 and 100. Invalid value: {self.value}")
        
        if self.date > timezone.now().date():
            raise ValidationError("Historical data cannot be in the future.")
    
    '''
        Stores historical data points for metrics.

        metric: The metric for which historical data is stored.
        date: The date of the data point.
        value: The value of the metric on that date.
        forecast: Optional link to a forecast for comparison.
    '''

class TimeDimension(TenantAwareMixin):
    date = models.DateField(unique=True)
    day = models.IntegerField()
    day_of_week = models.IntegerField()
    day_name = models.CharField(max_length=10)
    week = models.IntegerField()
    month = models.IntegerField()
    month_name = models.CharField(max_length=10)
    quarter = models.IntegerField()
    year = models.IntegerField()
    is_weekend = models.BooleanField()
    is_holiday = models.BooleanField()

    class Meta:
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['year', 'month', 'day']),
        ]

    def __str__(self):
        return str(self.date)
    
    '''
        A utility model for time-based operations.

        Stores various time-related attributes for each date.
        Useful for time-based analysis and reporting.
    '''

class Dashboard(TenantAwareMixin):
    name = models.CharField(max_length=100, db_index=True)
    layout = models.JSONField(default=dict, blank=True)
    
    '''
        Stores data for creating customizable dashboards.

        name: The name of the dashboard.
        layout: JSON field to store the layout configuration of the dashboard.
    '''

class Report(TenantAwareMixin):
    metric = models.ForeignKey(Metric, related_name='report', on_delete=models.CASCADE)
    tenant = models.ForeignKey(Client, related_name='tenant_report', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    configuration = models.JSONField(default=dict, blank=True)
    analysis_result = models.JSONField(null=True, blank=True)
    forecast_result = models.JSONField(null=True, blank=True)
    anomaly_result = models.JSONField(null=True, blank=True)
    relationship_result = models.JSONField(null=True, blank=True)
    report = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    '''
        Stores data for creating customizable reports.

        name: The name of the report.
        configuration: JSON field to store the configuration of the report.
    '''

class ComputationStatus(TenantAwareMixin):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    error_message = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

class Notification(TenantAwareMixin):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class PendingComputation(TenantAwareMixin):
    metric = models.ForeignKey('Metric', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('tenant', 'metric')

'''
Summary of related_name Attributes

This document provides a summary of all `related_name` attributes used in the models, along with suggestions for missing or improved names.

Client
- `tenant_%(class)ss` (used in TenantAwareMixin)

Team
- `members` (in CustomUser)
- `experiments` (in Experiment)
- `strategies` (in Strategy)

CustomUser
- `profile` (in UserProfile)
- `insights` (in Insight)

Project
- `tags` (in Tag)
- `metrics` (in Metric)

Category
- `metrics` (in Metric)

Tag
- `metrics` (in Metric)

Metric
- `targets` (in MetricTarget)
- `correlations_as_metric1` (in Correlation)
- `correlations_as_metric2` (in Correlation)
- `causes` (in Connection)
- `effects` (in Connection)
- `experiments` (in Experiment)
- `action_remarks` (in ActionRemark)
- `insights` (in Insight)
- `solutions` (in TacticalSolution)
- `forecasts` (in Forecast)
- `anomalies` (in Anomaly)
- `impact_analyses` (in ImpactAnalysis)
- `trends` (in Trend)
- `historical_data` (in HistoricalData)

Experiment
- `impact_analyses` (in ImpactAnalysis)

Forecast
- `historical_data` (in HistoricalData)

----------------------------------------------------

Usage Examples for Enum:

Usage examples:
# Experiment.objects.create(name="Test", status=ExperimentStatus.PLANNED.name)
# ActionRemark.objects.create(title="Important", impact=Impact.POSITIVE.name, importance=Importance.MAJOR.name)
# Anomaly.objects.create(anomaly_type=AnomalyType.OPPORTUNITY.name, quality=QualityType.HIGH.name)
# MetricMetadata.objects.create(rhythm=Rhythm.WEEKLY.name, confidence=Confidence.ON_TRACK.name)

'''