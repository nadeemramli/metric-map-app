# Test Run: metrics.tests.test_permanent_computations.api_tests

Total tests: 3
Passed: 0
Failed: 1
Errors: 2

## test_client_operations (metrics.tests.test_permanent_computations.api_tests.APITestCase)
Status: failure
Duration: 0.159 seconds

### Failure
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/api_tests.py", line 18, in test_client_operations
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
AssertionError: 404 != 201
```

### Output
```
2024-08-08 03:05:48,745 - metrics - DEBUG - Starting test: test_client_operations (metrics.tests.test_permanent_computations.api_tests.APITestCase)
2024-08-08 03:05:48,902 - django.request - WARNING - Not Found: /api/clients/
```

## test_metric_operations (metrics.tests.test_permanent_computations.api_tests.APITestCase)
Status: error
Duration: 0.174 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/api_tests.py", line 62, in test_metric_operations
    client = Client.objects.create(name="Test Client")
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
2024-08-08 03:05:48,905 - metrics - DEBUG - Starting test: test_metric_operations (metrics.tests.test_permanent_computations.api_tests.APITestCase)
```

## test_project_operations (metrics.tests.test_permanent_computations.api_tests.APITestCase)
Status: error
Duration: 0.176 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/api_tests.py", line 38, in test_project_operations
    client = Client.objects.create(name="Test Client")
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
2024-08-08 03:05:49,084 - metrics - DEBUG - Starting test: test_project_operations (metrics.tests.test_permanent_computations.api_tests.APITestCase)
```

