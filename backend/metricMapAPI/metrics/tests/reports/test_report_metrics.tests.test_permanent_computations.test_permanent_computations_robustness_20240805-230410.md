# Test Run: metrics.tests.test_permanent_computations.test_permanent_computations_robustness

Total tests: 7
Passed: 2
Failed: 2
Errors: 3

## test_computation_with_extreme_values (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
Status: error
Duration: 24.628 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_permanent_computations_robustness.py", line 137, in test_computation_with_extreme_values
    data_prep = DataPreparation(self.metric1, self.tenant, self.project)
TypeError: DataPreparation.__init__() takes 2 positional arguments but 4 were given
```

### Output
```
Starting setUp
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
  Applying sessions.0001_initial...
 OK
Initializing PermanentComputations with metric_ids: [5, 6]
Finished initializing PermanentComputations
Initializing DataPreparation for metric_id: 5
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 5
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 5
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 5
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
2024-08-05 23:00:43,377 - metrics - DEBUG - Starting test: test_computation_with_extreme_values (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
2024-08-05 23:00:43,386 - django.db.backends.schema - DEBUG - CREATE TABLE "django_migrations" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:00:43,406 - django.db.backends.schema - DEBUG - CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
2024-08-05 23:00:43,413 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params None)
2024-08-05 23:00:43,421 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL, "codename" varchar(100) NOT NULL); (params None)
2024-08-05 23:00:43,431 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(80) NOT NULL UNIQUE); (params None)
2024-08-05 23:00:43,440 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:00:43,453 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NOT NULL, "is_superuser" boolean NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:00:43,462 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:00:43,468 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:00:43,474 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename"); (params None)
2024-08-05 23:00:43,479 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:43,481 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id"); (params None)
2024-08-05 23:00:43,485 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_name_a6ea08ec_like" ON "auth_group" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:00:43,490 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id"); (params None)
2024-08-05 23:00:43,496 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:43,499 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:43,502 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id"); (params None)
2024-08-05 23:00:43,508 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id"); (params None)
2024-08-05 23:00:43,513 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_username_6821ab7c_like" ON "auth_user" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:00:43,518 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id"); (params None)
2024-08-05 23:00:43,523 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:43,526 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:43,529 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id"); (params None)
2024-08-05 23:00:43,535 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id"); (params None)
2024-08-05 23:00:43,540 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id"); (params None)
2024-08-05 23:00:43,545 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:43,548 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:43,550 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id"); (params None)
2024-08-05 23:00:43,558 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id"); (params None)
2024-08-05 23:00:43,579 - django.db.backends.schema - DEBUG - CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "action_time" timestamp with time zone NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL, "user_id" integer NOT NULL); (params None)
2024-08-05 23:00:43,592 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:43,595 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:43,598 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id"); (params None)
2024-08-05 23:00:43,603 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id"); (params None)
2024-08-05 23:00:43,642 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ALTER COLUMN "name" DROP NOT NULL; (params None)
2024-08-05 23:00:43,654 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" DROP COLUMN "name" CASCADE; (params None)
2024-08-05 23:00:43,676 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ALTER COLUMN "name" TYPE varchar(255); (params None)
2024-08-05 23:00:43,701 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "email" TYPE varchar(254); (params None)
2024-08-05 23:00:43,736 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_login" DROP NOT NULL; (params None)
2024-08-05 23:00:43,759 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "username" TYPE varchar(150); (params None)
2024-08-05 23:00:43,780 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_name" TYPE varchar(150); (params None)
2024-08-05 23:00:43,795 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group" ALTER COLUMN "name" TYPE varchar(150); (params None)
2024-08-05 23:00:43,823 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "first_name" TYPE varchar(150); (params None)
2024-08-05 23:00:43,884 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_client" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "schema_name" varchar(63) NOT NULL UNIQUE, "name" varchar(100) NOT NULL, "created_on" date NOT NULL); (params None)
2024-08-05 23:00:43,895 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_category" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:00:43,906 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dashboard" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "layout" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:00:43,920 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_domain" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "domain" varchar(253) NOT NULL UNIQUE, "is_primary" boolean NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:00:43,938 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "type" varchar(50) NOT NULL, "confidence" varchar(50) NOT NULL, "value_type" varchar(20) NOT NULL, "rhythm" varchar(20) NOT NULL, "description" text NOT NULL, "hypothesis" text NOT NULL, "technical_description" text NOT NULL, "last_updated" timestamp with time zone NOT NULL, "source" varchar(100) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL, "category_id" bigint NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:00:43,957 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_historicaldata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "value" double precision NOT NULL, "forecasted_value" double precision NULL, "anomaly_detected" boolean NOT NULL, "trend_component" varchar(50) NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:00:43,974 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_forecast" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "forecast_date" date NOT NULL, "forecast_value" double precision NOT NULL, "model_used" varchar(100) NOT NULL, "accuracy" double precision NULL, "confidence_interval" jsonb NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:00:43,994 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "status" varchar(50) NOT NULL, "results" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:00:44,002 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment_metrics" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "experiment_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:00:44,016 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_connection" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "relationship" varchar(100) NOT NULL, "correlation_coefficient" double precision NULL, "tenant_id" bigint NOT NULL, "from_metric_id" bigint NOT NULL, "to_metric_id" bigint NOT NULL); (params None)
2024-08-05 23:00:44,036 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_anomaly" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "detection_date" date NOT NULL, "anomaly_value" double precision NOT NULL, "anomaly_score" double precision NOT NULL, "notes" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:00:44,059 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_actionremark" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NULL, "description" text NOT NULL, "impact" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:00:44,091 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_project" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "created_on" date NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:00:44,109 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_report" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "configuration" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:00:44,130 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tag" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "project_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:00:44,147 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric_tags" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "metric_id" bigint NOT NULL, "tag_id" bigint NOT NULL); (params None)
2024-08-05 23:00:44,167 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_target" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "remarks" text NOT NULL, "target_kpi" varchar(100) NOT NULL, "target_date" date NULL, "target_value" double precision NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:00:44,189 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trend" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "trend_type" varchar(50) NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "trend_value" double precision NOT NULL, "notes" text NOT NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:00:44,197 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_schema_name_87d6fbb5_like" ON "metrics_client" ("schema_name" varchar_pattern_ops); (params None)
2024-08-05 23:00:44,201 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_category" ADD CONSTRAINT "metrics_category_tenant_id_67d98cc6_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,203 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_tenant_id_67d98cc6" ON "metrics_category" ("tenant_id"); (params None)
2024-08-05 23:00:44,206 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ADD CONSTRAINT "metrics_dashboard_tenant_id_50099a7d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,208 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_tenant_id_50099a7d" ON "metrics_dashboard" ("tenant_id"); (params None)
2024-08-05 23:00:44,212 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_domain" ADD CONSTRAINT "metrics_domain_tenant_id_259fb21f_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,214 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_domain_bdc97b86_like" ON "metrics_domain" ("domain" varchar_pattern_ops); (params None)
2024-08-05 23:00:44,217 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_is_primary_ac9d2eaf" ON "metrics_domain" ("is_primary"); (params None)
2024-08-05 23:00:44,222 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_tenant_id_259fb21f" ON "metrics_domain" ("tenant_id"); (params None)
2024-08-05 23:00:44,232 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_category_id_8793f683_fk_metrics_category_id" FOREIGN KEY ("category_id") REFERENCES "metrics_category" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,235 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_9606b577_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,236 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_category_id_8793f683" ON "metrics_metric" ("category_id"); (params None)
2024-08-05 23:00:44,240 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tenant_id_9606b577" ON "metrics_metric" ("tenant_id"); (params None)
2024-08-05 23:00:44,243 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_tenant_id_438c5ad4_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,244 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_metric_id_3f9e8174_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,246 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_tenant_id_438c5ad4" ON "metrics_historicaldata" ("tenant_id"); (params None)
2024-08-05 23:00:44,250 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_metric_id_3f9e8174" ON "metrics_historicaldata" ("metric_id"); (params None)
2024-08-05 23:00:44,255 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_tenant_id_92d37185_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,256 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_metric_id_e05f23a8_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,258 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_tenant_id_92d37185" ON "metrics_forecast" ("tenant_id"); (params None)
2024-08-05 23:00:44,262 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_metric_id_e05f23a8" ON "metrics_forecast" ("metric_id"); (params None)
2024-08-05 23:00:44,267 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD CONSTRAINT "metrics_experiment_tenant_id_10fa364a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,268 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_tenant_id_10fa364a" ON "metrics_experiment" ("tenant_id"); (params None)
2024-08-05 23:00:44,275 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_metri_experiment_id_metric_id_a9d54b29_uniq" UNIQUE ("experiment_id", "metric_id"); (params None)
2024-08-05 23:00:44,280 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_experiment_id_372c6b59_fk_metrics_e" FOREIGN KEY ("experiment_id") REFERENCES "metrics_experiment" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,282 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_metric_id_c8f84167_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,283 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_experiment_id_372c6b59" ON "metrics_experiment_metrics" ("experiment_id"); (params None)
2024-08-05 23:00:44,288 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_metric_id_c8f84167" ON "metrics_experiment_metrics" ("metric_id"); (params None)
2024-08-05 23:00:44,292 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_2e1e5750_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,294 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_from_metric_id_33b50521_fk_metrics_metric_id" FOREIGN KEY ("from_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,295 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_to_metric_id_94489c1c_fk_metrics_metric_id" FOREIGN KEY ("to_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,296 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_tenant_id_2e1e5750" ON "metrics_connection" ("tenant_id"); (params None)
2024-08-05 23:00:44,300 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_from_metric_id_33b50521" ON "metrics_connection" ("from_metric_id"); (params None)
2024-08-05 23:00:44,304 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_to_metric_id_94489c1c" ON "metrics_connection" ("to_metric_id"); (params None)
2024-08-05 23:00:44,308 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_tenant_id_9e474130_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,309 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_metric_id_1b3c3295_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,310 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_tenant_id_9e474130" ON "metrics_anomaly" ("tenant_id"); (params None)
2024-08-05 23:00:44,315 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_metric_id_1b3c3295" ON "metrics_anomaly" ("metric_id"); (params None)
2024-08-05 23:00:44,319 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_tenant_id_86ffa3a9_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,320 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_metric_id_c1b270f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,322 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_tenant_id_86ffa3a9" ON "metrics_actionremark" ("tenant_id"); (params None)
2024-08-05 23:00:44,325 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_metric_id_c1b270f2" ON "metrics_actionremark" ("metric_id"); (params None)
2024-08-05 23:00:44,329 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_project" ADD CONSTRAINT "metrics_project_tenant_id_db4a1170_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,331 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_tenant_id_db4a1170" ON "metrics_project" ("tenant_id"); (params None)
2024-08-05 23:00:44,335 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD CONSTRAINT "metrics_report_tenant_id_d1cf4812_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,336 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_tenant_id_d1cf4812" ON "metrics_report" ("tenant_id"); (params None)
2024-08-05 23:00:44,340 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_name_project_id_2d57d4da_uniq" UNIQUE ("name", "project_id"); (params None)
2024-08-05 23:00:44,344 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_project_id_b7ac5c8e_fk_metrics_project_id" FOREIGN KEY ("project_id") REFERENCES "metrics_project" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,346 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_tenant_id_c286653b_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,348 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_project_id_b7ac5c8e" ON "metrics_tag" ("project_id"); (params None)
2024-08-05 23:00:44,351 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_tenant_id_c286653b" ON "metrics_tag" ("tenant_id"); (params None)
2024-08-05 23:00:44,354 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_tag_id_a8e1a165_uniq" UNIQUE ("metric_id", "tag_id"); (params None)
2024-08-05 23:00:44,361 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_b2a068f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,363 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_tag_id_61869f56_fk_metrics_tag_id" FOREIGN KEY ("tag_id") REFERENCES "metrics_tag" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,364 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_metric_id_b2a068f2" ON "metrics_metric_tags" ("metric_id"); (params None)
2024-08-05 23:00:44,368 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_tag_id_61869f56" ON "metrics_metric_tags" ("tag_id"); (params None)
2024-08-05 23:00:44,373 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,375 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,376 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_metric_id_181e8748" ON "metrics_target" ("metric_id"); (params None)
2024-08-05 23:00:44,380 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_tenant_id_118eb54a" ON "metrics_target" ("tenant_id"); (params None)
2024-08-05 23:00:44,384 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_metric_id_25179b98_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,387 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_tenant_id_4cb1485d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:44,388 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_metric_id_25179b98" ON "metrics_trend" ("metric_id"); (params None)
2024-08-05 23:00:44,391 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_tenant_id_4cb1485d" ON "metrics_trend" ("tenant_id"); (params None)
2024-08-05 23:00:44,633 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_date_33d1e0bd" ON "metrics_actionremark" ("date"); (params None)
2024-08-05 23:00:44,925 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_detection_date_ee75a187" ON "metrics_anomaly" ("detection_date"); (params None)
2024-08-05 23:00:44,946 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c" ON "metrics_category" ("name"); (params None)
2024-08-05 23:00:44,950 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c_like" ON "metrics_category" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:00:44,967 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d" ON "metrics_client" ("name"); (params None)
2024-08-05 23:00:44,972 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d_like" ON "metrics_client" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:00:44,993 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET DEFAULT '{}'; (params None)
2024-08-05 23:00:44,995 - django.db.backends.schema - DEBUG - UPDATE "metrics_dashboard" SET "layout" = '{}' WHERE "layout" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:00:44,996 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET NOT NULL; (params None)
2024-08-05 23:00:44,997 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" DROP DEFAULT; (params None)
2024-08-05 23:00:45,013 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e" ON "metrics_dashboard" ("name"); (params None)
2024-08-05 23:00:45,017 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e_like" ON "metrics_dashboard" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:00:45,037 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_end_date_31af6c05" ON "metrics_experiment" ("end_date"); (params None)
2024-08-05 23:00:45,057 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7" ON "metrics_experiment" ("name"); (params None)
2024-08-05 23:00:45,063 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7_like" ON "metrics_experiment" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:00:45,088 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET DEFAULT '{}'; (params None)
2024-08-05 23:00:45,090 - django.db.backends.schema - DEBUG - UPDATE "metrics_experiment" SET "results" = '{}' WHERE "results" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:00:45,091 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET NOT NULL; (params None)
2024-08-05 23:00:45,092 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" DROP DEFAULT; (params None)
2024-08-05 23:00:45,108 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_start_date_a6deff13" ON "metrics_experiment" ("start_date"); (params None)
2024-08-05 23:00:45,126 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET DEFAULT '{}'; (params None)
2024-08-05 23:00:45,128 - django.db.backends.schema - DEBUG - UPDATE "metrics_forecast" SET "confidence_interval" = '{}' WHERE "confidence_interval" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:00:45,129 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET NOT NULL; (params None)
2024-08-05 23:00:45,130 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" DROP DEFAULT; (params None)
2024-08-05 23:00:45,151 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_forecast_date_71750ae8" ON "metrics_forecast" ("forecast_date"); (params None)
2024-08-05 23:00:45,173 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_date_f27e0e6a" ON "metrics_historicaldata" ("date"); (params None)
2024-08-05 23:00:45,193 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_last_updated_3e38a760" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:00:45,217 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5" ON "metrics_metric" ("name"); (params None)
2024-08-05 23:00:45,224 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5_like" ON "metrics_metric" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:00:45,252 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e" ON "metrics_metric" ("type"); (params None)
2024-08-05 23:00:45,258 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e_like" ON "metrics_metric" ("type" varchar_pattern_ops); (params None)
2024-08-05 23:00:45,297 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80" ON "metrics_project" ("name"); (params None)
2024-08-05 23:00:45,302 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80_like" ON "metrics_project" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:00:45,342 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET DEFAULT '{}'; (params None)
2024-08-05 23:00:45,343 - django.db.backends.schema - DEBUG - UPDATE "metrics_report" SET "configuration" = '{}' WHERE "configuration" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:00:45,344 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET NOT NULL; (params None)
2024-08-05 23:00:45,345 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" DROP DEFAULT; (params None)
2024-08-05 23:00:45,363 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34" ON "metrics_report" ("name"); (params None)
2024-08-05 23:00:45,368 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34_like" ON "metrics_report" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:00:45,391 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a" ON "metrics_tag" ("name"); (params None)
2024-08-05 23:00:45,396 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a_like" ON "metrics_tag" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:00:45,414 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_target_date_81507ff5" ON "metrics_target" ("target_date"); (params None)
2024-08-05 23:00:45,440 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_end_date_8444ef38" ON "metrics_trend" ("end_date"); (params None)
2024-08-05 23:00:45,458 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_start_date_7b1a850f" ON "metrics_trend" ("start_date"); (params None)
2024-08-05 23:00:45,478 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_act_metric__be3429_idx" ON "metrics_actionremark" ("metric_id", "date"); (params None)
2024-08-05 23:00:45,504 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ano_metric__84982d_idx" ON "metrics_anomaly" ("metric_id", "detection_date"); (params None)
2024-08-05 23:00:45,524 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_con_from_me_9411ea_idx" ON "metrics_connection" ("from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:00:45,545 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_exp_start_d_04716a_idx" ON "metrics_experiment" ("start_date", "end_date"); (params None)
2024-08-05 23:00:45,564 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_for_metric__4c9ae2_idx" ON "metrics_forecast" ("metric_id", "forecast_date"); (params None)
2024-08-05 23:00:45,588 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_his_metric__a2923a_idx" ON "metrics_historicaldata" ("metric_id", "date"); (params None)
2024-08-05 23:00:45,612 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_name_c9d100_idx" ON "metrics_metric" ("name", "type"); (params None)
2024-08-05 23:00:45,630 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_7984a6_idx" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:00:45,653 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1bdb27_idx" ON "metrics_tag" ("name", "project_id"); (params None)
2024-08-05 23:00:45,674 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tar_metric__234682_idx" ON "metrics_target" ("metric_id", "target_date"); (params None)
2024-08-05 23:00:45,693 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tre_metric__d386bb_idx" ON "metrics_trend" ("metric_id", "start_date", "end_date"); (params None)
2024-08-05 23:00:45,717 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_con_from_me_9411ea_idx"; (params None)
2024-08-05 23:00:45,738 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:00:45,742 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:00:45,762 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_from_metric_id_aa131d91_uniq" UNIQUE ("tenant_id", "from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:00:45,766 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_project_id_4c1b22ec" ON "metrics_connection" ("project_id"); (params None)
2024-08-05 23:00:45,793 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; ALTER TABLE "metrics_connection" DROP CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id"; (params None)
2024-08-05 23:00:45,795 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "project_id" CASCADE; (params None)
2024-08-05 23:00:45,817 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:00:45,820 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:00:45,837 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:00:45,841 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_project_id_36bdbe46" ON "metrics_metric" ("project_id"); (params None)
2024-08-05 23:00:45,847 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_correlation" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "lag" integer NOT NULL, "pearson_correlation" double precision NOT NULL, "spearman_correlation" double precision NOT NULL); (params None)
2024-08-05 23:00:45,855 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:00:45,866 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dataqualityscore" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_entry" varchar(255) NOT NULL, "completeness_score" double precision NOT NULL, "accuracy_score" double precision NOT NULL, "consistency_score" double precision NOT NULL, "timeliness_score" double precision NOT NULL, "overall_score" double precision NOT NULL); (params None)
2024-08-05 23:00:45,873 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_impactanalysis" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "before_value" double precision NOT NULL, "after_value" double precision NOT NULL, "percentage_change" double precision NOT NULL, "confidence" double precision NOT NULL, "artifact_link" varchar(200) NOT NULL); (params None)
2024-08-05 23:00:45,880 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_insight" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "title" varchar(200) NOT NULL, "content" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:00:45,891 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metricmetadata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_source" varchar(100) NOT NULL, "source_url" varchar(200) NOT NULL, "rhythm" varchar(20) NOT NULL, "last_updated" timestamp with time zone NOT NULL, "technical_description" text NOT NULL, "description" text NOT NULL, "artifacts_url" varchar(200) NOT NULL, "hypothesis" text NOT NULL, "confidence" varchar(20) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL); (params None)
2024-08-05 23:00:45,900 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metrictarget" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "target_kpi" varchar(100) NOT NULL, "target_remarks" text NOT NULL, "target_date" date NULL, "target_value" double precision NULL); (params None)
2024-08-05 23:00:45,910 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_strategy" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "estimated_time" interval NOT NULL, "artifacts_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:00:45,920 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tacticalsolution" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "artifact_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:00:45,929 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_team" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:00:45,938 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_technicalindicator" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "stochastic_value" double precision NOT NULL, "rsi_value" double precision NOT NULL, "percent_change" double precision NOT NULL, "moving_average" double precision NOT NULL); (params None)
2024-08-05 23:00:45,945 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_timedimension" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL UNIQUE, "day" integer NOT NULL, "day_of_week" integer NOT NULL, "day_name" varchar(10) NOT NULL, "week" integer NOT NULL, "month" integer NOT NULL, "month_name" varchar(10) NOT NULL, "quarter" integer NOT NULL, "year" integer NOT NULL, "is_weekend" boolean NOT NULL, "is_holiday" boolean NOT NULL); (params None)
2024-08-05 23:00:45,954 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_userprofile" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY); (params None)
2024-08-05 23:00:45,979 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_metric_id_181e8748_fk_metrics_metric_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id"; (params None)
2024-08-05 23:00:45,981 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "metric_id" CASCADE; (params None)
2024-08-05 23:00:46,005 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id"; (params None)
2024-08-05 23:00:46,006 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:00:46,024 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_name_c9d100_idx"; (params None)
2024-08-05 23:00:46,040 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_last_up_7984a6_idx"; (params None)
2024-08-05 23:00:46,058 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" RENAME COLUMN "description" TO "summary"; (params None)
2024-08-05 23:00:46,082 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq"; (params None)
2024-08-05 23:00:46,097 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "correlation_coefficient" CASCADE; (params None)
2024-08-05 23:00:46,113 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" DROP COLUMN "results" CASCADE; (params None)
2024-08-05 23:00:46,134 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "anomaly_detected" CASCADE; (params None)
2024-08-05 23:00:46,149 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "forecasted_value" CASCADE; (params None)
2024-08-05 23:00:46,164 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "trend_component" CASCADE; (params None)
2024-08-05 23:00:46,180 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "importance" varchar(20) DEFAULT 'MEDIUM' NOT NULL; (params None)
2024-08-05 23:00:46,182 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "importance" DROP DEFAULT; (params None)
2024-08-05 23:00:46,202 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:00:46.202052+00:00' NOT NULL; (params None)
2024-08-05 23:00:46,204 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:00:46,219 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "anomaly_type" varchar(20) DEFAULT 'IGNORE' NOT NULL; (params None)
2024-08-05 23:00:46,221 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "anomaly_type" DROP DEFAULT; (params None)
2024-08-05 23:00:46,237 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "quality" varchar(20) DEFAULT 'LOW' NOT NULL; (params None)
2024-08-05 23:00:46,238 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "quality" DROP DEFAULT; (params None)
2024-08-05 23:00:46,255 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "impact_description" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:00:46,256 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "impact_description" DROP DEFAULT; (params None)
2024-08-05 23:00:46,275 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "objective" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:00:46,276 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "objective" DROP DEFAULT; (params None)
2024-08-05 23:00:46,292 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_date" date NULL; (params None)
2024-08-05 23:00:46,309 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_files" varchar(100) NULL; (params None)
2024-08-05 23:00:46,329 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_summary" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:00:46,331 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "result_summary" DROP DEFAULT; (params None)
2024-08-05 23:00:46,346 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_value" double precision NULL; (params None)
2024-08-05 23:00:46,363 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:00:46.362882+00:00' NOT NULL; (params None)
2024-08-05 23:00:46,364 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:00:46,380 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "variance" double precision NULL; (params None)
2024-08-05 23:00:46,404 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD COLUMN "forecast_id" bigint NULL CONSTRAINT "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" REFERENCES "metrics_forecast"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" IMMEDIATE; (params None)
2024-08-05 23:00:46,424 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "impact" TYPE varchar(20) USING "impact"::varchar(20); (params None)
2024-08-05 23:00:46,902 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "status" TYPE varchar(20); (params None)
2024-08-05 23:00:47,130 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric1_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,150 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric2_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,171 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,184 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:00:47,223 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,252 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:00:47,290 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:00:47,321 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "experiment_id" bigint NOT NULL CONSTRAINT "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" REFERENCES "metrics_experiment"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" IMMEDIATE; (params None)
2024-08-05 23:00:47,352 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,389 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,420 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,462 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,486 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "user_id" bigint NOT NULL CONSTRAINT "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,515 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "data_quality_score_id" bigint NULL UNIQUE CONSTRAINT "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" REFERENCES "metrics_dataqualityscore"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" IMMEDIATE; (params None)
2024-08-05 23:00:47,550 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "metric_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,578 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,607 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,637 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,666 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:00:47,998 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:00:48,034 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:00:48,071 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_team" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:00:48,108 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "team_id" bigint NOT NULL CONSTRAINT "metrics_strategy_team_id_f1781500_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_team_id_f1781500_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:00:48,139 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:00:48,167 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:00:48,203 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_experiment_team_id_537107e3_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_experiment_team_id_537107e3_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:00:48,233 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:00:48,267 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:00:48,305 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_timedimension" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:00:48,347 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:00:48,380 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "user_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:00:48,387 - django.db.backends.schema - DEBUG - DROP TABLE "metrics_target" CASCADE; (params None)
2024-08-05 23:00:48,413 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "confidence" CASCADE; (params None)
2024-08-05 23:00:48,439 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "description" CASCADE; (params None)
2024-08-05 23:00:48,466 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "hypothesis" CASCADE; (params None)
2024-08-05 23:00:48,499 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "last_updated" CASCADE; (params None)
2024-08-05 23:00:48,528 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_x" CASCADE; (params None)
2024-08-05 23:00:48,555 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_y" CASCADE; (params None)
2024-08-05 23:00:48,893 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "rhythm" CASCADE; (params None)
2024-08-05 23:00:48,919 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "source" CASCADE; (params None)
2024-08-05 23:00:48,949 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "technical_description" CASCADE; (params None)
2024-08-05 23:00:48,975 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD CONSTRAINT "metrics_correlation_tenant_id_metric1_id_met_49a4c34a_uniq" UNIQUE ("tenant_id", "metric1_id", "metric2_id", "lag"); (params None)
2024-08-05 23:00:49,005 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_metric__b85d3a_idx" ON "metrics_insight" ("metric_id", "date"); (params None)
2024-08-05 23:00:49,034 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_user_id_1ebb42_idx" ON "metrics_insight" ("user_id", "date"); (params None)
2024-08-05 23:00:49,060 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_metric__a2b705_idx" ON "metrics_metrictarget" ("metric_id", "target_date"); (params None)
2024-08-05 23:00:49,093 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_6e2e67_idx" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:00:49,120 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_date_53cb14_idx" ON "metrics_timedimension" ("date"); (params None)
2024-08-05 23:00:49,150 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_year_92da9e_idx" ON "metrics_timedimension" ("year", "month", "day"); (params None)
2024-08-05 23:00:49,154 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_username_6e55f358_like" ON "metrics_customuser" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:00:49,157 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_date_ded95ba1" ON "metrics_insight" ("date"); (params None)
2024-08-05 23:00:49,161 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_last_updated_76599a1b" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:00:49,165 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_target_date_38cd9191" ON "metrics_metrictarget" ("target_date"); (params None)
2024-08-05 23:00:49,168 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_forecast_id_29590c29" ON "metrics_historicaldata" ("forecast_id"); (params None)
2024-08-05 23:00:49,171 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric1_id_6e1c2404" ON "metrics_correlation" ("metric1_id"); (params None)
2024-08-05 23:00:49,176 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric2_id_f2cc46dd" ON "metrics_correlation" ("metric2_id"); (params None)
2024-08-05 23:00:49,179 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_tenant_id_a00a5169" ON "metrics_correlation" ("tenant_id"); (params None)
2024-08-05 23:00:49,182 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_customuser_id_group_id_1c5fc435_uniq" UNIQUE ("customuser_id", "group_id"); (params None)
2024-08-05 23:00:49,187 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_g_customuser_id_fc13f3af_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:49,189 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_group_id_6b097e12_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:49,191 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_customuser_id_fc13f3af" ON "metrics_customuser_groups" ("customuser_id"); (params None)
2024-08-05 23:00:49,195 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_group_id_6b097e12" ON "metrics_customuser_groups" ("group_id"); (params None)
2024-08-05 23:00:49,199 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_tenant_id_02b7403c" ON "metrics_customuser" ("tenant_id"); (params None)
2024-08-05 23:00:49,205 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_user__customuser_id_permission_68cc320f_uniq" UNIQUE ("customuser_id", "permission_id"); (params None)
2024-08-05 23:00:49,211 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_customuser_id_46e97f00_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:49,214 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_permission_id_d66d657c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:49,216 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_customuser_id_46e97f00" ON "metrics_customuser_user_permissions" ("customuser_id"); (params None)
2024-08-05 23:00:49,229 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_permission_id_d66d657c" ON "metrics_customuser_user_permissions" ("permission_id"); (params None)
2024-08-05 23:00:49,235 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_tenant_id_8e9f296d" ON "metrics_dataqualityscore" ("tenant_id"); (params None)
2024-08-05 23:00:49,242 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_experiment_id_1beae7fe" ON "metrics_impactanalysis" ("experiment_id"); (params None)
2024-08-05 23:00:49,247 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_metric_id_f4b9eeb6" ON "metrics_impactanalysis" ("metric_id"); (params None)
2024-08-05 23:00:49,255 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_tenant_id_126ca20d" ON "metrics_impactanalysis" ("tenant_id"); (params None)
2024-08-05 23:00:49,261 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_metric_id_26d3a9d8" ON "metrics_insight" ("metric_id"); (params None)
2024-08-05 23:00:49,266 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_tenant_id_724d7d85" ON "metrics_insight" ("tenant_id"); (params None)
2024-08-05 23:00:49,272 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_user_id_83d421e1" ON "metrics_insight" ("user_id"); (params None)
2024-08-05 23:00:49,276 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_tenant_id_3277f967" ON "metrics_metricmetadata" ("tenant_id"); (params None)
2024-08-05 23:00:49,281 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_metric_id_7876e2c8" ON "metrics_metrictarget" ("metric_id"); (params None)
2024-08-05 23:00:49,286 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_tenant_id_b26a17f8" ON "metrics_metrictarget" ("tenant_id"); (params None)
2024-08-05 23:00:49,290 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_tenant_id_1323395e" ON "metrics_strategy" ("tenant_id"); (params None)
2024-08-05 23:00:49,294 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_metric_id_9887ffa4" ON "metrics_tacticalsolution" ("metric_id"); (params None)
2024-08-05 23:00:49,300 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_tenant_id_cf9028f0" ON "metrics_tacticalsolution" ("tenant_id"); (params None)
2024-08-05 23:00:49,303 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_team_tenant_id_3a14c47d" ON "metrics_team" ("tenant_id"); (params None)
2024-08-05 23:00:49,308 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_team_id_f1781500" ON "metrics_strategy" ("team_id"); (params None)
2024-08-05 23:00:49,312 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_team_id_f140658d" ON "metrics_metricmetadata" ("team_id"); (params None)
2024-08-05 23:00:49,317 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_team_id_4c4ffc18" ON "metrics_customuser" ("team_id"); (params None)
2024-08-05 23:00:49,322 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_team_id_537107e3" ON "metrics_experiment" ("team_id"); (params None)
2024-08-05 23:00:49,326 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_metric_id_3e2eead6" ON "metrics_technicalindicator" ("metric_id"); (params None)
2024-08-05 23:00:49,331 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_tenant_id_f4de3b44" ON "metrics_technicalindicator" ("tenant_id"); (params None)
2024-08-05 23:00:49,335 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_timedimension_tenant_id_f375bb45" ON "metrics_timedimension" ("tenant_id"); (params None)
2024-08-05 23:00:49,339 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_userprofile_tenant_id_cca71dae" ON "metrics_userprofile" ("tenant_id"); (params None)
2024-08-05 23:00:49,379 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "strength" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:00:49,381 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "strength" DROP DEFAULT; (params None)
2024-08-05 23:00:49,409 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "lower_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:00:49,410 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "lower_bound" DROP DEFAULT; (params None)
2024-08-05 23:00:49,445 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "upper_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:00:49,447 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "upper_bound" DROP DEFAULT; (params None)
2024-08-05 23:00:49,478 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD COLUMN "slope" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:00:49,480 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ALTER COLUMN "slope" DROP DEFAULT; (params None)
2024-08-05 23:00:49,520 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_movingaverage" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "ma_type" varchar(10) NOT NULL, "period" integer NOT NULL, "value" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:00:49,556 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_networkanalysisresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "analysis_type" varchar(20) NOT NULL, "result" jsonb NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:00:49,599 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_seasonalityresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "seasonality_type" varchar(20) NOT NULL, "strength" double precision NOT NULL, "period" integer NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:00:49,640 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trendchangepoint" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "change_type" varchar(20) NOT NULL, "significance" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:00:49,645 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD CONSTRAINT "metrics_movingaverage_metric_id_7c61cebf_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:49,648 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_metric_id_7c61cebf" ON "metrics_movingaverage" ("metric_id"); (params None)
2024-08-05 23:00:49,652 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD CONSTRAINT "metrics_networkanaly_metric_id_a4c90102_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:49,654 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_metric_id_a4c90102" ON "metrics_networkanalysisresult" ("metric_id"); (params None)
2024-08-05 23:00:49,656 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityr_metric_id_6e494791_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:49,658 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_metric_id_6e494791" ON "metrics_seasonalityresult" ("metric_id"); (params None)
2024-08-05 23:00:49,661 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD CONSTRAINT "metrics_trendchangep_metric_id_f8eb9f76_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:00:49,664 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_metric_id_f8eb9f76" ON "metrics_trendchangepoint" ("metric_id"); (params None)
2024-08-05 23:00:49,703 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:00:49,706 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:00:49,995 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" IMMEDIATE; (params None)
2024-08-05 23:00:49,997 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:00:50,029 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ALTER COLUMN "value" DROP NOT NULL; (params None)
2024-08-05 23:00:50,058 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD CONSTRAINT "metrics_dataqualityscore_tenant_id_metric_id_proj_66b9fb01_uniq" UNIQUE ("tenant_id", "metric_id", "project_id"); (params None)
2024-08-05 23:00:50,062 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_metric_id_1b6367d1" ON "metrics_dataqualityscore" ("metric_id"); (params None)
2024-08-05 23:00:50,066 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_project_id_123a4f58" ON "metrics_dataqualityscore" ("project_id"); (params None)
2024-08-05 23:00:50,101 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:00:50,149 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:00:50,152 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:00:50,192 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:00:50,194 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:00:50,237 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:00:50,239 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:00:50,279 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:00:50,281 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:00:50,314 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq" UNIQUE ("tenant_id", "metric_id"); (params None)
2024-08-05 23:00:50,318 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_tenant_id_5a9de228" ON "metrics_movingaverage" ("tenant_id"); (params None)
2024-08-05 23:00:50,321 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_tenant_id_16a6ba09" ON "metrics_networkanalysisresult" ("tenant_id"); (params None)
2024-08-05 23:00:50,325 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_tenant_id_ca2da3fd" ON "metrics_seasonalityresult" ("tenant_id"); (params None)
2024-08-05 23:00:50,328 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_tenant_id_da10d898" ON "metrics_trendchangepoint" ("tenant_id"); (params None)
2024-08-05 23:00:50,376 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:00:50,379 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:00:50,380 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_metric_id_c86f5720" ON "metrics_report" ("metric_id"); (params None)
2024-08-05 23:00:50,420 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "analysis_result" jsonb NULL; (params None)
2024-08-05 23:00:50,460 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "anomaly_result" jsonb NULL; (params None)
2024-08-05 23:00:50,499 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:00:50.498277+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:00:50,500 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:00:50,532 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "forecast_result" jsonb NULL; (params None)
2024-08-05 23:00:50,568 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "relationship_result" jsonb NULL; (params None)
2024-08-05 23:00:50,603 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "report" text DEFAULT '1' NOT NULL; (params None)
2024-08-05 23:00:50,604 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "report" DROP DEFAULT; (params None)
2024-08-05 23:00:50,631 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "updated_at" timestamp with time zone DEFAULT '2024-08-05T23:00:50.630695+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:00:50,632 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "updated_at" DROP DEFAULT; (params None)
2024-08-05 23:00:50,999 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_trendchangepoint" DROP CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c"; (params None)
2024-08-05 23:00:51,000 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:00:51,034 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "significance" DROP NOT NULL; (params None)
2024-08-05 23:00:51,090 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" RENAME COLUMN "change_type" TO "direction"; (params None)
2024-08-05 23:00:51,197 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:00:51.196575+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:00:51,199 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:00:51,251 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq"; (params None)
2024-08-05 23:00:51,252 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresul_metric_id_seasonality_ty_d3492b78_uniq" UNIQUE ("metric_id", "seasonality_type"); (params None)
2024-08-05 23:00:51,306 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c"; (params None)
2024-08-05 23:00:51,307 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:00:51,312 - django.db.backends.schema - DEBUG - CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:00:51,321 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" ("session_key" varchar_pattern_ops); (params None)
2024-08-05 23:00:51,325 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date"); (params None)
2024-08-05 23:00:52,942 - metrics.computations.data_preparation - INFO - Loaded metric 5 for tenant 3 and project 3
2024-08-05 23:00:52,942 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 5
2024-08-05 23:00:52,945 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:00:52,946 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:00:52,949 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 5
2024-08-05 23:00:52,956 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:00:52,957 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:00:52,961 - metrics.computations.data_preparation - INFO - DataFrame head: 
                value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:00:52,961 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:00:52,964 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                 value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:00:52,965 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:00:52,968 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:00:56,249 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 5
2024-08-05 23:00:56,253 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:00:56,256 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:00:56,257 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:00:56,261 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                 value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:00:56,262 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:00:56,266 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                 value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:00:56,270 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.364286503680747, Timeliness: nan
2024-08-05 23:00:56,270 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.47621678935823
2024-08-05 23:00:56,276 - metrics.computations.data_preparation - INFO - Data quality score: 45.47621678935823
2024-08-05 23:00:56,424 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 5, 'tenant_id': 3, 'project_id': 3, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.47621678935823, 'outliers_handled': True, 'profile': {'mean': 99.99075979798639, 'median': 99.94415548330196, 'std': 9.8466132870873, 'min': 76.74239741101312, 'max': 123.80642886326658, 'skewness': 0.08987880672759126, 'kurtosis': -0.2157523060542612, 'missing_percentage': 0.0}}
2024-08-05 23:00:56,435 - metrics.computations.data_preparation - INFO - Loaded metric 5 for tenant 3 and project 3
2024-08-05 23:00:56,435 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 5
2024-08-05 23:00:56,437 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:00:56,438 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:00:56,440 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 5
2024-08-05 23:00:56,460 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:00:56,468 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:00:56,476 - metrics.computations.data_preparation - INFO - DataFrame head: 
                value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:00:56,477 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:00:56,491 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                 value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:00:56,492 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:00:56,497 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:01:00,770 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 5
2024-08-05 23:01:00,774 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:01:00,777 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:01:00,777 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:01:00,782 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                 value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:01:00,782 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:01:00,785 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                 value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:01:00,789 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.364286503680747, Timeliness: nan
2024-08-05 23:01:00,789 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.47621678935823
2024-08-05 23:01:00,794 - metrics.computations.data_preparation - INFO - Data quality score: 45.47621678935823
2024-08-05 23:01:00,916 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 5, 'tenant_id': 3, 'project_id': 3, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.47621678935823, 'outliers_handled': True, 'profile': {'mean': 99.99075979798639, 'median': 99.94415548330196, 'std': 9.8466132870873, 'min': 76.74239741101312, 'max': 123.80642886326658, 'skewness': 0.08987880672759126, 'kurtosis': -0.2157523060542612, 'missing_percentage': 0.0}}
2024-08-05 23:01:00,917 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:01:00,917 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 5
2024-08-05 23:01:00,940 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=weekly, period=7, strength=0.01
2024-08-05 23:01:00,948 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=weekly, period=7, strength=0.01
2024-08-05 23:01:00,959 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 5
2024-08-05 23:01:00,959 - metrics.computations.feature_engineering - INFO - Parameters for metric 5: dynamic
2024-08-05 23:01:00,959 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 5: {'seasonality_period': 7, 'forecast_horizon': 7, 'correlation_window': 14, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:01:00,967 - metrics.computations.data_preparation - INFO - Loaded metric 5 for tenant 3 and project 3
2024-08-05 23:01:00,968 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 5
2024-08-05 23:01:00,969 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:00,970 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:00,974 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 5
2024-08-05 23:01:00,985 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:00,986 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:01:00,993 - metrics.computations.data_preparation - INFO - DataFrame head: 
                value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:01:00,993 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:00,998 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                 value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:01:00,999 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:01:01,003 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:01:04,504 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 5
2024-08-05 23:01:04,507 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:01:04,509 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:01:04,510 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:01:04,514 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                 value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:01:04,514 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:01:04,519 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                 value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:01:04,524 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.364286503680747, Timeliness: nan
2024-08-05 23:01:04,524 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.47621678935823
2024-08-05 23:01:04,529 - metrics.computations.data_preparation - INFO - Data quality score: 45.47621678935823
2024-08-05 23:01:04,748 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 5, 'tenant_id': 3, 'project_id': 3, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.47621678935823, 'outliers_handled': True, 'profile': {'mean': 99.99075979798639, 'median': 99.94415548330196, 'std': 9.8466132870873, 'min': 76.74239741101312, 'max': 123.80642886326658, 'skewness': 0.08987880672759126, 'kurtosis': -0.2157523060542612, 'missing_percentage': 0.0}}
2024-08-05 23:01:04,763 - metrics.computations.data_preparation - INFO - Loaded metric 5 for tenant 3 and project 3
2024-08-05 23:01:04,763 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 5
2024-08-05 23:01:04,765 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:04,765 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:04,772 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 5
2024-08-05 23:01:04,790 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:04,791 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:01:04,801 - metrics.computations.data_preparation - INFO - DataFrame head: 
                value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:01:04,801 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:04,807 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                 value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:01:04,808 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:01:04,815 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:01:07,626 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 5
2024-08-05 23:01:07,630 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:01:07,632 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:01:07,633 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:01:07,636 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                 value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:01:07,637 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:01:07,639 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                 value  tenant_id
date                            
2023-01-01  92.361376          3
2023-01-02  93.116282          3
2023-01-03  89.526828          3
2023-01-04  99.680005          3
2023-01-05  93.145132          3
2024-08-05 23:01:07,642 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.364286503680747, Timeliness: nan
2024-08-05 23:01:07,643 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.47621678935823
2024-08-05 23:01:07,648 - metrics.computations.data_preparation - INFO - Data quality score: 45.47621678935823
2024-08-05 23:01:07,796 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 5, 'tenant_id': 3, 'project_id': 3, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.47621678935823, 'outliers_handled': True, 'profile': {'mean': 99.99075979798639, 'median': 99.94415548330196, 'std': 9.8466132870873, 'min': 76.74239741101312, 'max': 123.80642886326658, 'skewness': 0.08987880672759126, 'kurtosis': -0.2157523060542612, 'missing_percentage': 0.0}}
2024-08-05 23:01:07,796 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:01:07,797 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 5
2024-08-05 23:01:07,811 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=weekly, period=7, strength=0.01
2024-08-05 23:01:07,831 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=weekly, period=7, strength=0.01
2024-08-05 23:01:07,841 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 5
2024-08-05 23:01:07,843 - metrics.computations.feature_engineering - INFO - Parameters for metric 5: dynamic
2024-08-05 23:01:07,844 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 5: {'seasonality_period': 7, 'forecast_horizon': 7, 'correlation_window': 14, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:01:07,847 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Setup completed
2024-08-05 23:01:08,002 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Teardown completed
```

## test_computation_with_missing_data (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
Status: error
Duration: 26.158 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_permanent_computations_robustness.py", line 124, in test_computation_with_missing_data
    data_prep = DataPreparation(metric_id=self.metric1.id)
TypeError: DataPreparation.__init__() got an unexpected keyword argument 'metric_id'
```

### Output
```
Starting setUp
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
  Applying sessions.0001_initial...
 OK
Initializing PermanentComputations with metric_ids: [7, 8]
Finished initializing PermanentComputations
Initializing DataPreparation for metric_id: 7
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 7
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 7
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 7
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 7
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/computations_anomalies.py:110: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
  context_z_scores = modified_z_scores.rolling(window=self.context_window, center=True).apply(lambda x: (x[self.context_window//2] - x.mean()) / x.std())
2024-08-05 23:01:08,023 - metrics - DEBUG - Starting test: test_computation_with_missing_data (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
2024-08-05 23:01:08,030 - django.db.backends.schema - DEBUG - CREATE TABLE "django_migrations" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:08,053 - django.db.backends.schema - DEBUG - CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
2024-08-05 23:01:08,059 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params None)
2024-08-05 23:01:08,068 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL, "codename" varchar(100) NOT NULL); (params None)
2024-08-05 23:01:08,076 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(80) NOT NULL UNIQUE); (params None)
2024-08-05 23:01:08,084 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:01:08,096 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NOT NULL, "is_superuser" boolean NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:08,103 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:01:08,109 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:01:08,113 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename"); (params None)
2024-08-05 23:01:08,117 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,119 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id"); (params None)
2024-08-05 23:01:08,122 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_name_a6ea08ec_like" ON "auth_group" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:08,126 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id"); (params None)
2024-08-05 23:01:08,129 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,131 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,133 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id"); (params None)
2024-08-05 23:01:08,136 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id"); (params None)
2024-08-05 23:01:08,139 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_username_6821ab7c_like" ON "auth_user" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:01:08,142 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id"); (params None)
2024-08-05 23:01:08,147 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,149 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,150 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id"); (params None)
2024-08-05 23:01:08,154 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id"); (params None)
2024-08-05 23:01:08,158 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id"); (params None)
2024-08-05 23:01:08,162 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,163 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,165 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id"); (params None)
2024-08-05 23:01:08,168 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id"); (params None)
2024-08-05 23:01:08,183 - django.db.backends.schema - DEBUG - CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "action_time" timestamp with time zone NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL, "user_id" integer NOT NULL); (params None)
2024-08-05 23:01:08,190 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,192 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,193 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id"); (params None)
2024-08-05 23:01:08,197 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id"); (params None)
2024-08-05 23:01:08,222 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ALTER COLUMN "name" DROP NOT NULL; (params None)
2024-08-05 23:01:08,237 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" DROP COLUMN "name" CASCADE; (params None)
2024-08-05 23:01:08,248 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ALTER COLUMN "name" TYPE varchar(255); (params None)
2024-08-05 23:01:08,259 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "email" TYPE varchar(254); (params None)
2024-08-05 23:01:08,278 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_login" DROP NOT NULL; (params None)
2024-08-05 23:01:08,300 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "username" TYPE varchar(150); (params None)
2024-08-05 23:01:08,321 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_name" TYPE varchar(150); (params None)
2024-08-05 23:01:08,332 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group" ALTER COLUMN "name" TYPE varchar(150); (params None)
2024-08-05 23:01:08,358 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "first_name" TYPE varchar(150); (params None)
2024-08-05 23:01:08,410 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_client" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "schema_name" varchar(63) NOT NULL UNIQUE, "name" varchar(100) NOT NULL, "created_on" date NOT NULL); (params None)
2024-08-05 23:01:08,420 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_category" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,428 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dashboard" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "layout" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,439 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_domain" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "domain" varchar(253) NOT NULL UNIQUE, "is_primary" boolean NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,458 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "type" varchar(50) NOT NULL, "confidence" varchar(50) NOT NULL, "value_type" varchar(20) NOT NULL, "rhythm" varchar(20) NOT NULL, "description" text NOT NULL, "hypothesis" text NOT NULL, "technical_description" text NOT NULL, "last_updated" timestamp with time zone NOT NULL, "source" varchar(100) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL, "category_id" bigint NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,472 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_historicaldata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "value" double precision NOT NULL, "forecasted_value" double precision NULL, "anomaly_detected" boolean NOT NULL, "trend_component" varchar(50) NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,485 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_forecast" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "forecast_date" date NOT NULL, "forecast_value" double precision NOT NULL, "model_used" varchar(100) NOT NULL, "accuracy" double precision NULL, "confidence_interval" jsonb NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,503 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "status" varchar(50) NOT NULL, "results" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,512 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment_metrics" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "experiment_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,525 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_connection" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "relationship" varchar(100) NOT NULL, "correlation_coefficient" double precision NULL, "tenant_id" bigint NOT NULL, "from_metric_id" bigint NOT NULL, "to_metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,542 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_anomaly" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "detection_date" date NOT NULL, "anomaly_value" double precision NOT NULL, "anomaly_score" double precision NOT NULL, "notes" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,559 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_actionremark" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NULL, "description" text NOT NULL, "impact" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,584 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_project" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "created_on" date NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,601 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_report" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "configuration" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,620 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tag" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "project_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,636 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric_tags" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "metric_id" bigint NOT NULL, "tag_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,665 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_target" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "remarks" text NOT NULL, "target_kpi" varchar(100) NOT NULL, "target_date" date NULL, "target_value" double precision NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,690 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trend" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "trend_type" varchar(50) NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "trend_value" double precision NOT NULL, "notes" text NOT NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:08,698 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_schema_name_87d6fbb5_like" ON "metrics_client" ("schema_name" varchar_pattern_ops); (params None)
2024-08-05 23:01:08,703 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_category" ADD CONSTRAINT "metrics_category_tenant_id_67d98cc6_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,705 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_tenant_id_67d98cc6" ON "metrics_category" ("tenant_id"); (params None)
2024-08-05 23:01:08,708 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ADD CONSTRAINT "metrics_dashboard_tenant_id_50099a7d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,710 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_tenant_id_50099a7d" ON "metrics_dashboard" ("tenant_id"); (params None)
2024-08-05 23:01:08,714 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_domain" ADD CONSTRAINT "metrics_domain_tenant_id_259fb21f_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,717 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_domain_bdc97b86_like" ON "metrics_domain" ("domain" varchar_pattern_ops); (params None)
2024-08-05 23:01:08,720 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_is_primary_ac9d2eaf" ON "metrics_domain" ("is_primary"); (params None)
2024-08-05 23:01:08,724 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_tenant_id_259fb21f" ON "metrics_domain" ("tenant_id"); (params None)
2024-08-05 23:01:08,727 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_category_id_8793f683_fk_metrics_category_id" FOREIGN KEY ("category_id") REFERENCES "metrics_category" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,729 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_9606b577_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,730 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_category_id_8793f683" ON "metrics_metric" ("category_id"); (params None)
2024-08-05 23:01:08,734 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tenant_id_9606b577" ON "metrics_metric" ("tenant_id"); (params None)
2024-08-05 23:01:08,738 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_tenant_id_438c5ad4_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,740 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_metric_id_3f9e8174_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,742 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_tenant_id_438c5ad4" ON "metrics_historicaldata" ("tenant_id"); (params None)
2024-08-05 23:01:08,746 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_metric_id_3f9e8174" ON "metrics_historicaldata" ("metric_id"); (params None)
2024-08-05 23:01:08,751 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_tenant_id_92d37185_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,753 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_metric_id_e05f23a8_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,755 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_tenant_id_92d37185" ON "metrics_forecast" ("tenant_id"); (params None)
2024-08-05 23:01:08,759 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_metric_id_e05f23a8" ON "metrics_forecast" ("metric_id"); (params None)
2024-08-05 23:01:08,763 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD CONSTRAINT "metrics_experiment_tenant_id_10fa364a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,765 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_tenant_id_10fa364a" ON "metrics_experiment" ("tenant_id"); (params None)
2024-08-05 23:01:08,768 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_metri_experiment_id_metric_id_a9d54b29_uniq" UNIQUE ("experiment_id", "metric_id"); (params None)
2024-08-05 23:01:08,772 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_experiment_id_372c6b59_fk_metrics_e" FOREIGN KEY ("experiment_id") REFERENCES "metrics_experiment" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,774 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_metric_id_c8f84167_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,775 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_experiment_id_372c6b59" ON "metrics_experiment_metrics" ("experiment_id"); (params None)
2024-08-05 23:01:08,778 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_metric_id_c8f84167" ON "metrics_experiment_metrics" ("metric_id"); (params None)
2024-08-05 23:01:08,782 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_2e1e5750_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,784 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_from_metric_id_33b50521_fk_metrics_metric_id" FOREIGN KEY ("from_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,785 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_to_metric_id_94489c1c_fk_metrics_metric_id" FOREIGN KEY ("to_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,787 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_tenant_id_2e1e5750" ON "metrics_connection" ("tenant_id"); (params None)
2024-08-05 23:01:08,790 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_from_metric_id_33b50521" ON "metrics_connection" ("from_metric_id"); (params None)
2024-08-05 23:01:08,793 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_to_metric_id_94489c1c" ON "metrics_connection" ("to_metric_id"); (params None)
2024-08-05 23:01:08,797 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_tenant_id_9e474130_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,799 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_metric_id_1b3c3295_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,800 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_tenant_id_9e474130" ON "metrics_anomaly" ("tenant_id"); (params None)
2024-08-05 23:01:08,804 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_metric_id_1b3c3295" ON "metrics_anomaly" ("metric_id"); (params None)
2024-08-05 23:01:08,807 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_tenant_id_86ffa3a9_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,809 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_metric_id_c1b270f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,811 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_tenant_id_86ffa3a9" ON "metrics_actionremark" ("tenant_id"); (params None)
2024-08-05 23:01:08,816 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_metric_id_c1b270f2" ON "metrics_actionremark" ("metric_id"); (params None)
2024-08-05 23:01:08,820 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_project" ADD CONSTRAINT "metrics_project_tenant_id_db4a1170_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,823 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_tenant_id_db4a1170" ON "metrics_project" ("tenant_id"); (params None)
2024-08-05 23:01:08,827 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD CONSTRAINT "metrics_report_tenant_id_d1cf4812_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,829 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_tenant_id_d1cf4812" ON "metrics_report" ("tenant_id"); (params None)
2024-08-05 23:01:08,833 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_name_project_id_2d57d4da_uniq" UNIQUE ("name", "project_id"); (params None)
2024-08-05 23:01:08,837 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_project_id_b7ac5c8e_fk_metrics_project_id" FOREIGN KEY ("project_id") REFERENCES "metrics_project" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,839 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_tenant_id_c286653b_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,840 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_project_id_b7ac5c8e" ON "metrics_tag" ("project_id"); (params None)
2024-08-05 23:01:08,845 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_tenant_id_c286653b" ON "metrics_tag" ("tenant_id"); (params None)
2024-08-05 23:01:08,848 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_tag_id_a8e1a165_uniq" UNIQUE ("metric_id", "tag_id"); (params None)
2024-08-05 23:01:08,852 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_b2a068f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,854 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_tag_id_61869f56_fk_metrics_tag_id" FOREIGN KEY ("tag_id") REFERENCES "metrics_tag" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,856 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_metric_id_b2a068f2" ON "metrics_metric_tags" ("metric_id"); (params None)
2024-08-05 23:01:08,859 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_tag_id_61869f56" ON "metrics_metric_tags" ("tag_id"); (params None)
2024-08-05 23:01:08,862 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,864 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,866 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_metric_id_181e8748" ON "metrics_target" ("metric_id"); (params None)
2024-08-05 23:01:08,869 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_tenant_id_118eb54a" ON "metrics_target" ("tenant_id"); (params None)
2024-08-05 23:01:08,872 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_metric_id_25179b98_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,874 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_tenant_id_4cb1485d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:08,875 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_metric_id_25179b98" ON "metrics_trend" ("metric_id"); (params None)
2024-08-05 23:01:08,880 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_tenant_id_4cb1485d" ON "metrics_trend" ("tenant_id"); (params None)
2024-08-05 23:01:09,464 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_date_33d1e0bd" ON "metrics_actionremark" ("date"); (params None)
2024-08-05 23:01:09,483 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_detection_date_ee75a187" ON "metrics_anomaly" ("detection_date"); (params None)
2024-08-05 23:01:09,502 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c" ON "metrics_category" ("name"); (params None)
2024-08-05 23:01:09,507 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c_like" ON "metrics_category" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:09,523 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d" ON "metrics_client" ("name"); (params None)
2024-08-05 23:01:09,528 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d_like" ON "metrics_client" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:09,552 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET DEFAULT '{}'; (params None)
2024-08-05 23:01:09,553 - django.db.backends.schema - DEBUG - UPDATE "metrics_dashboard" SET "layout" = '{}' WHERE "layout" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:01:09,554 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET NOT NULL; (params None)
2024-08-05 23:01:09,555 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" DROP DEFAULT; (params None)
2024-08-05 23:01:09,572 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e" ON "metrics_dashboard" ("name"); (params None)
2024-08-05 23:01:09,577 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e_like" ON "metrics_dashboard" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:09,595 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_end_date_31af6c05" ON "metrics_experiment" ("end_date"); (params None)
2024-08-05 23:01:09,621 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7" ON "metrics_experiment" ("name"); (params None)
2024-08-05 23:01:09,626 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7_like" ON "metrics_experiment" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:09,645 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET DEFAULT '{}'; (params None)
2024-08-05 23:01:09,646 - django.db.backends.schema - DEBUG - UPDATE "metrics_experiment" SET "results" = '{}' WHERE "results" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:01:09,647 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET NOT NULL; (params None)
2024-08-05 23:01:09,648 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" DROP DEFAULT; (params None)
2024-08-05 23:01:09,664 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_start_date_a6deff13" ON "metrics_experiment" ("start_date"); (params None)
2024-08-05 23:01:09,684 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET DEFAULT '{}'; (params None)
2024-08-05 23:01:09,685 - django.db.backends.schema - DEBUG - UPDATE "metrics_forecast" SET "confidence_interval" = '{}' WHERE "confidence_interval" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:01:09,686 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET NOT NULL; (params None)
2024-08-05 23:01:09,687 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" DROP DEFAULT; (params None)
2024-08-05 23:01:09,711 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_forecast_date_71750ae8" ON "metrics_forecast" ("forecast_date"); (params None)
2024-08-05 23:01:09,731 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_date_f27e0e6a" ON "metrics_historicaldata" ("date"); (params None)
2024-08-05 23:01:09,751 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_last_updated_3e38a760" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:01:09,771 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5" ON "metrics_metric" ("name"); (params None)
2024-08-05 23:01:09,775 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5_like" ON "metrics_metric" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:09,796 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e" ON "metrics_metric" ("type"); (params None)
2024-08-05 23:01:09,800 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e_like" ON "metrics_metric" ("type" varchar_pattern_ops); (params None)
2024-08-05 23:01:09,830 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80" ON "metrics_project" ("name"); (params None)
2024-08-05 23:01:09,835 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80_like" ON "metrics_project" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:09,860 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET DEFAULT '{}'; (params None)
2024-08-05 23:01:09,861 - django.db.backends.schema - DEBUG - UPDATE "metrics_report" SET "configuration" = '{}' WHERE "configuration" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:01:09,862 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET NOT NULL; (params None)
2024-08-05 23:01:09,863 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" DROP DEFAULT; (params None)
2024-08-05 23:01:09,879 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34" ON "metrics_report" ("name"); (params None)
2024-08-05 23:01:09,883 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34_like" ON "metrics_report" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:09,899 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a" ON "metrics_tag" ("name"); (params None)
2024-08-05 23:01:09,903 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a_like" ON "metrics_tag" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:09,923 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_target_date_81507ff5" ON "metrics_target" ("target_date"); (params None)
2024-08-05 23:01:09,948 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_end_date_8444ef38" ON "metrics_trend" ("end_date"); (params None)
2024-08-05 23:01:09,968 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_start_date_7b1a850f" ON "metrics_trend" ("start_date"); (params None)
2024-08-05 23:01:09,989 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_act_metric__be3429_idx" ON "metrics_actionremark" ("metric_id", "date"); (params None)
2024-08-05 23:01:10,013 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ano_metric__84982d_idx" ON "metrics_anomaly" ("metric_id", "detection_date"); (params None)
2024-08-05 23:01:10,032 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_con_from_me_9411ea_idx" ON "metrics_connection" ("from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:01:10,053 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_exp_start_d_04716a_idx" ON "metrics_experiment" ("start_date", "end_date"); (params None)
2024-08-05 23:01:10,072 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_for_metric__4c9ae2_idx" ON "metrics_forecast" ("metric_id", "forecast_date"); (params None)
2024-08-05 23:01:10,095 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_his_metric__a2923a_idx" ON "metrics_historicaldata" ("metric_id", "date"); (params None)
2024-08-05 23:01:10,114 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_name_c9d100_idx" ON "metrics_metric" ("name", "type"); (params None)
2024-08-05 23:01:10,133 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_7984a6_idx" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:01:10,155 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1bdb27_idx" ON "metrics_tag" ("name", "project_id"); (params None)
2024-08-05 23:01:10,175 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tar_metric__234682_idx" ON "metrics_target" ("metric_id", "target_date"); (params None)
2024-08-05 23:01:10,195 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tre_metric__d386bb_idx" ON "metrics_trend" ("metric_id", "start_date", "end_date"); (params None)
2024-08-05 23:01:10,217 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_con_from_me_9411ea_idx"; (params None)
2024-08-05 23:01:10,242 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:01:10,245 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:01:10,262 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_from_metric_id_aa131d91_uniq" UNIQUE ("tenant_id", "from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:01:10,266 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_project_id_4c1b22ec" ON "metrics_connection" ("project_id"); (params None)
2024-08-05 23:01:10,292 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; ALTER TABLE "metrics_connection" DROP CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id"; (params None)
2024-08-05 23:01:10,293 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "project_id" CASCADE; (params None)
2024-08-05 23:01:10,316 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:01:10,319 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:01:10,336 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:01:10,340 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_project_id_36bdbe46" ON "metrics_metric" ("project_id"); (params None)
2024-08-05 23:01:10,347 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_correlation" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "lag" integer NOT NULL, "pearson_correlation" double precision NOT NULL, "spearman_correlation" double precision NOT NULL); (params None)
2024-08-05 23:01:10,355 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:10,366 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dataqualityscore" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_entry" varchar(255) NOT NULL, "completeness_score" double precision NOT NULL, "accuracy_score" double precision NOT NULL, "consistency_score" double precision NOT NULL, "timeliness_score" double precision NOT NULL, "overall_score" double precision NOT NULL); (params None)
2024-08-05 23:01:10,373 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_impactanalysis" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "before_value" double precision NOT NULL, "after_value" double precision NOT NULL, "percentage_change" double precision NOT NULL, "confidence" double precision NOT NULL, "artifact_link" varchar(200) NOT NULL); (params None)
2024-08-05 23:01:10,381 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_insight" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "title" varchar(200) NOT NULL, "content" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:10,390 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metricmetadata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_source" varchar(100) NOT NULL, "source_url" varchar(200) NOT NULL, "rhythm" varchar(20) NOT NULL, "last_updated" timestamp with time zone NOT NULL, "technical_description" text NOT NULL, "description" text NOT NULL, "artifacts_url" varchar(200) NOT NULL, "hypothesis" text NOT NULL, "confidence" varchar(20) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL); (params None)
2024-08-05 23:01:10,400 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metrictarget" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "target_kpi" varchar(100) NOT NULL, "target_remarks" text NOT NULL, "target_date" date NULL, "target_value" double precision NULL); (params None)
2024-08-05 23:01:10,410 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_strategy" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "estimated_time" interval NOT NULL, "artifacts_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:10,419 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tacticalsolution" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "artifact_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:10,427 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_team" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:10,437 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_technicalindicator" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "stochastic_value" double precision NOT NULL, "rsi_value" double precision NOT NULL, "percent_change" double precision NOT NULL, "moving_average" double precision NOT NULL); (params None)
2024-08-05 23:01:10,444 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_timedimension" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL UNIQUE, "day" integer NOT NULL, "day_of_week" integer NOT NULL, "day_name" varchar(10) NOT NULL, "week" integer NOT NULL, "month" integer NOT NULL, "month_name" varchar(10) NOT NULL, "quarter" integer NOT NULL, "year" integer NOT NULL, "is_weekend" boolean NOT NULL, "is_holiday" boolean NOT NULL); (params None)
2024-08-05 23:01:10,455 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_userprofile" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY); (params None)
2024-08-05 23:01:10,481 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_metric_id_181e8748_fk_metrics_metric_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id"; (params None)
2024-08-05 23:01:10,483 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "metric_id" CASCADE; (params None)
2024-08-05 23:01:10,510 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id"; (params None)
2024-08-05 23:01:10,512 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:01:10,531 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_name_c9d100_idx"; (params None)
2024-08-05 23:01:10,547 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_last_up_7984a6_idx"; (params None)
2024-08-05 23:01:10,567 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" RENAME COLUMN "description" TO "summary"; (params None)
2024-08-05 23:01:10,587 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq"; (params None)
2024-08-05 23:01:10,603 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "correlation_coefficient" CASCADE; (params None)
2024-08-05 23:01:10,620 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" DROP COLUMN "results" CASCADE; (params None)
2024-08-05 23:01:10,636 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "anomaly_detected" CASCADE; (params None)
2024-08-05 23:01:10,652 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "forecasted_value" CASCADE; (params None)
2024-08-05 23:01:10,667 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "trend_component" CASCADE; (params None)
2024-08-05 23:01:10,684 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "importance" varchar(20) DEFAULT 'MEDIUM' NOT NULL; (params None)
2024-08-05 23:01:10,686 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "importance" DROP DEFAULT; (params None)
2024-08-05 23:01:10,708 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:01:10.707521+00:00' NOT NULL; (params None)
2024-08-05 23:01:10,709 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:01:10,724 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "anomaly_type" varchar(20) DEFAULT 'IGNORE' NOT NULL; (params None)
2024-08-05 23:01:10,726 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "anomaly_type" DROP DEFAULT; (params None)
2024-08-05 23:01:10,745 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "quality" varchar(20) DEFAULT 'LOW' NOT NULL; (params None)
2024-08-05 23:01:10,747 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "quality" DROP DEFAULT; (params None)
2024-08-05 23:01:10,775 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "impact_description" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:01:10,777 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "impact_description" DROP DEFAULT; (params None)
2024-08-05 23:01:10,800 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "objective" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:01:10,802 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "objective" DROP DEFAULT; (params None)
2024-08-05 23:01:10,822 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_date" date NULL; (params None)
2024-08-05 23:01:10,839 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_files" varchar(100) NULL; (params None)
2024-08-05 23:01:10,865 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_summary" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:01:10,866 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "result_summary" DROP DEFAULT; (params None)
2024-08-05 23:01:10,883 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_value" double precision NULL; (params None)
2024-08-05 23:01:10,900 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:01:10.899566+00:00' NOT NULL; (params None)
2024-08-05 23:01:10,901 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:01:10,920 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "variance" double precision NULL; (params None)
2024-08-05 23:01:10,941 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD COLUMN "forecast_id" bigint NULL CONSTRAINT "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" REFERENCES "metrics_forecast"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" IMMEDIATE; (params None)
2024-08-05 23:01:10,959 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "impact" TYPE varchar(20) USING "impact"::varchar(20); (params None)
2024-08-05 23:01:11,435 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "status" TYPE varchar(20); (params None)
2024-08-05 23:01:11,622 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric1_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:11,638 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric2_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:11,654 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:11,665 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:01:11,696 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:11,720 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:01:11,755 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:11,786 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "experiment_id" bigint NOT NULL CONSTRAINT "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" REFERENCES "metrics_experiment"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" IMMEDIATE; (params None)
2024-08-05 23:01:11,813 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:11,843 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:11,872 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:11,905 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:11,930 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "user_id" bigint NOT NULL CONSTRAINT "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:01:11,962 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "data_quality_score_id" bigint NULL UNIQUE CONSTRAINT "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" REFERENCES "metrics_dataqualityscore"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" IMMEDIATE; (params None)
2024-08-05 23:01:12,004 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "metric_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:12,038 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:12,081 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:12,116 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:12,147 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:12,185 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:01:12,586 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:12,615 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_team" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:12,652 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "team_id" bigint NOT NULL CONSTRAINT "metrics_strategy_team_id_f1781500_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_team_id_f1781500_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:01:12,682 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:01:12,716 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:01:12,760 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_experiment_team_id_537107e3_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_experiment_team_id_537107e3_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:01:12,796 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:01:12,827 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:12,859 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_timedimension" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:12,896 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:12,932 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "user_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:01:12,938 - django.db.backends.schema - DEBUG - DROP TABLE "metrics_target" CASCADE; (params None)
2024-08-05 23:01:12,969 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "confidence" CASCADE; (params None)
2024-08-05 23:01:12,999 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "description" CASCADE; (params None)
2024-08-05 23:01:13,025 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "hypothesis" CASCADE; (params None)
2024-08-05 23:01:13,057 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "last_updated" CASCADE; (params None)
2024-08-05 23:01:13,091 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_x" CASCADE; (params None)
2024-08-05 23:01:13,118 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_y" CASCADE; (params None)
2024-08-05 23:01:13,144 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "rhythm" CASCADE; (params None)
2024-08-05 23:01:13,169 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "source" CASCADE; (params None)
2024-08-05 23:01:13,533 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "technical_description" CASCADE; (params None)
2024-08-05 23:01:13,563 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD CONSTRAINT "metrics_correlation_tenant_id_metric1_id_met_49a4c34a_uniq" UNIQUE ("tenant_id", "metric1_id", "metric2_id", "lag"); (params None)
2024-08-05 23:01:13,603 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_metric__b85d3a_idx" ON "metrics_insight" ("metric_id", "date"); (params None)
2024-08-05 23:01:13,651 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_user_id_1ebb42_idx" ON "metrics_insight" ("user_id", "date"); (params None)
2024-08-05 23:01:13,682 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_metric__a2b705_idx" ON "metrics_metrictarget" ("metric_id", "target_date"); (params None)
2024-08-05 23:01:13,721 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_6e2e67_idx" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:01:13,753 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_date_53cb14_idx" ON "metrics_timedimension" ("date"); (params None)
2024-08-05 23:01:13,786 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_year_92da9e_idx" ON "metrics_timedimension" ("year", "month", "day"); (params None)
2024-08-05 23:01:13,791 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_username_6e55f358_like" ON "metrics_customuser" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:01:13,795 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_date_ded95ba1" ON "metrics_insight" ("date"); (params None)
2024-08-05 23:01:13,799 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_last_updated_76599a1b" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:01:13,802 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_target_date_38cd9191" ON "metrics_metrictarget" ("target_date"); (params None)
2024-08-05 23:01:13,806 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_forecast_id_29590c29" ON "metrics_historicaldata" ("forecast_id"); (params None)
2024-08-05 23:01:13,810 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric1_id_6e1c2404" ON "metrics_correlation" ("metric1_id"); (params None)
2024-08-05 23:01:13,814 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric2_id_f2cc46dd" ON "metrics_correlation" ("metric2_id"); (params None)
2024-08-05 23:01:13,819 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_tenant_id_a00a5169" ON "metrics_correlation" ("tenant_id"); (params None)
2024-08-05 23:01:13,823 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_customuser_id_group_id_1c5fc435_uniq" UNIQUE ("customuser_id", "group_id"); (params None)
2024-08-05 23:01:13,827 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_g_customuser_id_fc13f3af_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:13,830 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_group_id_6b097e12_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:13,831 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_customuser_id_fc13f3af" ON "metrics_customuser_groups" ("customuser_id"); (params None)
2024-08-05 23:01:13,837 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_group_id_6b097e12" ON "metrics_customuser_groups" ("group_id"); (params None)
2024-08-05 23:01:13,840 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_tenant_id_02b7403c" ON "metrics_customuser" ("tenant_id"); (params None)
2024-08-05 23:01:13,843 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_user__customuser_id_permission_68cc320f_uniq" UNIQUE ("customuser_id", "permission_id"); (params None)
2024-08-05 23:01:13,848 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_customuser_id_46e97f00_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:13,851 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_permission_id_d66d657c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:13,852 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_customuser_id_46e97f00" ON "metrics_customuser_user_permissions" ("customuser_id"); (params None)
2024-08-05 23:01:13,855 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_permission_id_d66d657c" ON "metrics_customuser_user_permissions" ("permission_id"); (params None)
2024-08-05 23:01:13,859 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_tenant_id_8e9f296d" ON "metrics_dataqualityscore" ("tenant_id"); (params None)
2024-08-05 23:01:13,863 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_experiment_id_1beae7fe" ON "metrics_impactanalysis" ("experiment_id"); (params None)
2024-08-05 23:01:13,867 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_metric_id_f4b9eeb6" ON "metrics_impactanalysis" ("metric_id"); (params None)
2024-08-05 23:01:13,871 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_tenant_id_126ca20d" ON "metrics_impactanalysis" ("tenant_id"); (params None)
2024-08-05 23:01:13,875 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_metric_id_26d3a9d8" ON "metrics_insight" ("metric_id"); (params None)
2024-08-05 23:01:13,879 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_tenant_id_724d7d85" ON "metrics_insight" ("tenant_id"); (params None)
2024-08-05 23:01:13,884 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_user_id_83d421e1" ON "metrics_insight" ("user_id"); (params None)
2024-08-05 23:01:13,889 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_tenant_id_3277f967" ON "metrics_metricmetadata" ("tenant_id"); (params None)
2024-08-05 23:01:13,893 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_metric_id_7876e2c8" ON "metrics_metrictarget" ("metric_id"); (params None)
2024-08-05 23:01:13,897 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_tenant_id_b26a17f8" ON "metrics_metrictarget" ("tenant_id"); (params None)
2024-08-05 23:01:13,901 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_tenant_id_1323395e" ON "metrics_strategy" ("tenant_id"); (params None)
2024-08-05 23:01:13,905 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_metric_id_9887ffa4" ON "metrics_tacticalsolution" ("metric_id"); (params None)
2024-08-05 23:01:13,908 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_tenant_id_cf9028f0" ON "metrics_tacticalsolution" ("tenant_id"); (params None)
2024-08-05 23:01:13,911 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_team_tenant_id_3a14c47d" ON "metrics_team" ("tenant_id"); (params None)
2024-08-05 23:01:13,915 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_team_id_f1781500" ON "metrics_strategy" ("team_id"); (params None)
2024-08-05 23:01:13,919 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_team_id_f140658d" ON "metrics_metricmetadata" ("team_id"); (params None)
2024-08-05 23:01:13,925 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_team_id_4c4ffc18" ON "metrics_customuser" ("team_id"); (params None)
2024-08-05 23:01:13,929 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_team_id_537107e3" ON "metrics_experiment" ("team_id"); (params None)
2024-08-05 23:01:13,933 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_metric_id_3e2eead6" ON "metrics_technicalindicator" ("metric_id"); (params None)
2024-08-05 23:01:13,937 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_tenant_id_f4de3b44" ON "metrics_technicalindicator" ("tenant_id"); (params None)
2024-08-05 23:01:13,941 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_timedimension_tenant_id_f375bb45" ON "metrics_timedimension" ("tenant_id"); (params None)
2024-08-05 23:01:13,944 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_userprofile_tenant_id_cca71dae" ON "metrics_userprofile" ("tenant_id"); (params None)
2024-08-05 23:01:13,984 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "strength" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:01:13,986 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "strength" DROP DEFAULT; (params None)
2024-08-05 23:01:14,013 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "lower_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:01:14,014 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "lower_bound" DROP DEFAULT; (params None)
2024-08-05 23:01:14,047 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "upper_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:01:14,049 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "upper_bound" DROP DEFAULT; (params None)
2024-08-05 23:01:14,079 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD COLUMN "slope" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:01:14,081 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ALTER COLUMN "slope" DROP DEFAULT; (params None)
2024-08-05 23:01:14,121 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_movingaverage" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "ma_type" varchar(10) NOT NULL, "period" integer NOT NULL, "value" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:14,164 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_networkanalysisresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "analysis_type" varchar(20) NOT NULL, "result" jsonb NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:14,214 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_seasonalityresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "seasonality_type" varchar(20) NOT NULL, "strength" double precision NOT NULL, "period" integer NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:14,257 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trendchangepoint" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "change_type" varchar(20) NOT NULL, "significance" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:14,263 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD CONSTRAINT "metrics_movingaverage_metric_id_7c61cebf_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:14,266 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_metric_id_7c61cebf" ON "metrics_movingaverage" ("metric_id"); (params None)
2024-08-05 23:01:14,271 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD CONSTRAINT "metrics_networkanaly_metric_id_a4c90102_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:14,273 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_metric_id_a4c90102" ON "metrics_networkanalysisresult" ("metric_id"); (params None)
2024-08-05 23:01:14,277 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityr_metric_id_6e494791_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:14,279 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_metric_id_6e494791" ON "metrics_seasonalityresult" ("metric_id"); (params None)
2024-08-05 23:01:14,282 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD CONSTRAINT "metrics_trendchangep_metric_id_f8eb9f76_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:14,284 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_metric_id_f8eb9f76" ON "metrics_trendchangepoint" ("metric_id"); (params None)
2024-08-05 23:01:14,326 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:01:14,329 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:01:14,364 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" IMMEDIATE; (params None)
2024-08-05 23:01:14,367 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:01:14,749 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ALTER COLUMN "value" DROP NOT NULL; (params None)
2024-08-05 23:01:14,779 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD CONSTRAINT "metrics_dataqualityscore_tenant_id_metric_id_proj_66b9fb01_uniq" UNIQUE ("tenant_id", "metric_id", "project_id"); (params None)
2024-08-05 23:01:14,784 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_metric_id_1b6367d1" ON "metrics_dataqualityscore" ("metric_id"); (params None)
2024-08-05 23:01:14,788 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_project_id_123a4f58" ON "metrics_dataqualityscore" ("project_id"); (params None)
2024-08-05 23:01:14,827 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:01:14,882 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:14,884 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:01:14,925 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:14,928 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:01:14,965 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:14,968 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:01:15,009 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:15,012 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:01:15,046 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq" UNIQUE ("tenant_id", "metric_id"); (params None)
2024-08-05 23:01:15,051 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_tenant_id_5a9de228" ON "metrics_movingaverage" ("tenant_id"); (params None)
2024-08-05 23:01:15,054 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_tenant_id_16a6ba09" ON "metrics_networkanalysisresult" ("tenant_id"); (params None)
2024-08-05 23:01:15,057 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_tenant_id_ca2da3fd" ON "metrics_seasonalityresult" ("tenant_id"); (params None)
2024-08-05 23:01:15,061 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_tenant_id_da10d898" ON "metrics_trendchangepoint" ("tenant_id"); (params None)
2024-08-05 23:01:15,106 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:15,109 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:01:15,110 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_metric_id_c86f5720" ON "metrics_report" ("metric_id"); (params None)
2024-08-05 23:01:15,148 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "analysis_result" jsonb NULL; (params None)
2024-08-05 23:01:15,181 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "anomaly_result" jsonb NULL; (params None)
2024-08-05 23:01:15,214 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:01:15.214047+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:01:15,216 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:01:15,249 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "forecast_result" jsonb NULL; (params None)
2024-08-05 23:01:15,291 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "relationship_result" jsonb NULL; (params None)
2024-08-05 23:01:15,327 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "report" text DEFAULT '1' NOT NULL; (params None)
2024-08-05 23:01:15,329 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "report" DROP DEFAULT; (params None)
2024-08-05 23:01:15,361 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "updated_at" timestamp with time zone DEFAULT '2024-08-05T23:01:15.360391+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:01:15,362 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "updated_at" DROP DEFAULT; (params None)
2024-08-05 23:01:15,794 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_trendchangepoint" DROP CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c"; (params None)
2024-08-05 23:01:15,795 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:01:15,820 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "significance" DROP NOT NULL; (params None)
2024-08-05 23:01:15,849 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" RENAME COLUMN "change_type" TO "direction"; (params None)
2024-08-05 23:01:15,917 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:01:15.916980+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:01:15,919 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:01:15,963 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq"; (params None)
2024-08-05 23:01:15,965 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresul_metric_id_seasonality_ty_d3492b78_uniq" UNIQUE ("metric_id", "seasonality_type"); (params None)
2024-08-05 23:01:16,015 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c"; (params None)
2024-08-05 23:01:16,016 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:01:16,022 - django.db.backends.schema - DEBUG - CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:16,029 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" ("session_key" varchar_pattern_ops); (params None)
2024-08-05 23:01:16,034 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date"); (params None)
2024-08-05 23:01:17,493 - metrics.computations.data_preparation - INFO - Loaded metric 7 for tenant 4 and project 4
2024-08-05 23:01:17,493 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 7
2024-08-05 23:01:17,495 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:17,496 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:17,499 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 7
2024-08-05 23:01:17,508 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:17,508 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:01:17,515 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:17,516 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:17,520 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:17,521 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:01:17,525 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:01:21,370 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 7
2024-08-05 23:01:21,374 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:01:21,379 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:01:21,379 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:01:21,384 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:21,384 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:01:21,387 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:21,391 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3730712106037531, Timeliness: nan
2024-08-05 23:01:21,391 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.769040353458436
2024-08-05 23:01:21,397 - metrics.computations.data_preparation - INFO - Data quality score: 45.769040353458436
2024-08-05 23:01:21,526 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 7, 'tenant_id': 4, 'project_id': 4, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.769040353458436, 'outliers_handled': True, 'profile': {'mean': 100.0119046270916, 'median': 100.13524698910996, 'std': 9.807847379162695, 'min': 77.0955313889259, 'max': 120.96348164625651, 'skewness': -0.04198847944515027, 'kurtosis': -0.5311868404112507, 'missing_percentage': 0.0}}
2024-08-05 23:01:21,532 - metrics.computations.data_preparation - INFO - Loaded metric 7 for tenant 4 and project 4
2024-08-05 23:01:21,532 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 7
2024-08-05 23:01:21,543 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:21,544 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:21,548 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 7
2024-08-05 23:01:21,561 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:21,562 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:01:21,567 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:21,568 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:21,573 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:21,575 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:01:21,582 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:01:24,473 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 7
2024-08-05 23:01:24,477 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:01:24,479 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:01:24,479 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:01:24,483 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:24,483 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:01:24,487 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:24,491 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3730712106037531, Timeliness: nan
2024-08-05 23:01:24,492 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.769040353458436
2024-08-05 23:01:24,497 - metrics.computations.data_preparation - INFO - Data quality score: 45.769040353458436
2024-08-05 23:01:24,554 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 7, 'tenant_id': 4, 'project_id': 4, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.769040353458436, 'outliers_handled': True, 'profile': {'mean': 100.0119046270916, 'median': 100.13524698910996, 'std': 9.807847379162695, 'min': 77.0955313889259, 'max': 120.96348164625651, 'skewness': -0.04198847944515027, 'kurtosis': -0.5311868404112507, 'missing_percentage': 0.0}}
2024-08-05 23:01:24,554 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:01:24,555 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 7
2024-08-05 23:01:24,572 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=3, strength=0.00
2024-08-05 23:01:24,580 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=3, strength=0.00
2024-08-05 23:01:24,586 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 7
2024-08-05 23:01:24,589 - metrics.computations.feature_engineering - INFO - Parameters for metric 7: dynamic
2024-08-05 23:01:24,589 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 7: {'seasonality_period': 3, 'forecast_horizon': 3, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:01:24,593 - metrics.computations.data_preparation - INFO - Loaded metric 7 for tenant 4 and project 4
2024-08-05 23:01:24,593 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 7
2024-08-05 23:01:24,595 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:24,596 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:24,601 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 7
2024-08-05 23:01:24,610 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:24,610 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:01:24,615 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:24,615 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:24,618 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:24,619 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:01:24,623 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:01:27,559 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 7
2024-08-05 23:01:27,563 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:01:27,565 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:01:27,566 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:01:27,569 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:27,570 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:01:27,573 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:27,577 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3730712106037531, Timeliness: nan
2024-08-05 23:01:27,577 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.769040353458436
2024-08-05 23:01:27,582 - metrics.computations.data_preparation - INFO - Data quality score: 45.769040353458436
2024-08-05 23:01:27,673 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 7, 'tenant_id': 4, 'project_id': 4, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.769040353458436, 'outliers_handled': True, 'profile': {'mean': 100.0119046270916, 'median': 100.13524698910996, 'std': 9.807847379162695, 'min': 77.0955313889259, 'max': 120.96348164625651, 'skewness': -0.04198847944515027, 'kurtosis': -0.5311868404112507, 'missing_percentage': 0.0}}
2024-08-05 23:01:27,685 - metrics.computations.data_preparation - INFO - Loaded metric 7 for tenant 4 and project 4
2024-08-05 23:01:27,686 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 7
2024-08-05 23:01:27,688 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:27,689 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:27,701 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 7
2024-08-05 23:01:27,718 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:27,718 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:01:27,724 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:27,724 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:27,729 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:27,730 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:01:27,736 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:01:30,476 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 7
2024-08-05 23:01:30,479 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:01:30,481 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:01:30,481 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:01:30,484 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:30,485 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:01:30,489 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:30,492 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3730712106037531, Timeliness: nan
2024-08-05 23:01:30,492 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.769040353458436
2024-08-05 23:01:30,498 - metrics.computations.data_preparation - INFO - Data quality score: 45.769040353458436
2024-08-05 23:01:30,565 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 7, 'tenant_id': 4, 'project_id': 4, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.769040353458436, 'outliers_handled': True, 'profile': {'mean': 100.0119046270916, 'median': 100.13524698910996, 'std': 9.807847379162695, 'min': 77.0955313889259, 'max': 120.96348164625651, 'skewness': -0.04198847944515027, 'kurtosis': -0.5311868404112507, 'missing_percentage': 0.0}}
2024-08-05 23:01:30,565 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:01:30,565 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 7
2024-08-05 23:01:30,581 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=3, strength=0.00
2024-08-05 23:01:30,590 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=3, strength=0.00
2024-08-05 23:01:30,597 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 7
2024-08-05 23:01:30,598 - metrics.computations.feature_engineering - INFO - Parameters for metric 7: dynamic
2024-08-05 23:01:30,598 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 7: {'seasonality_period': 3, 'forecast_horizon': 3, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:01:30,600 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Setup completed
2024-08-05 23:01:30,606 - metrics.computations.data_preparation - INFO - Loaded metric 7 for tenant 4 and project 4
2024-08-05 23:01:30,607 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 7
2024-08-05 23:01:30,608 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:30,609 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:30,615 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 7
2024-08-05 23:01:30,627 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:30,628 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:01:30,633 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:30,634 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:30,637 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:30,638 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:01:30,642 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:01:33,339 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 7
2024-08-05 23:01:33,342 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:01:33,344 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:01:33,344 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:01:33,347 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:33,347 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:01:33,350 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.549618          4
2023-01-02   93.556676          4
2023-01-03  102.562225          4
2023-01-04   99.374227          4
2023-01-05   96.087566          4
2024-08-05 23:01:33,353 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3730712106037531, Timeliness: nan
2024-08-05 23:01:33,353 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.769040353458436
2024-08-05 23:01:33,358 - metrics.computations.data_preparation - INFO - Data quality score: 45.769040353458436
2024-08-05 23:01:33,434 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 7, 'tenant_id': 4, 'project_id': 4, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.769040353458436, 'outliers_handled': True, 'profile': {'mean': 100.0119046270916, 'median': 100.13524698910996, 'std': 9.807847379162695, 'min': 77.0955313889259, 'max': 120.96348164625651, 'skewness': -0.04198847944515027, 'kurtosis': -0.5311868404112507, 'missing_percentage': 0.0}}
2024-08-05 23:01:33,435 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:01:33,437 - metrics.computations.computations_anomalies - INFO - Initialized AnomalyDetector for metric 7
2024-08-05 23:01:33,437 - metrics.computations.computations_anomalies - INFO - Seasonality period: 7
2024-08-05 23:01:33,437 - metrics.computations.computations_anomalies - INFO - Window size: 30
2024-08-05 23:01:33,437 - metrics.computations.computations_anomalies - INFO - Base threshold: 3.0
2024-08-05 23:01:33,437 - metrics.computations.computations_anomalies - INFO - Context window: 5
2024-08-05 23:01:33,437 - metrics.computations.computations_anomalies - INFO - Global threshold: 4.0
2024-08-05 23:01:33,438 - metrics.computations.computations_anomalies - INFO - Starting anomaly detection for metric 7
2024-08-05 23:01:33,438 - metrics.computations.computations_anomalies - INFO - Data shape: (1000, 2)
2024-08-05 23:01:33,440 - metrics.computations.computations_anomalies - INFO - Data summary: count    994.000000
mean     100.067302
std        9.996807
min       68.290290
25%       93.000307
50%      100.160260
75%      106.972066
max      130.971707
Name: value, dtype: float64
2024-08-05 23:01:33,447 - metrics.computations.computations_anomalies - INFO - Deseasonalized data summary: count    994.000000
mean     100.079765
std        9.988295
min       68.290290
25%       93.047735
50%      100.222176
75%      106.972066
max      130.971707
Name: value, dtype: float64
2024-08-05 23:01:33,684 - metrics.computations.computations_anomalies - INFO - Modified z-scores range: -3.486945881964963 to 3.398910669673398
2024-08-05 23:01:33,687 - metrics.computations.computations_anomalies - INFO - Modified z-scores summary: count    955.000000
mean      -0.003039
std        0.996323
min       -3.486946
25%       -0.663861
50%       -0.009974
75%        0.674519
max        3.398911
Name: value, dtype: float64
2024-08-05 23:01:33,917 - metrics.computations.computations_anomalies - INFO - Adaptive threshold range: 3.490290860147071 to 3.7524315117287528
2024-08-05 23:01:33,920 - metrics.computations.computations_anomalies - INFO - Adaptive threshold summary: count    955.000000
mean       3.615747
std        0.052831
min        3.490291
25%        3.576289
50%        3.614127
75%        3.657394
max        3.752432
Name: value, dtype: float64
2024-08-05 23:01:34,033 - metrics.computations.computations_anomalies - INFO - Contextual z-scores range: -1.7437692270806262 to 1.7643440260219572
2024-08-05 23:01:34,035 - metrics.computations.computations_anomalies - INFO - Contextual z-scores summary: count    951.000000
mean      -0.005989
std        0.883334
min       -1.743769
25%       -0.720222
50%        0.010603
75%        0.687231
max        1.764344
Name: value, dtype: float64
2024-08-05 23:01:34,036 - metrics.computations.computations_anomalies - INFO - Global mean: 100.07976507658546, Global std: 9.988295279343959
2024-08-05 23:01:34,036 - metrics.computations.computations_anomalies - INFO - Number of anomalies detected: 0
2024-08-05 23:01:34,039 - metrics.computations.computations_anomalies - INFO - Detected 0 anomalies for metric 7
2024-08-05 23:01:34,178 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Teardown completed
```

## test_forecast_computation_robustness (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
Status: error
Duration: 20.266 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/unittest/mock.py", line 1369, in patched
    return func(*newargs, **newkeywargs)
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_permanent_computations_robustness.py", line 98, in test_forecast_computation_robustness
    data_prep = DataPreparation(metric_id=self.metric1.id)
TypeError: DataPreparation.__init__() got an unexpected keyword argument 'metric_id'
```

### Output
```
Starting setUp
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
  Applying sessions.0001_initial...
 OK
Initializing PermanentComputations with metric_ids: [9, 10]
Finished initializing PermanentComputations
Initializing DataPreparation for metric_id: 9
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 9
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 9
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 9
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
2024-08-05 23:01:34,197 - metrics - DEBUG - Starting test: test_forecast_computation_robustness (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
2024-08-05 23:01:34,203 - django.db.backends.schema - DEBUG - CREATE TABLE "django_migrations" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:34,226 - django.db.backends.schema - DEBUG - CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
2024-08-05 23:01:34,232 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params None)
2024-08-05 23:01:34,240 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL, "codename" varchar(100) NOT NULL); (params None)
2024-08-05 23:01:34,249 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(80) NOT NULL UNIQUE); (params None)
2024-08-05 23:01:34,261 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:01:34,273 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NOT NULL, "is_superuser" boolean NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:34,281 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:01:34,285 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:01:34,291 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename"); (params None)
2024-08-05 23:01:34,294 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,295 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id"); (params None)
2024-08-05 23:01:34,299 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_name_a6ea08ec_like" ON "auth_group" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:34,303 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id"); (params None)
2024-08-05 23:01:34,307 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,309 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,310 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id"); (params None)
2024-08-05 23:01:34,313 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id"); (params None)
2024-08-05 23:01:34,317 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_username_6821ab7c_like" ON "auth_user" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:01:34,320 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id"); (params None)
2024-08-05 23:01:34,323 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,325 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,327 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id"); (params None)
2024-08-05 23:01:34,330 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id"); (params None)
2024-08-05 23:01:34,333 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id"); (params None)
2024-08-05 23:01:34,337 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,339 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,341 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id"); (params None)
2024-08-05 23:01:34,344 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id"); (params None)
2024-08-05 23:01:34,356 - django.db.backends.schema - DEBUG - CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "action_time" timestamp with time zone NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL, "user_id" integer NOT NULL); (params None)
2024-08-05 23:01:34,362 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,364 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,365 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id"); (params None)
2024-08-05 23:01:34,370 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id"); (params None)
2024-08-05 23:01:34,396 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ALTER COLUMN "name" DROP NOT NULL; (params None)
2024-08-05 23:01:34,406 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" DROP COLUMN "name" CASCADE; (params None)
2024-08-05 23:01:34,414 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ALTER COLUMN "name" TYPE varchar(255); (params None)
2024-08-05 23:01:34,428 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "email" TYPE varchar(254); (params None)
2024-08-05 23:01:34,445 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_login" DROP NOT NULL; (params None)
2024-08-05 23:01:34,463 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "username" TYPE varchar(150); (params None)
2024-08-05 23:01:34,477 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_name" TYPE varchar(150); (params None)
2024-08-05 23:01:34,488 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group" ALTER COLUMN "name" TYPE varchar(150); (params None)
2024-08-05 23:01:34,509 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "first_name" TYPE varchar(150); (params None)
2024-08-05 23:01:34,550 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_client" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "schema_name" varchar(63) NOT NULL UNIQUE, "name" varchar(100) NOT NULL, "created_on" date NOT NULL); (params None)
2024-08-05 23:01:34,560 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_category" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,567 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dashboard" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "layout" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,577 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_domain" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "domain" varchar(253) NOT NULL UNIQUE, "is_primary" boolean NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,591 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "type" varchar(50) NOT NULL, "confidence" varchar(50) NOT NULL, "value_type" varchar(20) NOT NULL, "rhythm" varchar(20) NOT NULL, "description" text NOT NULL, "hypothesis" text NOT NULL, "technical_description" text NOT NULL, "last_updated" timestamp with time zone NOT NULL, "source" varchar(100) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL, "category_id" bigint NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,605 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_historicaldata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "value" double precision NOT NULL, "forecasted_value" double precision NULL, "anomaly_detected" boolean NOT NULL, "trend_component" varchar(50) NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,616 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_forecast" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "forecast_date" date NOT NULL, "forecast_value" double precision NOT NULL, "model_used" varchar(100) NOT NULL, "accuracy" double precision NULL, "confidence_interval" jsonb NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,631 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "status" varchar(50) NOT NULL, "results" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,639 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment_metrics" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "experiment_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,653 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_connection" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "relationship" varchar(100) NOT NULL, "correlation_coefficient" double precision NULL, "tenant_id" bigint NOT NULL, "from_metric_id" bigint NOT NULL, "to_metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,667 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_anomaly" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "detection_date" date NOT NULL, "anomaly_value" double precision NOT NULL, "anomaly_score" double precision NOT NULL, "notes" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,684 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_actionremark" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NULL, "description" text NOT NULL, "impact" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,705 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_project" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "created_on" date NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,722 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_report" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "configuration" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,742 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tag" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "project_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,760 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric_tags" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "metric_id" bigint NOT NULL, "tag_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,781 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_target" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "remarks" text NOT NULL, "target_kpi" varchar(100) NOT NULL, "target_date" date NULL, "target_value" double precision NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,809 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trend" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "trend_type" varchar(50) NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "trend_value" double precision NOT NULL, "notes" text NOT NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:34,816 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_schema_name_87d6fbb5_like" ON "metrics_client" ("schema_name" varchar_pattern_ops); (params None)
2024-08-05 23:01:34,819 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_category" ADD CONSTRAINT "metrics_category_tenant_id_67d98cc6_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,821 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_tenant_id_67d98cc6" ON "metrics_category" ("tenant_id"); (params None)
2024-08-05 23:01:34,824 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ADD CONSTRAINT "metrics_dashboard_tenant_id_50099a7d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,825 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_tenant_id_50099a7d" ON "metrics_dashboard" ("tenant_id"); (params None)
2024-08-05 23:01:34,829 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_domain" ADD CONSTRAINT "metrics_domain_tenant_id_259fb21f_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,830 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_domain_bdc97b86_like" ON "metrics_domain" ("domain" varchar_pattern_ops); (params None)
2024-08-05 23:01:34,834 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_is_primary_ac9d2eaf" ON "metrics_domain" ("is_primary"); (params None)
2024-08-05 23:01:34,838 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_tenant_id_259fb21f" ON "metrics_domain" ("tenant_id"); (params None)
2024-08-05 23:01:34,842 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_category_id_8793f683_fk_metrics_category_id" FOREIGN KEY ("category_id") REFERENCES "metrics_category" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,843 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_9606b577_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,845 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_category_id_8793f683" ON "metrics_metric" ("category_id"); (params None)
2024-08-05 23:01:34,848 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tenant_id_9606b577" ON "metrics_metric" ("tenant_id"); (params None)
2024-08-05 23:01:34,852 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_tenant_id_438c5ad4_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,854 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_metric_id_3f9e8174_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,855 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_tenant_id_438c5ad4" ON "metrics_historicaldata" ("tenant_id"); (params None)
2024-08-05 23:01:34,859 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_metric_id_3f9e8174" ON "metrics_historicaldata" ("metric_id"); (params None)
2024-08-05 23:01:34,862 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_tenant_id_92d37185_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,864 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_metric_id_e05f23a8_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,865 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_tenant_id_92d37185" ON "metrics_forecast" ("tenant_id"); (params None)
2024-08-05 23:01:34,868 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_metric_id_e05f23a8" ON "metrics_forecast" ("metric_id"); (params None)
2024-08-05 23:01:34,872 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD CONSTRAINT "metrics_experiment_tenant_id_10fa364a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,874 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_tenant_id_10fa364a" ON "metrics_experiment" ("tenant_id"); (params None)
2024-08-05 23:01:34,878 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_metri_experiment_id_metric_id_a9d54b29_uniq" UNIQUE ("experiment_id", "metric_id"); (params None)
2024-08-05 23:01:34,881 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_experiment_id_372c6b59_fk_metrics_e" FOREIGN KEY ("experiment_id") REFERENCES "metrics_experiment" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,883 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_metric_id_c8f84167_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,884 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_experiment_id_372c6b59" ON "metrics_experiment_metrics" ("experiment_id"); (params None)
2024-08-05 23:01:34,888 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_metric_id_c8f84167" ON "metrics_experiment_metrics" ("metric_id"); (params None)
2024-08-05 23:01:34,891 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_2e1e5750_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,893 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_from_metric_id_33b50521_fk_metrics_metric_id" FOREIGN KEY ("from_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,894 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_to_metric_id_94489c1c_fk_metrics_metric_id" FOREIGN KEY ("to_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,895 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_tenant_id_2e1e5750" ON "metrics_connection" ("tenant_id"); (params None)
2024-08-05 23:01:34,899 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_from_metric_id_33b50521" ON "metrics_connection" ("from_metric_id"); (params None)
2024-08-05 23:01:34,903 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_to_metric_id_94489c1c" ON "metrics_connection" ("to_metric_id"); (params None)
2024-08-05 23:01:34,906 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_tenant_id_9e474130_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,908 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_metric_id_1b3c3295_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,909 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_tenant_id_9e474130" ON "metrics_anomaly" ("tenant_id"); (params None)
2024-08-05 23:01:34,913 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_metric_id_1b3c3295" ON "metrics_anomaly" ("metric_id"); (params None)
2024-08-05 23:01:34,916 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_tenant_id_86ffa3a9_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,918 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_metric_id_c1b270f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,920 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_tenant_id_86ffa3a9" ON "metrics_actionremark" ("tenant_id"); (params None)
2024-08-05 23:01:34,924 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_metric_id_c1b270f2" ON "metrics_actionremark" ("metric_id"); (params None)
2024-08-05 23:01:34,928 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_project" ADD CONSTRAINT "metrics_project_tenant_id_db4a1170_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,930 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_tenant_id_db4a1170" ON "metrics_project" ("tenant_id"); (params None)
2024-08-05 23:01:34,934 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD CONSTRAINT "metrics_report_tenant_id_d1cf4812_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,937 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_tenant_id_d1cf4812" ON "metrics_report" ("tenant_id"); (params None)
2024-08-05 23:01:34,940 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_name_project_id_2d57d4da_uniq" UNIQUE ("name", "project_id"); (params None)
2024-08-05 23:01:34,944 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_project_id_b7ac5c8e_fk_metrics_project_id" FOREIGN KEY ("project_id") REFERENCES "metrics_project" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,946 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_tenant_id_c286653b_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,948 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_project_id_b7ac5c8e" ON "metrics_tag" ("project_id"); (params None)
2024-08-05 23:01:34,951 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_tenant_id_c286653b" ON "metrics_tag" ("tenant_id"); (params None)
2024-08-05 23:01:34,955 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_tag_id_a8e1a165_uniq" UNIQUE ("metric_id", "tag_id"); (params None)
2024-08-05 23:01:34,958 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_b2a068f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,960 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_tag_id_61869f56_fk_metrics_tag_id" FOREIGN KEY ("tag_id") REFERENCES "metrics_tag" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,962 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_metric_id_b2a068f2" ON "metrics_metric_tags" ("metric_id"); (params None)
2024-08-05 23:01:34,965 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_tag_id_61869f56" ON "metrics_metric_tags" ("tag_id"); (params None)
2024-08-05 23:01:34,969 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,971 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,973 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_metric_id_181e8748" ON "metrics_target" ("metric_id"); (params None)
2024-08-05 23:01:34,976 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_tenant_id_118eb54a" ON "metrics_target" ("tenant_id"); (params None)
2024-08-05 23:01:34,980 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_metric_id_25179b98_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,982 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_tenant_id_4cb1485d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:34,983 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_metric_id_25179b98" ON "metrics_trend" ("metric_id"); (params None)
2024-08-05 23:01:34,987 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_tenant_id_4cb1485d" ON "metrics_trend" ("tenant_id"); (params None)
2024-08-05 23:01:35,186 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_date_33d1e0bd" ON "metrics_actionremark" ("date"); (params None)
2024-08-05 23:01:35,206 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_detection_date_ee75a187" ON "metrics_anomaly" ("detection_date"); (params None)
2024-08-05 23:01:35,223 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c" ON "metrics_category" ("name"); (params None)
2024-08-05 23:01:35,227 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c_like" ON "metrics_category" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:35,243 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d" ON "metrics_client" ("name"); (params None)
2024-08-05 23:01:35,247 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d_like" ON "metrics_client" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:35,269 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET DEFAULT '{}'; (params None)
2024-08-05 23:01:35,270 - django.db.backends.schema - DEBUG - UPDATE "metrics_dashboard" SET "layout" = '{}' WHERE "layout" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:01:35,271 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET NOT NULL; (params None)
2024-08-05 23:01:35,271 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" DROP DEFAULT; (params None)
2024-08-05 23:01:35,286 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e" ON "metrics_dashboard" ("name"); (params None)
2024-08-05 23:01:35,290 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e_like" ON "metrics_dashboard" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:35,307 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_end_date_31af6c05" ON "metrics_experiment" ("end_date"); (params None)
2024-08-05 23:01:35,323 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7" ON "metrics_experiment" ("name"); (params None)
2024-08-05 23:01:35,327 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7_like" ON "metrics_experiment" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:35,669 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET DEFAULT '{}'; (params None)
2024-08-05 23:01:35,670 - django.db.backends.schema - DEBUG - UPDATE "metrics_experiment" SET "results" = '{}' WHERE "results" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:01:35,671 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET NOT NULL; (params None)
2024-08-05 23:01:35,672 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" DROP DEFAULT; (params None)
2024-08-05 23:01:35,684 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_start_date_a6deff13" ON "metrics_experiment" ("start_date"); (params None)
2024-08-05 23:01:35,700 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET DEFAULT '{}'; (params None)
2024-08-05 23:01:35,701 - django.db.backends.schema - DEBUG - UPDATE "metrics_forecast" SET "confidence_interval" = '{}' WHERE "confidence_interval" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:01:35,702 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET NOT NULL; (params None)
2024-08-05 23:01:35,703 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" DROP DEFAULT; (params None)
2024-08-05 23:01:35,717 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_forecast_date_71750ae8" ON "metrics_forecast" ("forecast_date"); (params None)
2024-08-05 23:01:35,736 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_date_f27e0e6a" ON "metrics_historicaldata" ("date"); (params None)
2024-08-05 23:01:35,753 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_last_updated_3e38a760" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:01:35,770 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5" ON "metrics_metric" ("name"); (params None)
2024-08-05 23:01:35,775 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5_like" ON "metrics_metric" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:35,793 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e" ON "metrics_metric" ("type"); (params None)
2024-08-05 23:01:35,796 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e_like" ON "metrics_metric" ("type" varchar_pattern_ops); (params None)
2024-08-05 23:01:35,824 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80" ON "metrics_project" ("name"); (params None)
2024-08-05 23:01:35,829 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80_like" ON "metrics_project" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:35,847 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET DEFAULT '{}'; (params None)
2024-08-05 23:01:35,848 - django.db.backends.schema - DEBUG - UPDATE "metrics_report" SET "configuration" = '{}' WHERE "configuration" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:01:35,849 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET NOT NULL; (params None)
2024-08-05 23:01:35,850 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" DROP DEFAULT; (params None)
2024-08-05 23:01:35,866 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34" ON "metrics_report" ("name"); (params None)
2024-08-05 23:01:35,871 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34_like" ON "metrics_report" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:35,889 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a" ON "metrics_tag" ("name"); (params None)
2024-08-05 23:01:35,894 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a_like" ON "metrics_tag" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:35,910 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_target_date_81507ff5" ON "metrics_target" ("target_date"); (params None)
2024-08-05 23:01:35,929 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_end_date_8444ef38" ON "metrics_trend" ("end_date"); (params None)
2024-08-05 23:01:35,946 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_start_date_7b1a850f" ON "metrics_trend" ("start_date"); (params None)
2024-08-05 23:01:35,961 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_act_metric__be3429_idx" ON "metrics_actionremark" ("metric_id", "date"); (params None)
2024-08-05 23:01:35,979 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ano_metric__84982d_idx" ON "metrics_anomaly" ("metric_id", "detection_date"); (params None)
2024-08-05 23:01:35,999 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_con_from_me_9411ea_idx" ON "metrics_connection" ("from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:01:36,017 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_exp_start_d_04716a_idx" ON "metrics_experiment" ("start_date", "end_date"); (params None)
2024-08-05 23:01:36,034 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_for_metric__4c9ae2_idx" ON "metrics_forecast" ("metric_id", "forecast_date"); (params None)
2024-08-05 23:01:36,055 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_his_metric__a2923a_idx" ON "metrics_historicaldata" ("metric_id", "date"); (params None)
2024-08-05 23:01:36,074 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_name_c9d100_idx" ON "metrics_metric" ("name", "type"); (params None)
2024-08-05 23:01:36,092 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_7984a6_idx" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:01:36,109 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1bdb27_idx" ON "metrics_tag" ("name", "project_id"); (params None)
2024-08-05 23:01:36,130 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tar_metric__234682_idx" ON "metrics_target" ("metric_id", "target_date"); (params None)
2024-08-05 23:01:36,148 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tre_metric__d386bb_idx" ON "metrics_trend" ("metric_id", "start_date", "end_date"); (params None)
2024-08-05 23:01:36,169 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_con_from_me_9411ea_idx"; (params None)
2024-08-05 23:01:36,189 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:01:36,191 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:01:36,206 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_from_metric_id_aa131d91_uniq" UNIQUE ("tenant_id", "from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:01:36,210 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_project_id_4c1b22ec" ON "metrics_connection" ("project_id"); (params None)
2024-08-05 23:01:36,233 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; ALTER TABLE "metrics_connection" DROP CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id"; (params None)
2024-08-05 23:01:36,234 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "project_id" CASCADE; (params None)
2024-08-05 23:01:36,248 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:01:36,251 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:01:36,269 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:01:36,273 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_project_id_36bdbe46" ON "metrics_metric" ("project_id"); (params None)
2024-08-05 23:01:36,281 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_correlation" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "lag" integer NOT NULL, "pearson_correlation" double precision NOT NULL, "spearman_correlation" double precision NOT NULL); (params None)
2024-08-05 23:01:36,287 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:36,298 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dataqualityscore" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_entry" varchar(255) NOT NULL, "completeness_score" double precision NOT NULL, "accuracy_score" double precision NOT NULL, "consistency_score" double precision NOT NULL, "timeliness_score" double precision NOT NULL, "overall_score" double precision NOT NULL); (params None)
2024-08-05 23:01:36,304 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_impactanalysis" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "before_value" double precision NOT NULL, "after_value" double precision NOT NULL, "percentage_change" double precision NOT NULL, "confidence" double precision NOT NULL, "artifact_link" varchar(200) NOT NULL); (params None)
2024-08-05 23:01:36,312 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_insight" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "title" varchar(200) NOT NULL, "content" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:36,321 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metricmetadata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_source" varchar(100) NOT NULL, "source_url" varchar(200) NOT NULL, "rhythm" varchar(20) NOT NULL, "last_updated" timestamp with time zone NOT NULL, "technical_description" text NOT NULL, "description" text NOT NULL, "artifacts_url" varchar(200) NOT NULL, "hypothesis" text NOT NULL, "confidence" varchar(20) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL); (params None)
2024-08-05 23:01:36,330 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metrictarget" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "target_kpi" varchar(100) NOT NULL, "target_remarks" text NOT NULL, "target_date" date NULL, "target_value" double precision NULL); (params None)
2024-08-05 23:01:36,340 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_strategy" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "estimated_time" interval NOT NULL, "artifacts_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:36,350 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tacticalsolution" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "artifact_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:36,359 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_team" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:36,368 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_technicalindicator" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "stochastic_value" double precision NOT NULL, "rsi_value" double precision NOT NULL, "percent_change" double precision NOT NULL, "moving_average" double precision NOT NULL); (params None)
2024-08-05 23:01:36,377 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_timedimension" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL UNIQUE, "day" integer NOT NULL, "day_of_week" integer NOT NULL, "day_name" varchar(10) NOT NULL, "week" integer NOT NULL, "month" integer NOT NULL, "month_name" varchar(10) NOT NULL, "quarter" integer NOT NULL, "year" integer NOT NULL, "is_weekend" boolean NOT NULL, "is_holiday" boolean NOT NULL); (params None)
2024-08-05 23:01:36,387 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_userprofile" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY); (params None)
2024-08-05 23:01:36,413 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_metric_id_181e8748_fk_metrics_metric_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id"; (params None)
2024-08-05 23:01:36,414 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "metric_id" CASCADE; (params None)
2024-08-05 23:01:36,432 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id"; (params None)
2024-08-05 23:01:36,434 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:01:36,449 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_name_c9d100_idx"; (params None)
2024-08-05 23:01:36,467 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_last_up_7984a6_idx"; (params None)
2024-08-05 23:01:36,481 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" RENAME COLUMN "description" TO "summary"; (params None)
2024-08-05 23:01:36,506 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq"; (params None)
2024-08-05 23:01:36,523 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "correlation_coefficient" CASCADE; (params None)
2024-08-05 23:01:36,540 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" DROP COLUMN "results" CASCADE; (params None)
2024-08-05 23:01:36,555 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "anomaly_detected" CASCADE; (params None)
2024-08-05 23:01:36,574 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "forecasted_value" CASCADE; (params None)
2024-08-05 23:01:36,590 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "trend_component" CASCADE; (params None)
2024-08-05 23:01:36,604 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "importance" varchar(20) DEFAULT 'MEDIUM' NOT NULL; (params None)
2024-08-05 23:01:36,605 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "importance" DROP DEFAULT; (params None)
2024-08-05 23:01:36,622 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:01:36.621476+00:00' NOT NULL; (params None)
2024-08-05 23:01:36,623 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:01:36,638 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "anomaly_type" varchar(20) DEFAULT 'IGNORE' NOT NULL; (params None)
2024-08-05 23:01:36,639 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "anomaly_type" DROP DEFAULT; (params None)
2024-08-05 23:01:36,653 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "quality" varchar(20) DEFAULT 'LOW' NOT NULL; (params None)
2024-08-05 23:01:36,655 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "quality" DROP DEFAULT; (params None)
2024-08-05 23:01:36,670 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "impact_description" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:01:36,672 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "impact_description" DROP DEFAULT; (params None)
2024-08-05 23:01:36,689 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "objective" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:01:36,690 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "objective" DROP DEFAULT; (params None)
2024-08-05 23:01:36,703 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_date" date NULL; (params None)
2024-08-05 23:01:36,715 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_files" varchar(100) NULL; (params None)
2024-08-05 23:01:36,729 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_summary" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:01:36,730 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "result_summary" DROP DEFAULT; (params None)
2024-08-05 23:01:36,750 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_value" double precision NULL; (params None)
2024-08-05 23:01:36,766 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:01:36.766289+00:00' NOT NULL; (params None)
2024-08-05 23:01:36,768 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:01:36,781 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "variance" double precision NULL; (params None)
2024-08-05 23:01:36,798 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD COLUMN "forecast_id" bigint NULL CONSTRAINT "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" REFERENCES "metrics_forecast"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" IMMEDIATE; (params None)
2024-08-05 23:01:36,816 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "impact" TYPE varchar(20) USING "impact"::varchar(20); (params None)
2024-08-05 23:01:36,937 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "status" TYPE varchar(20); (params None)
2024-08-05 23:01:37,418 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric1_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,438 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric2_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,455 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,466 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:01:37,501 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,523 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:01:37,555 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:37,579 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "experiment_id" bigint NOT NULL CONSTRAINT "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" REFERENCES "metrics_experiment"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" IMMEDIATE; (params None)
2024-08-05 23:01:37,606 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,637 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,661 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,688 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,712 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "user_id" bigint NOT NULL CONSTRAINT "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,740 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "data_quality_score_id" bigint NULL UNIQUE CONSTRAINT "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" REFERENCES "metrics_dataqualityscore"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" IMMEDIATE; (params None)
2024-08-05 23:01:37,772 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "metric_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,802 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,833 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,858 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,889 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:37,918 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:01:37,945 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:38,302 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_team" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:38,332 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "team_id" bigint NOT NULL CONSTRAINT "metrics_strategy_team_id_f1781500_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_team_id_f1781500_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:01:38,360 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:01:38,396 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:01:38,425 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_experiment_team_id_537107e3_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_experiment_team_id_537107e3_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:01:38,455 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:01:38,487 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:38,521 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_timedimension" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:38,553 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:38,586 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "user_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:01:38,592 - django.db.backends.schema - DEBUG - DROP TABLE "metrics_target" CASCADE; (params None)
2024-08-05 23:01:38,616 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "confidence" CASCADE; (params None)
2024-08-05 23:01:38,643 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "description" CASCADE; (params None)
2024-08-05 23:01:38,668 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "hypothesis" CASCADE; (params None)
2024-08-05 23:01:38,696 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "last_updated" CASCADE; (params None)
2024-08-05 23:01:38,726 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_x" CASCADE; (params None)
2024-08-05 23:01:38,755 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_y" CASCADE; (params None)
2024-08-05 23:01:38,782 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "rhythm" CASCADE; (params None)
2024-08-05 23:01:38,808 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "source" CASCADE; (params None)
2024-08-05 23:01:39,170 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "technical_description" CASCADE; (params None)
2024-08-05 23:01:39,195 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD CONSTRAINT "metrics_correlation_tenant_id_metric1_id_met_49a4c34a_uniq" UNIQUE ("tenant_id", "metric1_id", "metric2_id", "lag"); (params None)
2024-08-05 23:01:39,231 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_metric__b85d3a_idx" ON "metrics_insight" ("metric_id", "date"); (params None)
2024-08-05 23:01:39,261 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_user_id_1ebb42_idx" ON "metrics_insight" ("user_id", "date"); (params None)
2024-08-05 23:01:39,291 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_metric__a2b705_idx" ON "metrics_metrictarget" ("metric_id", "target_date"); (params None)
2024-08-05 23:01:39,322 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_6e2e67_idx" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:01:39,349 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_date_53cb14_idx" ON "metrics_timedimension" ("date"); (params None)
2024-08-05 23:01:39,377 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_year_92da9e_idx" ON "metrics_timedimension" ("year", "month", "day"); (params None)
2024-08-05 23:01:39,382 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_username_6e55f358_like" ON "metrics_customuser" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:01:39,385 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_date_ded95ba1" ON "metrics_insight" ("date"); (params None)
2024-08-05 23:01:39,389 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_last_updated_76599a1b" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:01:39,392 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_target_date_38cd9191" ON "metrics_metrictarget" ("target_date"); (params None)
2024-08-05 23:01:39,394 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_forecast_id_29590c29" ON "metrics_historicaldata" ("forecast_id"); (params None)
2024-08-05 23:01:39,398 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric1_id_6e1c2404" ON "metrics_correlation" ("metric1_id"); (params None)
2024-08-05 23:01:39,402 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric2_id_f2cc46dd" ON "metrics_correlation" ("metric2_id"); (params None)
2024-08-05 23:01:39,405 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_tenant_id_a00a5169" ON "metrics_correlation" ("tenant_id"); (params None)
2024-08-05 23:01:39,409 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_customuser_id_group_id_1c5fc435_uniq" UNIQUE ("customuser_id", "group_id"); (params None)
2024-08-05 23:01:39,413 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_g_customuser_id_fc13f3af_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:39,415 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_group_id_6b097e12_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:39,416 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_customuser_id_fc13f3af" ON "metrics_customuser_groups" ("customuser_id"); (params None)
2024-08-05 23:01:39,420 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_group_id_6b097e12" ON "metrics_customuser_groups" ("group_id"); (params None)
2024-08-05 23:01:39,423 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_tenant_id_02b7403c" ON "metrics_customuser" ("tenant_id"); (params None)
2024-08-05 23:01:39,427 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_user__customuser_id_permission_68cc320f_uniq" UNIQUE ("customuser_id", "permission_id"); (params None)
2024-08-05 23:01:39,431 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_customuser_id_46e97f00_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:39,433 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_permission_id_d66d657c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:39,434 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_customuser_id_46e97f00" ON "metrics_customuser_user_permissions" ("customuser_id"); (params None)
2024-08-05 23:01:39,437 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_permission_id_d66d657c" ON "metrics_customuser_user_permissions" ("permission_id"); (params None)
2024-08-05 23:01:39,442 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_tenant_id_8e9f296d" ON "metrics_dataqualityscore" ("tenant_id"); (params None)
2024-08-05 23:01:39,446 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_experiment_id_1beae7fe" ON "metrics_impactanalysis" ("experiment_id"); (params None)
2024-08-05 23:01:39,449 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_metric_id_f4b9eeb6" ON "metrics_impactanalysis" ("metric_id"); (params None)
2024-08-05 23:01:39,453 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_tenant_id_126ca20d" ON "metrics_impactanalysis" ("tenant_id"); (params None)
2024-08-05 23:01:39,457 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_metric_id_26d3a9d8" ON "metrics_insight" ("metric_id"); (params None)
2024-08-05 23:01:39,461 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_tenant_id_724d7d85" ON "metrics_insight" ("tenant_id"); (params None)
2024-08-05 23:01:39,464 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_user_id_83d421e1" ON "metrics_insight" ("user_id"); (params None)
2024-08-05 23:01:39,468 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_tenant_id_3277f967" ON "metrics_metricmetadata" ("tenant_id"); (params None)
2024-08-05 23:01:39,472 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_metric_id_7876e2c8" ON "metrics_metrictarget" ("metric_id"); (params None)
2024-08-05 23:01:39,476 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_tenant_id_b26a17f8" ON "metrics_metrictarget" ("tenant_id"); (params None)
2024-08-05 23:01:39,480 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_tenant_id_1323395e" ON "metrics_strategy" ("tenant_id"); (params None)
2024-08-05 23:01:39,484 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_metric_id_9887ffa4" ON "metrics_tacticalsolution" ("metric_id"); (params None)
2024-08-05 23:01:39,487 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_tenant_id_cf9028f0" ON "metrics_tacticalsolution" ("tenant_id"); (params None)
2024-08-05 23:01:39,490 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_team_tenant_id_3a14c47d" ON "metrics_team" ("tenant_id"); (params None)
2024-08-05 23:01:39,495 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_team_id_f1781500" ON "metrics_strategy" ("team_id"); (params None)
2024-08-05 23:01:39,499 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_team_id_f140658d" ON "metrics_metricmetadata" ("team_id"); (params None)
2024-08-05 23:01:39,501 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_team_id_4c4ffc18" ON "metrics_customuser" ("team_id"); (params None)
2024-08-05 23:01:39,506 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_team_id_537107e3" ON "metrics_experiment" ("team_id"); (params None)
2024-08-05 23:01:39,510 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_metric_id_3e2eead6" ON "metrics_technicalindicator" ("metric_id"); (params None)
2024-08-05 23:01:39,513 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_tenant_id_f4de3b44" ON "metrics_technicalindicator" ("tenant_id"); (params None)
2024-08-05 23:01:39,516 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_timedimension_tenant_id_f375bb45" ON "metrics_timedimension" ("tenant_id"); (params None)
2024-08-05 23:01:39,520 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_userprofile_tenant_id_cca71dae" ON "metrics_userprofile" ("tenant_id"); (params None)
2024-08-05 23:01:39,549 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "strength" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:01:39,550 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "strength" DROP DEFAULT; (params None)
2024-08-05 23:01:39,576 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "lower_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:01:39,578 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "lower_bound" DROP DEFAULT; (params None)
2024-08-05 23:01:39,605 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "upper_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:01:39,606 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "upper_bound" DROP DEFAULT; (params None)
2024-08-05 23:01:39,629 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD COLUMN "slope" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:01:39,631 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ALTER COLUMN "slope" DROP DEFAULT; (params None)
2024-08-05 23:01:39,663 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_movingaverage" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "ma_type" varchar(10) NOT NULL, "period" integer NOT NULL, "value" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:39,698 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_networkanalysisresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "analysis_type" varchar(20) NOT NULL, "result" jsonb NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:39,742 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_seasonalityresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "seasonality_type" varchar(20) NOT NULL, "strength" double precision NOT NULL, "period" integer NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:39,780 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trendchangepoint" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "change_type" varchar(20) NOT NULL, "significance" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:39,785 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD CONSTRAINT "metrics_movingaverage_metric_id_7c61cebf_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:39,788 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_metric_id_7c61cebf" ON "metrics_movingaverage" ("metric_id"); (params None)
2024-08-05 23:01:39,791 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD CONSTRAINT "metrics_networkanaly_metric_id_a4c90102_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:39,794 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_metric_id_a4c90102" ON "metrics_networkanalysisresult" ("metric_id"); (params None)
2024-08-05 23:01:39,798 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityr_metric_id_6e494791_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:39,800 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_metric_id_6e494791" ON "metrics_seasonalityresult" ("metric_id"); (params None)
2024-08-05 23:01:39,803 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD CONSTRAINT "metrics_trendchangep_metric_id_f8eb9f76_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:39,805 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_metric_id_f8eb9f76" ON "metrics_trendchangepoint" ("metric_id"); (params None)
2024-08-05 23:01:39,845 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:01:39,847 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:01:39,881 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" IMMEDIATE; (params None)
2024-08-05 23:01:39,884 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:01:40,239 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ALTER COLUMN "value" DROP NOT NULL; (params None)
2024-08-05 23:01:40,265 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD CONSTRAINT "metrics_dataqualityscore_tenant_id_metric_id_proj_66b9fb01_uniq" UNIQUE ("tenant_id", "metric_id", "project_id"); (params None)
2024-08-05 23:01:40,270 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_metric_id_1b6367d1" ON "metrics_dataqualityscore" ("metric_id"); (params None)
2024-08-05 23:01:40,273 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_project_id_123a4f58" ON "metrics_dataqualityscore" ("project_id"); (params None)
2024-08-05 23:01:40,308 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:01:40,349 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:40,351 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:01:40,384 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:40,387 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:01:40,420 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:40,423 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:01:40,457 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:40,459 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:01:40,488 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq" UNIQUE ("tenant_id", "metric_id"); (params None)
2024-08-05 23:01:40,494 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_tenant_id_5a9de228" ON "metrics_movingaverage" ("tenant_id"); (params None)
2024-08-05 23:01:40,498 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_tenant_id_16a6ba09" ON "metrics_networkanalysisresult" ("tenant_id"); (params None)
2024-08-05 23:01:40,503 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_tenant_id_ca2da3fd" ON "metrics_seasonalityresult" ("tenant_id"); (params None)
2024-08-05 23:01:40,507 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_tenant_id_da10d898" ON "metrics_trendchangepoint" ("tenant_id"); (params None)
2024-08-05 23:01:40,548 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:40,550 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:01:40,551 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_metric_id_c86f5720" ON "metrics_report" ("metric_id"); (params None)
2024-08-05 23:01:40,582 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "analysis_result" jsonb NULL; (params None)
2024-08-05 23:01:40,612 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "anomaly_result" jsonb NULL; (params None)
2024-08-05 23:01:40,643 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:01:40.643012+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:01:40,645 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:01:40,671 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "forecast_result" jsonb NULL; (params None)
2024-08-05 23:01:40,700 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "relationship_result" jsonb NULL; (params None)
2024-08-05 23:01:40,733 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "report" text DEFAULT '1' NOT NULL; (params None)
2024-08-05 23:01:40,734 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "report" DROP DEFAULT; (params None)
2024-08-05 23:01:40,765 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "updated_at" timestamp with time zone DEFAULT '2024-08-05T23:01:40.764780+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:01:40,766 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "updated_at" DROP DEFAULT; (params None)
2024-08-05 23:01:41,177 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_trendchangepoint" DROP CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c"; (params None)
2024-08-05 23:01:41,178 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:01:41,200 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "significance" DROP NOT NULL; (params None)
2024-08-05 23:01:41,232 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" RENAME COLUMN "change_type" TO "direction"; (params None)
2024-08-05 23:01:41,297 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:01:41.296567+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:01:41,299 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:01:41,334 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq"; (params None)
2024-08-05 23:01:41,335 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresul_metric_id_seasonality_ty_d3492b78_uniq" UNIQUE ("metric_id", "seasonality_type"); (params None)
2024-08-05 23:01:41,379 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c"; (params None)
2024-08-05 23:01:41,381 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:01:41,386 - django.db.backends.schema - DEBUG - CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:41,393 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" ("session_key" varchar_pattern_ops); (params None)
2024-08-05 23:01:41,396 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date"); (params None)
2024-08-05 23:01:42,582 - metrics.computations.data_preparation - INFO - Loaded metric 9 for tenant 5 and project 5
2024-08-05 23:01:42,582 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 9
2024-08-05 23:01:42,583 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:42,584 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:42,586 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 9
2024-08-05 23:01:42,593 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:42,594 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:01:42,597 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:42,598 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:42,600 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:42,601 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:01:42,604 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:01:45,239 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 9
2024-08-05 23:01:45,241 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:01:45,243 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:01:45,243 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:01:45,247 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:45,248 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:01:45,252 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:45,255 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36543266002463065, Timeliness: nan
2024-08-05 23:01:45,256 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.51442200082103
2024-08-05 23:01:45,262 - metrics.computations.data_preparation - INFO - Data quality score: 45.51442200082103
2024-08-05 23:01:45,357 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 9, 'tenant_id': 5, 'project_id': 5, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.51442200082103, 'outliers_handled': True, 'profile': {'mean': 99.81602410659238, 'median': 99.71697116023687, 'std': 9.541590804904448, 'min': 77.9611021482892, 'max': 122.76749263830959, 'skewness': 0.06672942712752285, 'kurtosis': -0.43164642791855234, 'missing_percentage': 0.0}}
2024-08-05 23:01:45,369 - metrics.computations.data_preparation - INFO - Loaded metric 9 for tenant 5 and project 5
2024-08-05 23:01:45,369 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 9
2024-08-05 23:01:45,371 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:45,371 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:45,374 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 9
2024-08-05 23:01:45,385 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:45,391 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:01:45,398 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:45,400 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:45,404 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:45,405 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:01:45,409 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:01:48,219 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 9
2024-08-05 23:01:48,223 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:01:48,225 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:01:48,225 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:01:48,229 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:48,230 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:01:48,233 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:48,236 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36543266002463065, Timeliness: nan
2024-08-05 23:01:48,237 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.51442200082103
2024-08-05 23:01:48,242 - metrics.computations.data_preparation - INFO - Data quality score: 45.51442200082103
2024-08-05 23:01:48,420 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 9, 'tenant_id': 5, 'project_id': 5, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.51442200082103, 'outliers_handled': True, 'profile': {'mean': 99.81602410659238, 'median': 99.71697116023687, 'std': 9.541590804904448, 'min': 77.9611021482892, 'max': 122.76749263830959, 'skewness': 0.06672942712752285, 'kurtosis': -0.43164642791855234, 'missing_percentage': 0.0}}
2024-08-05 23:01:48,421 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:01:48,422 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 9
2024-08-05 23:01:48,440 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=3, strength=0.00
2024-08-05 23:01:48,457 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=3, strength=0.00
2024-08-05 23:01:48,469 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 9
2024-08-05 23:01:48,473 - metrics.computations.feature_engineering - INFO - Parameters for metric 9: dynamic
2024-08-05 23:01:48,480 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 9: {'seasonality_period': 3, 'forecast_horizon': 3, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:01:48,485 - metrics.computations.data_preparation - INFO - Loaded metric 9 for tenant 5 and project 5
2024-08-05 23:01:48,485 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 9
2024-08-05 23:01:48,486 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:48,487 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:48,491 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 9
2024-08-05 23:01:48,499 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:48,500 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:01:48,504 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:48,505 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:48,509 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:48,509 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:01:48,514 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:01:51,206 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 9
2024-08-05 23:01:51,209 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:01:51,211 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:01:51,211 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:01:51,215 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:51,215 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:01:51,218 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:51,221 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36543266002463065, Timeliness: nan
2024-08-05 23:01:51,222 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.51442200082103
2024-08-05 23:01:51,227 - metrics.computations.data_preparation - INFO - Data quality score: 45.51442200082103
2024-08-05 23:01:51,277 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 9, 'tenant_id': 5, 'project_id': 5, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.51442200082103, 'outliers_handled': True, 'profile': {'mean': 99.81602410659238, 'median': 99.71697116023687, 'std': 9.541590804904448, 'min': 77.9611021482892, 'max': 122.76749263830959, 'skewness': 0.06672942712752285, 'kurtosis': -0.43164642791855234, 'missing_percentage': 0.0}}
2024-08-05 23:01:51,282 - metrics.computations.data_preparation - INFO - Loaded metric 9 for tenant 5 and project 5
2024-08-05 23:01:51,282 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 9
2024-08-05 23:01:51,283 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:51,284 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:01:51,288 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 9
2024-08-05 23:01:51,298 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:51,298 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:01:51,304 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:51,305 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:01:51,318 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:51,319 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:01:51,324 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:01:54,112 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 9
2024-08-05 23:01:54,116 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:01:54,118 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:01:54,119 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:01:54,122 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:54,123 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:01:54,126 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   89.105211          5
2023-01-02  107.736355          5
2023-01-03  102.809256          5
2023-01-04   98.306901          5
2023-01-05   99.102699          5
2024-08-05 23:01:54,129 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36543266002463065, Timeliness: nan
2024-08-05 23:01:54,129 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.51442200082103
2024-08-05 23:01:54,134 - metrics.computations.data_preparation - INFO - Data quality score: 45.51442200082103
2024-08-05 23:01:54,266 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 9, 'tenant_id': 5, 'project_id': 5, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.51442200082103, 'outliers_handled': True, 'profile': {'mean': 99.81602410659238, 'median': 99.71697116023687, 'std': 9.541590804904448, 'min': 77.9611021482892, 'max': 122.76749263830959, 'skewness': 0.06672942712752285, 'kurtosis': -0.43164642791855234, 'missing_percentage': 0.0}}
2024-08-05 23:01:54,267 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:01:54,267 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 9
2024-08-05 23:01:54,278 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=3, strength=0.00
2024-08-05 23:01:54,287 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=3, strength=0.00
2024-08-05 23:01:54,298 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 9
2024-08-05 23:01:54,299 - metrics.computations.feature_engineering - INFO - Parameters for metric 9: dynamic
2024-08-05 23:01:54,299 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 9: {'seasonality_period': 3, 'forecast_horizon': 3, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:01:54,301 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Setup completed
2024-08-05 23:01:54,459 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Teardown completed
```

## test_permanent_computations_robustness (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
Status: failure
Duration: 80.354 seconds

### Failure
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_permanent_computations_robustness.py", line 155, in test_permanent_computations_robustness
    self.assertTrue(Forecast.objects.filter(metric=self.metric1).exists())
AssertionError: False is not true
```

### Output
```
Starting setUp
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
  Applying sessions.0001_initial...
 OK
Initializing PermanentComputations with metric_ids: [11, 12]
Finished initializing PermanentComputations
Initializing DataPreparation for metric_id: 11
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 11
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 11
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 11
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 11
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 11
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 11
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 11
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 11
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 11
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 11
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 12
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 12
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 12
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 12
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 12
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 12
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 12
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/statsmodels/tsa/base/tsa_model.py:473: ValueWarning: No frequency information was provided, so inferred frequency D will be used.
  self._init_dates(dates, freq)
/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/statsmodels/tsa/base/tsa_model.py:473: ValueWarning: No frequency information was provided, so inferred frequency D will be used.
  self._init_dates(dates, freq)
23:02:36 - cmdstanpy - INFO - Chain [1] start processing
23:02:36 - cmdstanpy - INFO - Chain [1] done processing
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/statsmodels/tsa/base/tsa_model.py:473: ValueWarning: No frequency information was provided, so inferred frequency D will be used.
  self._init_dates(dates, freq)
/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/statsmodels/tsa/base/tsa_model.py:473: ValueWarning: No frequency information was provided, so inferred frequency D will be used.
  self._init_dates(dates, freq)
23:03:04 - cmdstanpy - INFO - Chain [1] start processing
23:03:04 - cmdstanpy - INFO - Chain [1] done processing
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
2024-08-05 23:01:54,481 - metrics - DEBUG - Starting test: test_permanent_computations_robustness (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
2024-08-05 23:01:54,488 - django.db.backends.schema - DEBUG - CREATE TABLE "django_migrations" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:54,510 - django.db.backends.schema - DEBUG - CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
2024-08-05 23:01:54,516 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params None)
2024-08-05 23:01:54,524 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL, "codename" varchar(100) NOT NULL); (params None)
2024-08-05 23:01:54,532 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(80) NOT NULL UNIQUE); (params None)
2024-08-05 23:01:54,540 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:01:54,550 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NOT NULL, "is_superuser" boolean NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:54,557 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:01:54,562 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:01:54,568 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename"); (params None)
2024-08-05 23:01:54,571 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:54,573 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id"); (params None)
2024-08-05 23:01:54,577 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_name_a6ea08ec_like" ON "auth_group" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:54,580 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id"); (params None)
2024-08-05 23:01:54,583 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:54,585 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:54,586 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id"); (params None)
2024-08-05 23:01:54,590 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id"); (params None)
2024-08-05 23:01:54,593 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_username_6821ab7c_like" ON "auth_user" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:01:54,596 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id"); (params None)
2024-08-05 23:01:54,599 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:54,601 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:54,602 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id"); (params None)
2024-08-05 23:01:54,606 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id"); (params None)
2024-08-05 23:01:54,609 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id"); (params None)
2024-08-05 23:01:54,612 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:54,614 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:54,615 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id"); (params None)
2024-08-05 23:01:54,620 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id"); (params None)
2024-08-05 23:01:54,633 - django.db.backends.schema - DEBUG - CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "action_time" timestamp with time zone NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL, "user_id" integer NOT NULL); (params None)
2024-08-05 23:01:54,641 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:54,643 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:54,644 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id"); (params None)
2024-08-05 23:01:54,648 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id"); (params None)
2024-08-05 23:01:54,677 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ALTER COLUMN "name" DROP NOT NULL; (params None)
2024-08-05 23:01:54,685 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" DROP COLUMN "name" CASCADE; (params None)
2024-08-05 23:01:54,701 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ALTER COLUMN "name" TYPE varchar(255); (params None)
2024-08-05 23:01:54,711 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "email" TYPE varchar(254); (params None)
2024-08-05 23:01:54,727 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_login" DROP NOT NULL; (params None)
2024-08-05 23:01:54,747 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "username" TYPE varchar(150); (params None)
2024-08-05 23:01:54,762 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_name" TYPE varchar(150); (params None)
2024-08-05 23:01:54,772 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group" ALTER COLUMN "name" TYPE varchar(150); (params None)
2024-08-05 23:01:54,798 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "first_name" TYPE varchar(150); (params None)
2024-08-05 23:01:54,839 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_client" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "schema_name" varchar(63) NOT NULL UNIQUE, "name" varchar(100) NOT NULL, "created_on" date NOT NULL); (params None)
2024-08-05 23:01:54,849 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_category" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:54,857 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dashboard" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "layout" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:54,868 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_domain" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "domain" varchar(253) NOT NULL UNIQUE, "is_primary" boolean NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:54,886 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "type" varchar(50) NOT NULL, "confidence" varchar(50) NOT NULL, "value_type" varchar(20) NOT NULL, "rhythm" varchar(20) NOT NULL, "description" text NOT NULL, "hypothesis" text NOT NULL, "technical_description" text NOT NULL, "last_updated" timestamp with time zone NOT NULL, "source" varchar(100) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL, "category_id" bigint NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:54,900 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_historicaldata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "value" double precision NOT NULL, "forecasted_value" double precision NULL, "anomaly_detected" boolean NOT NULL, "trend_component" varchar(50) NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:54,911 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_forecast" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "forecast_date" date NOT NULL, "forecast_value" double precision NOT NULL, "model_used" varchar(100) NOT NULL, "accuracy" double precision NULL, "confidence_interval" jsonb NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:54,927 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "status" varchar(50) NOT NULL, "results" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:54,935 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment_metrics" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "experiment_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:54,949 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_connection" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "relationship" varchar(100) NOT NULL, "correlation_coefficient" double precision NULL, "tenant_id" bigint NOT NULL, "from_metric_id" bigint NOT NULL, "to_metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:54,964 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_anomaly" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "detection_date" date NOT NULL, "anomaly_value" double precision NOT NULL, "anomaly_score" double precision NOT NULL, "notes" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:54,980 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_actionremark" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NULL, "description" text NOT NULL, "impact" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:01:55,003 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_project" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "created_on" date NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:55,024 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_report" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "configuration" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:55,041 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tag" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "project_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:55,060 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric_tags" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "metric_id" bigint NOT NULL, "tag_id" bigint NOT NULL); (params None)
2024-08-05 23:01:55,080 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_target" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "remarks" text NOT NULL, "target_kpi" varchar(100) NOT NULL, "target_date" date NULL, "target_value" double precision NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:55,101 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trend" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "trend_type" varchar(50) NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "trend_value" double precision NOT NULL, "notes" text NOT NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:01:55,109 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_schema_name_87d6fbb5_like" ON "metrics_client" ("schema_name" varchar_pattern_ops); (params None)
2024-08-05 23:01:55,112 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_category" ADD CONSTRAINT "metrics_category_tenant_id_67d98cc6_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,114 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_tenant_id_67d98cc6" ON "metrics_category" ("tenant_id"); (params None)
2024-08-05 23:01:55,117 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ADD CONSTRAINT "metrics_dashboard_tenant_id_50099a7d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,118 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_tenant_id_50099a7d" ON "metrics_dashboard" ("tenant_id"); (params None)
2024-08-05 23:01:55,122 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_domain" ADD CONSTRAINT "metrics_domain_tenant_id_259fb21f_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,124 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_domain_bdc97b86_like" ON "metrics_domain" ("domain" varchar_pattern_ops); (params None)
2024-08-05 23:01:55,128 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_is_primary_ac9d2eaf" ON "metrics_domain" ("is_primary"); (params None)
2024-08-05 23:01:55,131 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_tenant_id_259fb21f" ON "metrics_domain" ("tenant_id"); (params None)
2024-08-05 23:01:55,136 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_category_id_8793f683_fk_metrics_category_id" FOREIGN KEY ("category_id") REFERENCES "metrics_category" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,138 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_9606b577_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,140 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_category_id_8793f683" ON "metrics_metric" ("category_id"); (params None)
2024-08-05 23:01:55,143 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tenant_id_9606b577" ON "metrics_metric" ("tenant_id"); (params None)
2024-08-05 23:01:55,147 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_tenant_id_438c5ad4_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,148 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_metric_id_3f9e8174_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,149 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_tenant_id_438c5ad4" ON "metrics_historicaldata" ("tenant_id"); (params None)
2024-08-05 23:01:55,153 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_metric_id_3f9e8174" ON "metrics_historicaldata" ("metric_id"); (params None)
2024-08-05 23:01:55,156 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_tenant_id_92d37185_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,157 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_metric_id_e05f23a8_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,158 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_tenant_id_92d37185" ON "metrics_forecast" ("tenant_id"); (params None)
2024-08-05 23:01:55,162 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_metric_id_e05f23a8" ON "metrics_forecast" ("metric_id"); (params None)
2024-08-05 23:01:55,166 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD CONSTRAINT "metrics_experiment_tenant_id_10fa364a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,168 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_tenant_id_10fa364a" ON "metrics_experiment" ("tenant_id"); (params None)
2024-08-05 23:01:55,171 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_metri_experiment_id_metric_id_a9d54b29_uniq" UNIQUE ("experiment_id", "metric_id"); (params None)
2024-08-05 23:01:55,175 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_experiment_id_372c6b59_fk_metrics_e" FOREIGN KEY ("experiment_id") REFERENCES "metrics_experiment" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,178 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_metric_id_c8f84167_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,179 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_experiment_id_372c6b59" ON "metrics_experiment_metrics" ("experiment_id"); (params None)
2024-08-05 23:01:55,182 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_metric_id_c8f84167" ON "metrics_experiment_metrics" ("metric_id"); (params None)
2024-08-05 23:01:55,184 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_2e1e5750_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,186 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_from_metric_id_33b50521_fk_metrics_metric_id" FOREIGN KEY ("from_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,187 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_to_metric_id_94489c1c_fk_metrics_metric_id" FOREIGN KEY ("to_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,189 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_tenant_id_2e1e5750" ON "metrics_connection" ("tenant_id"); (params None)
2024-08-05 23:01:55,193 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_from_metric_id_33b50521" ON "metrics_connection" ("from_metric_id"); (params None)
2024-08-05 23:01:55,196 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_to_metric_id_94489c1c" ON "metrics_connection" ("to_metric_id"); (params None)
2024-08-05 23:01:55,200 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_tenant_id_9e474130_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,202 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_metric_id_1b3c3295_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,203 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_tenant_id_9e474130" ON "metrics_anomaly" ("tenant_id"); (params None)
2024-08-05 23:01:55,206 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_metric_id_1b3c3295" ON "metrics_anomaly" ("metric_id"); (params None)
2024-08-05 23:01:55,210 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_tenant_id_86ffa3a9_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,212 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_metric_id_c1b270f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,214 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_tenant_id_86ffa3a9" ON "metrics_actionremark" ("tenant_id"); (params None)
2024-08-05 23:01:55,218 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_metric_id_c1b270f2" ON "metrics_actionremark" ("metric_id"); (params None)
2024-08-05 23:01:55,221 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_project" ADD CONSTRAINT "metrics_project_tenant_id_db4a1170_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,223 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_tenant_id_db4a1170" ON "metrics_project" ("tenant_id"); (params None)
2024-08-05 23:01:55,226 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD CONSTRAINT "metrics_report_tenant_id_d1cf4812_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,228 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_tenant_id_d1cf4812" ON "metrics_report" ("tenant_id"); (params None)
2024-08-05 23:01:55,232 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_name_project_id_2d57d4da_uniq" UNIQUE ("name", "project_id"); (params None)
2024-08-05 23:01:55,235 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_project_id_b7ac5c8e_fk_metrics_project_id" FOREIGN KEY ("project_id") REFERENCES "metrics_project" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,237 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_tenant_id_c286653b_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,238 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_project_id_b7ac5c8e" ON "metrics_tag" ("project_id"); (params None)
2024-08-05 23:01:55,243 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_tenant_id_c286653b" ON "metrics_tag" ("tenant_id"); (params None)
2024-08-05 23:01:55,247 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_tag_id_a8e1a165_uniq" UNIQUE ("metric_id", "tag_id"); (params None)
2024-08-05 23:01:55,250 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_b2a068f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,252 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_tag_id_61869f56_fk_metrics_tag_id" FOREIGN KEY ("tag_id") REFERENCES "metrics_tag" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,253 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_metric_id_b2a068f2" ON "metrics_metric_tags" ("metric_id"); (params None)
2024-08-05 23:01:55,257 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_tag_id_61869f56" ON "metrics_metric_tags" ("tag_id"); (params None)
2024-08-05 23:01:55,261 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,263 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,264 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_metric_id_181e8748" ON "metrics_target" ("metric_id"); (params None)
2024-08-05 23:01:55,268 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_tenant_id_118eb54a" ON "metrics_target" ("tenant_id"); (params None)
2024-08-05 23:01:55,272 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_metric_id_25179b98_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,274 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_tenant_id_4cb1485d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:55,275 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_metric_id_25179b98" ON "metrics_trend" ("metric_id"); (params None)
2024-08-05 23:01:55,278 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_tenant_id_4cb1485d" ON "metrics_trend" ("tenant_id"); (params None)
2024-08-05 23:01:55,485 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_date_33d1e0bd" ON "metrics_actionremark" ("date"); (params None)
2024-08-05 23:01:55,500 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_detection_date_ee75a187" ON "metrics_anomaly" ("detection_date"); (params None)
2024-08-05 23:01:55,517 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c" ON "metrics_category" ("name"); (params None)
2024-08-05 23:01:55,521 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c_like" ON "metrics_category" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:55,538 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d" ON "metrics_client" ("name"); (params None)
2024-08-05 23:01:55,542 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d_like" ON "metrics_client" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:55,889 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET DEFAULT '{}'; (params None)
2024-08-05 23:01:55,890 - django.db.backends.schema - DEBUG - UPDATE "metrics_dashboard" SET "layout" = '{}' WHERE "layout" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:01:55,891 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET NOT NULL; (params None)
2024-08-05 23:01:55,892 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" DROP DEFAULT; (params None)
2024-08-05 23:01:55,904 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e" ON "metrics_dashboard" ("name"); (params None)
2024-08-05 23:01:55,909 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e_like" ON "metrics_dashboard" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:55,931 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_end_date_31af6c05" ON "metrics_experiment" ("end_date"); (params None)
2024-08-05 23:01:55,946 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7" ON "metrics_experiment" ("name"); (params None)
2024-08-05 23:01:55,951 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7_like" ON "metrics_experiment" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:55,971 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET DEFAULT '{}'; (params None)
2024-08-05 23:01:55,972 - django.db.backends.schema - DEBUG - UPDATE "metrics_experiment" SET "results" = '{}' WHERE "results" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:01:55,973 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET NOT NULL; (params None)
2024-08-05 23:01:55,974 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" DROP DEFAULT; (params None)
2024-08-05 23:01:55,987 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_start_date_a6deff13" ON "metrics_experiment" ("start_date"); (params None)
2024-08-05 23:01:56,004 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET DEFAULT '{}'; (params None)
2024-08-05 23:01:56,005 - django.db.backends.schema - DEBUG - UPDATE "metrics_forecast" SET "confidence_interval" = '{}' WHERE "confidence_interval" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:01:56,006 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET NOT NULL; (params None)
2024-08-05 23:01:56,007 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" DROP DEFAULT; (params None)
2024-08-05 23:01:56,025 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_forecast_date_71750ae8" ON "metrics_forecast" ("forecast_date"); (params None)
2024-08-05 23:01:56,044 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_date_f27e0e6a" ON "metrics_historicaldata" ("date"); (params None)
2024-08-05 23:01:56,063 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_last_updated_3e38a760" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:01:56,082 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5" ON "metrics_metric" ("name"); (params None)
2024-08-05 23:01:56,086 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5_like" ON "metrics_metric" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:56,106 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e" ON "metrics_metric" ("type"); (params None)
2024-08-05 23:01:56,110 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e_like" ON "metrics_metric" ("type" varchar_pattern_ops); (params None)
2024-08-05 23:01:56,139 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80" ON "metrics_project" ("name"); (params None)
2024-08-05 23:01:56,144 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80_like" ON "metrics_project" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:56,162 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET DEFAULT '{}'; (params None)
2024-08-05 23:01:56,163 - django.db.backends.schema - DEBUG - UPDATE "metrics_report" SET "configuration" = '{}' WHERE "configuration" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:01:56,164 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET NOT NULL; (params None)
2024-08-05 23:01:56,165 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" DROP DEFAULT; (params None)
2024-08-05 23:01:56,181 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34" ON "metrics_report" ("name"); (params None)
2024-08-05 23:01:56,184 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34_like" ON "metrics_report" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:56,200 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a" ON "metrics_tag" ("name"); (params None)
2024-08-05 23:01:56,204 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a_like" ON "metrics_tag" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:01:56,220 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_target_date_81507ff5" ON "metrics_target" ("target_date"); (params None)
2024-08-05 23:01:56,240 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_end_date_8444ef38" ON "metrics_trend" ("end_date"); (params None)
2024-08-05 23:01:56,257 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_start_date_7b1a850f" ON "metrics_trend" ("start_date"); (params None)
2024-08-05 23:01:56,274 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_act_metric__be3429_idx" ON "metrics_actionremark" ("metric_id", "date"); (params None)
2024-08-05 23:01:56,291 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ano_metric__84982d_idx" ON "metrics_anomaly" ("metric_id", "detection_date"); (params None)
2024-08-05 23:01:56,309 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_con_from_me_9411ea_idx" ON "metrics_connection" ("from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:01:56,325 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_exp_start_d_04716a_idx" ON "metrics_experiment" ("start_date", "end_date"); (params None)
2024-08-05 23:01:56,341 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_for_metric__4c9ae2_idx" ON "metrics_forecast" ("metric_id", "forecast_date"); (params None)
2024-08-05 23:01:56,364 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_his_metric__a2923a_idx" ON "metrics_historicaldata" ("metric_id", "date"); (params None)
2024-08-05 23:01:56,382 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_name_c9d100_idx" ON "metrics_metric" ("name", "type"); (params None)
2024-08-05 23:01:56,402 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_7984a6_idx" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:01:56,421 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1bdb27_idx" ON "metrics_tag" ("name", "project_id"); (params None)
2024-08-05 23:01:56,439 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tar_metric__234682_idx" ON "metrics_target" ("metric_id", "target_date"); (params None)
2024-08-05 23:01:56,457 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tre_metric__d386bb_idx" ON "metrics_trend" ("metric_id", "start_date", "end_date"); (params None)
2024-08-05 23:01:56,477 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_con_from_me_9411ea_idx"; (params None)
2024-08-05 23:01:56,494 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:01:56,497 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:01:56,512 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_from_metric_id_aa131d91_uniq" UNIQUE ("tenant_id", "from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:01:56,516 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_project_id_4c1b22ec" ON "metrics_connection" ("project_id"); (params None)
2024-08-05 23:01:56,540 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; ALTER TABLE "metrics_connection" DROP CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id"; (params None)
2024-08-05 23:01:56,542 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "project_id" CASCADE; (params None)
2024-08-05 23:01:56,559 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:01:56,561 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:01:56,578 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:01:56,583 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_project_id_36bdbe46" ON "metrics_metric" ("project_id"); (params None)
2024-08-05 23:01:56,589 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_correlation" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "lag" integer NOT NULL, "pearson_correlation" double precision NOT NULL, "spearman_correlation" double precision NOT NULL); (params None)
2024-08-05 23:01:56,597 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:56,607 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dataqualityscore" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_entry" varchar(255) NOT NULL, "completeness_score" double precision NOT NULL, "accuracy_score" double precision NOT NULL, "consistency_score" double precision NOT NULL, "timeliness_score" double precision NOT NULL, "overall_score" double precision NOT NULL); (params None)
2024-08-05 23:01:56,614 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_impactanalysis" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "before_value" double precision NOT NULL, "after_value" double precision NOT NULL, "percentage_change" double precision NOT NULL, "confidence" double precision NOT NULL, "artifact_link" varchar(200) NOT NULL); (params None)
2024-08-05 23:01:56,621 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_insight" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "title" varchar(200) NOT NULL, "content" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:56,629 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metricmetadata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_source" varchar(100) NOT NULL, "source_url" varchar(200) NOT NULL, "rhythm" varchar(20) NOT NULL, "last_updated" timestamp with time zone NOT NULL, "technical_description" text NOT NULL, "description" text NOT NULL, "artifacts_url" varchar(200) NOT NULL, "hypothesis" text NOT NULL, "confidence" varchar(20) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL); (params None)
2024-08-05 23:01:56,639 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metrictarget" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "target_kpi" varchar(100) NOT NULL, "target_remarks" text NOT NULL, "target_date" date NULL, "target_value" double precision NULL); (params None)
2024-08-05 23:01:56,648 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_strategy" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "estimated_time" interval NOT NULL, "artifacts_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:56,657 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tacticalsolution" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "artifact_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:56,666 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_team" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:01:56,676 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_technicalindicator" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "stochastic_value" double precision NOT NULL, "rsi_value" double precision NOT NULL, "percent_change" double precision NOT NULL, "moving_average" double precision NOT NULL); (params None)
2024-08-05 23:01:56,683 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_timedimension" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL UNIQUE, "day" integer NOT NULL, "day_of_week" integer NOT NULL, "day_name" varchar(10) NOT NULL, "week" integer NOT NULL, "month" integer NOT NULL, "month_name" varchar(10) NOT NULL, "quarter" integer NOT NULL, "year" integer NOT NULL, "is_weekend" boolean NOT NULL, "is_holiday" boolean NOT NULL); (params None)
2024-08-05 23:01:56,692 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_userprofile" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY); (params None)
2024-08-05 23:01:56,714 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_metric_id_181e8748_fk_metrics_metric_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id"; (params None)
2024-08-05 23:01:56,715 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "metric_id" CASCADE; (params None)
2024-08-05 23:01:56,737 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id"; (params None)
2024-08-05 23:01:56,739 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:01:56,756 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_name_c9d100_idx"; (params None)
2024-08-05 23:01:56,771 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_last_up_7984a6_idx"; (params None)
2024-08-05 23:01:56,784 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" RENAME COLUMN "description" TO "summary"; (params None)
2024-08-05 23:01:56,805 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq"; (params None)
2024-08-05 23:01:56,818 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "correlation_coefficient" CASCADE; (params None)
2024-08-05 23:01:56,832 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" DROP COLUMN "results" CASCADE; (params None)
2024-08-05 23:01:56,849 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "anomaly_detected" CASCADE; (params None)
2024-08-05 23:01:56,863 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "forecasted_value" CASCADE; (params None)
2024-08-05 23:01:56,876 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "trend_component" CASCADE; (params None)
2024-08-05 23:01:56,890 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "importance" varchar(20) DEFAULT 'MEDIUM' NOT NULL; (params None)
2024-08-05 23:01:56,891 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "importance" DROP DEFAULT; (params None)
2024-08-05 23:01:56,910 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:01:56.909410+00:00' NOT NULL; (params None)
2024-08-05 23:01:56,911 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:01:56,925 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "anomaly_type" varchar(20) DEFAULT 'IGNORE' NOT NULL; (params None)
2024-08-05 23:01:56,926 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "anomaly_type" DROP DEFAULT; (params None)
2024-08-05 23:01:56,941 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "quality" varchar(20) DEFAULT 'LOW' NOT NULL; (params None)
2024-08-05 23:01:56,943 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "quality" DROP DEFAULT; (params None)
2024-08-05 23:01:56,957 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "impact_description" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:01:56,959 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "impact_description" DROP DEFAULT; (params None)
2024-08-05 23:01:56,976 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "objective" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:01:56,978 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "objective" DROP DEFAULT; (params None)
2024-08-05 23:01:56,993 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_date" date NULL; (params None)
2024-08-05 23:01:57,007 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_files" varchar(100) NULL; (params None)
2024-08-05 23:01:57,024 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_summary" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:01:57,026 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "result_summary" DROP DEFAULT; (params None)
2024-08-05 23:01:57,041 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_value" double precision NULL; (params None)
2024-08-05 23:01:57,057 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:01:57.056431+00:00' NOT NULL; (params None)
2024-08-05 23:01:57,058 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:01:57,072 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "variance" double precision NULL; (params None)
2024-08-05 23:01:57,089 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD COLUMN "forecast_id" bigint NULL CONSTRAINT "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" REFERENCES "metrics_forecast"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" IMMEDIATE; (params None)
2024-08-05 23:01:57,104 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "impact" TYPE varchar(20) USING "impact"::varchar(20); (params None)
2024-08-05 23:01:57,219 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "status" TYPE varchar(20); (params None)
2024-08-05 23:01:57,716 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric1_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:57,736 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric2_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:57,752 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:57,765 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:01:57,796 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:57,820 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:01:57,850 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:57,874 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "experiment_id" bigint NOT NULL CONSTRAINT "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" REFERENCES "metrics_experiment"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" IMMEDIATE; (params None)
2024-08-05 23:01:57,899 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:57,927 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:57,952 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:57,982 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,009 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "user_id" bigint NOT NULL CONSTRAINT "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,038 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "data_quality_score_id" bigint NULL UNIQUE CONSTRAINT "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" REFERENCES "metrics_dataqualityscore"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" IMMEDIATE; (params None)
2024-08-05 23:01:58,068 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "metric_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,097 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,129 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,158 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,187 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,216 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:01:58,254 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:58,617 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_team" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,647 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "team_id" bigint NOT NULL CONSTRAINT "metrics_strategy_team_id_f1781500_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_team_id_f1781500_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,680 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,710 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,740 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_experiment_team_id_537107e3_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_experiment_team_id_537107e3_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,774 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:01:58,804 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:01:58,836 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_timedimension" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,867 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,901 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "user_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:01:58,908 - django.db.backends.schema - DEBUG - DROP TABLE "metrics_target" CASCADE; (params None)
2024-08-05 23:01:58,934 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "confidence" CASCADE; (params None)
2024-08-05 23:01:58,961 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "description" CASCADE; (params None)
2024-08-05 23:01:58,986 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "hypothesis" CASCADE; (params None)
2024-08-05 23:01:59,016 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "last_updated" CASCADE; (params None)
2024-08-05 23:01:59,046 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_x" CASCADE; (params None)
2024-08-05 23:01:59,072 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_y" CASCADE; (params None)
2024-08-05 23:01:59,099 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "rhythm" CASCADE; (params None)
2024-08-05 23:01:59,122 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "source" CASCADE; (params None)
2024-08-05 23:01:59,472 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "technical_description" CASCADE; (params None)
2024-08-05 23:01:59,494 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD CONSTRAINT "metrics_correlation_tenant_id_metric1_id_met_49a4c34a_uniq" UNIQUE ("tenant_id", "metric1_id", "metric2_id", "lag"); (params None)
2024-08-05 23:01:59,525 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_metric__b85d3a_idx" ON "metrics_insight" ("metric_id", "date"); (params None)
2024-08-05 23:01:59,559 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_user_id_1ebb42_idx" ON "metrics_insight" ("user_id", "date"); (params None)
2024-08-05 23:01:59,587 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_metric__a2b705_idx" ON "metrics_metrictarget" ("metric_id", "target_date"); (params None)
2024-08-05 23:01:59,617 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_6e2e67_idx" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:01:59,644 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_date_53cb14_idx" ON "metrics_timedimension" ("date"); (params None)
2024-08-05 23:01:59,680 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_year_92da9e_idx" ON "metrics_timedimension" ("year", "month", "day"); (params None)
2024-08-05 23:01:59,686 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_username_6e55f358_like" ON "metrics_customuser" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:01:59,691 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_date_ded95ba1" ON "metrics_insight" ("date"); (params None)
2024-08-05 23:01:59,695 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_last_updated_76599a1b" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:01:59,698 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_target_date_38cd9191" ON "metrics_metrictarget" ("target_date"); (params None)
2024-08-05 23:01:59,702 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_forecast_id_29590c29" ON "metrics_historicaldata" ("forecast_id"); (params None)
2024-08-05 23:01:59,707 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric1_id_6e1c2404" ON "metrics_correlation" ("metric1_id"); (params None)
2024-08-05 23:01:59,710 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric2_id_f2cc46dd" ON "metrics_correlation" ("metric2_id"); (params None)
2024-08-05 23:01:59,714 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_tenant_id_a00a5169" ON "metrics_correlation" ("tenant_id"); (params None)
2024-08-05 23:01:59,718 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_customuser_id_group_id_1c5fc435_uniq" UNIQUE ("customuser_id", "group_id"); (params None)
2024-08-05 23:01:59,722 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_g_customuser_id_fc13f3af_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:59,724 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_group_id_6b097e12_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:59,725 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_customuser_id_fc13f3af" ON "metrics_customuser_groups" ("customuser_id"); (params None)
2024-08-05 23:01:59,731 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_group_id_6b097e12" ON "metrics_customuser_groups" ("group_id"); (params None)
2024-08-05 23:01:59,735 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_tenant_id_02b7403c" ON "metrics_customuser" ("tenant_id"); (params None)
2024-08-05 23:01:59,738 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_user__customuser_id_permission_68cc320f_uniq" UNIQUE ("customuser_id", "permission_id"); (params None)
2024-08-05 23:01:59,742 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_customuser_id_46e97f00_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:59,745 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_permission_id_d66d657c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:01:59,747 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_customuser_id_46e97f00" ON "metrics_customuser_user_permissions" ("customuser_id"); (params None)
2024-08-05 23:01:59,751 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_permission_id_d66d657c" ON "metrics_customuser_user_permissions" ("permission_id"); (params None)
2024-08-05 23:01:59,755 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_tenant_id_8e9f296d" ON "metrics_dataqualityscore" ("tenant_id"); (params None)
2024-08-05 23:01:59,759 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_experiment_id_1beae7fe" ON "metrics_impactanalysis" ("experiment_id"); (params None)
2024-08-05 23:01:59,763 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_metric_id_f4b9eeb6" ON "metrics_impactanalysis" ("metric_id"); (params None)
2024-08-05 23:01:59,766 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_tenant_id_126ca20d" ON "metrics_impactanalysis" ("tenant_id"); (params None)
2024-08-05 23:01:59,771 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_metric_id_26d3a9d8" ON "metrics_insight" ("metric_id"); (params None)
2024-08-05 23:01:59,774 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_tenant_id_724d7d85" ON "metrics_insight" ("tenant_id"); (params None)
2024-08-05 23:01:59,778 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_user_id_83d421e1" ON "metrics_insight" ("user_id"); (params None)
2024-08-05 23:01:59,781 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_tenant_id_3277f967" ON "metrics_metricmetadata" ("tenant_id"); (params None)
2024-08-05 23:01:59,785 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_metric_id_7876e2c8" ON "metrics_metrictarget" ("metric_id"); (params None)
2024-08-05 23:01:59,789 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_tenant_id_b26a17f8" ON "metrics_metrictarget" ("tenant_id"); (params None)
2024-08-05 23:01:59,791 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_tenant_id_1323395e" ON "metrics_strategy" ("tenant_id"); (params None)
2024-08-05 23:01:59,794 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_metric_id_9887ffa4" ON "metrics_tacticalsolution" ("metric_id"); (params None)
2024-08-05 23:01:59,798 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_tenant_id_cf9028f0" ON "metrics_tacticalsolution" ("tenant_id"); (params None)
2024-08-05 23:01:59,802 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_team_tenant_id_3a14c47d" ON "metrics_team" ("tenant_id"); (params None)
2024-08-05 23:01:59,805 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_team_id_f1781500" ON "metrics_strategy" ("team_id"); (params None)
2024-08-05 23:01:59,808 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_team_id_f140658d" ON "metrics_metricmetadata" ("team_id"); (params None)
2024-08-05 23:01:59,813 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_team_id_4c4ffc18" ON "metrics_customuser" ("team_id"); (params None)
2024-08-05 23:01:59,818 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_team_id_537107e3" ON "metrics_experiment" ("team_id"); (params None)
2024-08-05 23:01:59,821 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_metric_id_3e2eead6" ON "metrics_technicalindicator" ("metric_id"); (params None)
2024-08-05 23:01:59,824 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_tenant_id_f4de3b44" ON "metrics_technicalindicator" ("tenant_id"); (params None)
2024-08-05 23:01:59,828 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_timedimension_tenant_id_f375bb45" ON "metrics_timedimension" ("tenant_id"); (params None)
2024-08-05 23:01:59,831 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_userprofile_tenant_id_cca71dae" ON "metrics_userprofile" ("tenant_id"); (params None)
2024-08-05 23:01:59,861 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "strength" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:01:59,863 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "strength" DROP DEFAULT; (params None)
2024-08-05 23:01:59,887 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "lower_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:01:59,888 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "lower_bound" DROP DEFAULT; (params None)
2024-08-05 23:01:59,917 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "upper_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:01:59,918 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "upper_bound" DROP DEFAULT; (params None)
2024-08-05 23:01:59,941 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD COLUMN "slope" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:01:59,942 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ALTER COLUMN "slope" DROP DEFAULT; (params None)
2024-08-05 23:01:59,978 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_movingaverage" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "ma_type" varchar(10) NOT NULL, "period" integer NOT NULL, "value" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:02:00,014 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_networkanalysisresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "analysis_type" varchar(20) NOT NULL, "result" jsonb NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:02:00,055 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_seasonalityresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "seasonality_type" varchar(20) NOT NULL, "strength" double precision NOT NULL, "period" integer NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:02:00,089 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trendchangepoint" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "change_type" varchar(20) NOT NULL, "significance" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:02:00,094 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD CONSTRAINT "metrics_movingaverage_metric_id_7c61cebf_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:02:00,097 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_metric_id_7c61cebf" ON "metrics_movingaverage" ("metric_id"); (params None)
2024-08-05 23:02:00,100 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD CONSTRAINT "metrics_networkanaly_metric_id_a4c90102_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:02:00,102 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_metric_id_a4c90102" ON "metrics_networkanalysisresult" ("metric_id"); (params None)
2024-08-05 23:02:00,106 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityr_metric_id_6e494791_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:02:00,108 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_metric_id_6e494791" ON "metrics_seasonalityresult" ("metric_id"); (params None)
2024-08-05 23:02:00,111 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD CONSTRAINT "metrics_trendchangep_metric_id_f8eb9f76_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:02:00,113 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_metric_id_f8eb9f76" ON "metrics_trendchangepoint" ("metric_id"); (params None)
2024-08-05 23:02:00,150 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:02:00,152 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:02:00,190 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" IMMEDIATE; (params None)
2024-08-05 23:02:00,193 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:02:00,538 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ALTER COLUMN "value" DROP NOT NULL; (params None)
2024-08-05 23:02:00,563 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD CONSTRAINT "metrics_dataqualityscore_tenant_id_metric_id_proj_66b9fb01_uniq" UNIQUE ("tenant_id", "metric_id", "project_id"); (params None)
2024-08-05 23:02:00,568 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_metric_id_1b6367d1" ON "metrics_dataqualityscore" ("metric_id"); (params None)
2024-08-05 23:02:00,572 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_project_id_123a4f58" ON "metrics_dataqualityscore" ("project_id"); (params None)
2024-08-05 23:02:00,606 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:02:00,649 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:02:00,651 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:02:00,685 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:02:00,687 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:02:00,720 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:02:00,722 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:02:00,762 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:02:00,764 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:02:00,792 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq" UNIQUE ("tenant_id", "metric_id"); (params None)
2024-08-05 23:02:00,796 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_tenant_id_5a9de228" ON "metrics_movingaverage" ("tenant_id"); (params None)
2024-08-05 23:02:00,800 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_tenant_id_16a6ba09" ON "metrics_networkanalysisresult" ("tenant_id"); (params None)
2024-08-05 23:02:00,803 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_tenant_id_ca2da3fd" ON "metrics_seasonalityresult" ("tenant_id"); (params None)
2024-08-05 23:02:00,806 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_tenant_id_da10d898" ON "metrics_trendchangepoint" ("tenant_id"); (params None)
2024-08-05 23:02:00,848 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:02:00,851 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:02:00,852 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_metric_id_c86f5720" ON "metrics_report" ("metric_id"); (params None)
2024-08-05 23:02:00,885 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "analysis_result" jsonb NULL; (params None)
2024-08-05 23:02:00,914 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "anomaly_result" jsonb NULL; (params None)
2024-08-05 23:02:00,943 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:02:00.942646+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:02:00,944 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:02:00,971 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "forecast_result" jsonb NULL; (params None)
2024-08-05 23:02:01,002 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "relationship_result" jsonb NULL; (params None)
2024-08-05 23:02:01,030 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "report" text DEFAULT '1' NOT NULL; (params None)
2024-08-05 23:02:01,031 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "report" DROP DEFAULT; (params None)
2024-08-05 23:02:01,058 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "updated_at" timestamp with time zone DEFAULT '2024-08-05T23:02:01.057486+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:02:01,059 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "updated_at" DROP DEFAULT; (params None)
2024-08-05 23:02:01,473 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_trendchangepoint" DROP CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c"; (params None)
2024-08-05 23:02:01,475 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:02:01,499 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "significance" DROP NOT NULL; (params None)
2024-08-05 23:02:01,526 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" RENAME COLUMN "change_type" TO "direction"; (params None)
2024-08-05 23:02:01,582 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:02:01.581726+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:02:01,583 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:02:01,617 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq"; (params None)
2024-08-05 23:02:01,618 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresul_metric_id_seasonality_ty_d3492b78_uniq" UNIQUE ("metric_id", "seasonality_type"); (params None)
2024-08-05 23:02:01,660 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c"; (params None)
2024-08-05 23:02:01,662 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:02:01,666 - django.db.backends.schema - DEBUG - CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:02:01,674 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" ("session_key" varchar_pattern_ops); (params None)
2024-08-05 23:02:01,678 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date"); (params None)
2024-08-05 23:02:02,874 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:02:02,875 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:02:02,876 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:02,877 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:02,879 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:02:02,886 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:02,886 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:02,891 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:02,891 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:02,894 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:02,894 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:02,898 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:05,624 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:02:05,627 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:05,629 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:05,630 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:05,633 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:05,634 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:05,637 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:05,640 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:05,640 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:05,646 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:05,711 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 99.74387876437025, 'median': 99.66084084075082, 'std': 9.614150928926504, 'min': 77.06130887774056, 'max': 121.73660789777128, 'skewness': -0.02920782406806899, 'kurtosis': -0.3440381333179605, 'missing_percentage': 0.0}}
2024-08-05 23:02:05,724 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:02:05,725 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:02:05,726 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:05,726 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:05,728 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:02:05,739 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:05,740 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:05,745 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:05,746 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:05,750 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:05,751 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:05,755 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:08,453 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:02:08,456 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:08,458 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:08,459 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:08,462 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:08,462 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:08,466 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:08,469 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:08,469 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:08,474 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:08,544 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 99.74387876437025, 'median': 99.66084084075082, 'std': 9.614150928926504, 'min': 77.06130887774056, 'max': 121.73660789777128, 'skewness': -0.02920782406806899, 'kurtosis': -0.3440381333179605, 'missing_percentage': 0.0}}
2024-08-05 23:02:08,544 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:02:08,544 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 11
2024-08-05 23:02:08,562 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:02:08,570 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:02:08,583 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 11
2024-08-05 23:02:08,584 - metrics.computations.feature_engineering - INFO - Parameters for metric 11: dynamic
2024-08-05 23:02:08,584 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 11: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:02:08,588 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:02:08,589 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:02:08,591 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:08,591 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:08,596 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:02:08,606 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:08,607 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:08,612 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:08,613 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:08,616 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:08,617 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:08,620 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:11,259 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:02:11,262 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:11,264 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:11,265 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:11,268 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:11,269 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:11,272 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:11,275 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:11,276 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:11,280 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:11,350 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 99.74387876437025, 'median': 99.66084084075082, 'std': 9.614150928926504, 'min': 77.06130887774056, 'max': 121.73660789777128, 'skewness': -0.02920782406806899, 'kurtosis': -0.3440381333179605, 'missing_percentage': 0.0}}
2024-08-05 23:02:11,361 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:02:11,362 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:02:11,363 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:11,365 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:11,371 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:02:11,383 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:11,384 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:11,389 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:11,392 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:11,395 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:11,397 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:11,402 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:14,095 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:02:14,099 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:14,101 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:14,101 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:14,104 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:14,105 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:14,108 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:14,111 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:14,111 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:14,116 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:14,203 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 99.74387876437025, 'median': 99.66084084075082, 'std': 9.614150928926504, 'min': 77.06130887774056, 'max': 121.73660789777128, 'skewness': -0.02920782406806899, 'kurtosis': -0.3440381333179605, 'missing_percentage': 0.0}}
2024-08-05 23:02:14,204 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:02:14,204 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 11
2024-08-05 23:02:14,216 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:02:14,222 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:02:14,230 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 11
2024-08-05 23:02:14,230 - metrics.computations.feature_engineering - INFO - Parameters for metric 11: dynamic
2024-08-05 23:02:14,230 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 11: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:02:14,233 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Setup completed
2024-08-05 23:02:14,233 - metrics.computations.permanent_computations - INFO - Starting all computations for metrics: [11, 12]
2024-08-05 23:02:14,233 - metrics.computations.permanent_computations - INFO - Starting computations for metric 11
2024-08-05 23:02:14,234 - metrics.computations.permanent_computations - INFO - Starting data preparation for metric 11
2024-08-05 23:02:14,235 - metrics.computations.permanent_computations - INFO - Starting data preparation for metric 11
2024-08-05 23:02:14,237 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:02:14,237 - metrics.computations.permanent_computations - INFO - DataPreparation object created: <metrics.computations.data_preparation.DataPreparation object at 0x7f0c850ffeb0>
2024-08-05 23:02:14,237 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:02:14,239 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:14,244 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:14,255 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:02:14,271 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:14,272 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:14,280 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:14,280 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:14,286 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:14,286 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:14,290 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:16,953 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:02:16,956 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:16,958 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:16,958 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:16,962 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:16,962 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:16,965 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:16,968 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:16,968 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:16,972 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:17,005 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 99.74387876437025, 'median': 99.66084084075082, 'std': 9.614150928926504, 'min': 77.06130887774056, 'max': 121.73660789777128, 'skewness': -0.02920782406806899, 'kurtosis': -0.3440381333179605, 'missing_percentage': 0.0}}
2024-08-05 23:02:17,006 - metrics.computations.permanent_computations - INFO - prepare_data() called, returned DataFrame of shape (1000, 2)
2024-08-05 23:02:17,006 - metrics.computations.permanent_computations - INFO - Data preparation statistics for metric 11:
2024-08-05 23:02:17,006 - metrics.computations.permanent_computations - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:17,006 - metrics.computations.permanent_computations - INFO - Number of data points: 1000
2024-08-05 23:02:17,006 - metrics.computations.permanent_computations - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:17,006 - metrics.computations.permanent_computations - INFO - Metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 99.74387876437025, 'median': 99.66084084075082, 'std': 9.614150928926504, 'min': 77.06130887774056, 'max': 121.73660789777128, 'skewness': -0.02920782406806899, 'kurtosis': -0.3440381333179605, 'missing_percentage': 0.0}}
2024-08-05 23:02:17,006 - metrics.computations.permanent_computations - INFO - Date range: 2023-01-01 00:00:00 to 2025-09-26 00:00:00
2024-08-05 23:02:17,006 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:02:17,007 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:17,008 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:17,017 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:02:17,027 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:17,032 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:17,039 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:17,040 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:17,043 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:17,044 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:17,049 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:19,810 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:02:19,813 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:19,815 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:19,816 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:19,819 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:19,820 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:19,823 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:19,826 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:19,826 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:19,831 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:20,040 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 99.74387876437025, 'median': 99.66084084075082, 'std': 9.614150928926504, 'min': 77.06130887774056, 'max': 121.73660789777128, 'skewness': -0.02920782406806899, 'kurtosis': -0.3440381333179605, 'missing_percentage': 0.0}}
2024-08-05 23:02:20,041 - metrics.computations.permanent_computations - INFO - Data preparation completed for metric 11
2024-08-05 23:02:20,041 - metrics.computations.permanent_computations - INFO - Starting feature engineering for metric 11
2024-08-05 23:02:20,047 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:02:20,048 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:02:20,049 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:20,049 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:20,062 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:02:20,079 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:20,080 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:20,085 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:20,085 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:20,092 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:20,093 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:20,097 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:23,105 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:02:23,109 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:23,111 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:23,111 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:23,115 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:23,115 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:23,118 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:23,121 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:23,122 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:23,126 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:23,244 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 99.74387876437025, 'median': 99.66084084075082, 'std': 9.614150928926504, 'min': 77.06130887774056, 'max': 121.73660789777128, 'skewness': -0.02920782406806899, 'kurtosis': -0.3440381333179605, 'missing_percentage': 0.0}}
2024-08-05 23:02:23,244 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:02:23,244 - metrics.computations.feature_engineering - ERROR - Error in profile_data: 'date'
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - Data profile for metric 11:
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - count: 0
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - mean: nan
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - median: nan
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - std: nan
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - min: nan
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - max: nan
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - range: nan
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - skewness: nan
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - kurtosis: nan
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - variance: nan
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - coefficient_of_variation: nan
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - percentiles: {'1%': nan, '5%': nan, '25%': nan, '75%': nan, '95%': nan, '99%': nan}
2024-08-05 23:02:23,245 - metrics.computations.permanent_computations - INFO - missing_values: 0
2024-08-05 23:02:23,246 - metrics.computations.permanent_computations - INFO - missing_percentage: 0
2024-08-05 23:02:23,246 - metrics.computations.permanent_computations - INFO - unique_values: 0
2024-08-05 23:02:23,246 - metrics.computations.permanent_computations - INFO - time_range: {'start': None, 'end': None, 'duration_days': 0}
2024-08-05 23:02:23,246 - metrics.computations.permanent_computations - INFO - frequency: None
2024-08-05 23:02:23,246 - metrics.computations.permanent_computations - INFO - trend: None
2024-08-05 23:02:23,246 - metrics.computations.permanent_computations - INFO - stationarity: None
2024-08-05 23:02:23,246 - metrics.computations.permanent_computations - INFO - outliers: {'count': 0, 'percentage': 0}
2024-08-05 23:02:23,246 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 11
2024-08-05 23:02:23,255 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:02:23,269 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:02:23,279 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 11
2024-08-05 23:02:23,279 - metrics.computations.feature_engineering - INFO - Parameters for metric 11: dynamic
2024-08-05 23:02:23,279 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 11: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:02:23,279 - metrics.computations.permanent_computations - INFO - Feature engineering completed for metric 11
2024-08-05 23:02:23,279 - metrics.computations.permanent_computations - INFO - Starting analysis for metric 11
2024-08-05 23:02:23,284 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:02:23,284 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:02:23,285 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:23,285 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:23,297 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:02:23,312 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:23,312 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:23,317 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:23,317 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:23,321 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:23,322 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:23,325 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:26,026 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:02:26,030 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:26,032 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:26,032 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:26,036 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:26,037 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:26,042 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:26,046 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:26,047 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:26,051 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:26,086 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 99.74387876437025, 'median': 99.66084084075082, 'std': 9.614150928926504, 'min': 77.06130887774056, 'max': 121.73660789777128, 'skewness': -0.02920782406806899, 'kurtosis': -0.3440381333179605, 'missing_percentage': 0.0}}
2024-08-05 23:02:26,094 - metrics.computations.computations_analyzer - INFO - Analyzed trend for metric 11
2024-08-05 23:02:26,124 - metrics.computations.computations_analyzer - INFO - Calculated moving averages for metric 11
2024-08-05 23:02:26,126 - metrics.computations.computations_analyzer - INFO - Calculated technical indicators for metric 11
2024-08-05 23:02:26,136 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:02:26,137 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:02:26,138 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:26,138 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:26,145 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:02:26,160 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:26,161 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:26,165 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:26,165 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:26,169 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:26,170 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:26,173 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:28,938 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:02:28,941 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:28,944 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:28,944 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:28,948 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:28,948 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:28,953 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:28,957 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:28,957 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:28,961 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:29,048 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 99.74387876437025, 'median': 99.66084084075082, 'std': 9.614150928926504, 'min': 77.06130887774056, 'max': 121.73660789777128, 'skewness': -0.02920782406806899, 'kurtosis': -0.3440381333179605, 'missing_percentage': 0.0}}
2024-08-05 23:02:29,059 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:02:29,060 - metrics.computations.computations_analyzer - ERROR - Error detecting seasonality for metric 11: 'dict' object has no attribute 'strength'
2024-08-05 23:02:29,533 - metrics.computations.computations_analyzer - INFO - Detected trend change point for metric 11
2024-08-05 23:02:29,542 - metrics.computations.permanent_computations - ERROR - Unexpected error saving analysis results for metric 11: string indices must be integers
2024-08-05 23:02:29,542 - metrics.computations.permanent_computations - INFO - Analysis completed for metric 11
2024-08-05 23:02:29,543 - metrics.computations.permanent_computations - INFO - Starting forecasting for metric 11
2024-08-05 23:02:29,548 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:02:29,548 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:02:29,549 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:29,550 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:29,557 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:02:29,568 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:29,569 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:29,574 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:29,574 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:29,577 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:29,578 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:29,582 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:32,330 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:02:32,333 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:32,336 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:32,336 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:32,340 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:32,340 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:32,344 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:32,347 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:32,347 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:32,352 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:32,442 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 99.74387876437025, 'median': 99.66084084075082, 'std': 9.614150928926504, 'min': 77.06130887774056, 'max': 121.73660789777128, 'skewness': -0.02920782406806899, 'kurtosis': -0.3440381333179605, 'missing_percentage': 0.0}}
2024-08-05 23:02:32,444 - metrics.computations.computations_forecaster - WARNING - SARIMA model not recommended for metric 11. Using it anyway.
2024-08-05 23:02:35,970 - metrics.computations.computations_forecaster - INFO - Generated SARIMA forecast for metric 11
2024-08-05 23:02:35,972 - metrics.computations.computations_forecaster - WARNING - Prophet model not recommended for metric 11. Using it anyway.
2024-08-05 23:02:35,973 - prophet - DEBUG - Trying to load backend: CMDSTANPY
2024-08-05 23:02:36,004 - prophet - DEBUG - Loaded stan backend: CMDSTANPY
2024-08-05 23:02:36,014 - prophet - INFO - Disabling daily seasonality. Run prophet with daily_seasonality=True to override this.
2024-08-05 23:02:36,032 - cmdstanpy - DEBUG - input tempfile: /tmp/tmp9m_j37ac/t10mx7b2.json
2024-08-05 23:02:36,080 - cmdstanpy - DEBUG - input tempfile: /tmp/tmp9m_j37ac/qx8yi7gz.json
2024-08-05 23:02:36,081 - cmdstanpy - DEBUG - idx 0
2024-08-05 23:02:36,081 - cmdstanpy - DEBUG - running CmdStan, num_threads: None
2024-08-05 23:02:36,081 - cmdstanpy - DEBUG - CmdStan args: ['/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/prophet/stan_model/prophet_model.bin', 'random', 'seed=2664', 'data', 'file=/tmp/tmp9m_j37ac/t10mx7b2.json', 'init=/tmp/tmp9m_j37ac/qx8yi7gz.json', 'output', 'file=/tmp/tmp9m_j37ac/prophet_model_m_d583_/prophet_model-20240805230236.csv', 'method=optimize', 'algorithm=lbfgs', 'iter=10000']
2024-08-05 23:02:36,082 - cmdstanpy - INFO - Chain [1] start processing
2024-08-05 23:02:36,134 - cmdstanpy - INFO - Chain [1] done processing
2024-08-05 23:02:36,309 - metrics.computations.computations_forecaster - INFO - Generated Prophet forecast for metric 11
2024-08-05 23:02:36,311 - metrics.computations.permanent_computations - ERROR - Error in forecasting for metric 11: string indices must be integers
2024-08-05 23:02:36,312 - metrics.computations.permanent_computations - INFO - Starting anomaly detection for metric 11
2024-08-05 23:02:36,316 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:02:36,316 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:02:36,317 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:36,317 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:36,325 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:02:36,336 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:36,336 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:36,339 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:36,339 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:36,343 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:36,343 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:36,346 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:39,144 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:02:39,148 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:39,150 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:39,150 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:39,154 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:39,154 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:39,158 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:39,161 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:39,161 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:39,166 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:39,300 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 99.74387876437025, 'median': 99.66084084075082, 'std': 9.614150928926504, 'min': 77.06130887774056, 'max': 121.73660789777128, 'skewness': -0.02920782406806899, 'kurtosis': -0.3440381333179605, 'missing_percentage': 0.0}}
2024-08-05 23:02:39,305 - metrics.computations.computations_anomalies - INFO - Initialized AnomalyDetector for metric 11
2024-08-05 23:02:39,306 - metrics.computations.computations_anomalies - INFO - Seasonality period: 2
2024-08-05 23:02:39,306 - metrics.computations.computations_anomalies - INFO - Window size: 1000
2024-08-05 23:02:39,306 - metrics.computations.computations_anomalies - INFO - Base threshold: 5.0
2024-08-05 23:02:39,311 - metrics.computations.computations_anomalies - INFO - Context window: 15
2024-08-05 23:02:39,311 - metrics.computations.computations_anomalies - INFO - Global threshold: 5.0
2024-08-05 23:02:39,312 - metrics.computations.computations_anomalies - INFO - Starting anomaly detection for metric 11
2024-08-05 23:02:39,312 - metrics.computations.computations_anomalies - INFO - Data shape: (1000, 2)
2024-08-05 23:02:39,314 - metrics.computations.computations_anomalies - INFO - Data summary: count    1000.000000
mean       99.743879
std         9.614151
min        77.061309
25%        93.205757
50%        99.660841
75%       106.252128
max       121.736608
Name: value, dtype: float64
2024-08-05 23:02:39,320 - metrics.computations.computations_anomalies - INFO - Deseasonalized data summary: count    1000.000000
mean       99.763208
std         9.612728
min        77.061309
25%        93.246765
50%        99.660841
75%       106.300904
max       121.736608
Name: value, dtype: float64
2024-08-05 23:02:39,329 - metrics.computations.computations_anomalies - INFO - Modified z-scores range: -0.23387331003869288 to -0.23387331003869288
2024-08-05 23:02:39,333 - metrics.computations.computations_anomalies - INFO - Modified z-scores summary: count    1.000000
mean    -0.233873
std           NaN
min     -0.233873
25%     -0.233873
50%     -0.233873
75%     -0.233873
max     -0.233873
Name: value, dtype: float64
2024-08-05 23:02:39,335 - metrics.computations.computations_anomalies - INFO - Adaptive threshold range: 6.010105594381269 to 6.010105594381269
2024-08-05 23:02:39,338 - metrics.computations.computations_anomalies - INFO - Adaptive threshold summary: count    1.000000
mean     6.010106
std           NaN
min      6.010106
25%      6.010106
50%      6.010106
75%      6.010106
max      6.010106
Name: value, dtype: float64
2024-08-05 23:02:39,340 - metrics.computations.computations_anomalies - INFO - Contextual z-scores range: nan to nan
2024-08-05 23:02:39,345 - metrics.computations.computations_anomalies - INFO - Contextual z-scores summary: count    0.0
mean     NaN
std      NaN
min      NaN
25%      NaN
50%      NaN
75%      NaN
max      NaN
Name: value, dtype: float64
2024-08-05 23:02:39,346 - metrics.computations.computations_anomalies - INFO - Global mean: 99.76320752094684, Global std: 9.612727992446437
2024-08-05 23:02:39,347 - metrics.computations.computations_anomalies - INFO - Number of anomalies detected: 0
2024-08-05 23:02:39,352 - metrics.computations.computations_anomalies - INFO - Detected 0 anomalies for metric 11
2024-08-05 23:02:39,355 - metrics.computations.permanent_computations - ERROR - Error in anomaly detection for metric 11: 'anomalies'
2024-08-05 23:02:39,356 - metrics.computations.permanent_computations - INFO - Starting relationship analysis for metric 11
2024-08-05 23:02:39,361 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:02:39,362 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:02:39,364 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:39,365 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:39,377 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:02:39,391 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:39,392 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:39,396 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:39,396 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:39,399 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:39,399 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:39,403 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:42,197 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:02:42,201 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:42,203 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:42,203 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:42,206 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:42,207 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:42,210 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   99.621211          6
2023-01-02  112.306443          6
2023-01-03   88.709492          6
2023-01-04   93.850374          6
2023-01-05  112.937364          6
2024-08-05 23:02:42,214 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:42,214 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:42,219 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:42,308 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 99.74387876437025, 'median': 99.66084084075082, 'std': 9.614150928926504, 'min': 77.06130887774056, 'max': 121.73660789777128, 'skewness': -0.02920782406806899, 'kurtosis': -0.3440381333179605, 'missing_percentage': 0.0}}
2024-08-05 23:02:42,311 - metrics.computations.permanent_computations - ERROR - Error in relationship analysis for metric 11: RelationshipAnalyzer.analyze_relationships() missing 1 required positional argument: 'other_metric_ids'
2024-08-05 23:02:42,311 - metrics.computations.permanent_computations - INFO - Generating report for metric 11
2024-08-05 23:02:42,312 - metrics.computations.permanent_computations - ERROR - Error generating or saving report for metric 11: -1
2024-08-05 23:02:42,312 - metrics.computations.permanent_computations - INFO - All computations completed for metric 11
2024-08-05 23:02:42,313 - metrics.computations.permanent_computations - INFO - Starting computations for metric 12
2024-08-05 23:02:42,316 - metrics.computations.permanent_computations - INFO - Starting data preparation for metric 12
2024-08-05 23:02:42,316 - metrics.computations.permanent_computations - INFO - Starting data preparation for metric 12
2024-08-05 23:02:42,321 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:02:42,322 - metrics.computations.permanent_computations - INFO - DataPreparation object created: <metrics.computations.data_preparation.DataPreparation object at 0x7f0c850256c0>
2024-08-05 23:02:42,322 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:02:42,326 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:42,329 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:42,333 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:02:42,343 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:42,348 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:42,353 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:42,354 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:42,358 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:42,358 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:42,363 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:44,782 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:02:44,785 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:44,787 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:44,787 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:44,791 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:44,791 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:44,794 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:44,798 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:44,798 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:44,804 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:44,980 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 109.71826664080727, 'median': 109.62692492482591, 'std': 10.575566021819155, 'min': 84.76743976551462, 'max': 133.9102686875484, 'skewness': -0.029207824068065498, 'kurtosis': -0.3440381333179614, 'missing_percentage': 0.0}}
2024-08-05 23:02:44,981 - metrics.computations.permanent_computations - INFO - prepare_data() called, returned DataFrame of shape (1000, 2)
2024-08-05 23:02:44,981 - metrics.computations.permanent_computations - INFO - Data preparation statistics for metric 12:
2024-08-05 23:02:44,982 - metrics.computations.permanent_computations - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:44,982 - metrics.computations.permanent_computations - INFO - Number of data points: 1000
2024-08-05 23:02:44,983 - metrics.computations.permanent_computations - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:44,984 - metrics.computations.permanent_computations - INFO - Metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 109.71826664080727, 'median': 109.62692492482591, 'std': 10.575566021819155, 'min': 84.76743976551462, 'max': 133.9102686875484, 'skewness': -0.029207824068065498, 'kurtosis': -0.3440381333179614, 'missing_percentage': 0.0}}
2024-08-05 23:02:44,984 - metrics.computations.permanent_computations - INFO - Date range: 2023-01-01 00:00:00 to 2025-09-26 00:00:00
2024-08-05 23:02:44,985 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:02:44,986 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:44,987 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:44,990 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:02:45,021 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:45,022 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:45,029 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:45,030 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:45,038 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:45,039 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:45,043 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:47,421 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:02:47,425 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:47,427 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:47,427 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:47,432 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:47,432 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:47,437 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:47,440 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:47,441 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:47,445 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:47,542 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 109.71826664080727, 'median': 109.62692492482591, 'std': 10.575566021819155, 'min': 84.76743976551462, 'max': 133.9102686875484, 'skewness': -0.029207824068065498, 'kurtosis': -0.3440381333179614, 'missing_percentage': 0.0}}
2024-08-05 23:02:47,543 - metrics.computations.permanent_computations - INFO - Data preparation completed for metric 12
2024-08-05 23:02:47,543 - metrics.computations.permanent_computations - INFO - Starting feature engineering for metric 12
2024-08-05 23:02:47,548 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:02:47,548 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:02:47,549 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:47,550 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:47,561 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:02:47,577 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:47,579 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:47,585 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:47,586 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:47,590 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:47,591 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:47,598 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:50,042 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:02:50,045 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:50,047 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:50,048 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:50,051 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:50,051 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:50,054 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:50,057 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:50,058 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:50,062 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:50,147 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 109.71826664080727, 'median': 109.62692492482591, 'std': 10.575566021819155, 'min': 84.76743976551462, 'max': 133.9102686875484, 'skewness': -0.029207824068065498, 'kurtosis': -0.3440381333179614, 'missing_percentage': 0.0}}
2024-08-05 23:02:50,148 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:02:50,148 - metrics.computations.feature_engineering - ERROR - Error in profile_data: 'date'
2024-08-05 23:02:50,149 - metrics.computations.permanent_computations - INFO - Data profile for metric 12:
2024-08-05 23:02:50,149 - metrics.computations.permanent_computations - INFO - count: 0
2024-08-05 23:02:50,149 - metrics.computations.permanent_computations - INFO - mean: nan
2024-08-05 23:02:50,149 - metrics.computations.permanent_computations - INFO - median: nan
2024-08-05 23:02:50,149 - metrics.computations.permanent_computations - INFO - std: nan
2024-08-05 23:02:50,149 - metrics.computations.permanent_computations - INFO - min: nan
2024-08-05 23:02:50,149 - metrics.computations.permanent_computations - INFO - max: nan
2024-08-05 23:02:50,149 - metrics.computations.permanent_computations - INFO - range: nan
2024-08-05 23:02:50,149 - metrics.computations.permanent_computations - INFO - skewness: nan
2024-08-05 23:02:50,149 - metrics.computations.permanent_computations - INFO - kurtosis: nan
2024-08-05 23:02:50,150 - metrics.computations.permanent_computations - INFO - variance: nan
2024-08-05 23:02:50,150 - metrics.computations.permanent_computations - INFO - coefficient_of_variation: nan
2024-08-05 23:02:50,150 - metrics.computations.permanent_computations - INFO - percentiles: {'1%': nan, '5%': nan, '25%': nan, '75%': nan, '95%': nan, '99%': nan}
2024-08-05 23:02:50,150 - metrics.computations.permanent_computations - INFO - missing_values: 0
2024-08-05 23:02:50,150 - metrics.computations.permanent_computations - INFO - missing_percentage: 0
2024-08-05 23:02:50,150 - metrics.computations.permanent_computations - INFO - unique_values: 0
2024-08-05 23:02:50,150 - metrics.computations.permanent_computations - INFO - time_range: {'start': None, 'end': None, 'duration_days': 0}
2024-08-05 23:02:50,150 - metrics.computations.permanent_computations - INFO - frequency: None
2024-08-05 23:02:50,150 - metrics.computations.permanent_computations - INFO - trend: None
2024-08-05 23:02:50,150 - metrics.computations.permanent_computations - INFO - stationarity: None
2024-08-05 23:02:50,150 - metrics.computations.permanent_computations - INFO - outliers: {'count': 0, 'percentage': 0}
2024-08-05 23:02:50,151 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 12
2024-08-05 23:02:50,166 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:02:50,179 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:02:50,185 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 12
2024-08-05 23:02:50,185 - metrics.computations.feature_engineering - INFO - Parameters for metric 12: dynamic
2024-08-05 23:02:50,186 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 12: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:02:50,186 - metrics.computations.permanent_computations - INFO - Feature engineering completed for metric 12
2024-08-05 23:02:50,191 - metrics.computations.permanent_computations - INFO - Starting analysis for metric 12
2024-08-05 23:02:50,196 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:02:50,196 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:02:50,197 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:50,198 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:50,202 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:02:50,214 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:50,215 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:50,219 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:50,220 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:50,224 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:50,224 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:50,228 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:52,758 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:02:52,760 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:52,762 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:52,762 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:52,766 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:52,766 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:52,769 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:52,773 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:52,773 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:52,777 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:52,826 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 109.71826664080727, 'median': 109.62692492482591, 'std': 10.575566021819155, 'min': 84.76743976551462, 'max': 133.9102686875484, 'skewness': -0.029207824068065498, 'kurtosis': -0.3440381333179614, 'missing_percentage': 0.0}}
2024-08-05 23:02:52,834 - metrics.computations.computations_analyzer - INFO - Analyzed trend for metric 12
2024-08-05 23:02:52,891 - metrics.computations.computations_analyzer - INFO - Calculated moving averages for metric 12
2024-08-05 23:02:52,891 - metrics.computations.computations_analyzer - INFO - Calculated technical indicators for metric 12
2024-08-05 23:02:52,896 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:02:52,896 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:02:52,898 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:52,899 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:52,903 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:02:52,915 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:52,915 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:52,921 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:52,921 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:52,927 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:52,928 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:52,932 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:55,701 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:02:55,704 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:55,706 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:55,707 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:55,710 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:55,710 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:55,713 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:55,716 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:55,716 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:55,720 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:55,773 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 109.71826664080727, 'median': 109.62692492482591, 'std': 10.575566021819155, 'min': 84.76743976551462, 'max': 133.9102686875484, 'skewness': -0.029207824068065498, 'kurtosis': -0.3440381333179614, 'missing_percentage': 0.0}}
2024-08-05 23:02:55,779 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:02:55,779 - metrics.computations.computations_analyzer - ERROR - Error detecting seasonality for metric 12: 'dict' object has no attribute 'strength'
2024-08-05 23:02:56,248 - metrics.computations.computations_analyzer - INFO - Detected trend change point for metric 12
2024-08-05 23:02:56,256 - metrics.computations.permanent_computations - ERROR - Unexpected error saving analysis results for metric 12: string indices must be integers
2024-08-05 23:02:56,256 - metrics.computations.permanent_computations - INFO - Analysis completed for metric 12
2024-08-05 23:02:56,256 - metrics.computations.permanent_computations - INFO - Starting forecasting for metric 12
2024-08-05 23:02:56,261 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:02:56,261 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:02:56,262 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:56,263 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:02:56,267 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:02:56,277 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:56,277 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:02:56,281 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:56,281 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:02:56,284 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:56,285 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:02:56,288 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:02:58,929 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:02:58,932 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:02:58,934 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:02:58,934 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:02:58,937 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:58,938 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:02:58,941 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:02:58,944 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:02:58,944 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:02:58,949 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:02:59,014 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 109.71826664080727, 'median': 109.62692492482591, 'std': 10.575566021819155, 'min': 84.76743976551462, 'max': 133.9102686875484, 'skewness': -0.029207824068065498, 'kurtosis': -0.3440381333179614, 'missing_percentage': 0.0}}
2024-08-05 23:02:59,016 - metrics.computations.computations_forecaster - WARNING - SARIMA model not recommended for metric 12. Using it anyway.
2024-08-05 23:03:04,571 - metrics.computations.computations_forecaster - INFO - Generated SARIMA forecast for metric 12
2024-08-05 23:03:04,572 - metrics.computations.computations_forecaster - WARNING - Prophet model not recommended for metric 12. Using it anyway.
2024-08-05 23:03:04,573 - prophet - DEBUG - Trying to load backend: CMDSTANPY
2024-08-05 23:03:04,574 - prophet - DEBUG - Loaded stan backend: CMDSTANPY
2024-08-05 23:03:04,583 - prophet - INFO - Disabling daily seasonality. Run prophet with daily_seasonality=True to override this.
2024-08-05 23:03:04,603 - cmdstanpy - DEBUG - input tempfile: /tmp/tmp9m_j37ac/lr7cjwmr.json
2024-08-05 23:03:04,656 - cmdstanpy - DEBUG - input tempfile: /tmp/tmp9m_j37ac/a62wwdwf.json
2024-08-05 23:03:04,658 - cmdstanpy - DEBUG - idx 0
2024-08-05 23:03:04,658 - cmdstanpy - DEBUG - running CmdStan, num_threads: None
2024-08-05 23:03:04,658 - cmdstanpy - DEBUG - CmdStan args: ['/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/prophet/stan_model/prophet_model.bin', 'random', 'seed=41128', 'data', 'file=/tmp/tmp9m_j37ac/lr7cjwmr.json', 'init=/tmp/tmp9m_j37ac/a62wwdwf.json', 'output', 'file=/tmp/tmp9m_j37ac/prophet_modellpd1ofdb/prophet_model-20240805230304.csv', 'method=optimize', 'algorithm=lbfgs', 'iter=10000']
2024-08-05 23:03:04,658 - cmdstanpy - INFO - Chain [1] start processing
2024-08-05 23:03:04,690 - cmdstanpy - INFO - Chain [1] done processing
2024-08-05 23:03:04,916 - metrics.computations.computations_forecaster - INFO - Generated Prophet forecast for metric 12
2024-08-05 23:03:04,918 - metrics.computations.permanent_computations - ERROR - Error in forecasting for metric 12: string indices must be integers
2024-08-05 23:03:04,918 - metrics.computations.permanent_computations - INFO - Starting anomaly detection for metric 12
2024-08-05 23:03:04,924 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:03:04,924 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:03:04,925 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:04,926 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:04,933 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:03:04,943 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:04,943 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:03:04,947 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:03:04,947 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:04,952 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:03:04,953 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:03:04,959 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:03:09,998 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:03:10,001 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:03:10,003 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:03:10,003 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:03:10,006 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:03:10,006 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:03:10,009 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:03:10,012 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:03:10,013 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:03:10,017 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:03:10,159 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 109.71826664080727, 'median': 109.62692492482591, 'std': 10.575566021819155, 'min': 84.76743976551462, 'max': 133.9102686875484, 'skewness': -0.029207824068065498, 'kurtosis': -0.3440381333179614, 'missing_percentage': 0.0}}
2024-08-05 23:03:10,160 - metrics.computations.computations_anomalies - INFO - Initialized AnomalyDetector for metric 12
2024-08-05 23:03:10,160 - metrics.computations.computations_anomalies - INFO - Seasonality period: 2
2024-08-05 23:03:10,161 - metrics.computations.computations_anomalies - INFO - Window size: 1000
2024-08-05 23:03:10,161 - metrics.computations.computations_anomalies - INFO - Base threshold: 5.0
2024-08-05 23:03:10,161 - metrics.computations.computations_anomalies - INFO - Context window: 15
2024-08-05 23:03:10,161 - metrics.computations.computations_anomalies - INFO - Global threshold: 5.0
2024-08-05 23:03:10,164 - metrics.computations.computations_anomalies - INFO - Starting anomaly detection for metric 12
2024-08-05 23:03:10,166 - metrics.computations.computations_anomalies - INFO - Data shape: (1000, 2)
2024-08-05 23:03:10,170 - metrics.computations.computations_anomalies - INFO - Data summary: count    1000.000000
mean      109.718267
std        10.575566
min        84.767440
25%       102.526333
50%       109.626925
75%       116.877341
max       133.910269
Name: value, dtype: float64
2024-08-05 23:03:10,175 - metrics.computations.computations_anomalies - INFO - Deseasonalized data summary: count    1000.000000
mean      109.739528
std        10.574001
min        84.767440
25%       102.571442
50%       109.626925
75%       116.930995
max       133.910269
Name: value, dtype: float64
2024-08-05 23:03:10,178 - metrics.computations.computations_anomalies - INFO - Modified z-scores range: -0.23387331003869316 to -0.23387331003869316
2024-08-05 23:03:10,187 - metrics.computations.computations_anomalies - INFO - Modified z-scores summary: count    1.000000
mean    -0.233873
std           NaN
min     -0.233873
25%     -0.233873
50%     -0.233873
75%     -0.233873
max     -0.233873
Name: value, dtype: float64
2024-08-05 23:03:10,192 - metrics.computations.computations_anomalies - INFO - Adaptive threshold range: 6.051695525852162 to 6.051695525852162
2024-08-05 23:03:10,195 - metrics.computations.computations_anomalies - INFO - Adaptive threshold summary: count    1.000000
mean     6.051696
std           NaN
min      6.051696
25%      6.051696
50%      6.051696
75%      6.051696
max      6.051696
Name: value, dtype: float64
2024-08-05 23:03:10,196 - metrics.computations.computations_anomalies - INFO - Contextual z-scores range: nan to nan
2024-08-05 23:03:10,198 - metrics.computations.computations_anomalies - INFO - Contextual z-scores summary: count    0.0
mean     NaN
std      NaN
min      NaN
25%      NaN
50%      NaN
75%      NaN
max      NaN
Name: value, dtype: float64
2024-08-05 23:03:10,199 - metrics.computations.computations_anomalies - INFO - Global mean: 109.73952827304153, Global std: 10.574000791691084
2024-08-05 23:03:10,200 - metrics.computations.computations_anomalies - INFO - Number of anomalies detected: 0
2024-08-05 23:03:10,204 - metrics.computations.computations_anomalies - INFO - Detected 0 anomalies for metric 12
2024-08-05 23:03:10,207 - metrics.computations.permanent_computations - ERROR - Error in anomaly detection for metric 12: 'anomalies'
2024-08-05 23:03:10,208 - metrics.computations.permanent_computations - INFO - Starting relationship analysis for metric 12
2024-08-05 23:03:10,213 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:03:10,214 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:03:10,214 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:10,215 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:10,223 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:03:10,234 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:10,234 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:03:10,238 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:03:10,238 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:10,240 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:03:10,241 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:03:10,244 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:03:14,332 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:03:14,335 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:03:14,337 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:03:14,338 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:03:14,342 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:03:14,343 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:03:14,347 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  109.583332          6
2023-01-02  123.537087          6
2023-01-03   97.580441          6
2023-01-04  103.235411          6
2023-01-05  124.231100          6
2024-08-05 23:03:14,351 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3650580635797409, Timeliness: nan
2024-08-05 23:03:14,352 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.50193545265803
2024-08-05 23:03:14,360 - metrics.computations.data_preparation - INFO - Data quality score: 45.50193545265803
2024-08-05 23:03:14,575 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.50193545265803, 'outliers_handled': True, 'profile': {'mean': 109.71826664080727, 'median': 109.62692492482591, 'std': 10.575566021819155, 'min': 84.76743976551462, 'max': 133.9102686875484, 'skewness': -0.029207824068065498, 'kurtosis': -0.3440381333179614, 'missing_percentage': 0.0}}
2024-08-05 23:03:14,577 - metrics.computations.permanent_computations - ERROR - Error in relationship analysis for metric 12: RelationshipAnalyzer.analyze_relationships() missing 1 required positional argument: 'other_metric_ids'
2024-08-05 23:03:14,578 - metrics.computations.permanent_computations - INFO - Generating report for metric 12
2024-08-05 23:03:14,583 - metrics.computations.permanent_computations - ERROR - Error generating or saving report for metric 12: -1
2024-08-05 23:03:14,584 - metrics.computations.permanent_computations - INFO - All computations completed for metric 12
2024-08-05 23:03:14,587 - metrics.computations.permanent_computations - ERROR - Error storing results for metric 11: -1
2024-08-05 23:03:14,588 - metrics.computations.permanent_computations - ERROR - Error storing results for metric 12: -1
2024-08-05 23:03:14,832 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Teardown completed
```

## test_relationships_robustness (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
Status: failure
Duration: 55.846 seconds

### Failure
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_permanent_computations_robustness.py", line 226, in test_relationships_robustness
    self.assertNotEqual(connection.strength, 0.5)
AssertionError: 0.5 == 0.5
```

### Output
```
Starting setUp
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
  Applying sessions.0001_initial...
 OK
Initializing PermanentComputations with metric_ids: [13, 14]
Finished initializing PermanentComputations
Initializing DataPreparation for metric_id: 13
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 13
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 13
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 13
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 14
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 14
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 14
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 14
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 14
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 14
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 14
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Initializing DataPreparation for metric_id: 14
Finished initializing DataPreparation
Starting prepare_data
Finished prepare_data
Relationship Analyzer Computation time: 7.260857343673706 seconds
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
2024-08-05 23:03:14,853 - metrics - DEBUG - Starting test: test_relationships_robustness (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
2024-08-05 23:03:14,860 - django.db.backends.schema - DEBUG - CREATE TABLE "django_migrations" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:03:14,882 - django.db.backends.schema - DEBUG - CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
2024-08-05 23:03:14,887 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params None)
2024-08-05 23:03:14,895 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL, "codename" varchar(100) NOT NULL); (params None)
2024-08-05 23:03:14,905 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(80) NOT NULL UNIQUE); (params None)
2024-08-05 23:03:14,911 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:03:14,921 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NOT NULL, "is_superuser" boolean NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:03:14,929 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:03:14,934 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:03:14,939 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename"); (params None)
2024-08-05 23:03:14,943 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:14,945 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id"); (params None)
2024-08-05 23:03:14,949 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_name_a6ea08ec_like" ON "auth_group" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:03:14,953 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id"); (params None)
2024-08-05 23:03:14,958 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:14,960 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:14,962 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id"); (params None)
2024-08-05 23:03:14,966 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id"); (params None)
2024-08-05 23:03:14,971 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_username_6821ab7c_like" ON "auth_user" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:03:14,976 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id"); (params None)
2024-08-05 23:03:14,980 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:14,982 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:14,984 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id"); (params None)
2024-08-05 23:03:14,988 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id"); (params None)
2024-08-05 23:03:14,991 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id"); (params None)
2024-08-05 23:03:14,996 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:14,999 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,001 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id"); (params None)
2024-08-05 23:03:15,004 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id"); (params None)
2024-08-05 23:03:15,017 - django.db.backends.schema - DEBUG - CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "action_time" timestamp with time zone NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL, "user_id" integer NOT NULL); (params None)
2024-08-05 23:03:15,026 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,028 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,029 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id"); (params None)
2024-08-05 23:03:15,032 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id"); (params None)
2024-08-05 23:03:15,058 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ALTER COLUMN "name" DROP NOT NULL; (params None)
2024-08-05 23:03:15,071 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" DROP COLUMN "name" CASCADE; (params None)
2024-08-05 23:03:15,081 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ALTER COLUMN "name" TYPE varchar(255); (params None)
2024-08-05 23:03:15,091 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "email" TYPE varchar(254); (params None)
2024-08-05 23:03:15,109 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_login" DROP NOT NULL; (params None)
2024-08-05 23:03:15,131 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "username" TYPE varchar(150); (params None)
2024-08-05 23:03:15,146 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_name" TYPE varchar(150); (params None)
2024-08-05 23:03:15,160 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group" ALTER COLUMN "name" TYPE varchar(150); (params None)
2024-08-05 23:03:15,178 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "first_name" TYPE varchar(150); (params None)
2024-08-05 23:03:15,229 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_client" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "schema_name" varchar(63) NOT NULL UNIQUE, "name" varchar(100) NOT NULL, "created_on" date NOT NULL); (params None)
2024-08-05 23:03:15,241 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_category" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,258 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dashboard" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "layout" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,273 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_domain" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "domain" varchar(253) NOT NULL UNIQUE, "is_primary" boolean NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,289 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "type" varchar(50) NOT NULL, "confidence" varchar(50) NOT NULL, "value_type" varchar(20) NOT NULL, "rhythm" varchar(20) NOT NULL, "description" text NOT NULL, "hypothesis" text NOT NULL, "technical_description" text NOT NULL, "last_updated" timestamp with time zone NOT NULL, "source" varchar(100) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL, "category_id" bigint NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,302 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_historicaldata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "value" double precision NOT NULL, "forecasted_value" double precision NULL, "anomaly_detected" boolean NOT NULL, "trend_component" varchar(50) NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,315 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_forecast" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "forecast_date" date NOT NULL, "forecast_value" double precision NOT NULL, "model_used" varchar(100) NOT NULL, "accuracy" double precision NULL, "confidence_interval" jsonb NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,331 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "status" varchar(50) NOT NULL, "results" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,340 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment_metrics" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "experiment_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,356 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_connection" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "relationship" varchar(100) NOT NULL, "correlation_coefficient" double precision NULL, "tenant_id" bigint NOT NULL, "from_metric_id" bigint NOT NULL, "to_metric_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,374 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_anomaly" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "detection_date" date NOT NULL, "anomaly_value" double precision NOT NULL, "anomaly_score" double precision NOT NULL, "notes" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,400 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_actionremark" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NULL, "description" text NOT NULL, "impact" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,418 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_project" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "created_on" date NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,432 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_report" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "configuration" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,450 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tag" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "project_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,465 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric_tags" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "metric_id" bigint NOT NULL, "tag_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,489 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_target" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "remarks" text NOT NULL, "target_kpi" varchar(100) NOT NULL, "target_date" date NULL, "target_value" double precision NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,514 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trend" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "trend_type" varchar(50) NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "trend_value" double precision NOT NULL, "notes" text NOT NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:03:15,522 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_schema_name_87d6fbb5_like" ON "metrics_client" ("schema_name" varchar_pattern_ops); (params None)
2024-08-05 23:03:15,526 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_category" ADD CONSTRAINT "metrics_category_tenant_id_67d98cc6_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,528 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_tenant_id_67d98cc6" ON "metrics_category" ("tenant_id"); (params None)
2024-08-05 23:03:15,532 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ADD CONSTRAINT "metrics_dashboard_tenant_id_50099a7d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,534 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_tenant_id_50099a7d" ON "metrics_dashboard" ("tenant_id"); (params None)
2024-08-05 23:03:15,537 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_domain" ADD CONSTRAINT "metrics_domain_tenant_id_259fb21f_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,539 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_domain_bdc97b86_like" ON "metrics_domain" ("domain" varchar_pattern_ops); (params None)
2024-08-05 23:03:15,544 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_is_primary_ac9d2eaf" ON "metrics_domain" ("is_primary"); (params None)
2024-08-05 23:03:15,547 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_tenant_id_259fb21f" ON "metrics_domain" ("tenant_id"); (params None)
2024-08-05 23:03:15,550 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_category_id_8793f683_fk_metrics_category_id" FOREIGN KEY ("category_id") REFERENCES "metrics_category" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,551 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_9606b577_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,553 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_category_id_8793f683" ON "metrics_metric" ("category_id"); (params None)
2024-08-05 23:03:15,557 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tenant_id_9606b577" ON "metrics_metric" ("tenant_id"); (params None)
2024-08-05 23:03:15,560 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_tenant_id_438c5ad4_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,562 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_metric_id_3f9e8174_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,563 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_tenant_id_438c5ad4" ON "metrics_historicaldata" ("tenant_id"); (params None)
2024-08-05 23:03:15,567 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_metric_id_3f9e8174" ON "metrics_historicaldata" ("metric_id"); (params None)
2024-08-05 23:03:15,571 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_tenant_id_92d37185_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,573 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_metric_id_e05f23a8_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,574 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_tenant_id_92d37185" ON "metrics_forecast" ("tenant_id"); (params None)
2024-08-05 23:03:15,577 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_metric_id_e05f23a8" ON "metrics_forecast" ("metric_id"); (params None)
2024-08-05 23:03:15,580 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD CONSTRAINT "metrics_experiment_tenant_id_10fa364a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,583 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_tenant_id_10fa364a" ON "metrics_experiment" ("tenant_id"); (params None)
2024-08-05 23:03:15,586 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_metri_experiment_id_metric_id_a9d54b29_uniq" UNIQUE ("experiment_id", "metric_id"); (params None)
2024-08-05 23:03:15,590 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_experiment_id_372c6b59_fk_metrics_e" FOREIGN KEY ("experiment_id") REFERENCES "metrics_experiment" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,592 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_metric_id_c8f84167_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,593 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_experiment_id_372c6b59" ON "metrics_experiment_metrics" ("experiment_id"); (params None)
2024-08-05 23:03:15,597 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_metric_id_c8f84167" ON "metrics_experiment_metrics" ("metric_id"); (params None)
2024-08-05 23:03:15,601 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_2e1e5750_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,603 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_from_metric_id_33b50521_fk_metrics_metric_id" FOREIGN KEY ("from_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,604 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_to_metric_id_94489c1c_fk_metrics_metric_id" FOREIGN KEY ("to_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,605 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_tenant_id_2e1e5750" ON "metrics_connection" ("tenant_id"); (params None)
2024-08-05 23:03:15,609 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_from_metric_id_33b50521" ON "metrics_connection" ("from_metric_id"); (params None)
2024-08-05 23:03:15,613 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_to_metric_id_94489c1c" ON "metrics_connection" ("to_metric_id"); (params None)
2024-08-05 23:03:15,616 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_tenant_id_9e474130_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,619 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_metric_id_1b3c3295_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,620 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_tenant_id_9e474130" ON "metrics_anomaly" ("tenant_id"); (params None)
2024-08-05 23:03:15,624 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_metric_id_1b3c3295" ON "metrics_anomaly" ("metric_id"); (params None)
2024-08-05 23:03:15,628 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_tenant_id_86ffa3a9_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,630 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_metric_id_c1b270f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,632 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_tenant_id_86ffa3a9" ON "metrics_actionremark" ("tenant_id"); (params None)
2024-08-05 23:03:15,636 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_metric_id_c1b270f2" ON "metrics_actionremark" ("metric_id"); (params None)
2024-08-05 23:03:15,641 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_project" ADD CONSTRAINT "metrics_project_tenant_id_db4a1170_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,643 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_tenant_id_db4a1170" ON "metrics_project" ("tenant_id"); (params None)
2024-08-05 23:03:15,646 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD CONSTRAINT "metrics_report_tenant_id_d1cf4812_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,648 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_tenant_id_d1cf4812" ON "metrics_report" ("tenant_id"); (params None)
2024-08-05 23:03:15,653 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_name_project_id_2d57d4da_uniq" UNIQUE ("name", "project_id"); (params None)
2024-08-05 23:03:15,656 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_project_id_b7ac5c8e_fk_metrics_project_id" FOREIGN KEY ("project_id") REFERENCES "metrics_project" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,658 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_tenant_id_c286653b_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,659 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_project_id_b7ac5c8e" ON "metrics_tag" ("project_id"); (params None)
2024-08-05 23:03:15,664 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_tenant_id_c286653b" ON "metrics_tag" ("tenant_id"); (params None)
2024-08-05 23:03:15,669 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_tag_id_a8e1a165_uniq" UNIQUE ("metric_id", "tag_id"); (params None)
2024-08-05 23:03:15,672 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_b2a068f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,675 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_tag_id_61869f56_fk_metrics_tag_id" FOREIGN KEY ("tag_id") REFERENCES "metrics_tag" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,677 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_metric_id_b2a068f2" ON "metrics_metric_tags" ("metric_id"); (params None)
2024-08-05 23:03:15,680 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_tag_id_61869f56" ON "metrics_metric_tags" ("tag_id"); (params None)
2024-08-05 23:03:15,684 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,686 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,687 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_metric_id_181e8748" ON "metrics_target" ("metric_id"); (params None)
2024-08-05 23:03:15,692 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_tenant_id_118eb54a" ON "metrics_target" ("tenant_id"); (params None)
2024-08-05 23:03:15,696 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_metric_id_25179b98_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,698 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_tenant_id_4cb1485d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:15,699 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_metric_id_25179b98" ON "metrics_trend" ("metric_id"); (params None)
2024-08-05 23:03:15,702 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_tenant_id_4cb1485d" ON "metrics_trend" ("tenant_id"); (params None)
2024-08-05 23:03:16,297 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_date_33d1e0bd" ON "metrics_actionremark" ("date"); (params None)
2024-08-05 23:03:16,315 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_detection_date_ee75a187" ON "metrics_anomaly" ("detection_date"); (params None)
2024-08-05 23:03:16,335 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c" ON "metrics_category" ("name"); (params None)
2024-08-05 23:03:16,339 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c_like" ON "metrics_category" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:03:16,357 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d" ON "metrics_client" ("name"); (params None)
2024-08-05 23:03:16,360 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d_like" ON "metrics_client" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:03:16,385 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET DEFAULT '{}'; (params None)
2024-08-05 23:03:16,386 - django.db.backends.schema - DEBUG - UPDATE "metrics_dashboard" SET "layout" = '{}' WHERE "layout" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:03:16,387 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET NOT NULL; (params None)
2024-08-05 23:03:16,388 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" DROP DEFAULT; (params None)
2024-08-05 23:03:16,403 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e" ON "metrics_dashboard" ("name"); (params None)
2024-08-05 23:03:16,407 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e_like" ON "metrics_dashboard" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:03:16,428 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_end_date_31af6c05" ON "metrics_experiment" ("end_date"); (params None)
2024-08-05 23:03:16,451 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7" ON "metrics_experiment" ("name"); (params None)
2024-08-05 23:03:16,456 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7_like" ON "metrics_experiment" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:03:16,473 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET DEFAULT '{}'; (params None)
2024-08-05 23:03:16,474 - django.db.backends.schema - DEBUG - UPDATE "metrics_experiment" SET "results" = '{}' WHERE "results" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:03:16,476 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET NOT NULL; (params None)
2024-08-05 23:03:16,476 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" DROP DEFAULT; (params None)
2024-08-05 23:03:16,490 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_start_date_a6deff13" ON "metrics_experiment" ("start_date"); (params None)
2024-08-05 23:03:16,514 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET DEFAULT '{}'; (params None)
2024-08-05 23:03:16,516 - django.db.backends.schema - DEBUG - UPDATE "metrics_forecast" SET "confidence_interval" = '{}' WHERE "confidence_interval" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:03:16,517 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET NOT NULL; (params None)
2024-08-05 23:03:16,518 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" DROP DEFAULT; (params None)
2024-08-05 23:03:16,533 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_forecast_date_71750ae8" ON "metrics_forecast" ("forecast_date"); (params None)
2024-08-05 23:03:16,549 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_date_f27e0e6a" ON "metrics_historicaldata" ("date"); (params None)
2024-08-05 23:03:16,565 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_last_updated_3e38a760" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:03:16,586 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5" ON "metrics_metric" ("name"); (params None)
2024-08-05 23:03:16,590 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5_like" ON "metrics_metric" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:03:16,607 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e" ON "metrics_metric" ("type"); (params None)
2024-08-05 23:03:16,612 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e_like" ON "metrics_metric" ("type" varchar_pattern_ops); (params None)
2024-08-05 23:03:16,641 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80" ON "metrics_project" ("name"); (params None)
2024-08-05 23:03:16,645 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80_like" ON "metrics_project" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:03:16,662 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET DEFAULT '{}'; (params None)
2024-08-05 23:03:16,663 - django.db.backends.schema - DEBUG - UPDATE "metrics_report" SET "configuration" = '{}' WHERE "configuration" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:03:16,664 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET NOT NULL; (params None)
2024-08-05 23:03:16,665 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" DROP DEFAULT; (params None)
2024-08-05 23:03:16,679 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34" ON "metrics_report" ("name"); (params None)
2024-08-05 23:03:16,683 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34_like" ON "metrics_report" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:03:16,699 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a" ON "metrics_tag" ("name"); (params None)
2024-08-05 23:03:16,705 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a_like" ON "metrics_tag" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:03:16,730 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_target_date_81507ff5" ON "metrics_target" ("target_date"); (params None)
2024-08-05 23:03:16,747 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_end_date_8444ef38" ON "metrics_trend" ("end_date"); (params None)
2024-08-05 23:03:16,765 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_start_date_7b1a850f" ON "metrics_trend" ("start_date"); (params None)
2024-08-05 23:03:16,783 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_act_metric__be3429_idx" ON "metrics_actionremark" ("metric_id", "date"); (params None)
2024-08-05 23:03:16,803 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ano_metric__84982d_idx" ON "metrics_anomaly" ("metric_id", "detection_date"); (params None)
2024-08-05 23:03:16,820 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_con_from_me_9411ea_idx" ON "metrics_connection" ("from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:03:16,835 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_exp_start_d_04716a_idx" ON "metrics_experiment" ("start_date", "end_date"); (params None)
2024-08-05 23:03:16,853 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_for_metric__4c9ae2_idx" ON "metrics_forecast" ("metric_id", "forecast_date"); (params None)
2024-08-05 23:03:16,871 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_his_metric__a2923a_idx" ON "metrics_historicaldata" ("metric_id", "date"); (params None)
2024-08-05 23:03:16,892 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_name_c9d100_idx" ON "metrics_metric" ("name", "type"); (params None)
2024-08-05 23:03:16,911 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_7984a6_idx" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:03:16,935 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1bdb27_idx" ON "metrics_tag" ("name", "project_id"); (params None)
2024-08-05 23:03:16,954 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tar_metric__234682_idx" ON "metrics_target" ("metric_id", "target_date"); (params None)
2024-08-05 23:03:16,972 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tre_metric__d386bb_idx" ON "metrics_trend" ("metric_id", "start_date", "end_date"); (params None)
2024-08-05 23:03:16,998 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_con_from_me_9411ea_idx"; (params None)
2024-08-05 23:03:17,014 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:03:17,016 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:03:17,032 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_from_metric_id_aa131d91_uniq" UNIQUE ("tenant_id", "from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:03:17,036 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_project_id_4c1b22ec" ON "metrics_connection" ("project_id"); (params None)
2024-08-05 23:03:17,056 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; ALTER TABLE "metrics_connection" DROP CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id"; (params None)
2024-08-05 23:03:17,057 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "project_id" CASCADE; (params None)
2024-08-05 23:03:17,078 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:03:17,081 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:03:17,095 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:03:17,098 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_project_id_36bdbe46" ON "metrics_metric" ("project_id"); (params None)
2024-08-05 23:03:17,105 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_correlation" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "lag" integer NOT NULL, "pearson_correlation" double precision NOT NULL, "spearman_correlation" double precision NOT NULL); (params None)
2024-08-05 23:03:17,111 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:03:17,121 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dataqualityscore" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_entry" varchar(255) NOT NULL, "completeness_score" double precision NOT NULL, "accuracy_score" double precision NOT NULL, "consistency_score" double precision NOT NULL, "timeliness_score" double precision NOT NULL, "overall_score" double precision NOT NULL); (params None)
2024-08-05 23:03:17,128 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_impactanalysis" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "before_value" double precision NOT NULL, "after_value" double precision NOT NULL, "percentage_change" double precision NOT NULL, "confidence" double precision NOT NULL, "artifact_link" varchar(200) NOT NULL); (params None)
2024-08-05 23:03:17,136 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_insight" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "title" varchar(200) NOT NULL, "content" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:03:17,147 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metricmetadata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_source" varchar(100) NOT NULL, "source_url" varchar(200) NOT NULL, "rhythm" varchar(20) NOT NULL, "last_updated" timestamp with time zone NOT NULL, "technical_description" text NOT NULL, "description" text NOT NULL, "artifacts_url" varchar(200) NOT NULL, "hypothesis" text NOT NULL, "confidence" varchar(20) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL); (params None)
2024-08-05 23:03:17,156 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metrictarget" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "target_kpi" varchar(100) NOT NULL, "target_remarks" text NOT NULL, "target_date" date NULL, "target_value" double precision NULL); (params None)
2024-08-05 23:03:17,166 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_strategy" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "estimated_time" interval NOT NULL, "artifacts_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:03:17,176 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tacticalsolution" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "artifact_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:03:17,185 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_team" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:03:17,194 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_technicalindicator" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "stochastic_value" double precision NOT NULL, "rsi_value" double precision NOT NULL, "percent_change" double precision NOT NULL, "moving_average" double precision NOT NULL); (params None)
2024-08-05 23:03:17,202 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_timedimension" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL UNIQUE, "day" integer NOT NULL, "day_of_week" integer NOT NULL, "day_name" varchar(10) NOT NULL, "week" integer NOT NULL, "month" integer NOT NULL, "month_name" varchar(10) NOT NULL, "quarter" integer NOT NULL, "year" integer NOT NULL, "is_weekend" boolean NOT NULL, "is_holiday" boolean NOT NULL); (params None)
2024-08-05 23:03:17,211 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_userprofile" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY); (params None)
2024-08-05 23:03:17,239 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_metric_id_181e8748_fk_metrics_metric_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id"; (params None)
2024-08-05 23:03:17,240 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "metric_id" CASCADE; (params None)
2024-08-05 23:03:17,260 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id"; (params None)
2024-08-05 23:03:17,261 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:03:17,275 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_name_c9d100_idx"; (params None)
2024-08-05 23:03:17,288 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_last_up_7984a6_idx"; (params None)
2024-08-05 23:03:17,305 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" RENAME COLUMN "description" TO "summary"; (params None)
2024-08-05 23:03:17,322 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq"; (params None)
2024-08-05 23:03:17,337 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "correlation_coefficient" CASCADE; (params None)
2024-08-05 23:03:17,350 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" DROP COLUMN "results" CASCADE; (params None)
2024-08-05 23:03:17,364 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "anomaly_detected" CASCADE; (params None)
2024-08-05 23:03:17,378 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "forecasted_value" CASCADE; (params None)
2024-08-05 23:03:17,398 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "trend_component" CASCADE; (params None)
2024-08-05 23:03:17,420 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "importance" varchar(20) DEFAULT 'MEDIUM' NOT NULL; (params None)
2024-08-05 23:03:17,423 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "importance" DROP DEFAULT; (params None)
2024-08-05 23:03:17,482 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:03:17.481345+00:00' NOT NULL; (params None)
2024-08-05 23:03:17,484 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:03:17,524 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "anomaly_type" varchar(20) DEFAULT 'IGNORE' NOT NULL; (params None)
2024-08-05 23:03:17,531 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "anomaly_type" DROP DEFAULT; (params None)
2024-08-05 23:03:17,565 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "quality" varchar(20) DEFAULT 'LOW' NOT NULL; (params None)
2024-08-05 23:03:17,567 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "quality" DROP DEFAULT; (params None)
2024-08-05 23:03:17,608 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "impact_description" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:03:17,610 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "impact_description" DROP DEFAULT; (params None)
2024-08-05 23:03:17,631 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "objective" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:03:17,632 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "objective" DROP DEFAULT; (params None)
2024-08-05 23:03:17,652 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_date" date NULL; (params None)
2024-08-05 23:03:17,670 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_files" varchar(100) NULL; (params None)
2024-08-05 23:03:17,720 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_summary" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:03:17,722 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "result_summary" DROP DEFAULT; (params None)
2024-08-05 23:03:17,776 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_value" double precision NULL; (params None)
2024-08-05 23:03:17,803 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:03:17.802514+00:00' NOT NULL; (params None)
2024-08-05 23:03:17,805 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:03:17,835 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "variance" double precision NULL; (params None)
2024-08-05 23:03:17,856 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD COLUMN "forecast_id" bigint NULL CONSTRAINT "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" REFERENCES "metrics_forecast"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" IMMEDIATE; (params None)
2024-08-05 23:03:17,875 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "impact" TYPE varchar(20) USING "impact"::varchar(20); (params None)
2024-08-05 23:03:18,414 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "status" TYPE varchar(20); (params None)
2024-08-05 23:03:18,601 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric1_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:03:18,616 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric2_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:03:18,632 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:03:18,646 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:03:18,674 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:03:18,703 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:03:18,730 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:03:18,754 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "experiment_id" bigint NOT NULL CONSTRAINT "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" REFERENCES "metrics_experiment"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" IMMEDIATE; (params None)
2024-08-05 23:03:18,778 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:03:18,809 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:03:18,835 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:03:18,872 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:03:18,920 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "user_id" bigint NOT NULL CONSTRAINT "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:03:18,963 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "data_quality_score_id" bigint NULL UNIQUE CONSTRAINT "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" REFERENCES "metrics_dataqualityscore"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" IMMEDIATE; (params None)
2024-08-05 23:03:19,026 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "metric_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:03:19,074 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:03:19,138 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:03:19,174 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:03:19,213 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:03:19,647 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:03:19,704 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:03:19,742 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_team" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:03:19,778 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "team_id" bigint NOT NULL CONSTRAINT "metrics_strategy_team_id_f1781500_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_team_id_f1781500_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:03:19,814 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:03:19,848 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:03:19,883 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_experiment_team_id_537107e3_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_experiment_team_id_537107e3_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:03:19,929 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:03:19,974 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:03:20,007 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_timedimension" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:03:20,046 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:03:20,078 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "user_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:03:20,084 - django.db.backends.schema - DEBUG - DROP TABLE "metrics_target" CASCADE; (params None)
2024-08-05 23:03:20,109 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "confidence" CASCADE; (params None)
2024-08-05 23:03:20,136 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "description" CASCADE; (params None)
2024-08-05 23:03:20,161 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "hypothesis" CASCADE; (params None)
2024-08-05 23:03:20,186 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "last_updated" CASCADE; (params None)
2024-08-05 23:03:20,212 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_x" CASCADE; (params None)
2024-08-05 23:03:20,237 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_y" CASCADE; (params None)
2024-08-05 23:03:20,263 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "rhythm" CASCADE; (params None)
2024-08-05 23:03:20,285 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "source" CASCADE; (params None)
2024-08-05 23:03:20,649 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "technical_description" CASCADE; (params None)
2024-08-05 23:03:20,674 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD CONSTRAINT "metrics_correlation_tenant_id_metric1_id_met_49a4c34a_uniq" UNIQUE ("tenant_id", "metric1_id", "metric2_id", "lag"); (params None)
2024-08-05 23:03:20,701 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_metric__b85d3a_idx" ON "metrics_insight" ("metric_id", "date"); (params None)
2024-08-05 23:03:20,730 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_user_id_1ebb42_idx" ON "metrics_insight" ("user_id", "date"); (params None)
2024-08-05 23:03:20,755 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_metric__a2b705_idx" ON "metrics_metrictarget" ("metric_id", "target_date"); (params None)
2024-08-05 23:03:20,782 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_6e2e67_idx" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:03:20,809 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_date_53cb14_idx" ON "metrics_timedimension" ("date"); (params None)
2024-08-05 23:03:20,835 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_year_92da9e_idx" ON "metrics_timedimension" ("year", "month", "day"); (params None)
2024-08-05 23:03:20,839 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_username_6e55f358_like" ON "metrics_customuser" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:03:20,842 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_date_ded95ba1" ON "metrics_insight" ("date"); (params None)
2024-08-05 23:03:20,846 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_last_updated_76599a1b" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:03:20,849 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_target_date_38cd9191" ON "metrics_metrictarget" ("target_date"); (params None)
2024-08-05 23:03:20,851 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_forecast_id_29590c29" ON "metrics_historicaldata" ("forecast_id"); (params None)
2024-08-05 23:03:20,854 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric1_id_6e1c2404" ON "metrics_correlation" ("metric1_id"); (params None)
2024-08-05 23:03:20,857 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric2_id_f2cc46dd" ON "metrics_correlation" ("metric2_id"); (params None)
2024-08-05 23:03:20,860 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_tenant_id_a00a5169" ON "metrics_correlation" ("tenant_id"); (params None)
2024-08-05 23:03:20,863 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_customuser_id_group_id_1c5fc435_uniq" UNIQUE ("customuser_id", "group_id"); (params None)
2024-08-05 23:03:20,866 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_g_customuser_id_fc13f3af_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:20,868 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_group_id_6b097e12_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:20,869 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_customuser_id_fc13f3af" ON "metrics_customuser_groups" ("customuser_id"); (params None)
2024-08-05 23:03:20,872 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_group_id_6b097e12" ON "metrics_customuser_groups" ("group_id"); (params None)
2024-08-05 23:03:20,874 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_tenant_id_02b7403c" ON "metrics_customuser" ("tenant_id"); (params None)
2024-08-05 23:03:20,878 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_user__customuser_id_permission_68cc320f_uniq" UNIQUE ("customuser_id", "permission_id"); (params None)
2024-08-05 23:03:20,882 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_customuser_id_46e97f00_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:20,883 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_permission_id_d66d657c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:20,884 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_customuser_id_46e97f00" ON "metrics_customuser_user_permissions" ("customuser_id"); (params None)
2024-08-05 23:03:20,887 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_permission_id_d66d657c" ON "metrics_customuser_user_permissions" ("permission_id"); (params None)
2024-08-05 23:03:20,890 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_tenant_id_8e9f296d" ON "metrics_dataqualityscore" ("tenant_id"); (params None)
2024-08-05 23:03:20,894 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_experiment_id_1beae7fe" ON "metrics_impactanalysis" ("experiment_id"); (params None)
2024-08-05 23:03:20,897 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_metric_id_f4b9eeb6" ON "metrics_impactanalysis" ("metric_id"); (params None)
2024-08-05 23:03:20,901 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_tenant_id_126ca20d" ON "metrics_impactanalysis" ("tenant_id"); (params None)
2024-08-05 23:03:20,904 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_metric_id_26d3a9d8" ON "metrics_insight" ("metric_id"); (params None)
2024-08-05 23:03:20,907 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_tenant_id_724d7d85" ON "metrics_insight" ("tenant_id"); (params None)
2024-08-05 23:03:20,910 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_user_id_83d421e1" ON "metrics_insight" ("user_id"); (params None)
2024-08-05 23:03:20,912 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_tenant_id_3277f967" ON "metrics_metricmetadata" ("tenant_id"); (params None)
2024-08-05 23:03:20,916 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_metric_id_7876e2c8" ON "metrics_metrictarget" ("metric_id"); (params None)
2024-08-05 23:03:20,920 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_tenant_id_b26a17f8" ON "metrics_metrictarget" ("tenant_id"); (params None)
2024-08-05 23:03:20,923 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_tenant_id_1323395e" ON "metrics_strategy" ("tenant_id"); (params None)
2024-08-05 23:03:20,928 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_metric_id_9887ffa4" ON "metrics_tacticalsolution" ("metric_id"); (params None)
2024-08-05 23:03:20,932 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_tenant_id_cf9028f0" ON "metrics_tacticalsolution" ("tenant_id"); (params None)
2024-08-05 23:03:20,936 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_team_tenant_id_3a14c47d" ON "metrics_team" ("tenant_id"); (params None)
2024-08-05 23:03:20,938 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_team_id_f1781500" ON "metrics_strategy" ("team_id"); (params None)
2024-08-05 23:03:20,941 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_team_id_f140658d" ON "metrics_metricmetadata" ("team_id"); (params None)
2024-08-05 23:03:20,945 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_team_id_4c4ffc18" ON "metrics_customuser" ("team_id"); (params None)
2024-08-05 23:03:20,948 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_team_id_537107e3" ON "metrics_experiment" ("team_id"); (params None)
2024-08-05 23:03:20,951 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_metric_id_3e2eead6" ON "metrics_technicalindicator" ("metric_id"); (params None)
2024-08-05 23:03:20,954 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_tenant_id_f4de3b44" ON "metrics_technicalindicator" ("tenant_id"); (params None)
2024-08-05 23:03:20,957 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_timedimension_tenant_id_f375bb45" ON "metrics_timedimension" ("tenant_id"); (params None)
2024-08-05 23:03:20,961 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_userprofile_tenant_id_cca71dae" ON "metrics_userprofile" ("tenant_id"); (params None)
2024-08-05 23:03:20,991 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "strength" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:03:20,993 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "strength" DROP DEFAULT; (params None)
2024-08-05 23:03:21,016 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "lower_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:03:21,017 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "lower_bound" DROP DEFAULT; (params None)
2024-08-05 23:03:21,043 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "upper_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:03:21,044 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "upper_bound" DROP DEFAULT; (params None)
2024-08-05 23:03:21,067 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD COLUMN "slope" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:03:21,069 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ALTER COLUMN "slope" DROP DEFAULT; (params None)
2024-08-05 23:03:21,099 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_movingaverage" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "ma_type" varchar(10) NOT NULL, "period" integer NOT NULL, "value" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:03:21,139 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_networkanalysisresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "analysis_type" varchar(20) NOT NULL, "result" jsonb NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:03:21,180 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_seasonalityresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "seasonality_type" varchar(20) NOT NULL, "strength" double precision NOT NULL, "period" integer NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:03:21,217 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trendchangepoint" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "change_type" varchar(20) NOT NULL, "significance" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:03:21,222 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD CONSTRAINT "metrics_movingaverage_metric_id_7c61cebf_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:21,225 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_metric_id_7c61cebf" ON "metrics_movingaverage" ("metric_id"); (params None)
2024-08-05 23:03:21,229 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD CONSTRAINT "metrics_networkanaly_metric_id_a4c90102_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:21,231 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_metric_id_a4c90102" ON "metrics_networkanalysisresult" ("metric_id"); (params None)
2024-08-05 23:03:21,234 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityr_metric_id_6e494791_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:21,235 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_metric_id_6e494791" ON "metrics_seasonalityresult" ("metric_id"); (params None)
2024-08-05 23:03:21,238 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD CONSTRAINT "metrics_trendchangep_metric_id_f8eb9f76_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:03:21,240 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_metric_id_f8eb9f76" ON "metrics_trendchangepoint" ("metric_id"); (params None)
2024-08-05 23:03:21,277 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:03:21,280 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:03:21,317 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" IMMEDIATE; (params None)
2024-08-05 23:03:21,319 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:03:21,350 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ALTER COLUMN "value" DROP NOT NULL; (params None)
2024-08-05 23:03:21,376 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD CONSTRAINT "metrics_dataqualityscore_tenant_id_metric_id_proj_66b9fb01_uniq" UNIQUE ("tenant_id", "metric_id", "project_id"); (params None)
2024-08-05 23:03:21,380 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_metric_id_1b6367d1" ON "metrics_dataqualityscore" ("metric_id"); (params None)
2024-08-05 23:03:21,383 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_project_id_123a4f58" ON "metrics_dataqualityscore" ("project_id"); (params None)
2024-08-05 23:03:21,768 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:03:21,810 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:03:21,812 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:03:21,848 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:03:21,851 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:03:21,887 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:03:21,889 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:03:21,919 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:03:21,921 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:03:21,950 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq" UNIQUE ("tenant_id", "metric_id"); (params None)
2024-08-05 23:03:21,954 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_tenant_id_5a9de228" ON "metrics_movingaverage" ("tenant_id"); (params None)
2024-08-05 23:03:21,958 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_tenant_id_16a6ba09" ON "metrics_networkanalysisresult" ("tenant_id"); (params None)
2024-08-05 23:03:21,962 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_tenant_id_ca2da3fd" ON "metrics_seasonalityresult" ("tenant_id"); (params None)
2024-08-05 23:03:21,964 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_tenant_id_da10d898" ON "metrics_trendchangepoint" ("tenant_id"); (params None)
2024-08-05 23:03:22,000 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:03:22,002 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:03:22,003 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_metric_id_c86f5720" ON "metrics_report" ("metric_id"); (params None)
2024-08-05 23:03:22,033 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "analysis_result" jsonb NULL; (params None)
2024-08-05 23:03:22,061 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "anomaly_result" jsonb NULL; (params None)
2024-08-05 23:03:22,087 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:03:22.087383+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:03:22,089 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:03:22,115 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "forecast_result" jsonb NULL; (params None)
2024-08-05 23:03:22,141 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "relationship_result" jsonb NULL; (params None)
2024-08-05 23:03:22,170 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "report" text DEFAULT '1' NOT NULL; (params None)
2024-08-05 23:03:22,172 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "report" DROP DEFAULT; (params None)
2024-08-05 23:03:22,203 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "updated_at" timestamp with time zone DEFAULT '2024-08-05T23:03:22.202991+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:03:22,204 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "updated_at" DROP DEFAULT; (params None)
2024-08-05 23:03:22,288 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_trendchangepoint" DROP CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c"; (params None)
2024-08-05 23:03:22,289 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:03:22,311 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "significance" DROP NOT NULL; (params None)
2024-08-05 23:03:22,335 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" RENAME COLUMN "change_type" TO "direction"; (params None)
2024-08-05 23:03:22,724 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:03:22.723756+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:03:22,725 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:03:22,761 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq"; (params None)
2024-08-05 23:03:22,763 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresul_metric_id_seasonality_ty_d3492b78_uniq" UNIQUE ("metric_id", "seasonality_type"); (params None)
2024-08-05 23:03:22,807 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c"; (params None)
2024-08-05 23:03:22,808 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:03:22,813 - django.db.backends.schema - DEBUG - CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:03:22,821 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" ("session_key" varchar_pattern_ops); (params None)
2024-08-05 23:03:22,826 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date"); (params None)
2024-08-05 23:03:24,164 - metrics.computations.data_preparation - INFO - Loaded metric 13 for tenant 7 and project 7
2024-08-05 23:03:24,165 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 13
2024-08-05 23:03:24,166 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:24,166 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:24,168 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 13
2024-08-05 23:03:24,175 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:24,175 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:03:24,179 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:24,180 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:24,183 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:24,184 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:03:24,189 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:03:28,283 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 13
2024-08-05 23:03:28,287 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:03:28,290 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:03:28,290 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:03:28,294 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:28,294 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:03:28,298 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:28,302 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37075950656866563, Timeliness: nan
2024-08-05 23:03:28,302 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.69198355228885
2024-08-05 23:03:28,310 - metrics.computations.data_preparation - INFO - Data quality score: 45.69198355228885
2024-08-05 23:03:28,492 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 13, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.69198355228885, 'outliers_handled': True, 'profile': {'mean': 99.7507557182948, 'median': 99.90618515353746, 'std': 9.771907731172034, 'min': 75.28548453778413, 'max': 122.20707725779151, 'skewness': -0.0798012610126702, 'kurtosis': -0.23813044891507973, 'missing_percentage': 0.0}}
2024-08-05 23:03:28,497 - metrics.computations.data_preparation - INFO - Loaded metric 13 for tenant 7 and project 7
2024-08-05 23:03:28,498 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 13
2024-08-05 23:03:28,500 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:28,501 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:28,504 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 13
2024-08-05 23:03:28,531 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:28,533 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:03:28,551 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:28,551 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:28,558 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:28,559 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:03:28,563 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:03:33,931 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 13
2024-08-05 23:03:33,934 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:03:33,937 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:03:33,938 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:03:33,941 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:33,942 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:03:33,945 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:33,948 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37075950656866563, Timeliness: nan
2024-08-05 23:03:33,948 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.69198355228885
2024-08-05 23:03:33,953 - metrics.computations.data_preparation - INFO - Data quality score: 45.69198355228885
2024-08-05 23:03:34,075 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 13, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.69198355228885, 'outliers_handled': True, 'profile': {'mean': 99.7507557182948, 'median': 99.90618515353746, 'std': 9.771907731172034, 'min': 75.28548453778413, 'max': 122.20707725779151, 'skewness': -0.0798012610126702, 'kurtosis': -0.23813044891507973, 'missing_percentage': 0.0}}
2024-08-05 23:03:34,076 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:03:34,076 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 13
2024-08-05 23:03:34,086 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:03:34,092 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:03:34,098 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 13
2024-08-05 23:03:34,099 - metrics.computations.feature_engineering - INFO - Parameters for metric 13: dynamic
2024-08-05 23:03:34,099 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 13: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:03:34,103 - metrics.computations.data_preparation - INFO - Loaded metric 13 for tenant 7 and project 7
2024-08-05 23:03:34,104 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 13
2024-08-05 23:03:34,105 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:34,106 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:34,109 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 13
2024-08-05 23:03:34,118 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:34,118 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:03:34,123 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:34,124 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:34,130 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:34,131 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:03:34,137 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:03:38,510 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 13
2024-08-05 23:03:38,513 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:03:38,517 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:03:38,517 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:03:38,523 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:38,523 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:03:38,529 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:38,534 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37075950656866563, Timeliness: nan
2024-08-05 23:03:38,534 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.69198355228885
2024-08-05 23:03:38,540 - metrics.computations.data_preparation - INFO - Data quality score: 45.69198355228885
2024-08-05 23:03:39,174 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 13, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.69198355228885, 'outliers_handled': True, 'profile': {'mean': 99.7507557182948, 'median': 99.90618515353746, 'std': 9.771907731172034, 'min': 75.28548453778413, 'max': 122.20707725779151, 'skewness': -0.0798012610126702, 'kurtosis': -0.23813044891507973, 'missing_percentage': 0.0}}
2024-08-05 23:03:39,182 - metrics.computations.data_preparation - INFO - Loaded metric 13 for tenant 7 and project 7
2024-08-05 23:03:39,183 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 13
2024-08-05 23:03:39,184 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:39,185 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:39,189 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 13
2024-08-05 23:03:39,202 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:39,203 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:03:39,207 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:39,208 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:39,213 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:39,214 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:03:39,220 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:03:43,186 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 13
2024-08-05 23:03:43,191 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:03:43,196 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:03:43,197 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:03:43,201 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:43,201 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:03:43,207 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   88.882249          7
2023-01-02   88.270332          7
2023-01-03  105.519390          7
2023-01-04   94.362032          7
2023-01-05  108.460997          7
2024-08-05 23:03:43,210 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37075950656866563, Timeliness: nan
2024-08-05 23:03:43,210 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.69198355228885
2024-08-05 23:03:43,215 - metrics.computations.data_preparation - INFO - Data quality score: 45.69198355228885
2024-08-05 23:03:43,404 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 13, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.69198355228885, 'outliers_handled': True, 'profile': {'mean': 99.7507557182948, 'median': 99.90618515353746, 'std': 9.771907731172034, 'min': 75.28548453778413, 'max': 122.20707725779151, 'skewness': -0.0798012610126702, 'kurtosis': -0.23813044891507973, 'missing_percentage': 0.0}}
2024-08-05 23:03:43,405 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:03:43,406 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 13
2024-08-05 23:03:43,414 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:03:43,421 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:03:43,427 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 13
2024-08-05 23:03:43,428 - metrics.computations.feature_engineering - INFO - Parameters for metric 13: dynamic
2024-08-05 23:03:43,428 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 13: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:03:43,429 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Setup completed
2024-08-05 23:03:43,434 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:03:43,435 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:03:43,436 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:43,436 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:43,438 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:03:43,445 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:43,446 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:03:43,457 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:43,457 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:43,461 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:43,462 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:03:43,471 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:03:46,526 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:03:46,529 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:03:46,531 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:03:46,531 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:03:46,534 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:46,534 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:03:46,536 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:46,538 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3707595065686656, Timeliness: nan
2024-08-05 23:03:46,539 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.69198355228885
2024-08-05 23:03:46,543 - metrics.computations.data_preparation - INFO - Data quality score: 45.69198355228885
2024-08-05 23:03:46,639 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.69198355228885, 'outliers_handled': True, 'profile': {'mean': 109.72583129012429, 'median': 109.89680366889121, 'std': 10.749098504289238, 'min': 82.81403299156256, 'max': 134.4277849835707, 'skewness': -0.07980126101267095, 'kurtosis': -0.23813044891507928, 'missing_percentage': 0.0}}
2024-08-05 23:03:46,642 - metrics.computations.computations_relationships - INFO - Calculated pearson correlation between metrics 13 and 14
2024-08-05 23:03:46,644 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:03:46,644 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:03:46,645 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:46,652 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:46,657 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:03:46,670 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:46,671 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:03:46,677 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:46,677 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:46,683 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:46,684 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:03:46,688 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:03:49,603 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:03:49,606 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:03:49,609 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:03:49,609 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:03:49,613 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:49,614 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:03:49,616 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:49,619 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3707595065686656, Timeliness: nan
2024-08-05 23:03:49,620 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.69198355228885
2024-08-05 23:03:49,624 - metrics.computations.data_preparation - INFO - Data quality score: 45.69198355228885
2024-08-05 23:03:49,701 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.69198355228885, 'outliers_handled': True, 'profile': {'mean': 109.72583129012429, 'median': 109.89680366889121, 'std': 10.749098504289238, 'min': 82.81403299156256, 'max': 134.4277849835707, 'skewness': -0.07980126101267095, 'kurtosis': -0.23813044891507928, 'missing_percentage': 0.0}}
2024-08-05 23:03:49,704 - metrics.computations.computations_relationships - INFO - Calculated spearman correlation between metrics 13 and 14
2024-08-05 23:03:49,737 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:03:49,737 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:03:49,738 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:49,739 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:49,742 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:03:49,750 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:49,751 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:03:49,755 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:49,755 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:49,758 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:49,759 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:03:49,763 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:03:52,782 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:03:52,785 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:03:52,787 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:03:52,787 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:03:52,791 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:52,791 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:03:52,793 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:52,796 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3707595065686656, Timeliness: nan
2024-08-05 23:03:52,797 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.69198355228885
2024-08-05 23:03:52,801 - metrics.computations.data_preparation - INFO - Data quality score: 45.69198355228885
2024-08-05 23:03:52,993 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.69198355228885, 'outliers_handled': True, 'profile': {'mean': 109.72583129012429, 'median': 109.89680366889121, 'std': 10.749098504289238, 'min': 82.81403299156256, 'max': 134.4277849835707, 'skewness': -0.07980126101267095, 'kurtosis': -0.23813044891507928, 'missing_percentage': 0.0}}
2024-08-05 23:03:52,996 - metrics.computations.computations_relationships - INFO - Calculated pearson correlation between metrics 13 and 14
2024-08-05 23:03:53,003 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:03:53,004 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:03:53,006 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:53,007 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:53,011 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:03:53,022 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:53,023 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:03:53,027 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:53,027 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:53,031 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:53,032 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:03:53,041 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:03:56,328 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:03:56,331 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:03:56,333 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:03:56,333 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:03:56,336 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:56,337 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:03:56,340 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:56,343 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3707595065686656, Timeliness: nan
2024-08-05 23:03:56,343 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.69198355228885
2024-08-05 23:03:56,347 - metrics.computations.data_preparation - INFO - Data quality score: 45.69198355228885
2024-08-05 23:03:56,400 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.69198355228885, 'outliers_handled': True, 'profile': {'mean': 109.72583129012429, 'median': 109.89680366889121, 'std': 10.749098504289238, 'min': 82.81403299156256, 'max': 134.4277849835707, 'skewness': -0.07980126101267095, 'kurtosis': -0.23813044891507928, 'missing_percentage': 0.0}}
2024-08-05 23:03:56,403 - metrics.computations.computations_relationships - INFO - Calculated spearman correlation between metrics 13 and 14
2024-08-05 23:03:56,412 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:03:56,412 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:03:56,413 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:56,413 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:56,418 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:03:56,436 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:56,436 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:03:56,440 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:56,440 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:56,446 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:56,447 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:03:56,450 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:03:59,508 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:03:59,511 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:03:59,513 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:03:59,514 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:03:59,517 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:59,517 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:03:59,520 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:59,523 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3707595065686656, Timeliness: nan
2024-08-05 23:03:59,523 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.69198355228885
2024-08-05 23:03:59,527 - metrics.computations.data_preparation - INFO - Data quality score: 45.69198355228885
2024-08-05 23:03:59,720 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.69198355228885, 'outliers_handled': True, 'profile': {'mean': 109.72583129012429, 'median': 109.89680366889121, 'std': 10.749098504289238, 'min': 82.81403299156256, 'max': 134.4277849835707, 'skewness': -0.07980126101267095, 'kurtosis': -0.23813044891507928, 'missing_percentage': 0.0}}
2024-08-05 23:03:59,724 - metrics.computations.computations_relationships - INFO - Calculated pearson correlation between metrics 13 and 14
2024-08-05 23:03:59,735 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:03:59,735 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:03:59,737 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:59,738 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:03:59,747 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:03:59,771 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:59,772 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:03:59,778 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:59,779 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:03:59,784 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:03:59,786 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:03:59,793 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:04:03,039 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:04:03,043 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:04:03,045 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:04:03,046 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:04:03,049 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:04:03,049 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:04:03,052 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:04:03,055 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3707595065686656, Timeliness: nan
2024-08-05 23:04:03,056 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.69198355228885
2024-08-05 23:04:03,059 - metrics.computations.data_preparation - INFO - Data quality score: 45.69198355228885
2024-08-05 23:04:03,208 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.69198355228885, 'outliers_handled': True, 'profile': {'mean': 109.72583129012429, 'median': 109.89680366889121, 'std': 10.749098504289238, 'min': 82.81403299156256, 'max': 134.4277849835707, 'skewness': -0.07980126101267095, 'kurtosis': -0.23813044891507928, 'missing_percentage': 0.0}}
2024-08-05 23:04:03,211 - metrics.computations.computations_relationships - INFO - Calculated spearman correlation between metrics 13 and 14
2024-08-05 23:04:03,214 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:04:03,214 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:04:03,215 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:04:03,217 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:04:03,225 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:04:03,242 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:04:03,243 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:04:03,247 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:04:03,247 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:04:03,252 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:04:03,253 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:04:03,257 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:04:06,208 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:04:06,211 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:04:06,213 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:04:06,213 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:04:06,218 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:04:06,218 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:04:06,223 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:04:06,228 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3707595065686656, Timeliness: nan
2024-08-05 23:04:06,228 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.69198355228885
2024-08-05 23:04:06,235 - metrics.computations.data_preparation - INFO - Data quality score: 45.69198355228885
2024-08-05 23:04:06,383 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.69198355228885, 'outliers_handled': True, 'profile': {'mean': 109.72583129012429, 'median': 109.89680366889121, 'std': 10.749098504289238, 'min': 82.81403299156256, 'max': 134.4277849835707, 'skewness': -0.07980126101267095, 'kurtosis': -0.23813044891507928, 'missing_percentage': 0.0}}
2024-08-05 23:04:06,395 - metrics.computations.computations_relationships - INFO - Calculated pearson correlation between metrics 13 and 14
2024-08-05 23:04:06,402 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:04:06,404 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:04:06,405 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:04:06,406 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:04:06,416 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:04:06,435 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:04:06,436 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:04:06,442 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:04:06,443 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:04:06,448 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:04:06,451 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:04:06,456 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:04:10,291 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:04:10,295 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:04:10,297 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:04:10,298 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:04:10,302 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:04:10,303 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:04:10,307 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   97.770474          7
2023-01-02   97.097366          7
2023-01-03  116.071329          7
2023-01-04  103.798235          7
2023-01-05  119.307096          7
2024-08-05 23:04:10,310 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3707595065686656, Timeliness: nan
2024-08-05 23:04:10,310 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.69198355228885
2024-08-05 23:04:10,317 - metrics.computations.data_preparation - INFO - Data quality score: 45.69198355228885
2024-08-05 23:04:10,468 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.69198355228885, 'outliers_handled': True, 'profile': {'mean': 109.72583129012429, 'median': 109.89680366889121, 'std': 10.749098504289238, 'min': 82.81403299156256, 'max': 134.4277849835707, 'skewness': -0.07980126101267095, 'kurtosis': -0.23813044891507928, 'missing_percentage': 0.0}}
2024-08-05 23:04:10,472 - metrics.computations.computations_relationships - INFO - Calculated spearman correlation between metrics 13 and 14
2024-08-05 23:04:10,473 - metrics.computations.computations_relationships - ERROR - Error analyzing connections for metric 13: 'Metric' object has no attribute 'connections_from'
2024-08-05 23:04:10,697 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Teardown completed
```

