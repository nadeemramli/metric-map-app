from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100, db_index=True)
    created_on = models.DateField(auto_now_add=True)
    
    auto_create_schema = True

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass

class TenantAwareMixin(models.Model):
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='%(class)ss')

    class Meta:
        abstract = True

class Project(TenantAwareMixin):
    name = models.CharField(max_length=100, db_index=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(TenantAwareMixin):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

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

class Metric(TenantAwareMixin):
    class Rhythm(models.TextChoices):
        DAILY = 'Daily', 'Daily'
        WEEKLY = 'Weekly', 'Weekly'
        BI_WEEKLY = 'Bi-Weekly', 'Bi-Weekly'
        MONTHLY = 'Monthly', 'Monthly'
        QUARTERLY = 'Quarterly', 'Quarterly'
        YEARLY = 'Yearly', 'Yearly'

    class ValueType(models.TextChoices):
        COUNT = 'Count', 'Count'
        PERCENTAGE = 'Percentage', 'Percentage'
        CURRENCY = 'Currency', 'Currency'
        RATIO = 'Ratio', 'Ratio'

    class Type(models.TextChoices):
        KPI = 'KPI', 'Key Performance Indicator'
        NORTH_STAR = 'North Star', 'North Star Metric'
        INPUT = 'Input Metric', 'Input Metric'
        DIAGNOSIS = 'Diagnosis', 'Diagnosis Metric'
        OUTPUT = 'Output Metric', 'Output Metric'

    class Confidence(models.TextChoices):
        VERY_LOW = 'Very Low', 'Very Low'
        BELOW_AVERAGE = 'Below Average', 'Below Average'
        AVERAGE = 'Average', 'Average'
        ABOVE_AVERAGE = 'Above Average', 'Above Average'
        VERY_HIGH = 'Very High', 'Very High'

    name = models.CharField(max_length=100, db_index=True)
    type = models.CharField(max_length=50, choices=Type.choices, default=Type.KPI, db_index=True)
    confidence = models.CharField(max_length=50, choices=Confidence.choices, default=Confidence.AVERAGE)
    value_type = models.CharField(max_length=20, choices=ValueType.choices, default=ValueType.COUNT)
    rhythm = models.CharField(max_length=20, choices=Rhythm.choices, default=Rhythm.MONTHLY)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='metrics')
    description = models.TextField(blank=True)
    hypothesis = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='metrics')
    technical_description = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True, db_index=True)
    source = models.CharField(max_length=100, blank=True)
    position_x = models.FloatField(default=0)
    position_y = models.FloatField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'type']),
            models.Index(fields=['last_updated']),
        ]

    def __str__(self):
        return self.name

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y
        self.save()

    @property
    def position(self):
        return {"x": self.position_x, "y": self.position_y}

class Connection(TenantAwareMixin):
    from_metric = models.ForeignKey(Metric, related_name='causes', on_delete=models.CASCADE)
    to_metric = models.ForeignKey(Metric, related_name='effects', on_delete=models.CASCADE)
    relationship = models.CharField(max_length=100, blank=True)
    correlation_coefficient = models.FloatField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['from_metric', 'to_metric']),
        ]

class HistoricalData(TenantAwareMixin):
    metric = models.ForeignKey(Metric, related_name='historical_data', on_delete=models.CASCADE)
    date = models.DateField(db_index=True)
    value = models.FloatField()
    forecasted_value = models.FloatField(null=True, blank=True)
    anomaly_detected = models.BooleanField(default=False)
    trend_component = models.CharField(max_length=50, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['metric', 'date']),
        ]

class Target(TenantAwareMixin):
    metric = models.ForeignKey(Metric, related_name='targets', on_delete=models.CASCADE)
    remarks = models.TextField(blank=True)
    target_kpi = models.CharField(max_length=100)
    target_date = models.DateField(null=True, blank=True, db_index=True)
    target_value = models.FloatField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['metric', 'target_date']),
        ]

class ActionRemark(TenantAwareMixin):
    metric = models.ForeignKey(Metric, related_name='action_remarks', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True, db_index=True)
    description = models.TextField()
    impact = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['metric', 'date']),
        ]

class Dashboard(TenantAwareMixin):
    name = models.CharField(max_length=100, db_index=True)
    layout = models.JSONField(default=dict, blank=True)

class Report(TenantAwareMixin):
    name = models.CharField(max_length=100, db_index=True)
    configuration = models.JSONField(default=dict, blank=True)

class Experiment(TenantAwareMixin):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    start_date = models.DateField(db_index=True)
    end_date = models.DateField(null=True, blank=True, db_index=True)
    status = models.CharField(max_length=50, default='Ongoing')
    results = models.JSONField(default=dict, blank=True)
    metrics = models.ManyToManyField(Metric, related_name='experiments')

    class Meta:
        indexes = [
            models.Index(fields=['start_date', 'end_date']),
        ]

    def __str__(self):
        return self.name

class Forecast(TenantAwareMixin):
    metric = models.ForeignKey(Metric, related_name='forecasts', on_delete=models.CASCADE)
    forecast_date = models.DateField(db_index=True)
    forecast_value = models.FloatField()
    model_used = models.CharField(max_length=100)
    accuracy = models.FloatField(null=True, blank=True)
    confidence_interval = models.JSONField(default=dict, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['metric', 'forecast_date']),
        ]

    def __str__(self):
        return f"{self.metric.name} forecast on {self.forecast_date}"

class Anomaly(TenantAwareMixin):
    metric = models.ForeignKey(Metric, related_name='anomalies', on_delete=models.CASCADE)
    detection_date = models.DateField(db_index=True)
    anomaly_value = models.FloatField()
    anomaly_score = models.FloatField()
    notes = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['metric', 'detection_date']),
        ]

    def __str__(self):
        return f"Anomaly in {self.metric.name} on {self.detection_date}"

class Trend(TenantAwareMixin):
    metric = models.ForeignKey(Metric, related_name='trends', on_delete=models.CASCADE)
    trend_type = models.CharField(max_length=50)
    start_date = models.DateField(db_index=True)
    end_date = models.DateField(null=True, blank=True, db_index=True)
    trend_value = models.FloatField()
    notes = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['metric', 'start_date', 'end_date']),
        ]

    def __str__(self):
        return f"Trend in {self.metric.name} from {self.start_date} to {self.end_date}"