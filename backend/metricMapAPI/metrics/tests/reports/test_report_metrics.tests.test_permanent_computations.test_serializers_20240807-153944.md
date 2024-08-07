# Test Run: metrics.tests.test_permanent_computations.test_serializers

Total tests: 55
Passed: 0
Failed: 0
Errors: 55

## test_action_remark_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.038 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:42,769 - metrics - DEBUG - Starting test: test_action_remark_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_anomaly_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.031 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:42,814 - metrics - DEBUG - Starting test: test_anomaly_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_bulk_create_metrics (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.036 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:42,848 - metrics - DEBUG - Starting test: test_bulk_create_metrics (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_category_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.037 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:42,888 - metrics - DEBUG - Starting test: test_category_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_client_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.042 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:42,928 - metrics - DEBUG - Starting test: test_client_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_computation_status_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.035 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:42,975 - metrics - DEBUG - Starting test: test_computation_status_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_connection_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.034 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,015 - metrics - DEBUG - Starting test: test_connection_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_correlation_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.034 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,051 - metrics - DEBUG - Starting test: test_correlation_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_custom_method_to_representation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.033 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,088 - metrics - DEBUG - Starting test: test_custom_method_to_representation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_custom_user_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.032 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,124 - metrics - DEBUG - Starting test: test_custom_user_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_dashboard_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.035 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,159 - metrics - DEBUG - Starting test: test_dashboard_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_data_quality_score_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.032 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,197 - metrics - DEBUG - Starting test: test_data_quality_score_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_date_time_field_handling (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.032 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,232 - metrics - DEBUG - Starting test: test_date_time_field_handling (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_domain_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.033 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,266 - metrics - DEBUG - Starting test: test_domain_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_deserialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.028 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,301 - metrics - DEBUG - Starting test: test_experiment_deserialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_edge_cases (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.034 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,334 - metrics - DEBUG - Starting test: test_experiment_edge_cases (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_metric_relationship (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.031 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,371 - metrics - DEBUG - Starting test: test_experiment_metric_relationship (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_nested_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.033 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,405 - metrics - DEBUG - Starting test: test_experiment_nested_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_read_only_fields (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.037 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,441 - metrics - DEBUG - Starting test: test_experiment_read_only_fields (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.036 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,480 - metrics - DEBUG - Starting test: test_experiment_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_validation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.034 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,518 - metrics - DEBUG - Starting test: test_experiment_validation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_forecast_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.031 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,554 - metrics - DEBUG - Starting test: test_forecast_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_historical_data_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.031 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,589 - metrics - DEBUG - Starting test: test_historical_data_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_impact_analysis_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.032 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,622 - metrics - DEBUG - Starting test: test_impact_analysis_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_insight_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.034 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,657 - metrics - DEBUG - Starting test: test_insight_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_many_to_many_relationship (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.034 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,694 - metrics - DEBUG - Starting test: test_many_to_many_relationship (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_deserialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.030 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,730 - metrics - DEBUG - Starting test: test_metric_deserialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_edge_cases (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.033 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,764 - metrics - DEBUG - Starting test: test_metric_edge_cases (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_error_handling (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.032 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,799 - metrics - DEBUG - Starting test: test_metric_error_handling (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_metadata_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.028 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,834 - metrics - DEBUG - Starting test: test_metric_metadata_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.030 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,865 - metrics - DEBUG - Starting test: test_metric_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_target_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.031 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,899 - metrics - DEBUG - Starting test: test_metric_target_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_validation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.031 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,933 - metrics - DEBUG - Starting test: test_metric_validation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_moving_average_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.031 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:43,966 - metrics - DEBUG - Starting test: test_moving_average_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_network_analysis_result_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.033 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,001 - metrics - DEBUG - Starting test: test_network_analysis_result_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_notification_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.032 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,036 - metrics - DEBUG - Starting test: test_notification_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_pending_computation_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.033 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,072 - metrics - DEBUG - Starting test: test_pending_computation_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_project_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.034 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,108 - metrics - DEBUG - Starting test: test_project_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_report_complex_field_deserialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.034 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,144 - metrics - DEBUG - Starting test: test_report_complex_field_deserialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_report_complex_field_serialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.033 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,181 - metrics - DEBUG - Starting test: test_report_complex_field_serialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_report_complex_field_validation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.035 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,218 - metrics - DEBUG - Starting test: test_report_complex_field_validation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_report_edge_cases (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.031 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,256 - metrics - DEBUG - Starting test: test_report_edge_cases (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_report_metric_relationship (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.031 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,291 - metrics - DEBUG - Starting test: test_report_metric_relationship (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_report_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.033 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,325 - metrics - DEBUG - Starting test: test_report_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_seasonality_result_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.034 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,363 - metrics - DEBUG - Starting test: test_seasonality_result_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_strategy_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.038 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,400 - metrics - DEBUG - Starting test: test_strategy_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_tactical_solution_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.037 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,441 - metrics - DEBUG - Starting test: test_tactical_solution_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_tag_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.037 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,481 - metrics - DEBUG - Starting test: test_tag_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_team_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.036 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,521 - metrics - DEBUG - Starting test: test_team_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_technical_indicator_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.033 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,560 - metrics - DEBUG - Starting test: test_technical_indicator_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_time_dimension_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.036 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,595 - metrics - DEBUG - Starting test: test_time_dimension_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_trend_change_point_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.040 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,634 - metrics - DEBUG - Starting test: test_trend_change_point_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_trend_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.035 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,676 - metrics - DEBUG - Starting test: test_trend_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_user_profile_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.031 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,714 - metrics - DEBUG - Starting test: test_user_profile_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_write_only_field (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.037 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 31, in setUp
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
2024-08-07 15:39:44,748 - metrics - DEBUG - Starting test: test_write_only_field (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

