# Test Run: metrics.tests.test_permanent_computations.test_serializers

Total tests: 54
Passed: 0
Failed: 0
Errors: 54

## test_action_remark_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 5.837 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/backends/utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
psycopg2.errors.NotNullViolation: null value in column "tenant_id" of relation "metrics_team" violates not-null constraint
DETAIL:  Failing row contains (1, Test Team, Test Description, 2024-08-07 18:44:39.195215+00, 2024-08-07 18:44:39.195229+00, null).


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 47, in setUp
    self.team = Team.objects.create(name="Test Team", description="Test Description")
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/base.py", line 822, in save
    self.save_base(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/base.py", line 909, in save_base
    updated = self._save_table(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/base.py", line 1071, in _save_table
    results = self._do_insert(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/base.py", line 1112, in _do_insert
    return manager._insert(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 1847, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/sql/compiler.py", line 1823, in execute_sql
    cursor.execute(sql, params)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/backends/utils.py", line 79, in execute
    return self._execute_with_wrappers(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/backends/utils.py", line 92, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/backends/utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/backends/utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
django.db.utils.IntegrityError: null value in column "tenant_id" of relation "metrics_team" violates not-null constraint
DETAIL:  Failing row contains (1, Test Team, Test Description, 2024-08-07 18:44:39.195215+00, 2024-08-07 18:44:39.195229+00, null).

```

### Output
```
=== Starting migration
Operations to perform:
  Apply all migrations: admin, auth, authtoken, contenttypes, metrics, sessions
Running migrations:
  Applying contenttypes.0001_initial...
 OK
  Applying auth.0001_initial...
 OK
  Applying admin.0001_initial...
 OK
  Applying admin.0002_logentry_remove_auto_add...
 OK
  Applying admin.0003_logentry_add_action_flag_choices...
 OK
  Applying contenttypes.0002_remove_content_type_name...
 OK
  Applying auth.0002_alter_permission_name_max_length...
 OK
  Applying auth.0003_alter_user_email_max_length...
 OK
  Applying auth.0004_alter_user_username_opts...
 OK
  Applying auth.0005_alter_user_last_login_null...
 OK
  Applying auth.0006_require_contenttypes_0002...
 OK
  Applying auth.0007_alter_validators_add_error_messages...
 OK
  Applying auth.0008_alter_user_username_max_length...
 OK
  Applying auth.0009_alter_user_last_name_max_length...
 OK
  Applying auth.0010_alter_group_name_max_length...
 OK
  Applying auth.0011_update_proxy_permissions...
 OK
  Applying auth.0012_alter_user_first_name_max_length...
 OK
  Applying authtoken.0001_initial...
 OK
  Applying authtoken.0002_auto_20160226_1747...
 OK
  Applying authtoken.0003_tokenproxy...
 OK
  Applying authtoken.0004_alter_tokenproxy_options...
 OK
  Applying metrics.0001_initial...
 OK
  Applying metrics.0002_alter_actionremark_tenant_alter_anomaly_tenant_and_more...
 OK
  Applying metrics.0003_alter_actionremark_date_alter_anomaly_detection_date_and_more...
 OK
  Applying metrics.0004_remove_connection_metrics_con_from_me_9411ea_idx_and_more...
 OK
  Applying metrics.0005_remove_connection_project_metric_project_and_more...
 OK
  Applying metrics.0006_correlation_customuser_dataqualityscore_and_more...
 OK
  Applying metrics.0007_connection_strength_forecast_lower_bound_and_more...
 OK
  Applying metrics.0008_dataqualityscore_metric_dataqualityscore_project_and_more...
 OK
  Applying metrics.0009_alter_metric_unique_together...
 OK
  Applying metrics.0010_movingaverage_tenant_networkanalysisresult_tenant_and_more...
 OK
  Applying metrics.0011_report_metric...
 OK
  Applying metrics.0012_report_analysis_result_report_anomaly_result_and_more...
 OK
  Applying metrics.0013_remove_trendchangepoint_tenant_and_more...
 OK
  Applying metrics.0014_rename_change_type_trendchangepoint_direction...
 OK
  Applying metrics.0015_alter_seasonalityresult_options_and_more...
 OK
  Applying metrics.0016_alter_seasonalityresult_unique_together_and_more...
 OK
  Applying metrics.0017_computationstatus_notification_pendingcomputation...
 OK
  Applying metrics.0018_seasonalityresult_tenant...
 OK
  Applying sessions.0001_initial...
 OK
2024-08-07 18:44:33,374 - metrics - DEBUG - Starting test: test_action_remark_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
2024-08-07 18:44:33,382 - django.db.backends.schema - DEBUG - CREATE TABLE "django_migrations" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" timestamp with time zone NOT NULL); (params None)
2024-08-07 18:44:33,400 - django.db.backends.schema - DEBUG - CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
2024-08-07 18:44:33,406 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params None)
2024-08-07 18:44:33,413 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL, "codename" varchar(100) NOT NULL); (params None)
2024-08-07 18:44:33,421 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(80) NOT NULL UNIQUE); (params None)
2024-08-07 18:44:33,426 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-07 18:44:33,438 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NOT NULL, "is_superuser" boolean NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-07 18:44:33,448 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-07 18:44:33,453 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-07 18:44:33,458 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename"); (params None)
2024-08-07 18:44:33,462 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:33,464 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id"); (params None)
2024-08-07 18:44:33,467 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_name_a6ea08ec_like" ON "auth_group" ("name" varchar_pattern_ops); (params None)
2024-08-07 18:44:33,470 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id"); (params None)
2024-08-07 18:44:33,474 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:33,477 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:33,478 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id"); (params None)
2024-08-07 18:44:33,482 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id"); (params None)
2024-08-07 18:44:33,491 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_username_6821ab7c_like" ON "auth_user" ("username" varchar_pattern_ops); (params None)
2024-08-07 18:44:33,494 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id"); (params None)
2024-08-07 18:44:33,498 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:33,500 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:33,501 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id"); (params None)
2024-08-07 18:44:33,505 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id"); (params None)
2024-08-07 18:44:33,510 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id"); (params None)
2024-08-07 18:44:33,515 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:33,517 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:33,518 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id"); (params None)
2024-08-07 18:44:33,522 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id"); (params None)
2024-08-07 18:44:33,534 - django.db.backends.schema - DEBUG - CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "action_time" timestamp with time zone NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL, "user_id" integer NOT NULL); (params None)
2024-08-07 18:44:33,543 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:33,544 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:33,545 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id"); (params None)
2024-08-07 18:44:33,549 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id"); (params None)
2024-08-07 18:44:33,581 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ALTER COLUMN "name" DROP NOT NULL; (params None)
2024-08-07 18:44:33,596 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" DROP COLUMN "name" CASCADE; (params None)
2024-08-07 18:44:33,608 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ALTER COLUMN "name" TYPE varchar(255); (params None)
2024-08-07 18:44:33,622 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "email" TYPE varchar(254); (params None)
2024-08-07 18:44:33,645 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_login" DROP NOT NULL; (params None)
2024-08-07 18:44:33,664 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "username" TYPE varchar(150); (params None)
2024-08-07 18:44:33,676 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_name" TYPE varchar(150); (params None)
2024-08-07 18:44:33,695 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group" ALTER COLUMN "name" TYPE varchar(150); (params None)
2024-08-07 18:44:33,721 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "first_name" TYPE varchar(150); (params None)
2024-08-07 18:44:33,775 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_client" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "schema_name" varchar(63) NOT NULL UNIQUE, "name" varchar(100) NOT NULL, "created_on" date NOT NULL); (params None)
2024-08-07 18:44:33,787 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_category" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-07 18:44:33,800 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dashboard" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "layout" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-07 18:44:33,811 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_domain" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "domain" varchar(253) NOT NULL UNIQUE, "is_primary" boolean NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-07 18:44:33,825 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "type" varchar(50) NOT NULL, "confidence" varchar(50) NOT NULL, "value_type" varchar(20) NOT NULL, "rhythm" varchar(20) NOT NULL, "description" text NOT NULL, "hypothesis" text NOT NULL, "technical_description" text NOT NULL, "last_updated" timestamp with time zone NOT NULL, "source" varchar(100) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL, "category_id" bigint NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-07 18:44:33,840 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_historicaldata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "value" double precision NOT NULL, "forecasted_value" double precision NULL, "anomaly_detected" boolean NOT NULL, "trend_component" varchar(50) NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-07 18:44:33,854 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_forecast" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "forecast_date" date NOT NULL, "forecast_value" double precision NOT NULL, "model_used" varchar(100) NOT NULL, "accuracy" double precision NULL, "confidence_interval" jsonb NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-07 18:44:33,873 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "status" varchar(50) NOT NULL, "results" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-07 18:44:33,881 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment_metrics" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "experiment_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-07 18:44:33,894 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_connection" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "relationship" varchar(100) NOT NULL, "correlation_coefficient" double precision NULL, "tenant_id" bigint NOT NULL, "from_metric_id" bigint NOT NULL, "to_metric_id" bigint NOT NULL); (params None)
2024-08-07 18:44:33,906 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_anomaly" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "detection_date" date NOT NULL, "anomaly_value" double precision NOT NULL, "anomaly_score" double precision NOT NULL, "notes" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-07 18:44:33,941 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_actionremark" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NULL, "description" text NOT NULL, "impact" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-07 18:44:33,960 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_project" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "created_on" date NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-07 18:44:33,976 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_report" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "configuration" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-07 18:44:33,995 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tag" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "project_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-07 18:44:34,013 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric_tags" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "metric_id" bigint NOT NULL, "tag_id" bigint NOT NULL); (params None)
2024-08-07 18:44:34,041 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_target" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "remarks" text NOT NULL, "target_kpi" varchar(100) NOT NULL, "target_date" date NULL, "target_value" double precision NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-07 18:44:34,065 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trend" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "trend_type" varchar(50) NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "trend_value" double precision NOT NULL, "notes" text NOT NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-07 18:44:34,073 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_schema_name_87d6fbb5_like" ON "metrics_client" ("schema_name" varchar_pattern_ops); (params None)
2024-08-07 18:44:34,077 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_category" ADD CONSTRAINT "metrics_category_tenant_id_67d98cc6_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,078 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_tenant_id_67d98cc6" ON "metrics_category" ("tenant_id"); (params None)
2024-08-07 18:44:34,084 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ADD CONSTRAINT "metrics_dashboard_tenant_id_50099a7d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,087 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_tenant_id_50099a7d" ON "metrics_dashboard" ("tenant_id"); (params None)
2024-08-07 18:44:34,090 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_domain" ADD CONSTRAINT "metrics_domain_tenant_id_259fb21f_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,093 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_domain_bdc97b86_like" ON "metrics_domain" ("domain" varchar_pattern_ops); (params None)
2024-08-07 18:44:34,097 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_is_primary_ac9d2eaf" ON "metrics_domain" ("is_primary"); (params None)
2024-08-07 18:44:34,101 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_tenant_id_259fb21f" ON "metrics_domain" ("tenant_id"); (params None)
2024-08-07 18:44:34,105 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_category_id_8793f683_fk_metrics_category_id" FOREIGN KEY ("category_id") REFERENCES "metrics_category" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,107 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_9606b577_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,108 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_category_id_8793f683" ON "metrics_metric" ("category_id"); (params None)
2024-08-07 18:44:34,143 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tenant_id_9606b577" ON "metrics_metric" ("tenant_id"); (params None)
2024-08-07 18:44:34,146 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_tenant_id_438c5ad4_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,148 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_metric_id_3f9e8174_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,150 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_tenant_id_438c5ad4" ON "metrics_historicaldata" ("tenant_id"); (params None)
2024-08-07 18:44:34,156 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_metric_id_3f9e8174" ON "metrics_historicaldata" ("metric_id"); (params None)
2024-08-07 18:44:34,159 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_tenant_id_92d37185_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,161 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_metric_id_e05f23a8_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,163 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_tenant_id_92d37185" ON "metrics_forecast" ("tenant_id"); (params None)
2024-08-07 18:44:34,167 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_metric_id_e05f23a8" ON "metrics_forecast" ("metric_id"); (params None)
2024-08-07 18:44:34,170 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD CONSTRAINT "metrics_experiment_tenant_id_10fa364a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,172 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_tenant_id_10fa364a" ON "metrics_experiment" ("tenant_id"); (params None)
2024-08-07 18:44:34,175 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_metri_experiment_id_metric_id_a9d54b29_uniq" UNIQUE ("experiment_id", "metric_id"); (params None)
2024-08-07 18:44:34,178 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_experiment_id_372c6b59_fk_metrics_e" FOREIGN KEY ("experiment_id") REFERENCES "metrics_experiment" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,180 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_metric_id_c8f84167_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,181 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_experiment_id_372c6b59" ON "metrics_experiment_metrics" ("experiment_id"); (params None)
2024-08-07 18:44:34,184 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_metric_id_c8f84167" ON "metrics_experiment_metrics" ("metric_id"); (params None)
2024-08-07 18:44:34,188 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_2e1e5750_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,190 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_from_metric_id_33b50521_fk_metrics_metric_id" FOREIGN KEY ("from_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,192 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_to_metric_id_94489c1c_fk_metrics_metric_id" FOREIGN KEY ("to_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,193 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_tenant_id_2e1e5750" ON "metrics_connection" ("tenant_id"); (params None)
2024-08-07 18:44:34,196 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_from_metric_id_33b50521" ON "metrics_connection" ("from_metric_id"); (params None)
2024-08-07 18:44:34,199 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_to_metric_id_94489c1c" ON "metrics_connection" ("to_metric_id"); (params None)
2024-08-07 18:44:34,203 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_tenant_id_9e474130_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,205 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_metric_id_1b3c3295_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,207 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_tenant_id_9e474130" ON "metrics_anomaly" ("tenant_id"); (params None)
2024-08-07 18:44:34,210 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_metric_id_1b3c3295" ON "metrics_anomaly" ("metric_id"); (params None)
2024-08-07 18:44:34,213 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_tenant_id_86ffa3a9_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,214 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_metric_id_c1b270f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,215 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_tenant_id_86ffa3a9" ON "metrics_actionremark" ("tenant_id"); (params None)
2024-08-07 18:44:34,219 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_metric_id_c1b270f2" ON "metrics_actionremark" ("metric_id"); (params None)
2024-08-07 18:44:34,224 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_project" ADD CONSTRAINT "metrics_project_tenant_id_db4a1170_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,226 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_tenant_id_db4a1170" ON "metrics_project" ("tenant_id"); (params None)
2024-08-07 18:44:34,229 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD CONSTRAINT "metrics_report_tenant_id_d1cf4812_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,231 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_tenant_id_d1cf4812" ON "metrics_report" ("tenant_id"); (params None)
2024-08-07 18:44:34,235 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_name_project_id_2d57d4da_uniq" UNIQUE ("name", "project_id"); (params None)
2024-08-07 18:44:34,238 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_project_id_b7ac5c8e_fk_metrics_project_id" FOREIGN KEY ("project_id") REFERENCES "metrics_project" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,240 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_tenant_id_c286653b_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,241 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_project_id_b7ac5c8e" ON "metrics_tag" ("project_id"); (params None)
2024-08-07 18:44:34,245 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_tenant_id_c286653b" ON "metrics_tag" ("tenant_id"); (params None)
2024-08-07 18:44:34,248 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_tag_id_a8e1a165_uniq" UNIQUE ("metric_id", "tag_id"); (params None)
2024-08-07 18:44:34,252 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_b2a068f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,253 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_tag_id_61869f56_fk_metrics_tag_id" FOREIGN KEY ("tag_id") REFERENCES "metrics_tag" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,254 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_metric_id_b2a068f2" ON "metrics_metric_tags" ("metric_id"); (params None)
2024-08-07 18:44:34,257 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_tag_id_61869f56" ON "metrics_metric_tags" ("tag_id"); (params None)
2024-08-07 18:44:34,261 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,263 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,264 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_metric_id_181e8748" ON "metrics_target" ("metric_id"); (params None)
2024-08-07 18:44:34,267 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_tenant_id_118eb54a" ON "metrics_target" ("tenant_id"); (params None)
2024-08-07 18:44:34,271 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_metric_id_25179b98_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,274 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_tenant_id_4cb1485d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:34,275 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_metric_id_25179b98" ON "metrics_trend" ("metric_id"); (params None)
2024-08-07 18:44:34,277 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_tenant_id_4cb1485d" ON "metrics_trend" ("tenant_id"); (params None)
2024-08-07 18:44:34,541 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_date_33d1e0bd" ON "metrics_actionremark" ("date"); (params None)
2024-08-07 18:44:34,556 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_detection_date_ee75a187" ON "metrics_anomaly" ("detection_date"); (params None)
2024-08-07 18:44:34,570 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c" ON "metrics_category" ("name"); (params None)
2024-08-07 18:44:34,573 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c_like" ON "metrics_category" ("name" varchar_pattern_ops); (params None)
2024-08-07 18:44:34,590 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d" ON "metrics_client" ("name"); (params None)
2024-08-07 18:44:34,593 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d_like" ON "metrics_client" ("name" varchar_pattern_ops); (params None)
2024-08-07 18:44:34,609 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET DEFAULT '{}'; (params None)
2024-08-07 18:44:34,610 - django.db.backends.schema - DEBUG - UPDATE "metrics_dashboard" SET "layout" = '{}' WHERE "layout" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-07 18:44:34,611 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET NOT NULL; (params None)
2024-08-07 18:44:34,612 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" DROP DEFAULT; (params None)
2024-08-07 18:44:34,625 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e" ON "metrics_dashboard" ("name"); (params None)
2024-08-07 18:44:34,628 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e_like" ON "metrics_dashboard" ("name" varchar_pattern_ops); (params None)
2024-08-07 18:44:34,644 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_end_date_31af6c05" ON "metrics_experiment" ("end_date"); (params None)
2024-08-07 18:44:34,663 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7" ON "metrics_experiment" ("name"); (params None)
2024-08-07 18:44:34,666 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7_like" ON "metrics_experiment" ("name" varchar_pattern_ops); (params None)
2024-08-07 18:44:34,680 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET DEFAULT '{}'; (params None)
2024-08-07 18:44:34,681 - django.db.backends.schema - DEBUG - UPDATE "metrics_experiment" SET "results" = '{}' WHERE "results" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-07 18:44:34,682 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET NOT NULL; (params None)
2024-08-07 18:44:34,682 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" DROP DEFAULT; (params None)
2024-08-07 18:44:34,695 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_start_date_a6deff13" ON "metrics_experiment" ("start_date"); (params None)
2024-08-07 18:44:34,712 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET DEFAULT '{}'; (params None)
2024-08-07 18:44:34,713 - django.db.backends.schema - DEBUG - UPDATE "metrics_forecast" SET "confidence_interval" = '{}' WHERE "confidence_interval" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-07 18:44:34,714 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET NOT NULL; (params None)
2024-08-07 18:44:34,715 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" DROP DEFAULT; (params None)
2024-08-07 18:44:34,729 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_forecast_date_71750ae8" ON "metrics_forecast" ("forecast_date"); (params None)
2024-08-07 18:44:34,744 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_date_f27e0e6a" ON "metrics_historicaldata" ("date"); (params None)
2024-08-07 18:44:34,759 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_last_updated_3e38a760" ON "metrics_metric" ("last_updated"); (params None)
2024-08-07 18:44:34,779 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5" ON "metrics_metric" ("name"); (params None)
2024-08-07 18:44:34,783 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5_like" ON "metrics_metric" ("name" varchar_pattern_ops); (params None)
2024-08-07 18:44:34,797 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e" ON "metrics_metric" ("type"); (params None)
2024-08-07 18:44:34,800 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e_like" ON "metrics_metric" ("type" varchar_pattern_ops); (params None)
2024-08-07 18:44:34,828 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80" ON "metrics_project" ("name"); (params None)
2024-08-07 18:44:34,832 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80_like" ON "metrics_project" ("name" varchar_pattern_ops); (params None)
2024-08-07 18:44:34,850 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET DEFAULT '{}'; (params None)
2024-08-07 18:44:34,850 - django.db.backends.schema - DEBUG - UPDATE "metrics_report" SET "configuration" = '{}' WHERE "configuration" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-07 18:44:34,851 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET NOT NULL; (params None)
2024-08-07 18:44:34,852 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" DROP DEFAULT; (params None)
2024-08-07 18:44:34,864 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34" ON "metrics_report" ("name"); (params None)
2024-08-07 18:44:34,867 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34_like" ON "metrics_report" ("name" varchar_pattern_ops); (params None)
2024-08-07 18:44:34,886 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a" ON "metrics_tag" ("name"); (params None)
2024-08-07 18:44:34,890 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a_like" ON "metrics_tag" ("name" varchar_pattern_ops); (params None)
2024-08-07 18:44:34,907 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_target_date_81507ff5" ON "metrics_target" ("target_date"); (params None)
2024-08-07 18:44:34,924 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_end_date_8444ef38" ON "metrics_trend" ("end_date"); (params None)
2024-08-07 18:44:34,942 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_start_date_7b1a850f" ON "metrics_trend" ("start_date"); (params None)
2024-08-07 18:44:34,959 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_act_metric__be3429_idx" ON "metrics_actionremark" ("metric_id", "date"); (params None)
2024-08-07 18:44:34,974 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ano_metric__84982d_idx" ON "metrics_anomaly" ("metric_id", "detection_date"); (params None)
2024-08-07 18:44:34,988 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_con_from_me_9411ea_idx" ON "metrics_connection" ("from_metric_id", "to_metric_id"); (params None)
2024-08-07 18:44:35,005 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_exp_start_d_04716a_idx" ON "metrics_experiment" ("start_date", "end_date"); (params None)
2024-08-07 18:44:35,021 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_for_metric__4c9ae2_idx" ON "metrics_forecast" ("metric_id", "forecast_date"); (params None)
2024-08-07 18:44:35,039 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_his_metric__a2923a_idx" ON "metrics_historicaldata" ("metric_id", "date"); (params None)
2024-08-07 18:44:35,055 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_name_c9d100_idx" ON "metrics_metric" ("name", "type"); (params None)
2024-08-07 18:44:35,074 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_7984a6_idx" ON "metrics_metric" ("last_updated"); (params None)
2024-08-07 18:44:35,098 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1bdb27_idx" ON "metrics_tag" ("name", "project_id"); (params None)
2024-08-07 18:44:35,120 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tar_metric__234682_idx" ON "metrics_target" ("metric_id", "target_date"); (params None)
2024-08-07 18:44:35,138 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tre_metric__d386bb_idx" ON "metrics_trend" ("metric_id", "start_date", "end_date"); (params None)
2024-08-07 18:44:35,156 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_con_from_me_9411ea_idx"; (params None)
2024-08-07 18:44:35,320 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-07 18:44:35,322 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-07 18:44:35,334 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_from_metric_id_aa131d91_uniq" UNIQUE ("tenant_id", "from_metric_id", "to_metric_id"); (params None)
2024-08-07 18:44:35,337 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_project_id_4c1b22ec" ON "metrics_connection" ("project_id"); (params None)
2024-08-07 18:44:35,357 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; ALTER TABLE "metrics_connection" DROP CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id"; (params None)
2024-08-07 18:44:35,358 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "project_id" CASCADE; (params None)
2024-08-07 18:44:35,372 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-07 18:44:35,374 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-07 18:44:35,387 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-07 18:44:35,391 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_project_id_36bdbe46" ON "metrics_metric" ("project_id"); (params None)
2024-08-07 18:44:35,396 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_correlation" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "lag" integer NOT NULL, "pearson_correlation" double precision NOT NULL, "spearman_correlation" double precision NOT NULL); (params None)
2024-08-07 18:44:35,401 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-07 18:44:35,410 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dataqualityscore" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_entry" varchar(255) NOT NULL, "completeness_score" double precision NOT NULL, "accuracy_score" double precision NOT NULL, "consistency_score" double precision NOT NULL, "timeliness_score" double precision NOT NULL, "overall_score" double precision NOT NULL); (params None)
2024-08-07 18:44:35,414 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_impactanalysis" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "before_value" double precision NOT NULL, "after_value" double precision NOT NULL, "percentage_change" double precision NOT NULL, "confidence" double precision NOT NULL, "artifact_link" varchar(200) NOT NULL); (params None)
2024-08-07 18:44:35,419 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_insight" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "title" varchar(200) NOT NULL, "content" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-07 18:44:35,427 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metricmetadata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_source" varchar(100) NOT NULL, "source_url" varchar(200) NOT NULL, "rhythm" varchar(20) NOT NULL, "last_updated" timestamp with time zone NOT NULL, "technical_description" text NOT NULL, "description" text NOT NULL, "artifacts_url" varchar(200) NOT NULL, "hypothesis" text NOT NULL, "confidence" varchar(20) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL); (params None)
2024-08-07 18:44:35,435 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metrictarget" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "target_kpi" varchar(100) NOT NULL, "target_remarks" text NOT NULL, "target_date" date NULL, "target_value" double precision NULL); (params None)
2024-08-07 18:44:35,442 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_strategy" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "estimated_time" interval NOT NULL, "artifacts_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-07 18:44:35,450 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tacticalsolution" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "artifact_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-07 18:44:35,457 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_team" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-07 18:44:35,464 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_technicalindicator" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "stochastic_value" double precision NOT NULL, "rsi_value" double precision NOT NULL, "percent_change" double precision NOT NULL, "moving_average" double precision NOT NULL); (params None)
2024-08-07 18:44:35,470 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_timedimension" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL UNIQUE, "day" integer NOT NULL, "day_of_week" integer NOT NULL, "day_name" varchar(10) NOT NULL, "week" integer NOT NULL, "month" integer NOT NULL, "month_name" varchar(10) NOT NULL, "quarter" integer NOT NULL, "year" integer NOT NULL, "is_weekend" boolean NOT NULL, "is_holiday" boolean NOT NULL); (params None)
2024-08-07 18:44:35,477 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_userprofile" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY); (params None)
2024-08-07 18:44:35,499 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_metric_id_181e8748_fk_metrics_metric_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id"; (params None)
2024-08-07 18:44:35,500 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "metric_id" CASCADE; (params None)
2024-08-07 18:44:35,519 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id"; (params None)
2024-08-07 18:44:35,520 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-07 18:44:35,532 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_name_c9d100_idx"; (params None)
2024-08-07 18:44:35,543 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_last_up_7984a6_idx"; (params None)
2024-08-07 18:44:35,562 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" RENAME COLUMN "description" TO "summary"; (params None)
2024-08-07 18:44:35,579 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq"; (params None)
2024-08-07 18:44:35,591 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "correlation_coefficient" CASCADE; (params None)
2024-08-07 18:44:35,605 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" DROP COLUMN "results" CASCADE; (params None)
2024-08-07 18:44:35,617 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "anomaly_detected" CASCADE; (params None)
2024-08-07 18:44:35,632 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "forecasted_value" CASCADE; (params None)
2024-08-07 18:44:35,644 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "trend_component" CASCADE; (params None)
2024-08-07 18:44:35,656 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "importance" varchar(20) DEFAULT 'MEDIUM' NOT NULL; (params None)
2024-08-07 18:44:35,657 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "importance" DROP DEFAULT; (params None)
2024-08-07 18:44:35,676 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-07 18:44:35.674866+00:00' NOT NULL; (params None)
2024-08-07 18:44:35,679 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-07 18:44:35,723 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "anomaly_type" varchar(20) DEFAULT 'IGNORE' NOT NULL; (params None)
2024-08-07 18:44:35,725 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "anomaly_type" DROP DEFAULT; (params None)
2024-08-07 18:44:35,744 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "quality" varchar(20) DEFAULT 'LOW' NOT NULL; (params None)
2024-08-07 18:44:35,745 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "quality" DROP DEFAULT; (params None)
2024-08-07 18:44:35,757 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "impact_description" text DEFAULT '' NOT NULL; (params None)
2024-08-07 18:44:35,759 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "impact_description" DROP DEFAULT; (params None)
2024-08-07 18:44:35,773 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "objective" text DEFAULT '' NOT NULL; (params None)
2024-08-07 18:44:35,774 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "objective" DROP DEFAULT; (params None)
2024-08-07 18:44:35,785 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_date" date NULL; (params None)
2024-08-07 18:44:35,796 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_files" varchar(100) NULL; (params None)
2024-08-07 18:44:35,811 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_summary" text DEFAULT '' NOT NULL; (params None)
2024-08-07 18:44:35,812 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "result_summary" DROP DEFAULT; (params None)
2024-08-07 18:44:35,824 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_value" double precision NULL; (params None)
2024-08-07 18:44:35,838 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-07 18:44:35.837667+00:00' NOT NULL; (params None)
2024-08-07 18:44:35,839 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-07 18:44:35,851 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "variance" double precision NULL; (params None)
2024-08-07 18:44:35,866 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD COLUMN "forecast_id" bigint NULL CONSTRAINT "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" REFERENCES "metrics_forecast"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" IMMEDIATE; (params None)
2024-08-07 18:44:35,880 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "impact" TYPE varchar(20) USING "impact"::varchar(20); (params None)
2024-08-07 18:44:35,982 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "status" TYPE varchar(20); (params None)
2024-08-07 18:44:36,126 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric1_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,140 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric2_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,153 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,161 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-07 18:44:36,185 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,205 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-07 18:44:36,360 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" IMMEDIATE; (params None)
2024-08-07 18:44:36,379 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "experiment_id" bigint NOT NULL CONSTRAINT "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" REFERENCES "metrics_experiment"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" IMMEDIATE; (params None)
2024-08-07 18:44:36,402 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,423 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,444 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,471 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,498 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "user_id" bigint NOT NULL CONSTRAINT "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,533 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "data_quality_score_id" bigint NULL UNIQUE CONSTRAINT "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" REFERENCES "metrics_dataqualityscore"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" IMMEDIATE; (params None)
2024-08-07 18:44:36,567 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "metric_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,597 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,621 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,643 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,667 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,692 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" IMMEDIATE; (params None)
2024-08-07 18:44:36,715 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" IMMEDIATE; (params None)
2024-08-07 18:44:36,740 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_team" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,763 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "team_id" bigint NOT NULL CONSTRAINT "metrics_strategy_team_id_f1781500_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_team_id_f1781500_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,787 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,927 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,953 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_experiment_team_id_537107e3_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_experiment_team_id_537107e3_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-07 18:44:36,980 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" IMMEDIATE; (params None)
2024-08-07 18:44:37,015 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" IMMEDIATE; (params None)
2024-08-07 18:44:37,045 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_timedimension" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-07 18:44:37,073 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-07 18:44:37,098 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "user_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-07 18:44:37,102 - django.db.backends.schema - DEBUG - DROP TABLE "metrics_target" CASCADE; (params None)
2024-08-07 18:44:37,125 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "confidence" CASCADE; (params None)
2024-08-07 18:44:37,147 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "description" CASCADE; (params None)
2024-08-07 18:44:37,168 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "hypothesis" CASCADE; (params None)
2024-08-07 18:44:37,197 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "last_updated" CASCADE; (params None)
2024-08-07 18:44:37,223 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_x" CASCADE; (params None)
2024-08-07 18:44:37,245 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_y" CASCADE; (params None)
2024-08-07 18:44:37,266 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "rhythm" CASCADE; (params None)
2024-08-07 18:44:37,287 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "source" CASCADE; (params None)
2024-08-07 18:44:37,307 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "technical_description" CASCADE; (params None)
2024-08-07 18:44:37,327 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD CONSTRAINT "metrics_correlation_tenant_id_metric1_id_met_49a4c34a_uniq" UNIQUE ("tenant_id", "metric1_id", "metric2_id", "lag"); (params None)
2024-08-07 18:44:37,473 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_metric__b85d3a_idx" ON "metrics_insight" ("metric_id", "date"); (params None)
2024-08-07 18:44:37,496 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_user_id_1ebb42_idx" ON "metrics_insight" ("user_id", "date"); (params None)
2024-08-07 18:44:37,520 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_metric__a2b705_idx" ON "metrics_metrictarget" ("metric_id", "target_date"); (params None)
2024-08-07 18:44:37,545 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_6e2e67_idx" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-07 18:44:37,568 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_date_53cb14_idx" ON "metrics_timedimension" ("date"); (params None)
2024-08-07 18:44:37,591 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_year_92da9e_idx" ON "metrics_timedimension" ("year", "month", "day"); (params None)
2024-08-07 18:44:37,594 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_username_6e55f358_like" ON "metrics_customuser" ("username" varchar_pattern_ops); (params None)
2024-08-07 18:44:37,597 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_date_ded95ba1" ON "metrics_insight" ("date"); (params None)
2024-08-07 18:44:37,599 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_last_updated_76599a1b" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-07 18:44:37,601 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_target_date_38cd9191" ON "metrics_metrictarget" ("target_date"); (params None)
2024-08-07 18:44:37,604 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_forecast_id_29590c29" ON "metrics_historicaldata" ("forecast_id"); (params None)
2024-08-07 18:44:37,607 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric1_id_6e1c2404" ON "metrics_correlation" ("metric1_id"); (params None)
2024-08-07 18:44:37,609 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric2_id_f2cc46dd" ON "metrics_correlation" ("metric2_id"); (params None)
2024-08-07 18:44:37,611 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_tenant_id_a00a5169" ON "metrics_correlation" ("tenant_id"); (params None)
2024-08-07 18:44:37,613 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_customuser_id_group_id_1c5fc435_uniq" UNIQUE ("customuser_id", "group_id"); (params None)
2024-08-07 18:44:37,615 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_g_customuser_id_fc13f3af_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:37,616 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_group_id_6b097e12_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:37,617 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_customuser_id_fc13f3af" ON "metrics_customuser_groups" ("customuser_id"); (params None)
2024-08-07 18:44:37,621 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_group_id_6b097e12" ON "metrics_customuser_groups" ("group_id"); (params None)
2024-08-07 18:44:37,623 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_tenant_id_02b7403c" ON "metrics_customuser" ("tenant_id"); (params None)
2024-08-07 18:44:37,625 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_user__customuser_id_permission_68cc320f_uniq" UNIQUE ("customuser_id", "permission_id"); (params None)
2024-08-07 18:44:37,627 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_customuser_id_46e97f00_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:37,628 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_permission_id_d66d657c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:37,629 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_customuser_id_46e97f00" ON "metrics_customuser_user_permissions" ("customuser_id"); (params None)
2024-08-07 18:44:37,632 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_permission_id_d66d657c" ON "metrics_customuser_user_permissions" ("permission_id"); (params None)
2024-08-07 18:44:37,636 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_tenant_id_8e9f296d" ON "metrics_dataqualityscore" ("tenant_id"); (params None)
2024-08-07 18:44:37,638 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_experiment_id_1beae7fe" ON "metrics_impactanalysis" ("experiment_id"); (params None)
2024-08-07 18:44:37,640 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_metric_id_f4b9eeb6" ON "metrics_impactanalysis" ("metric_id"); (params None)
2024-08-07 18:44:37,642 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_tenant_id_126ca20d" ON "metrics_impactanalysis" ("tenant_id"); (params None)
2024-08-07 18:44:37,644 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_metric_id_26d3a9d8" ON "metrics_insight" ("metric_id"); (params None)
2024-08-07 18:44:37,647 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_tenant_id_724d7d85" ON "metrics_insight" ("tenant_id"); (params None)
2024-08-07 18:44:37,650 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_user_id_83d421e1" ON "metrics_insight" ("user_id"); (params None)
2024-08-07 18:44:37,652 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_tenant_id_3277f967" ON "metrics_metricmetadata" ("tenant_id"); (params None)
2024-08-07 18:44:37,654 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_metric_id_7876e2c8" ON "metrics_metrictarget" ("metric_id"); (params None)
2024-08-07 18:44:37,656 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_tenant_id_b26a17f8" ON "metrics_metrictarget" ("tenant_id"); (params None)
2024-08-07 18:44:37,658 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_tenant_id_1323395e" ON "metrics_strategy" ("tenant_id"); (params None)
2024-08-07 18:44:37,661 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_metric_id_9887ffa4" ON "metrics_tacticalsolution" ("metric_id"); (params None)
2024-08-07 18:44:37,664 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_tenant_id_cf9028f0" ON "metrics_tacticalsolution" ("tenant_id"); (params None)
2024-08-07 18:44:37,666 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_team_tenant_id_3a14c47d" ON "metrics_team" ("tenant_id"); (params None)
2024-08-07 18:44:37,668 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_team_id_f1781500" ON "metrics_strategy" ("team_id"); (params None)
2024-08-07 18:44:37,670 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_team_id_f140658d" ON "metrics_metricmetadata" ("team_id"); (params None)
2024-08-07 18:44:37,673 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_team_id_4c4ffc18" ON "metrics_customuser" ("team_id"); (params None)
2024-08-07 18:44:37,676 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_team_id_537107e3" ON "metrics_experiment" ("team_id"); (params None)
2024-08-07 18:44:37,678 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_metric_id_3e2eead6" ON "metrics_technicalindicator" ("metric_id"); (params None)
2024-08-07 18:44:37,680 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_tenant_id_f4de3b44" ON "metrics_technicalindicator" ("tenant_id"); (params None)
2024-08-07 18:44:37,682 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_timedimension_tenant_id_f375bb45" ON "metrics_timedimension" ("tenant_id"); (params None)
2024-08-07 18:44:37,684 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_userprofile_tenant_id_cca71dae" ON "metrics_userprofile" ("tenant_id"); (params None)
2024-08-07 18:44:37,708 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "strength" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-07 18:44:37,709 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "strength" DROP DEFAULT; (params None)
2024-08-07 18:44:37,731 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "lower_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-07 18:44:37,732 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "lower_bound" DROP DEFAULT; (params None)
2024-08-07 18:44:37,753 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "upper_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-07 18:44:37,754 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "upper_bound" DROP DEFAULT; (params None)
2024-08-07 18:44:37,775 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD COLUMN "slope" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-07 18:44:37,776 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ALTER COLUMN "slope" DROP DEFAULT; (params None)
2024-08-07 18:44:37,802 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_movingaverage" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "ma_type" varchar(10) NOT NULL, "period" integer NOT NULL, "value" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-07 18:44:37,833 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_networkanalysisresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "analysis_type" varchar(20) NOT NULL, "result" jsonb NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-07 18:44:37,879 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_seasonalityresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "seasonality_type" varchar(20) NOT NULL, "strength" double precision NOT NULL, "period" integer NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-07 18:44:37,909 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trendchangepoint" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "change_type" varchar(20) NOT NULL, "significance" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-07 18:44:37,914 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD CONSTRAINT "metrics_movingaverage_metric_id_7c61cebf_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:37,915 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_metric_id_7c61cebf" ON "metrics_movingaverage" ("metric_id"); (params None)
2024-08-07 18:44:37,917 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD CONSTRAINT "metrics_networkanaly_metric_id_a4c90102_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:37,919 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_metric_id_a4c90102" ON "metrics_networkanalysisresult" ("metric_id"); (params None)
2024-08-07 18:44:37,921 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityr_metric_id_6e494791_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:37,922 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_metric_id_6e494791" ON "metrics_seasonalityresult" ("metric_id"); (params None)
2024-08-07 18:44:37,925 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD CONSTRAINT "metrics_trendchangep_metric_id_f8eb9f76_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:37,927 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_metric_id_f8eb9f76" ON "metrics_trendchangepoint" ("metric_id"); (params None)
2024-08-07 18:44:37,959 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" IMMEDIATE; (params None)
2024-08-07 18:44:37,961 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-07 18:44:37,990 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" IMMEDIATE; (params None)
2024-08-07 18:44:37,992 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-07 18:44:38,015 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ALTER COLUMN "value" DROP NOT NULL; (params None)
2024-08-07 18:44:38,181 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD CONSTRAINT "metrics_dataqualityscore_tenant_id_metric_id_proj_66b9fb01_uniq" UNIQUE ("tenant_id", "metric_id", "project_id"); (params None)
2024-08-07 18:44:38,183 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_metric_id_1b6367d1" ON "metrics_dataqualityscore" ("metric_id"); (params None)
2024-08-07 18:44:38,185 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_project_id_123a4f58" ON "metrics_dataqualityscore" ("project_id"); (params None)
2024-08-07 18:44:38,211 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-07 18:44:38,243 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-07 18:44:38,244 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-07 18:44:38,272 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" IMMEDIATE; (params None)
2024-08-07 18:44:38,274 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-07 18:44:38,304 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; (params None)
2024-08-07 18:44:38,306 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-07 18:44:38,334 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; (params None)
2024-08-07 18:44:38,336 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-07 18:44:38,361 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq" UNIQUE ("tenant_id", "metric_id"); (params None)
2024-08-07 18:44:38,364 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_tenant_id_5a9de228" ON "metrics_movingaverage" ("tenant_id"); (params None)
2024-08-07 18:44:38,367 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_tenant_id_16a6ba09" ON "metrics_networkanalysisresult" ("tenant_id"); (params None)
2024-08-07 18:44:38,370 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_tenant_id_ca2da3fd" ON "metrics_seasonalityresult" ("tenant_id"); (params None)
2024-08-07 18:44:38,372 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_tenant_id_da10d898" ON "metrics_trendchangepoint" ("tenant_id"); (params None)
2024-08-07 18:44:38,403 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-07 18:44:38,404 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-07 18:44:38,405 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_metric_id_c86f5720" ON "metrics_report" ("metric_id"); (params None)
2024-08-07 18:44:38,431 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "analysis_result" jsonb NULL; (params None)
2024-08-07 18:44:38,456 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "anomaly_result" jsonb NULL; (params None)
2024-08-07 18:44:38,479 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-07T18:44:38.479462+00:00'::timestamptz NOT NULL; (params None)
2024-08-07 18:44:38,480 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-07 18:44:38,503 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "forecast_result" jsonb NULL; (params None)
2024-08-07 18:44:38,525 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "relationship_result" jsonb NULL; (params None)
2024-08-07 18:44:38,549 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "report" text DEFAULT '1' NOT NULL; (params None)
2024-08-07 18:44:38,550 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "report" DROP DEFAULT; (params None)
2024-08-07 18:44:38,574 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "updated_at" timestamp with time zone DEFAULT '2024-08-07T18:44:38.574165+00:00'::timestamptz NOT NULL; (params None)
2024-08-07 18:44:38,575 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "updated_at" DROP DEFAULT; (params None)
2024-08-07 18:44:38,773 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_trendchangepoint" DROP CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c"; (params None)
2024-08-07 18:44:38,774 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-07 18:44:38,795 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "significance" DROP NOT NULL; (params None)
2024-08-07 18:44:38,818 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" RENAME COLUMN "change_type" TO "direction"; (params None)
2024-08-07 18:44:38,865 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-07T18:44:38.864747+00:00'::timestamptz NOT NULL; (params None)
2024-08-07 18:44:38,866 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-07 18:44:38,893 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq"; (params None)
2024-08-07 18:44:38,894 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresul_metric_id_seasonality_ty_d3492b78_uniq" UNIQUE ("metric_id", "seasonality_type"); (params None)
2024-08-07 18:44:38,928 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c"; (params None)
2024-08-07 18:44:38,929 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-07 18:44:38,958 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_computationstatus" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "status" varchar(20) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL, "error_message" text NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-07 18:44:38,991 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_notification" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "message" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "is_read" boolean NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-07 18:44:39,026 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_pendingcomputation" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "created_at" timestamp with time zone NOT NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-07 18:44:39,030 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_computationstatus" ADD CONSTRAINT "metrics_computations_tenant_id_9db248bb_fk_metrics_c" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:39,031 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_computationstatus_tenant_id_9db248bb" ON "metrics_computationstatus" ("tenant_id"); (params None)
2024-08-07 18:44:39,034 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_notification" ADD CONSTRAINT "metrics_notification_tenant_id_c3c627a8_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:39,036 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_notification_tenant_id_c3c627a8" ON "metrics_notification" ("tenant_id"); (params None)
2024-08-07 18:44:39,038 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_pendingcomputation" ADD CONSTRAINT "metrics_pendingcomputation_tenant_id_metric_id_3d717a39_uniq" UNIQUE ("tenant_id", "metric_id"); (params None)
2024-08-07 18:44:39,040 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_pendingcomputation" ADD CONSTRAINT "metrics_pendingcompu_metric_id_ac49fde0_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:39,042 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_pendingcomputation" ADD CONSTRAINT "metrics_pendingcompu_tenant_id_43cda605_fk_metrics_c" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-07 18:44:39,042 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_pendingcomputation_metric_id_ac49fde0" ON "metrics_pendingcomputation" ("metric_id"); (params None)
2024-08-07 18:44:39,045 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_pendingcomputation_tenant_id_43cda605" ON "metrics_pendingcomputation" ("tenant_id"); (params None)
2024-08-07 18:44:39,081 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; (params None)
2024-08-07 18:44:39,082 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-07 18:44:39,083 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_tenant_id_ca2da3fd" ON "metrics_seasonalityresult" ("tenant_id"); (params None)
2024-08-07 18:44:39,089 - django.db.backends.schema - DEBUG - CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" timestamp with time zone NOT NULL); (params None)
2024-08-07 18:44:39,093 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" ("session_key" varchar_pattern_ops); (params None)
2024-08-07 18:44:39,096 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date"); (params None)
```

## test_anomaly_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.002 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,213 - metrics - DEBUG - Starting test: test_anomaly_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_bulk_create_metrics (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,216 - metrics - DEBUG - Starting test: test_bulk_create_metrics (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_category_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.002 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,218 - metrics - DEBUG - Starting test: test_category_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_computation_status_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,222 - metrics - DEBUG - Starting test: test_computation_status_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_connection_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,225 - metrics - DEBUG - Starting test: test_connection_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_correlation_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,228 - metrics - DEBUG - Starting test: test_correlation_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_custom_method_to_representation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,230 - metrics - DEBUG - Starting test: test_custom_method_to_representation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_custom_user_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.002 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,234 - metrics - DEBUG - Starting test: test_custom_user_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_dashboard_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,238 - metrics - DEBUG - Starting test: test_dashboard_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_data_quality_score_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,241 - metrics - DEBUG - Starting test: test_data_quality_score_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_date_time_field_handling (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,243 - metrics - DEBUG - Starting test: test_date_time_field_handling (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_domain_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.002 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,247 - metrics - DEBUG - Starting test: test_domain_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_deserialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,250 - metrics - DEBUG - Starting test: test_experiment_deserialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_edge_cases (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,253 - metrics - DEBUG - Starting test: test_experiment_edge_cases (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_metric_relationship (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,256 - metrics - DEBUG - Starting test: test_experiment_metric_relationship (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_nested_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.003 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,260 - metrics - DEBUG - Starting test: test_experiment_nested_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_read_only_fields (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,264 - metrics - DEBUG - Starting test: test_experiment_read_only_fields (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,266 - metrics - DEBUG - Starting test: test_experiment_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_experiment_validation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.002 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,269 - metrics - DEBUG - Starting test: test_experiment_validation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_forecast_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.002 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,273 - metrics - DEBUG - Starting test: test_forecast_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_historical_data_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,277 - metrics - DEBUG - Starting test: test_historical_data_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_impact_analysis_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,280 - metrics - DEBUG - Starting test: test_impact_analysis_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_insight_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,282 - metrics - DEBUG - Starting test: test_insight_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_many_to_many_relationship (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,285 - metrics - DEBUG - Starting test: test_many_to_many_relationship (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_deserialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,289 - metrics - DEBUG - Starting test: test_metric_deserialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_edge_cases (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,291 - metrics - DEBUG - Starting test: test_metric_edge_cases (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_error_handling (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,294 - metrics - DEBUG - Starting test: test_metric_error_handling (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_metadata_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,296 - metrics - DEBUG - Starting test: test_metric_metadata_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.002 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,299 - metrics - DEBUG - Starting test: test_metric_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_target_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,303 - metrics - DEBUG - Starting test: test_metric_target_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_metric_validation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,306 - metrics - DEBUG - Starting test: test_metric_validation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_moving_average_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,309 - metrics - DEBUG - Starting test: test_moving_average_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_network_analysis_result_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,311 - metrics - DEBUG - Starting test: test_network_analysis_result_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_notification_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,315 - metrics - DEBUG - Starting test: test_notification_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_pending_computation_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,318 - metrics - DEBUG - Starting test: test_pending_computation_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_project_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,321 - metrics - DEBUG - Starting test: test_project_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_report_complex_field_deserialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,323 - metrics - DEBUG - Starting test: test_report_complex_field_deserialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_report_complex_field_serialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,326 - metrics - DEBUG - Starting test: test_report_complex_field_serialization (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_report_complex_field_validation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,329 - metrics - DEBUG - Starting test: test_report_complex_field_validation (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_report_edge_cases (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,333 - metrics - DEBUG - Starting test: test_report_edge_cases (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_report_metric_relationship (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,336 - metrics - DEBUG - Starting test: test_report_metric_relationship (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_report_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.002 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,340 - metrics - DEBUG - Starting test: test_report_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_seasonality_result_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,343 - metrics - DEBUG - Starting test: test_seasonality_result_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_strategy_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,346 - metrics - DEBUG - Starting test: test_strategy_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_tactical_solution_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,348 - metrics - DEBUG - Starting test: test_tactical_solution_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_tag_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.002 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,351 - metrics - DEBUG - Starting test: test_tag_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_team_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,356 - metrics - DEBUG - Starting test: test_team_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_technical_indicator_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,359 - metrics - DEBUG - Starting test: test_technical_indicator_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_time_dimension_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,362 - metrics - DEBUG - Starting test: test_time_dimension_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_trend_change_point_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.003 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,365 - metrics - DEBUG - Starting test: test_trend_change_point_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_trend_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,370 - metrics - DEBUG - Starting test: test_trend_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_user_profile_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,373 - metrics - DEBUG - Starting test: test_user_profile_serializer (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

## test_write_only_field (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
Status: error
Duration: 0.001 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_serializers.py", line 32, in setUp
    self.tenant = Client.objects.create(
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django/db/models/query.py", line 679, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/django_tenants/models.py", line 100, in save
    raise Exception("Can't create tenant outside the public schema. "
Exception: Can't create tenant outside the public schema. Current schema is test_tenant.
```

### Output
```
2024-08-07 18:44:39,375 - metrics - DEBUG - Starting test: test_write_only_field (metrics.tests.test_permanent_computations.test_serializers.SerializerTestCase)
```

