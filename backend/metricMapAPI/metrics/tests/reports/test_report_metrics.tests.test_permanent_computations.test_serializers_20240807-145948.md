# Test Run: metrics.tests.test_permanent_computations.test_serializers

Total tests: 35
Passed: 0
Failed: 0
Errors: 35

## test_action_remark_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.027 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:47,664 - metrics - DEBUG - Starting test: test_action_remark_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_anomaly_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.024 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:47,695 - metrics - DEBUG - Starting test: test_anomaly_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_category_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.026 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:47,723 - metrics - DEBUG - Starting test: test_category_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_client_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.024 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:47,752 - metrics - DEBUG - Starting test: test_client_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_computation_status_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.025 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:47,779 - metrics - DEBUG - Starting test: test_computation_status_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_connection_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.025 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:47,808 - metrics - DEBUG - Starting test: test_connection_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_correlation_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.025 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:47,835 - metrics - DEBUG - Starting test: test_correlation_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_custom_user_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.025 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:47,862 - metrics - DEBUG - Starting test: test_custom_user_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_dashboard_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.024 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:47,889 - metrics - DEBUG - Starting test: test_dashboard_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_data_quality_score_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.025 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:47,915 - metrics - DEBUG - Starting test: test_data_quality_score_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_domain_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.024 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:47,942 - metrics - DEBUG - Starting test: test_domain_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.025 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:47,968 - metrics - DEBUG - Starting test: test_experiment_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_forecast_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.025 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:47,995 - metrics - DEBUG - Starting test: test_forecast_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_historical_data_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.025 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,022 - metrics - DEBUG - Starting test: test_historical_data_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_impact_analysis_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.024 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,049 - metrics - DEBUG - Starting test: test_impact_analysis_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_insight_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.023 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,074 - metrics - DEBUG - Starting test: test_insight_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_metadata_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.023 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,100 - metrics - DEBUG - Starting test: test_metric_metadata_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.025 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,125 - metrics - DEBUG - Starting test: test_metric_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_target_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.024 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,152 - metrics - DEBUG - Starting test: test_metric_target_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_moving_average_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.025 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,178 - metrics - DEBUG - Starting test: test_moving_average_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_network_analysis_result_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.023 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,205 - metrics - DEBUG - Starting test: test_network_analysis_result_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_notification_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.023 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,231 - metrics - DEBUG - Starting test: test_notification_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_pending_computation_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.023 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,256 - metrics - DEBUG - Starting test: test_pending_computation_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_project_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.024 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,282 - metrics - DEBUG - Starting test: test_project_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_report_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.025 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,309 - metrics - DEBUG - Starting test: test_report_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_seasonality_result_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.024 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,336 - metrics - DEBUG - Starting test: test_seasonality_result_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_strategy_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.024 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,363 - metrics - DEBUG - Starting test: test_strategy_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_tactical_solution_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.023 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,390 - metrics - DEBUG - Starting test: test_tactical_solution_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_tag_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.023 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,415 - metrics - DEBUG - Starting test: test_tag_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_team_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.023 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,440 - metrics - DEBUG - Starting test: test_team_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_technical_indicator_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.024 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,466 - metrics - DEBUG - Starting test: test_technical_indicator_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_time_dimension_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.025 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,491 - metrics - DEBUG - Starting test: test_time_dimension_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_trend_change_point_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.025 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,518 - metrics - DEBUG - Starting test: test_trend_change_point_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_trend_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.024 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,545 - metrics - DEBUG - Starting test: test_trend_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_user_profile_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.024 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 29, in setUp
    self.client = Client.objects.create(name="Test Client")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 111, in save
    self.create_schema(check_if_exists=True, verbosity=verbosity)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 174, in create_schema
    _check_schema_name(self.schema_name)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/postgresql_backend/base.py", line 57, in _check_schema_name
    raise ValidationError("Invalid string used for the schema name.")
django.core.exceptions.ValidationError: ['Invalid string used for the schema name.']
```

### Output
```
2024-08-07 14:59:48,571 - metrics - DEBUG - Starting test: test_user_profile_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

