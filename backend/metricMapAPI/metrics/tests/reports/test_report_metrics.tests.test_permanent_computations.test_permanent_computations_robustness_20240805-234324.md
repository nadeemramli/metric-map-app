# Test Run: metrics.tests.test_permanent_computations.test_permanent_computations_robustness

Total tests: 7
Passed: 2
Failed: 4
Errors: 1

## test_computation_with_extreme_values (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
Status: failure
Duration: 16.698 seconds

### Failure
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_permanent_computations_robustness.py", line 143, in test_computation_with_extreme_values
    self.assertIsInstance(anomalies, dict)
AssertionError: Empty DataFrame
Columns: [date, value, anomaly_score, type]
Index: [] is not an instance of <class 'dict'>
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
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
2024-08-05 23:41:17,550 - metrics - DEBUG - Starting test: test_computation_with_extreme_values (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
2024-08-05 23:41:17,554 - django.db.backends.schema - DEBUG - CREATE TABLE "django_migrations" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:17,568 - django.db.backends.schema - DEBUG - CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
2024-08-05 23:41:17,571 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params None)
2024-08-05 23:41:17,576 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL, "codename" varchar(100) NOT NULL); (params None)
2024-08-05 23:41:17,581 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(80) NOT NULL UNIQUE); (params None)
2024-08-05 23:41:17,585 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:41:17,592 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NOT NULL, "is_superuser" boolean NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:17,597 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:41:17,600 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:41:17,602 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename"); (params None)
2024-08-05 23:41:17,604 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,605 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id"); (params None)
2024-08-05 23:41:17,608 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_name_a6ea08ec_like" ON "auth_group" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:17,611 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id"); (params None)
2024-08-05 23:41:17,613 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,614 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,616 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id"); (params None)
2024-08-05 23:41:17,618 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id"); (params None)
2024-08-05 23:41:17,620 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_username_6821ab7c_like" ON "auth_user" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:41:17,623 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id"); (params None)
2024-08-05 23:41:17,625 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,626 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,627 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id"); (params None)
2024-08-05 23:41:17,629 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id"); (params None)
2024-08-05 23:41:17,631 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id"); (params None)
2024-08-05 23:41:17,633 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,635 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,635 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id"); (params None)
2024-08-05 23:41:17,638 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id"); (params None)
2024-08-05 23:41:17,645 - django.db.backends.schema - DEBUG - CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "action_time" timestamp with time zone NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL, "user_id" integer NOT NULL); (params None)
2024-08-05 23:41:17,650 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,651 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,652 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id"); (params None)
2024-08-05 23:41:17,655 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id"); (params None)
2024-08-05 23:41:17,672 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ALTER COLUMN "name" DROP NOT NULL; (params None)
2024-08-05 23:41:17,680 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" DROP COLUMN "name" CASCADE; (params None)
2024-08-05 23:41:17,686 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ALTER COLUMN "name" TYPE varchar(255); (params None)
2024-08-05 23:41:17,692 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "email" TYPE varchar(254); (params None)
2024-08-05 23:41:17,704 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_login" DROP NOT NULL; (params None)
2024-08-05 23:41:17,716 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "username" TYPE varchar(150); (params None)
2024-08-05 23:41:17,725 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_name" TYPE varchar(150); (params None)
2024-08-05 23:41:17,732 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group" ALTER COLUMN "name" TYPE varchar(150); (params None)
2024-08-05 23:41:17,745 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "first_name" TYPE varchar(150); (params None)
2024-08-05 23:41:17,775 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_client" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "schema_name" varchar(63) NOT NULL UNIQUE, "name" varchar(100) NOT NULL, "created_on" date NOT NULL); (params None)
2024-08-05 23:41:17,782 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_category" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,786 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dashboard" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "layout" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,795 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_domain" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "domain" varchar(253) NOT NULL UNIQUE, "is_primary" boolean NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,802 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "type" varchar(50) NOT NULL, "confidence" varchar(50) NOT NULL, "value_type" varchar(20) NOT NULL, "rhythm" varchar(20) NOT NULL, "description" text NOT NULL, "hypothesis" text NOT NULL, "technical_description" text NOT NULL, "last_updated" timestamp with time zone NOT NULL, "source" varchar(100) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL, "category_id" bigint NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,811 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_historicaldata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "value" double precision NOT NULL, "forecasted_value" double precision NULL, "anomaly_detected" boolean NOT NULL, "trend_component" varchar(50) NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,818 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_forecast" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "forecast_date" date NOT NULL, "forecast_value" double precision NOT NULL, "model_used" varchar(100) NOT NULL, "accuracy" double precision NULL, "confidence_interval" jsonb NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,828 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "status" varchar(50) NOT NULL, "results" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,832 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment_metrics" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "experiment_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,842 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_connection" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "relationship" varchar(100) NOT NULL, "correlation_coefficient" double precision NULL, "tenant_id" bigint NOT NULL, "from_metric_id" bigint NOT NULL, "to_metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,851 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_anomaly" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "detection_date" date NOT NULL, "anomaly_value" double precision NOT NULL, "anomaly_score" double precision NOT NULL, "notes" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,864 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_actionremark" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NULL, "description" text NOT NULL, "impact" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,876 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_project" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "created_on" date NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,886 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_report" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "configuration" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,900 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tag" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "project_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,913 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric_tags" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "metric_id" bigint NOT NULL, "tag_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,929 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_target" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "remarks" text NOT NULL, "target_kpi" varchar(100) NOT NULL, "target_date" date NULL, "target_value" double precision NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,945 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trend" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "trend_type" varchar(50) NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "trend_value" double precision NOT NULL, "notes" text NOT NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:17,952 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_schema_name_87d6fbb5_like" ON "metrics_client" ("schema_name" varchar_pattern_ops); (params None)
2024-08-05 23:41:17,955 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_category" ADD CONSTRAINT "metrics_category_tenant_id_67d98cc6_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,957 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_tenant_id_67d98cc6" ON "metrics_category" ("tenant_id"); (params None)
2024-08-05 23:41:17,959 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ADD CONSTRAINT "metrics_dashboard_tenant_id_50099a7d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,960 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_tenant_id_50099a7d" ON "metrics_dashboard" ("tenant_id"); (params None)
2024-08-05 23:41:17,962 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_domain" ADD CONSTRAINT "metrics_domain_tenant_id_259fb21f_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,963 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_domain_bdc97b86_like" ON "metrics_domain" ("domain" varchar_pattern_ops); (params None)
2024-08-05 23:41:17,966 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_is_primary_ac9d2eaf" ON "metrics_domain" ("is_primary"); (params None)
2024-08-05 23:41:17,969 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_tenant_id_259fb21f" ON "metrics_domain" ("tenant_id"); (params None)
2024-08-05 23:41:17,971 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_category_id_8793f683_fk_metrics_category_id" FOREIGN KEY ("category_id") REFERENCES "metrics_category" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,972 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_9606b577_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,973 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_category_id_8793f683" ON "metrics_metric" ("category_id"); (params None)
2024-08-05 23:41:17,976 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tenant_id_9606b577" ON "metrics_metric" ("tenant_id"); (params None)
2024-08-05 23:41:17,978 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_tenant_id_438c5ad4_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,979 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_metric_id_3f9e8174_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,980 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_tenant_id_438c5ad4" ON "metrics_historicaldata" ("tenant_id"); (params None)
2024-08-05 23:41:17,983 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_metric_id_3f9e8174" ON "metrics_historicaldata" ("metric_id"); (params None)
2024-08-05 23:41:17,985 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_tenant_id_92d37185_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,986 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_metric_id_e05f23a8_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,987 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_tenant_id_92d37185" ON "metrics_forecast" ("tenant_id"); (params None)
2024-08-05 23:41:17,989 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_metric_id_e05f23a8" ON "metrics_forecast" ("metric_id"); (params None)
2024-08-05 23:41:17,991 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD CONSTRAINT "metrics_experiment_tenant_id_10fa364a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,993 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_tenant_id_10fa364a" ON "metrics_experiment" ("tenant_id"); (params None)
2024-08-05 23:41:17,995 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_metri_experiment_id_metric_id_a9d54b29_uniq" UNIQUE ("experiment_id", "metric_id"); (params None)
2024-08-05 23:41:17,997 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_experiment_id_372c6b59_fk_metrics_e" FOREIGN KEY ("experiment_id") REFERENCES "metrics_experiment" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,998 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_metric_id_c8f84167_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:17,999 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_experiment_id_372c6b59" ON "metrics_experiment_metrics" ("experiment_id"); (params None)
2024-08-05 23:41:18,002 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_metric_id_c8f84167" ON "metrics_experiment_metrics" ("metric_id"); (params None)
2024-08-05 23:41:18,004 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_2e1e5750_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,005 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_from_metric_id_33b50521_fk_metrics_metric_id" FOREIGN KEY ("from_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,006 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_to_metric_id_94489c1c_fk_metrics_metric_id" FOREIGN KEY ("to_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,007 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_tenant_id_2e1e5750" ON "metrics_connection" ("tenant_id"); (params None)
2024-08-05 23:41:18,009 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_from_metric_id_33b50521" ON "metrics_connection" ("from_metric_id"); (params None)
2024-08-05 23:41:18,011 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_to_metric_id_94489c1c" ON "metrics_connection" ("to_metric_id"); (params None)
2024-08-05 23:41:18,013 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_tenant_id_9e474130_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,014 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_metric_id_1b3c3295_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,015 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_tenant_id_9e474130" ON "metrics_anomaly" ("tenant_id"); (params None)
2024-08-05 23:41:18,017 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_metric_id_1b3c3295" ON "metrics_anomaly" ("metric_id"); (params None)
2024-08-05 23:41:18,020 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_tenant_id_86ffa3a9_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,021 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_metric_id_c1b270f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,023 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_tenant_id_86ffa3a9" ON "metrics_actionremark" ("tenant_id"); (params None)
2024-08-05 23:41:18,025 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_metric_id_c1b270f2" ON "metrics_actionremark" ("metric_id"); (params None)
2024-08-05 23:41:18,027 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_project" ADD CONSTRAINT "metrics_project_tenant_id_db4a1170_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,028 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_tenant_id_db4a1170" ON "metrics_project" ("tenant_id"); (params None)
2024-08-05 23:41:18,030 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD CONSTRAINT "metrics_report_tenant_id_d1cf4812_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,031 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_tenant_id_d1cf4812" ON "metrics_report" ("tenant_id"); (params None)
2024-08-05 23:41:18,034 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_name_project_id_2d57d4da_uniq" UNIQUE ("name", "project_id"); (params None)
2024-08-05 23:41:18,036 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_project_id_b7ac5c8e_fk_metrics_project_id" FOREIGN KEY ("project_id") REFERENCES "metrics_project" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,037 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_tenant_id_c286653b_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,038 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_project_id_b7ac5c8e" ON "metrics_tag" ("project_id"); (params None)
2024-08-05 23:41:18,040 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_tenant_id_c286653b" ON "metrics_tag" ("tenant_id"); (params None)
2024-08-05 23:41:18,042 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_tag_id_a8e1a165_uniq" UNIQUE ("metric_id", "tag_id"); (params None)
2024-08-05 23:41:18,044 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_b2a068f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,045 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_tag_id_61869f56_fk_metrics_tag_id" FOREIGN KEY ("tag_id") REFERENCES "metrics_tag" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,046 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_metric_id_b2a068f2" ON "metrics_metric_tags" ("metric_id"); (params None)
2024-08-05 23:41:18,049 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_tag_id_61869f56" ON "metrics_metric_tags" ("tag_id"); (params None)
2024-08-05 23:41:18,051 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,052 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,053 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_metric_id_181e8748" ON "metrics_target" ("metric_id"); (params None)
2024-08-05 23:41:18,055 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_tenant_id_118eb54a" ON "metrics_target" ("tenant_id"); (params None)
2024-08-05 23:41:18,057 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_metric_id_25179b98_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,058 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_tenant_id_4cb1485d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:18,059 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_metric_id_25179b98" ON "metrics_trend" ("metric_id"); (params None)
2024-08-05 23:41:18,062 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_tenant_id_4cb1485d" ON "metrics_trend" ("tenant_id"); (params None)
2024-08-05 23:41:18,227 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_date_33d1e0bd" ON "metrics_actionremark" ("date"); (params None)
2024-08-05 23:41:18,239 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_detection_date_ee75a187" ON "metrics_anomaly" ("detection_date"); (params None)
2024-08-05 23:41:18,250 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c" ON "metrics_category" ("name"); (params None)
2024-08-05 23:41:18,253 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c_like" ON "metrics_category" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:18,264 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d" ON "metrics_client" ("name"); (params None)
2024-08-05 23:41:18,266 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d_like" ON "metrics_client" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:18,279 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET DEFAULT '{}'; (params None)
2024-08-05 23:41:18,280 - django.db.backends.schema - DEBUG - UPDATE "metrics_dashboard" SET "layout" = '{}' WHERE "layout" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:41:18,281 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET NOT NULL; (params None)
2024-08-05 23:41:18,281 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" DROP DEFAULT; (params None)
2024-08-05 23:41:18,291 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e" ON "metrics_dashboard" ("name"); (params None)
2024-08-05 23:41:18,294 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e_like" ON "metrics_dashboard" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:18,305 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_end_date_31af6c05" ON "metrics_experiment" ("end_date"); (params None)
2024-08-05 23:41:18,317 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7" ON "metrics_experiment" ("name"); (params None)
2024-08-05 23:41:18,319 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7_like" ON "metrics_experiment" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:18,332 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET DEFAULT '{}'; (params None)
2024-08-05 23:41:18,332 - django.db.backends.schema - DEBUG - UPDATE "metrics_experiment" SET "results" = '{}' WHERE "results" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:41:18,333 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET NOT NULL; (params None)
2024-08-05 23:41:18,334 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" DROP DEFAULT; (params None)
2024-08-05 23:41:18,344 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_start_date_a6deff13" ON "metrics_experiment" ("start_date"); (params None)
2024-08-05 23:41:18,356 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET DEFAULT '{}'; (params None)
2024-08-05 23:41:18,357 - django.db.backends.schema - DEBUG - UPDATE "metrics_forecast" SET "confidence_interval" = '{}' WHERE "confidence_interval" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:41:18,357 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET NOT NULL; (params None)
2024-08-05 23:41:18,358 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" DROP DEFAULT; (params None)
2024-08-05 23:41:18,368 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_forecast_date_71750ae8" ON "metrics_forecast" ("forecast_date"); (params None)
2024-08-05 23:41:18,382 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_date_f27e0e6a" ON "metrics_historicaldata" ("date"); (params None)
2024-08-05 23:41:18,394 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_last_updated_3e38a760" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:41:18,406 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5" ON "metrics_metric" ("name"); (params None)
2024-08-05 23:41:18,409 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5_like" ON "metrics_metric" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:18,424 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e" ON "metrics_metric" ("type"); (params None)
2024-08-05 23:41:18,427 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e_like" ON "metrics_metric" ("type" varchar_pattern_ops); (params None)
2024-08-05 23:41:18,448 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80" ON "metrics_project" ("name"); (params None)
2024-08-05 23:41:18,450 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80_like" ON "metrics_project" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:18,462 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET DEFAULT '{}'; (params None)
2024-08-05 23:41:18,463 - django.db.backends.schema - DEBUG - UPDATE "metrics_report" SET "configuration" = '{}' WHERE "configuration" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:41:18,464 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET NOT NULL; (params None)
2024-08-05 23:41:18,464 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" DROP DEFAULT; (params None)
2024-08-05 23:41:18,476 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34" ON "metrics_report" ("name"); (params None)
2024-08-05 23:41:18,478 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34_like" ON "metrics_report" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:18,490 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a" ON "metrics_tag" ("name"); (params None)
2024-08-05 23:41:18,492 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a_like" ON "metrics_tag" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:18,504 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_target_date_81507ff5" ON "metrics_target" ("target_date"); (params None)
2024-08-05 23:41:18,515 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_end_date_8444ef38" ON "metrics_trend" ("end_date"); (params None)
2024-08-05 23:41:18,529 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_start_date_7b1a850f" ON "metrics_trend" ("start_date"); (params None)
2024-08-05 23:41:18,541 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_act_metric__be3429_idx" ON "metrics_actionremark" ("metric_id", "date"); (params None)
2024-08-05 23:41:18,553 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ano_metric__84982d_idx" ON "metrics_anomaly" ("metric_id", "detection_date"); (params None)
2024-08-05 23:41:18,566 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_con_from_me_9411ea_idx" ON "metrics_connection" ("from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:41:18,580 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_exp_start_d_04716a_idx" ON "metrics_experiment" ("start_date", "end_date"); (params None)
2024-08-05 23:41:18,591 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_for_metric__4c9ae2_idx" ON "metrics_forecast" ("metric_id", "forecast_date"); (params None)
2024-08-05 23:41:18,603 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_his_metric__a2923a_idx" ON "metrics_historicaldata" ("metric_id", "date"); (params None)
2024-08-05 23:41:18,617 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_name_c9d100_idx" ON "metrics_metric" ("name", "type"); (params None)
2024-08-05 23:41:18,630 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_7984a6_idx" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:41:18,644 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1bdb27_idx" ON "metrics_tag" ("name", "project_id"); (params None)
2024-08-05 23:41:18,656 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tar_metric__234682_idx" ON "metrics_target" ("metric_id", "target_date"); (params None)
2024-08-05 23:41:18,803 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tre_metric__d386bb_idx" ON "metrics_trend" ("metric_id", "start_date", "end_date"); (params None)
2024-08-05 23:41:18,817 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_con_from_me_9411ea_idx"; (params None)
2024-08-05 23:41:18,828 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:41:18,829 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:41:18,841 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_from_metric_id_aa131d91_uniq" UNIQUE ("tenant_id", "from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:41:18,843 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_project_id_4c1b22ec" ON "metrics_connection" ("project_id"); (params None)
2024-08-05 23:41:18,860 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; ALTER TABLE "metrics_connection" DROP CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id"; (params None)
2024-08-05 23:41:18,861 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "project_id" CASCADE; (params None)
2024-08-05 23:41:18,875 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:41:18,877 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:41:18,889 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:41:18,891 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_project_id_36bdbe46" ON "metrics_metric" ("project_id"); (params None)
2024-08-05 23:41:18,895 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_correlation" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "lag" integer NOT NULL, "pearson_correlation" double precision NOT NULL, "spearman_correlation" double precision NOT NULL); (params None)
2024-08-05 23:41:18,899 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:18,906 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dataqualityscore" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_entry" varchar(255) NOT NULL, "completeness_score" double precision NOT NULL, "accuracy_score" double precision NOT NULL, "consistency_score" double precision NOT NULL, "timeliness_score" double precision NOT NULL, "overall_score" double precision NOT NULL); (params None)
2024-08-05 23:41:18,910 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_impactanalysis" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "before_value" double precision NOT NULL, "after_value" double precision NOT NULL, "percentage_change" double precision NOT NULL, "confidence" double precision NOT NULL, "artifact_link" varchar(200) NOT NULL); (params None)
2024-08-05 23:41:18,917 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_insight" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "title" varchar(200) NOT NULL, "content" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:18,922 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metricmetadata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_source" varchar(100) NOT NULL, "source_url" varchar(200) NOT NULL, "rhythm" varchar(20) NOT NULL, "last_updated" timestamp with time zone NOT NULL, "technical_description" text NOT NULL, "description" text NOT NULL, "artifacts_url" varchar(200) NOT NULL, "hypothesis" text NOT NULL, "confidence" varchar(20) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL); (params None)
2024-08-05 23:41:18,928 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metrictarget" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "target_kpi" varchar(100) NOT NULL, "target_remarks" text NOT NULL, "target_date" date NULL, "target_value" double precision NULL); (params None)
2024-08-05 23:41:18,934 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_strategy" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "estimated_time" interval NOT NULL, "artifacts_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:18,939 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tacticalsolution" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "artifact_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:18,945 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_team" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:18,950 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_technicalindicator" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "stochastic_value" double precision NOT NULL, "rsi_value" double precision NOT NULL, "percent_change" double precision NOT NULL, "moving_average" double precision NOT NULL); (params None)
2024-08-05 23:41:18,955 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_timedimension" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL UNIQUE, "day" integer NOT NULL, "day_of_week" integer NOT NULL, "day_name" varchar(10) NOT NULL, "week" integer NOT NULL, "month" integer NOT NULL, "month_name" varchar(10) NOT NULL, "quarter" integer NOT NULL, "year" integer NOT NULL, "is_weekend" boolean NOT NULL, "is_holiday" boolean NOT NULL); (params None)
2024-08-05 23:41:18,961 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_userprofile" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY); (params None)
2024-08-05 23:41:18,976 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_metric_id_181e8748_fk_metrics_metric_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id"; (params None)
2024-08-05 23:41:18,977 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "metric_id" CASCADE; (params None)
2024-08-05 23:41:18,991 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id"; (params None)
2024-08-05 23:41:18,992 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:41:19,005 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_name_c9d100_idx"; (params None)
2024-08-05 23:41:19,016 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_last_up_7984a6_idx"; (params None)
2024-08-05 23:41:19,026 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" RENAME COLUMN "description" TO "summary"; (params None)
2024-08-05 23:41:19,038 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq"; (params None)
2024-08-05 23:41:19,050 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "correlation_coefficient" CASCADE; (params None)
2024-08-05 23:41:19,061 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" DROP COLUMN "results" CASCADE; (params None)
2024-08-05 23:41:19,072 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "anomaly_detected" CASCADE; (params None)
2024-08-05 23:41:19,083 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "forecasted_value" CASCADE; (params None)
2024-08-05 23:41:19,095 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "trend_component" CASCADE; (params None)
2024-08-05 23:41:19,105 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "importance" varchar(20) DEFAULT 'MEDIUM' NOT NULL; (params None)
2024-08-05 23:41:19,105 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "importance" DROP DEFAULT; (params None)
2024-08-05 23:41:19,116 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:41:19.116580+00:00' NOT NULL; (params None)
2024-08-05 23:41:19,117 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:41:19,130 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "anomaly_type" varchar(20) DEFAULT 'IGNORE' NOT NULL; (params None)
2024-08-05 23:41:19,131 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "anomaly_type" DROP DEFAULT; (params None)
2024-08-05 23:41:19,150 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "quality" varchar(20) DEFAULT 'LOW' NOT NULL; (params None)
2024-08-05 23:41:19,151 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "quality" DROP DEFAULT; (params None)
2024-08-05 23:41:19,165 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "impact_description" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:41:19,166 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "impact_description" DROP DEFAULT; (params None)
2024-08-05 23:41:19,177 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "objective" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:41:19,178 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "objective" DROP DEFAULT; (params None)
2024-08-05 23:41:19,191 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_date" date NULL; (params None)
2024-08-05 23:41:19,203 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_files" varchar(100) NULL; (params None)
2024-08-05 23:41:19,219 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_summary" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:41:19,220 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "result_summary" DROP DEFAULT; (params None)
2024-08-05 23:41:19,233 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_value" double precision NULL; (params None)
2024-08-05 23:41:19,244 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:41:19.244491+00:00' NOT NULL; (params None)
2024-08-05 23:41:19,246 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:41:19,258 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "variance" double precision NULL; (params None)
2024-08-05 23:41:19,274 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD COLUMN "forecast_id" bigint NULL CONSTRAINT "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" REFERENCES "metrics_forecast"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" IMMEDIATE; (params None)
2024-08-05 23:41:19,302 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "impact" TYPE varchar(20) USING "impact"::varchar(20); (params None)
2024-08-05 23:41:19,438 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "status" TYPE varchar(20); (params None)
2024-08-05 23:41:19,601 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric1_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:19,615 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric2_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:19,636 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:19,645 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:41:19,685 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:19,708 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:41:19,729 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:19,748 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "experiment_id" bigint NOT NULL CONSTRAINT "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" REFERENCES "metrics_experiment"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" IMMEDIATE; (params None)
2024-08-05 23:41:19,895 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:19,913 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:19,933 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:19,952 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:19,972 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "user_id" bigint NOT NULL CONSTRAINT "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:41:19,991 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "data_quality_score_id" bigint NULL UNIQUE CONSTRAINT "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" REFERENCES "metrics_dataqualityscore"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" IMMEDIATE; (params None)
2024-08-05 23:41:20,014 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "metric_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:20,038 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:20,058 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:20,082 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:20,107 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:20,131 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:41:20,153 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:20,176 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_team" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:20,198 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "team_id" bigint NOT NULL CONSTRAINT "metrics_strategy_team_id_f1781500_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_team_id_f1781500_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:41:20,221 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:41:20,243 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:41:20,264 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_experiment_team_id_537107e3_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_experiment_team_id_537107e3_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:41:20,286 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:41:20,309 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:20,332 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_timedimension" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:20,496 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:20,519 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "user_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:41:20,523 - django.db.backends.schema - DEBUG - DROP TABLE "metrics_target" CASCADE; (params None)
2024-08-05 23:41:20,541 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "confidence" CASCADE; (params None)
2024-08-05 23:41:20,559 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "description" CASCADE; (params None)
2024-08-05 23:41:20,578 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "hypothesis" CASCADE; (params None)
2024-08-05 23:41:20,597 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "last_updated" CASCADE; (params None)
2024-08-05 23:41:20,616 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_x" CASCADE; (params None)
2024-08-05 23:41:20,634 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_y" CASCADE; (params None)
2024-08-05 23:41:20,653 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "rhythm" CASCADE; (params None)
2024-08-05 23:41:20,671 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "source" CASCADE; (params None)
2024-08-05 23:41:20,689 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "technical_description" CASCADE; (params None)
2024-08-05 23:41:20,708 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD CONSTRAINT "metrics_correlation_tenant_id_metric1_id_met_49a4c34a_uniq" UNIQUE ("tenant_id", "metric1_id", "metric2_id", "lag"); (params None)
2024-08-05 23:41:20,731 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_metric__b85d3a_idx" ON "metrics_insight" ("metric_id", "date"); (params None)
2024-08-05 23:41:20,755 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_user_id_1ebb42_idx" ON "metrics_insight" ("user_id", "date"); (params None)
2024-08-05 23:41:20,778 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_metric__a2b705_idx" ON "metrics_metrictarget" ("metric_id", "target_date"); (params None)
2024-08-05 23:41:20,799 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_6e2e67_idx" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:41:20,821 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_date_53cb14_idx" ON "metrics_timedimension" ("date"); (params None)
2024-08-05 23:41:20,842 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_year_92da9e_idx" ON "metrics_timedimension" ("year", "month", "day"); (params None)
2024-08-05 23:41:20,845 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_username_6e55f358_like" ON "metrics_customuser" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:41:20,847 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_date_ded95ba1" ON "metrics_insight" ("date"); (params None)
2024-08-05 23:41:20,849 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_last_updated_76599a1b" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:41:20,852 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_target_date_38cd9191" ON "metrics_metrictarget" ("target_date"); (params None)
2024-08-05 23:41:20,853 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_forecast_id_29590c29" ON "metrics_historicaldata" ("forecast_id"); (params None)
2024-08-05 23:41:20,855 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric1_id_6e1c2404" ON "metrics_correlation" ("metric1_id"); (params None)
2024-08-05 23:41:20,857 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric2_id_f2cc46dd" ON "metrics_correlation" ("metric2_id"); (params None)
2024-08-05 23:41:20,859 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_tenant_id_a00a5169" ON "metrics_correlation" ("tenant_id"); (params None)
2024-08-05 23:41:20,862 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_customuser_id_group_id_1c5fc435_uniq" UNIQUE ("customuser_id", "group_id"); (params None)
2024-08-05 23:41:20,864 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_g_customuser_id_fc13f3af_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:20,865 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_group_id_6b097e12_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:20,866 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_customuser_id_fc13f3af" ON "metrics_customuser_groups" ("customuser_id"); (params None)
2024-08-05 23:41:20,868 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_group_id_6b097e12" ON "metrics_customuser_groups" ("group_id"); (params None)
2024-08-05 23:41:20,870 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_tenant_id_02b7403c" ON "metrics_customuser" ("tenant_id"); (params None)
2024-08-05 23:41:20,872 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_user__customuser_id_permission_68cc320f_uniq" UNIQUE ("customuser_id", "permission_id"); (params None)
2024-08-05 23:41:20,874 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_customuser_id_46e97f00_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:20,876 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_permission_id_d66d657c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:20,877 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_customuser_id_46e97f00" ON "metrics_customuser_user_permissions" ("customuser_id"); (params None)
2024-08-05 23:41:20,879 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_permission_id_d66d657c" ON "metrics_customuser_user_permissions" ("permission_id"); (params None)
2024-08-05 23:41:20,881 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_tenant_id_8e9f296d" ON "metrics_dataqualityscore" ("tenant_id"); (params None)
2024-08-05 23:41:20,883 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_experiment_id_1beae7fe" ON "metrics_impactanalysis" ("experiment_id"); (params None)
2024-08-05 23:41:20,885 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_metric_id_f4b9eeb6" ON "metrics_impactanalysis" ("metric_id"); (params None)
2024-08-05 23:41:20,887 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_tenant_id_126ca20d" ON "metrics_impactanalysis" ("tenant_id"); (params None)
2024-08-05 23:41:20,889 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_metric_id_26d3a9d8" ON "metrics_insight" ("metric_id"); (params None)
2024-08-05 23:41:20,892 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_tenant_id_724d7d85" ON "metrics_insight" ("tenant_id"); (params None)
2024-08-05 23:41:20,894 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_user_id_83d421e1" ON "metrics_insight" ("user_id"); (params None)
2024-08-05 23:41:20,896 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_tenant_id_3277f967" ON "metrics_metricmetadata" ("tenant_id"); (params None)
2024-08-05 23:41:20,898 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_metric_id_7876e2c8" ON "metrics_metrictarget" ("metric_id"); (params None)
2024-08-05 23:41:20,899 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_tenant_id_b26a17f8" ON "metrics_metrictarget" ("tenant_id"); (params None)
2024-08-05 23:41:20,901 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_tenant_id_1323395e" ON "metrics_strategy" ("tenant_id"); (params None)
2024-08-05 23:41:20,903 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_metric_id_9887ffa4" ON "metrics_tacticalsolution" ("metric_id"); (params None)
2024-08-05 23:41:20,905 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_tenant_id_cf9028f0" ON "metrics_tacticalsolution" ("tenant_id"); (params None)
2024-08-05 23:41:20,907 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_team_tenant_id_3a14c47d" ON "metrics_team" ("tenant_id"); (params None)
2024-08-05 23:41:20,909 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_team_id_f1781500" ON "metrics_strategy" ("team_id"); (params None)
2024-08-05 23:41:20,911 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_team_id_f140658d" ON "metrics_metricmetadata" ("team_id"); (params None)
2024-08-05 23:41:20,913 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_team_id_4c4ffc18" ON "metrics_customuser" ("team_id"); (params None)
2024-08-05 23:41:20,915 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_team_id_537107e3" ON "metrics_experiment" ("team_id"); (params None)
2024-08-05 23:41:20,917 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_metric_id_3e2eead6" ON "metrics_technicalindicator" ("metric_id"); (params None)
2024-08-05 23:41:20,919 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_tenant_id_f4de3b44" ON "metrics_technicalindicator" ("tenant_id"); (params None)
2024-08-05 23:41:20,921 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_timedimension_tenant_id_f375bb45" ON "metrics_timedimension" ("tenant_id"); (params None)
2024-08-05 23:41:20,923 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_userprofile_tenant_id_cca71dae" ON "metrics_userprofile" ("tenant_id"); (params None)
2024-08-05 23:41:20,946 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "strength" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:41:20,947 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "strength" DROP DEFAULT; (params None)
2024-08-05 23:41:20,968 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "lower_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:41:20,969 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "lower_bound" DROP DEFAULT; (params None)
2024-08-05 23:41:21,115 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "upper_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:41:21,116 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "upper_bound" DROP DEFAULT; (params None)
2024-08-05 23:41:21,135 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD COLUMN "slope" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:41:21,136 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ALTER COLUMN "slope" DROP DEFAULT; (params None)
2024-08-05 23:41:21,158 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_movingaverage" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "ma_type" varchar(10) NOT NULL, "period" integer NOT NULL, "value" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:21,185 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_networkanalysisresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "analysis_type" varchar(20) NOT NULL, "result" jsonb NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:21,214 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_seasonalityresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "seasonality_type" varchar(20) NOT NULL, "strength" double precision NOT NULL, "period" integer NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:21,242 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trendchangepoint" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "change_type" varchar(20) NOT NULL, "significance" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:21,252 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD CONSTRAINT "metrics_movingaverage_metric_id_7c61cebf_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:21,253 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_metric_id_7c61cebf" ON "metrics_movingaverage" ("metric_id"); (params None)
2024-08-05 23:41:21,255 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD CONSTRAINT "metrics_networkanaly_metric_id_a4c90102_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:21,256 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_metric_id_a4c90102" ON "metrics_networkanalysisresult" ("metric_id"); (params None)
2024-08-05 23:41:21,258 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityr_metric_id_6e494791_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:21,259 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_metric_id_6e494791" ON "metrics_seasonalityresult" ("metric_id"); (params None)
2024-08-05 23:41:21,261 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD CONSTRAINT "metrics_trendchangep_metric_id_f8eb9f76_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:21,262 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_metric_id_f8eb9f76" ON "metrics_trendchangepoint" ("metric_id"); (params None)
2024-08-05 23:41:21,291 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:41:21,293 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:41:21,319 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" IMMEDIATE; (params None)
2024-08-05 23:41:21,321 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:41:21,343 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ALTER COLUMN "value" DROP NOT NULL; (params None)
2024-08-05 23:41:21,364 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD CONSTRAINT "metrics_dataqualityscore_tenant_id_metric_id_proj_66b9fb01_uniq" UNIQUE ("tenant_id", "metric_id", "project_id"); (params None)
2024-08-05 23:41:21,367 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_metric_id_1b6367d1" ON "metrics_dataqualityscore" ("metric_id"); (params None)
2024-08-05 23:41:21,370 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_project_id_123a4f58" ON "metrics_dataqualityscore" ("project_id"); (params None)
2024-08-05 23:41:21,393 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:41:21,425 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:21,426 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:41:21,452 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:21,454 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:41:21,480 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:21,482 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:41:21,507 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:21,509 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:41:21,529 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq" UNIQUE ("tenant_id", "metric_id"); (params None)
2024-08-05 23:41:21,532 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_tenant_id_5a9de228" ON "metrics_movingaverage" ("tenant_id"); (params None)
2024-08-05 23:41:21,535 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_tenant_id_16a6ba09" ON "metrics_networkanalysisresult" ("tenant_id"); (params None)
2024-08-05 23:41:21,537 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_tenant_id_ca2da3fd" ON "metrics_seasonalityresult" ("tenant_id"); (params None)
2024-08-05 23:41:21,540 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_tenant_id_da10d898" ON "metrics_trendchangepoint" ("tenant_id"); (params None)
2024-08-05 23:41:21,571 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:21,572 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:41:21,573 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_metric_id_c86f5720" ON "metrics_report" ("metric_id"); (params None)
2024-08-05 23:41:21,724 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "analysis_result" jsonb NULL; (params None)
2024-08-05 23:41:21,744 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "anomaly_result" jsonb NULL; (params None)
2024-08-05 23:41:21,766 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:41:21.765770+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:41:21,766 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:41:21,788 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "forecast_result" jsonb NULL; (params None)
2024-08-05 23:41:21,807 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "relationship_result" jsonb NULL; (params None)
2024-08-05 23:41:21,829 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "report" text DEFAULT '1' NOT NULL; (params None)
2024-08-05 23:41:21,830 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "report" DROP DEFAULT; (params None)
2024-08-05 23:41:21,852 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "updated_at" timestamp with time zone DEFAULT '2024-08-05T23:41:21.851730+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:41:21,852 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "updated_at" DROP DEFAULT; (params None)
2024-08-05 23:41:21,905 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_trendchangepoint" DROP CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c"; (params None)
2024-08-05 23:41:21,906 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:41:21,923 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "significance" DROP NOT NULL; (params None)
2024-08-05 23:41:21,941 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" RENAME COLUMN "change_type" TO "direction"; (params None)
2024-08-05 23:41:21,984 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:41:21.984414+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:41:21,985 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:41:22,009 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq"; (params None)
2024-08-05 23:41:22,010 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresul_metric_id_seasonality_ty_d3492b78_uniq" UNIQUE ("metric_id", "seasonality_type"); (params None)
2024-08-05 23:41:22,040 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c"; (params None)
2024-08-05 23:41:22,041 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:41:22,044 - django.db.backends.schema - DEBUG - CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:22,048 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" ("session_key" varchar_pattern_ops); (params None)
2024-08-05 23:41:22,050 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date"); (params None)
2024-08-05 23:41:23,030 - metrics.computations.data_preparation - INFO - Loaded metric 5 for tenant 3 and project 3
2024-08-05 23:41:23,030 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 5
2024-08-05 23:41:23,031 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:23,031 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:23,032 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 5
2024-08-05 23:41:23,037 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:23,037 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:23,040 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:23,040 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:23,042 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:23,043 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:23,045 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:24,824 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 5
2024-08-05 23:41:24,826 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:24,828 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:24,828 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:24,830 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:24,831 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:24,833 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:24,835 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3646743844035821, Timeliness: nan
2024-08-05 23:41:24,835 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48914614678607
2024-08-05 23:41:24,839 - metrics.computations.data_preparation - INFO - Data quality score: 45.48914614678607
2024-08-05 23:41:24,854 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 5, 'tenant_id': 3, 'project_id': 3, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48914614678607, 'outliers_handled': True, 'profile': {'mean': 100.45306848616362, 'median': 100.69183658789358, 'std': 9.82434001976125, 'min': 77.63255035093705, 'max': 124.1836399833664, 'skewness': 0.026375760596621837, 'kurtosis': -0.41598750262309725, 'missing_percentage': 0.0}}
2024-08-05 23:41:24,858 - metrics.computations.data_preparation - INFO - Loaded metric 5 for tenant 3 and project 3
2024-08-05 23:41:24,858 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 5
2024-08-05 23:41:24,859 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:24,859 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:24,863 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 5
2024-08-05 23:41:24,869 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:24,869 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:24,873 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:24,873 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:24,876 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:24,876 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:24,879 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:26,654 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 5
2024-08-05 23:41:26,657 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:26,658 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:26,658 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:26,661 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:26,661 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:26,663 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:26,665 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3646743844035821, Timeliness: nan
2024-08-05 23:41:26,666 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48914614678607
2024-08-05 23:41:26,668 - metrics.computations.data_preparation - INFO - Data quality score: 45.48914614678607
2024-08-05 23:41:26,687 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 5, 'tenant_id': 3, 'project_id': 3, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48914614678607, 'outliers_handled': True, 'profile': {'mean': 100.45306848616362, 'median': 100.69183658789358, 'std': 9.82434001976125, 'min': 77.63255035093705, 'max': 124.1836399833664, 'skewness': 0.026375760596621837, 'kurtosis': -0.41598750262309725, 'missing_percentage': 0.0}}
2024-08-05 23:41:26,687 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:41:26,687 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 5
2024-08-05 23:41:26,698 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:41:26,703 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:41:26,709 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 5
2024-08-05 23:41:26,709 - metrics.computations.feature_engineering - INFO - Parameters for metric 5: dynamic
2024-08-05 23:41:26,710 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 5: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:41:26,712 - metrics.computations.data_preparation - INFO - Loaded metric 5 for tenant 3 and project 3
2024-08-05 23:41:26,712 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 5
2024-08-05 23:41:26,713 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:26,713 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:26,715 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 5
2024-08-05 23:41:26,722 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:26,722 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:26,725 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:26,725 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:26,728 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:26,728 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:26,731 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:28,506 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 5
2024-08-05 23:41:28,508 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:28,510 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:28,510 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:28,513 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:28,513 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:28,516 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:28,520 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3646743844035821, Timeliness: nan
2024-08-05 23:41:28,520 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48914614678607
2024-08-05 23:41:28,524 - metrics.computations.data_preparation - INFO - Data quality score: 45.48914614678607
2024-08-05 23:41:28,620 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 5, 'tenant_id': 3, 'project_id': 3, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48914614678607, 'outliers_handled': True, 'profile': {'mean': 100.45306848616362, 'median': 100.69183658789358, 'std': 9.82434001976125, 'min': 77.63255035093705, 'max': 124.1836399833664, 'skewness': 0.026375760596621837, 'kurtosis': -0.41598750262309725, 'missing_percentage': 0.0}}
2024-08-05 23:41:28,628 - metrics.computations.data_preparation - INFO - Loaded metric 5 for tenant 3 and project 3
2024-08-05 23:41:28,629 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 5
2024-08-05 23:41:28,630 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:28,631 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:28,638 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 5
2024-08-05 23:41:28,647 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:28,648 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:28,651 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:28,652 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:28,656 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:28,656 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:28,660 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:30,416 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 5
2024-08-05 23:41:30,419 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:30,420 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:30,420 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:30,423 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:30,423 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:30,425 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:30,427 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3646743844035821, Timeliness: nan
2024-08-05 23:41:30,428 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48914614678607
2024-08-05 23:41:30,431 - metrics.computations.data_preparation - INFO - Data quality score: 45.48914614678607
2024-08-05 23:41:30,450 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 5, 'tenant_id': 3, 'project_id': 3, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48914614678607, 'outliers_handled': True, 'profile': {'mean': 100.45306848616362, 'median': 100.69183658789358, 'std': 9.82434001976125, 'min': 77.63255035093705, 'max': 124.1836399833664, 'skewness': 0.026375760596621837, 'kurtosis': -0.41598750262309725, 'missing_percentage': 0.0}}
2024-08-05 23:41:30,451 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:41:30,451 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 5
2024-08-05 23:41:30,456 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:41:30,461 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:41:30,465 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 5
2024-08-05 23:41:30,466 - metrics.computations.feature_engineering - INFO - Parameters for metric 5: dynamic
2024-08-05 23:41:30,466 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 5: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:41:30,467 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Setup completed
2024-08-05 23:41:30,470 - metrics.computations.data_preparation - INFO - Loaded metric 5 for tenant 3 and project 3
2024-08-05 23:41:30,470 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 5
2024-08-05 23:41:30,471 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:30,471 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:30,475 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 5
2024-08-05 23:41:30,484 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:30,484 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:30,488 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:30,488 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:30,491 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:30,491 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:30,495 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:32,262 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 5
2024-08-05 23:41:32,264 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:32,266 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:32,266 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:32,269 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:32,269 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:32,271 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:32,273 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3646743844035821, Timeliness: nan
2024-08-05 23:41:32,273 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48914614678607
2024-08-05 23:41:32,276 - metrics.computations.data_preparation - INFO - Data quality score: 45.48914614678607
2024-08-05 23:41:32,291 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 5, 'tenant_id': 3, 'project_id': 3, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48914614678607, 'outliers_handled': True, 'profile': {'mean': 100.45306848616362, 'median': 100.69183658789358, 'std': 9.82434001976125, 'min': 77.63255035093705, 'max': 124.1836399833664, 'skewness': 0.026375760596621837, 'kurtosis': -0.41598750262309725, 'missing_percentage': 0.0}}
2024-08-05 23:41:32,296 - metrics.computations.data_preparation - INFO - Loaded metric 5 for tenant 3 and project 3
2024-08-05 23:41:32,296 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 5
2024-08-05 23:41:32,297 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:32,298 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 5 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:32,302 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 5
2024-08-05 23:41:32,310 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:32,311 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:32,314 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:32,314 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:32,317 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:32,318 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:32,320 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:34,089 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 5
2024-08-05 23:41:34,091 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:34,092 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:34,093 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:34,095 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:34,095 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:34,097 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.841687          3
2023-01-02  106.840917          3
2023-01-03  106.978537          3
2023-01-04   98.913838          3
2023-01-05  120.459808          3
2024-08-05 23:41:34,099 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3646743844035821, Timeliness: nan
2024-08-05 23:41:34,100 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48914614678607
2024-08-05 23:41:34,103 - metrics.computations.data_preparation - INFO - Data quality score: 45.48914614678607
2024-08-05 23:41:34,117 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 5, 'tenant_id': 3, 'project_id': 3, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48914614678607, 'outliers_handled': True, 'profile': {'mean': 100.45306848616362, 'median': 100.69183658789358, 'std': 9.82434001976125, 'min': 77.63255035093705, 'max': 124.1836399833664, 'skewness': 0.026375760596621837, 'kurtosis': -0.41598750262309725, 'missing_percentage': 0.0}}
2024-08-05 23:41:34,120 - metrics.computations.computations_anomalies - INFO - Initialized AnomalyDetector for metric 5
2024-08-05 23:41:34,120 - metrics.computations.computations_anomalies - INFO - Seasonality period: 7
2024-08-05 23:41:34,120 - metrics.computations.computations_anomalies - INFO - Window size: 30
2024-08-05 23:41:34,120 - metrics.computations.computations_anomalies - INFO - Base threshold: 3.0
2024-08-05 23:41:34,120 - metrics.computations.computations_anomalies - INFO - Context window: 5
2024-08-05 23:41:34,120 - metrics.computations.computations_anomalies - INFO - Global threshold: 4.0
2024-08-05 23:41:34,120 - metrics.computations.computations_anomalies - WARNING - Not enough data for anomaly detection for metric 5
2024-08-05 23:41:34,246 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Teardown completed
```

## test_computation_with_missing_data (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
Status: failure
Duration: 16.618 seconds

### Failure
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_permanent_computations_robustness.py", line 126, in test_computation_with_missing_data
    self.assertIsInstance(anomalies, dict)
AssertionError: Empty DataFrame
Columns: [date, value, anomaly_score, type]
Index: [] is not an instance of <class 'dict'>
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
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
2024-08-05 23:41:34,262 - metrics - DEBUG - Starting test: test_computation_with_missing_data (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
2024-08-05 23:41:34,266 - django.db.backends.schema - DEBUG - CREATE TABLE "django_migrations" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:34,282 - django.db.backends.schema - DEBUG - CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
2024-08-05 23:41:34,287 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params None)
2024-08-05 23:41:34,292 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL, "codename" varchar(100) NOT NULL); (params None)
2024-08-05 23:41:34,298 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(80) NOT NULL UNIQUE); (params None)
2024-08-05 23:41:34,303 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:41:34,310 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NOT NULL, "is_superuser" boolean NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:34,314 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:41:34,317 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:41:34,320 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename"); (params None)
2024-08-05 23:41:34,322 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,324 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id"); (params None)
2024-08-05 23:41:34,326 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_name_a6ea08ec_like" ON "auth_group" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:34,328 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id"); (params None)
2024-08-05 23:41:34,330 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,331 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,332 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id"); (params None)
2024-08-05 23:41:34,334 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id"); (params None)
2024-08-05 23:41:34,337 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_username_6821ab7c_like" ON "auth_user" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:41:34,339 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id"); (params None)
2024-08-05 23:41:34,341 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,342 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,342 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id"); (params None)
2024-08-05 23:41:34,345 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id"); (params None)
2024-08-05 23:41:34,347 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id"); (params None)
2024-08-05 23:41:34,350 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,351 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,352 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id"); (params None)
2024-08-05 23:41:34,354 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id"); (params None)
2024-08-05 23:41:34,362 - django.db.backends.schema - DEBUG - CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "action_time" timestamp with time zone NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL, "user_id" integer NOT NULL); (params None)
2024-08-05 23:41:34,367 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,368 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,369 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id"); (params None)
2024-08-05 23:41:34,371 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id"); (params None)
2024-08-05 23:41:34,390 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ALTER COLUMN "name" DROP NOT NULL; (params None)
2024-08-05 23:41:34,396 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" DROP COLUMN "name" CASCADE; (params None)
2024-08-05 23:41:34,402 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ALTER COLUMN "name" TYPE varchar(255); (params None)
2024-08-05 23:41:34,408 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "email" TYPE varchar(254); (params None)
2024-08-05 23:41:34,422 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_login" DROP NOT NULL; (params None)
2024-08-05 23:41:34,435 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "username" TYPE varchar(150); (params None)
2024-08-05 23:41:34,445 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_name" TYPE varchar(150); (params None)
2024-08-05 23:41:34,451 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group" ALTER COLUMN "name" TYPE varchar(150); (params None)
2024-08-05 23:41:34,467 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "first_name" TYPE varchar(150); (params None)
2024-08-05 23:41:34,501 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_client" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "schema_name" varchar(63) NOT NULL UNIQUE, "name" varchar(100) NOT NULL, "created_on" date NOT NULL); (params None)
2024-08-05 23:41:34,507 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_category" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,512 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dashboard" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "layout" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,518 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_domain" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "domain" varchar(253) NOT NULL UNIQUE, "is_primary" boolean NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,526 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "type" varchar(50) NOT NULL, "confidence" varchar(50) NOT NULL, "value_type" varchar(20) NOT NULL, "rhythm" varchar(20) NOT NULL, "description" text NOT NULL, "hypothesis" text NOT NULL, "technical_description" text NOT NULL, "last_updated" timestamp with time zone NOT NULL, "source" varchar(100) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL, "category_id" bigint NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,534 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_historicaldata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "value" double precision NOT NULL, "forecasted_value" double precision NULL, "anomaly_detected" boolean NOT NULL, "trend_component" varchar(50) NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,541 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_forecast" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "forecast_date" date NOT NULL, "forecast_value" double precision NOT NULL, "model_used" varchar(100) NOT NULL, "accuracy" double precision NULL, "confidence_interval" jsonb NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,552 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "status" varchar(50) NOT NULL, "results" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,557 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment_metrics" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "experiment_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,711 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_connection" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "relationship" varchar(100) NOT NULL, "correlation_coefficient" double precision NULL, "tenant_id" bigint NOT NULL, "from_metric_id" bigint NOT NULL, "to_metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,721 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_anomaly" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "detection_date" date NOT NULL, "anomaly_value" double precision NOT NULL, "anomaly_score" double precision NOT NULL, "notes" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,733 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_actionremark" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NULL, "description" text NOT NULL, "impact" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,747 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_project" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "created_on" date NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,759 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_report" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "configuration" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,773 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tag" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "project_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,785 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric_tags" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "metric_id" bigint NOT NULL, "tag_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,799 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_target" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "remarks" text NOT NULL, "target_kpi" varchar(100) NOT NULL, "target_date" date NULL, "target_value" double precision NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,815 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trend" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "trend_type" varchar(50) NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "trend_value" double precision NOT NULL, "notes" text NOT NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:34,820 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_schema_name_87d6fbb5_like" ON "metrics_client" ("schema_name" varchar_pattern_ops); (params None)
2024-08-05 23:41:34,822 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_category" ADD CONSTRAINT "metrics_category_tenant_id_67d98cc6_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,824 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_tenant_id_67d98cc6" ON "metrics_category" ("tenant_id"); (params None)
2024-08-05 23:41:34,826 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ADD CONSTRAINT "metrics_dashboard_tenant_id_50099a7d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,827 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_tenant_id_50099a7d" ON "metrics_dashboard" ("tenant_id"); (params None)
2024-08-05 23:41:34,829 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_domain" ADD CONSTRAINT "metrics_domain_tenant_id_259fb21f_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,830 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_domain_bdc97b86_like" ON "metrics_domain" ("domain" varchar_pattern_ops); (params None)
2024-08-05 23:41:34,833 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_is_primary_ac9d2eaf" ON "metrics_domain" ("is_primary"); (params None)
2024-08-05 23:41:34,835 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_tenant_id_259fb21f" ON "metrics_domain" ("tenant_id"); (params None)
2024-08-05 23:41:34,837 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_category_id_8793f683_fk_metrics_category_id" FOREIGN KEY ("category_id") REFERENCES "metrics_category" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,838 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_9606b577_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,839 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_category_id_8793f683" ON "metrics_metric" ("category_id"); (params None)
2024-08-05 23:41:34,841 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tenant_id_9606b577" ON "metrics_metric" ("tenant_id"); (params None)
2024-08-05 23:41:34,844 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_tenant_id_438c5ad4_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,845 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_metric_id_3f9e8174_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,845 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_tenant_id_438c5ad4" ON "metrics_historicaldata" ("tenant_id"); (params None)
2024-08-05 23:41:34,847 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_metric_id_3f9e8174" ON "metrics_historicaldata" ("metric_id"); (params None)
2024-08-05 23:41:34,850 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_tenant_id_92d37185_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,851 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_metric_id_e05f23a8_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,851 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_tenant_id_92d37185" ON "metrics_forecast" ("tenant_id"); (params None)
2024-08-05 23:41:34,854 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_metric_id_e05f23a8" ON "metrics_forecast" ("metric_id"); (params None)
2024-08-05 23:41:34,856 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD CONSTRAINT "metrics_experiment_tenant_id_10fa364a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,858 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_tenant_id_10fa364a" ON "metrics_experiment" ("tenant_id"); (params None)
2024-08-05 23:41:34,860 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_metri_experiment_id_metric_id_a9d54b29_uniq" UNIQUE ("experiment_id", "metric_id"); (params None)
2024-08-05 23:41:34,863 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_experiment_id_372c6b59_fk_metrics_e" FOREIGN KEY ("experiment_id") REFERENCES "metrics_experiment" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,864 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_metric_id_c8f84167_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,865 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_experiment_id_372c6b59" ON "metrics_experiment_metrics" ("experiment_id"); (params None)
2024-08-05 23:41:34,867 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_metric_id_c8f84167" ON "metrics_experiment_metrics" ("metric_id"); (params None)
2024-08-05 23:41:34,869 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_2e1e5750_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,871 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_from_metric_id_33b50521_fk_metrics_metric_id" FOREIGN KEY ("from_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,872 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_to_metric_id_94489c1c_fk_metrics_metric_id" FOREIGN KEY ("to_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,872 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_tenant_id_2e1e5750" ON "metrics_connection" ("tenant_id"); (params None)
2024-08-05 23:41:34,874 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_from_metric_id_33b50521" ON "metrics_connection" ("from_metric_id"); (params None)
2024-08-05 23:41:34,876 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_to_metric_id_94489c1c" ON "metrics_connection" ("to_metric_id"); (params None)
2024-08-05 23:41:34,878 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_tenant_id_9e474130_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,879 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_metric_id_1b3c3295_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,880 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_tenant_id_9e474130" ON "metrics_anomaly" ("tenant_id"); (params None)
2024-08-05 23:41:34,883 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_metric_id_1b3c3295" ON "metrics_anomaly" ("metric_id"); (params None)
2024-08-05 23:41:34,885 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_tenant_id_86ffa3a9_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,886 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_metric_id_c1b270f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,887 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_tenant_id_86ffa3a9" ON "metrics_actionremark" ("tenant_id"); (params None)
2024-08-05 23:41:34,888 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_metric_id_c1b270f2" ON "metrics_actionremark" ("metric_id"); (params None)
2024-08-05 23:41:34,890 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_project" ADD CONSTRAINT "metrics_project_tenant_id_db4a1170_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,891 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_tenant_id_db4a1170" ON "metrics_project" ("tenant_id"); (params None)
2024-08-05 23:41:34,894 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD CONSTRAINT "metrics_report_tenant_id_d1cf4812_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,895 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_tenant_id_d1cf4812" ON "metrics_report" ("tenant_id"); (params None)
2024-08-05 23:41:34,898 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_name_project_id_2d57d4da_uniq" UNIQUE ("name", "project_id"); (params None)
2024-08-05 23:41:34,900 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_project_id_b7ac5c8e_fk_metrics_project_id" FOREIGN KEY ("project_id") REFERENCES "metrics_project" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,902 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_tenant_id_c286653b_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,902 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_project_id_b7ac5c8e" ON "metrics_tag" ("project_id"); (params None)
2024-08-05 23:41:34,904 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_tenant_id_c286653b" ON "metrics_tag" ("tenant_id"); (params None)
2024-08-05 23:41:34,907 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_tag_id_a8e1a165_uniq" UNIQUE ("metric_id", "tag_id"); (params None)
2024-08-05 23:41:34,910 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_b2a068f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,911 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_tag_id_61869f56_fk_metrics_tag_id" FOREIGN KEY ("tag_id") REFERENCES "metrics_tag" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,912 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_metric_id_b2a068f2" ON "metrics_metric_tags" ("metric_id"); (params None)
2024-08-05 23:41:34,914 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_tag_id_61869f56" ON "metrics_metric_tags" ("tag_id"); (params None)
2024-08-05 23:41:34,917 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,917 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,919 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_metric_id_181e8748" ON "metrics_target" ("metric_id"); (params None)
2024-08-05 23:41:34,922 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_tenant_id_118eb54a" ON "metrics_target" ("tenant_id"); (params None)
2024-08-05 23:41:34,924 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_metric_id_25179b98_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,926 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_tenant_id_4cb1485d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:34,927 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_metric_id_25179b98" ON "metrics_trend" ("metric_id"); (params None)
2024-08-05 23:41:34,930 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_tenant_id_4cb1485d" ON "metrics_trend" ("tenant_id"); (params None)
2024-08-05 23:41:35,096 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_date_33d1e0bd" ON "metrics_actionremark" ("date"); (params None)
2024-08-05 23:41:35,109 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_detection_date_ee75a187" ON "metrics_anomaly" ("detection_date"); (params None)
2024-08-05 23:41:35,121 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c" ON "metrics_category" ("name"); (params None)
2024-08-05 23:41:35,124 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c_like" ON "metrics_category" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:35,135 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d" ON "metrics_client" ("name"); (params None)
2024-08-05 23:41:35,137 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d_like" ON "metrics_client" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:35,148 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET DEFAULT '{}'; (params None)
2024-08-05 23:41:35,149 - django.db.backends.schema - DEBUG - UPDATE "metrics_dashboard" SET "layout" = '{}' WHERE "layout" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:41:35,150 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET NOT NULL; (params None)
2024-08-05 23:41:35,150 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" DROP DEFAULT; (params None)
2024-08-05 23:41:35,161 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e" ON "metrics_dashboard" ("name"); (params None)
2024-08-05 23:41:35,164 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e_like" ON "metrics_dashboard" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:35,175 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_end_date_31af6c05" ON "metrics_experiment" ("end_date"); (params None)
2024-08-05 23:41:35,186 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7" ON "metrics_experiment" ("name"); (params None)
2024-08-05 23:41:35,189 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7_like" ON "metrics_experiment" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:35,203 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET DEFAULT '{}'; (params None)
2024-08-05 23:41:35,204 - django.db.backends.schema - DEBUG - UPDATE "metrics_experiment" SET "results" = '{}' WHERE "results" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:41:35,205 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET NOT NULL; (params None)
2024-08-05 23:41:35,205 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" DROP DEFAULT; (params None)
2024-08-05 23:41:35,216 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_start_date_a6deff13" ON "metrics_experiment" ("start_date"); (params None)
2024-08-05 23:41:35,228 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET DEFAULT '{}'; (params None)
2024-08-05 23:41:35,229 - django.db.backends.schema - DEBUG - UPDATE "metrics_forecast" SET "confidence_interval" = '{}' WHERE "confidence_interval" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:41:35,230 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET NOT NULL; (params None)
2024-08-05 23:41:35,230 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" DROP DEFAULT; (params None)
2024-08-05 23:41:35,240 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_forecast_date_71750ae8" ON "metrics_forecast" ("forecast_date"); (params None)
2024-08-05 23:41:35,254 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_date_f27e0e6a" ON "metrics_historicaldata" ("date"); (params None)
2024-08-05 23:41:35,267 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_last_updated_3e38a760" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:41:35,279 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5" ON "metrics_metric" ("name"); (params None)
2024-08-05 23:41:35,282 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5_like" ON "metrics_metric" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:35,295 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e" ON "metrics_metric" ("type"); (params None)
2024-08-05 23:41:35,298 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e_like" ON "metrics_metric" ("type" varchar_pattern_ops); (params None)
2024-08-05 23:41:35,318 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80" ON "metrics_project" ("name"); (params None)
2024-08-05 23:41:35,322 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80_like" ON "metrics_project" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:35,333 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET DEFAULT '{}'; (params None)
2024-08-05 23:41:35,334 - django.db.backends.schema - DEBUG - UPDATE "metrics_report" SET "configuration" = '{}' WHERE "configuration" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:41:35,334 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET NOT NULL; (params None)
2024-08-05 23:41:35,335 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" DROP DEFAULT; (params None)
2024-08-05 23:41:35,346 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34" ON "metrics_report" ("name"); (params None)
2024-08-05 23:41:35,349 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34_like" ON "metrics_report" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:35,362 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a" ON "metrics_tag" ("name"); (params None)
2024-08-05 23:41:35,365 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a_like" ON "metrics_tag" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:35,377 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_target_date_81507ff5" ON "metrics_target" ("target_date"); (params None)
2024-08-05 23:41:35,389 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_end_date_8444ef38" ON "metrics_trend" ("end_date"); (params None)
2024-08-05 23:41:35,403 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_start_date_7b1a850f" ON "metrics_trend" ("start_date"); (params None)
2024-08-05 23:41:35,414 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_act_metric__be3429_idx" ON "metrics_actionremark" ("metric_id", "date"); (params None)
2024-08-05 23:41:35,426 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ano_metric__84982d_idx" ON "metrics_anomaly" ("metric_id", "detection_date"); (params None)
2024-08-05 23:41:35,440 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_con_from_me_9411ea_idx" ON "metrics_connection" ("from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:41:35,452 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_exp_start_d_04716a_idx" ON "metrics_experiment" ("start_date", "end_date"); (params None)
2024-08-05 23:41:35,464 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_for_metric__4c9ae2_idx" ON "metrics_forecast" ("metric_id", "forecast_date"); (params None)
2024-08-05 23:41:35,476 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_his_metric__a2923a_idx" ON "metrics_historicaldata" ("metric_id", "date"); (params None)
2024-08-05 23:41:35,488 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_name_c9d100_idx" ON "metrics_metric" ("name", "type"); (params None)
2024-08-05 23:41:35,500 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_7984a6_idx" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:41:35,512 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1bdb27_idx" ON "metrics_tag" ("name", "project_id"); (params None)
2024-08-05 23:41:35,528 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tar_metric__234682_idx" ON "metrics_target" ("metric_id", "target_date"); (params None)
2024-08-05 23:41:35,540 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tre_metric__d386bb_idx" ON "metrics_trend" ("metric_id", "start_date", "end_date"); (params None)
2024-08-05 23:41:35,554 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_con_from_me_9411ea_idx"; (params None)
2024-08-05 23:41:35,564 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:41:35,566 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:41:35,578 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_from_metric_id_aa131d91_uniq" UNIQUE ("tenant_id", "from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:41:35,581 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_project_id_4c1b22ec" ON "metrics_connection" ("project_id"); (params None)
2024-08-05 23:41:35,597 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; ALTER TABLE "metrics_connection" DROP CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id"; (params None)
2024-08-05 23:41:35,598 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "project_id" CASCADE; (params None)
2024-08-05 23:41:35,609 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:41:35,611 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:41:35,623 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:41:35,625 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_project_id_36bdbe46" ON "metrics_metric" ("project_id"); (params None)
2024-08-05 23:41:35,630 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_correlation" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "lag" integer NOT NULL, "pearson_correlation" double precision NOT NULL, "spearman_correlation" double precision NOT NULL); (params None)
2024-08-05 23:41:35,634 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:35,642 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dataqualityscore" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_entry" varchar(255) NOT NULL, "completeness_score" double precision NOT NULL, "accuracy_score" double precision NOT NULL, "consistency_score" double precision NOT NULL, "timeliness_score" double precision NOT NULL, "overall_score" double precision NOT NULL); (params None)
2024-08-05 23:41:35,646 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_impactanalysis" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "before_value" double precision NOT NULL, "after_value" double precision NOT NULL, "percentage_change" double precision NOT NULL, "confidence" double precision NOT NULL, "artifact_link" varchar(200) NOT NULL); (params None)
2024-08-05 23:41:35,649 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_insight" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "title" varchar(200) NOT NULL, "content" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:35,655 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metricmetadata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_source" varchar(100) NOT NULL, "source_url" varchar(200) NOT NULL, "rhythm" varchar(20) NOT NULL, "last_updated" timestamp with time zone NOT NULL, "technical_description" text NOT NULL, "description" text NOT NULL, "artifacts_url" varchar(200) NOT NULL, "hypothesis" text NOT NULL, "confidence" varchar(20) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL); (params None)
2024-08-05 23:41:35,660 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metrictarget" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "target_kpi" varchar(100) NOT NULL, "target_remarks" text NOT NULL, "target_date" date NULL, "target_value" double precision NULL); (params None)
2024-08-05 23:41:35,666 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_strategy" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "estimated_time" interval NOT NULL, "artifacts_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:35,672 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tacticalsolution" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "artifact_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:35,678 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_team" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:35,684 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_technicalindicator" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "stochastic_value" double precision NOT NULL, "rsi_value" double precision NOT NULL, "percent_change" double precision NOT NULL, "moving_average" double precision NOT NULL); (params None)
2024-08-05 23:41:35,688 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_timedimension" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL UNIQUE, "day" integer NOT NULL, "day_of_week" integer NOT NULL, "day_name" varchar(10) NOT NULL, "week" integer NOT NULL, "month" integer NOT NULL, "month_name" varchar(10) NOT NULL, "quarter" integer NOT NULL, "year" integer NOT NULL, "is_weekend" boolean NOT NULL, "is_holiday" boolean NOT NULL); (params None)
2024-08-05 23:41:35,692 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_userprofile" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY); (params None)
2024-08-05 23:41:35,708 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_metric_id_181e8748_fk_metrics_metric_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id"; (params None)
2024-08-05 23:41:35,709 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "metric_id" CASCADE; (params None)
2024-08-05 23:41:35,721 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id"; (params None)
2024-08-05 23:41:35,722 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:41:35,733 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_name_c9d100_idx"; (params None)
2024-08-05 23:41:35,744 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_last_up_7984a6_idx"; (params None)
2024-08-05 23:41:35,755 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" RENAME COLUMN "description" TO "summary"; (params None)
2024-08-05 23:41:35,767 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq"; (params None)
2024-08-05 23:41:35,904 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "correlation_coefficient" CASCADE; (params None)
2024-08-05 23:41:35,914 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" DROP COLUMN "results" CASCADE; (params None)
2024-08-05 23:41:35,924 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "anomaly_detected" CASCADE; (params None)
2024-08-05 23:41:35,935 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "forecasted_value" CASCADE; (params None)
2024-08-05 23:41:35,945 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "trend_component" CASCADE; (params None)
2024-08-05 23:41:35,956 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "importance" varchar(20) DEFAULT 'MEDIUM' NOT NULL; (params None)
2024-08-05 23:41:35,957 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "importance" DROP DEFAULT; (params None)
2024-08-05 23:41:35,967 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:41:35.966913+00:00' NOT NULL; (params None)
2024-08-05 23:41:35,968 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:41:35,979 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "anomaly_type" varchar(20) DEFAULT 'IGNORE' NOT NULL; (params None)
2024-08-05 23:41:35,980 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "anomaly_type" DROP DEFAULT; (params None)
2024-08-05 23:41:35,991 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "quality" varchar(20) DEFAULT 'LOW' NOT NULL; (params None)
2024-08-05 23:41:35,992 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "quality" DROP DEFAULT; (params None)
2024-08-05 23:41:36,001 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "impact_description" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:41:36,002 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "impact_description" DROP DEFAULT; (params None)
2024-08-05 23:41:36,012 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "objective" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:41:36,013 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "objective" DROP DEFAULT; (params None)
2024-08-05 23:41:36,025 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_date" date NULL; (params None)
2024-08-05 23:41:36,035 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_files" varchar(100) NULL; (params None)
2024-08-05 23:41:36,046 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_summary" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:41:36,046 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "result_summary" DROP DEFAULT; (params None)
2024-08-05 23:41:36,058 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_value" double precision NULL; (params None)
2024-08-05 23:41:36,068 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:41:36.068313+00:00' NOT NULL; (params None)
2024-08-05 23:41:36,069 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:41:36,079 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "variance" double precision NULL; (params None)
2024-08-05 23:41:36,090 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD COLUMN "forecast_id" bigint NULL CONSTRAINT "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" REFERENCES "metrics_forecast"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" IMMEDIATE; (params None)
2024-08-05 23:41:36,103 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "impact" TYPE varchar(20) USING "impact"::varchar(20); (params None)
2024-08-05 23:41:36,191 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "status" TYPE varchar(20); (params None)
2024-08-05 23:41:36,317 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric1_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,329 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric2_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,342 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,350 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:41:36,369 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,388 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:41:36,408 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:36,427 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "experiment_id" bigint NOT NULL CONSTRAINT "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" REFERENCES "metrics_experiment"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" IMMEDIATE; (params None)
2024-08-05 23:41:36,446 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,466 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,487 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,506 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,527 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "user_id" bigint NOT NULL CONSTRAINT "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,547 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "data_quality_score_id" bigint NULL UNIQUE CONSTRAINT "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" REFERENCES "metrics_dataqualityscore"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" IMMEDIATE; (params None)
2024-08-05 23:41:36,694 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "metric_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,717 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,737 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,758 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,781 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,802 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:41:36,824 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:36,847 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_team" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,872 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "team_id" bigint NOT NULL CONSTRAINT "metrics_strategy_team_id_f1781500_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_team_id_f1781500_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,896 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,918 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,941 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_experiment_team_id_537107e3_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_experiment_team_id_537107e3_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:41:36,964 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:41:36,988 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:37,012 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_timedimension" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:37,038 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:37,065 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "user_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:41:37,070 - django.db.backends.schema - DEBUG - DROP TABLE "metrics_target" CASCADE; (params None)
2024-08-05 23:41:37,092 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "confidence" CASCADE; (params None)
2024-08-05 23:41:37,113 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "description" CASCADE; (params None)
2024-08-05 23:41:37,271 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "hypothesis" CASCADE; (params None)
2024-08-05 23:41:37,290 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "last_updated" CASCADE; (params None)
2024-08-05 23:41:37,309 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_x" CASCADE; (params None)
2024-08-05 23:41:37,328 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_y" CASCADE; (params None)
2024-08-05 23:41:37,346 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "rhythm" CASCADE; (params None)
2024-08-05 23:41:37,365 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "source" CASCADE; (params None)
2024-08-05 23:41:37,384 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "technical_description" CASCADE; (params None)
2024-08-05 23:41:37,404 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD CONSTRAINT "metrics_correlation_tenant_id_metric1_id_met_49a4c34a_uniq" UNIQUE ("tenant_id", "metric1_id", "metric2_id", "lag"); (params None)
2024-08-05 23:41:37,424 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_metric__b85d3a_idx" ON "metrics_insight" ("metric_id", "date"); (params None)
2024-08-05 23:41:37,446 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_user_id_1ebb42_idx" ON "metrics_insight" ("user_id", "date"); (params None)
2024-08-05 23:41:37,467 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_metric__a2b705_idx" ON "metrics_metrictarget" ("metric_id", "target_date"); (params None)
2024-08-05 23:41:37,488 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_6e2e67_idx" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:41:37,508 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_date_53cb14_idx" ON "metrics_timedimension" ("date"); (params None)
2024-08-05 23:41:37,529 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_year_92da9e_idx" ON "metrics_timedimension" ("year", "month", "day"); (params None)
2024-08-05 23:41:37,532 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_username_6e55f358_like" ON "metrics_customuser" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:41:37,534 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_date_ded95ba1" ON "metrics_insight" ("date"); (params None)
2024-08-05 23:41:37,537 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_last_updated_76599a1b" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:41:37,539 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_target_date_38cd9191" ON "metrics_metrictarget" ("target_date"); (params None)
2024-08-05 23:41:37,541 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_forecast_id_29590c29" ON "metrics_historicaldata" ("forecast_id"); (params None)
2024-08-05 23:41:37,543 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric1_id_6e1c2404" ON "metrics_correlation" ("metric1_id"); (params None)
2024-08-05 23:41:37,545 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric2_id_f2cc46dd" ON "metrics_correlation" ("metric2_id"); (params None)
2024-08-05 23:41:37,547 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_tenant_id_a00a5169" ON "metrics_correlation" ("tenant_id"); (params None)
2024-08-05 23:41:37,550 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_customuser_id_group_id_1c5fc435_uniq" UNIQUE ("customuser_id", "group_id"); (params None)
2024-08-05 23:41:37,553 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_g_customuser_id_fc13f3af_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:37,554 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_group_id_6b097e12_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:37,555 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_customuser_id_fc13f3af" ON "metrics_customuser_groups" ("customuser_id"); (params None)
2024-08-05 23:41:37,558 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_group_id_6b097e12" ON "metrics_customuser_groups" ("group_id"); (params None)
2024-08-05 23:41:37,561 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_tenant_id_02b7403c" ON "metrics_customuser" ("tenant_id"); (params None)
2024-08-05 23:41:37,563 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_user__customuser_id_permission_68cc320f_uniq" UNIQUE ("customuser_id", "permission_id"); (params None)
2024-08-05 23:41:37,566 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_customuser_id_46e97f00_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:37,567 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_permission_id_d66d657c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:37,568 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_customuser_id_46e97f00" ON "metrics_customuser_user_permissions" ("customuser_id"); (params None)
2024-08-05 23:41:37,570 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_permission_id_d66d657c" ON "metrics_customuser_user_permissions" ("permission_id"); (params None)
2024-08-05 23:41:37,572 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_tenant_id_8e9f296d" ON "metrics_dataqualityscore" ("tenant_id"); (params None)
2024-08-05 23:41:37,574 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_experiment_id_1beae7fe" ON "metrics_impactanalysis" ("experiment_id"); (params None)
2024-08-05 23:41:37,577 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_metric_id_f4b9eeb6" ON "metrics_impactanalysis" ("metric_id"); (params None)
2024-08-05 23:41:37,579 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_tenant_id_126ca20d" ON "metrics_impactanalysis" ("tenant_id"); (params None)
2024-08-05 23:41:37,581 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_metric_id_26d3a9d8" ON "metrics_insight" ("metric_id"); (params None)
2024-08-05 23:41:37,583 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_tenant_id_724d7d85" ON "metrics_insight" ("tenant_id"); (params None)
2024-08-05 23:41:37,585 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_user_id_83d421e1" ON "metrics_insight" ("user_id"); (params None)
2024-08-05 23:41:37,587 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_tenant_id_3277f967" ON "metrics_metricmetadata" ("tenant_id"); (params None)
2024-08-05 23:41:37,589 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_metric_id_7876e2c8" ON "metrics_metrictarget" ("metric_id"); (params None)
2024-08-05 23:41:37,592 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_tenant_id_b26a17f8" ON "metrics_metrictarget" ("tenant_id"); (params None)
2024-08-05 23:41:37,594 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_tenant_id_1323395e" ON "metrics_strategy" ("tenant_id"); (params None)
2024-08-05 23:41:37,596 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_metric_id_9887ffa4" ON "metrics_tacticalsolution" ("metric_id"); (params None)
2024-08-05 23:41:37,598 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_tenant_id_cf9028f0" ON "metrics_tacticalsolution" ("tenant_id"); (params None)
2024-08-05 23:41:37,599 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_team_tenant_id_3a14c47d" ON "metrics_team" ("tenant_id"); (params None)
2024-08-05 23:41:37,602 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_team_id_f1781500" ON "metrics_strategy" ("team_id"); (params None)
2024-08-05 23:41:37,605 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_team_id_f140658d" ON "metrics_metricmetadata" ("team_id"); (params None)
2024-08-05 23:41:37,607 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_team_id_4c4ffc18" ON "metrics_customuser" ("team_id"); (params None)
2024-08-05 23:41:37,610 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_team_id_537107e3" ON "metrics_experiment" ("team_id"); (params None)
2024-08-05 23:41:37,612 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_metric_id_3e2eead6" ON "metrics_technicalindicator" ("metric_id"); (params None)
2024-08-05 23:41:37,614 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_tenant_id_f4de3b44" ON "metrics_technicalindicator" ("tenant_id"); (params None)
2024-08-05 23:41:37,617 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_timedimension_tenant_id_f375bb45" ON "metrics_timedimension" ("tenant_id"); (params None)
2024-08-05 23:41:37,619 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_userprofile_tenant_id_cca71dae" ON "metrics_userprofile" ("tenant_id"); (params None)
2024-08-05 23:41:37,642 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "strength" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:41:37,642 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "strength" DROP DEFAULT; (params None)
2024-08-05 23:41:37,662 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "lower_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:41:37,663 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "lower_bound" DROP DEFAULT; (params None)
2024-08-05 23:41:37,681 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "upper_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:41:37,682 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "upper_bound" DROP DEFAULT; (params None)
2024-08-05 23:41:37,703 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD COLUMN "slope" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:41:37,704 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ALTER COLUMN "slope" DROP DEFAULT; (params None)
2024-08-05 23:41:37,727 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_movingaverage" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "ma_type" varchar(10) NOT NULL, "period" integer NOT NULL, "value" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:37,753 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_networkanalysisresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "analysis_type" varchar(20) NOT NULL, "result" jsonb NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:37,782 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_seasonalityresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "seasonality_type" varchar(20) NOT NULL, "strength" double precision NOT NULL, "period" integer NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:37,945 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trendchangepoint" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "change_type" varchar(20) NOT NULL, "significance" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:37,948 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD CONSTRAINT "metrics_movingaverage_metric_id_7c61cebf_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:37,949 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_metric_id_7c61cebf" ON "metrics_movingaverage" ("metric_id"); (params None)
2024-08-05 23:41:37,951 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD CONSTRAINT "metrics_networkanaly_metric_id_a4c90102_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:37,952 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_metric_id_a4c90102" ON "metrics_networkanalysisresult" ("metric_id"); (params None)
2024-08-05 23:41:37,954 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityr_metric_id_6e494791_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:37,955 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_metric_id_6e494791" ON "metrics_seasonalityresult" ("metric_id"); (params None)
2024-08-05 23:41:37,957 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD CONSTRAINT "metrics_trendchangep_metric_id_f8eb9f76_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:37,958 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_metric_id_f8eb9f76" ON "metrics_trendchangepoint" ("metric_id"); (params None)
2024-08-05 23:41:37,987 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:41:37,989 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:41:38,014 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" IMMEDIATE; (params None)
2024-08-05 23:41:38,016 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:41:38,040 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ALTER COLUMN "value" DROP NOT NULL; (params None)
2024-08-05 23:41:38,063 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD CONSTRAINT "metrics_dataqualityscore_tenant_id_metric_id_proj_66b9fb01_uniq" UNIQUE ("tenant_id", "metric_id", "project_id"); (params None)
2024-08-05 23:41:38,065 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_metric_id_1b6367d1" ON "metrics_dataqualityscore" ("metric_id"); (params None)
2024-08-05 23:41:38,068 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_project_id_123a4f58" ON "metrics_dataqualityscore" ("project_id"); (params None)
2024-08-05 23:41:38,091 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:41:38,120 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:38,122 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:41:38,148 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:38,149 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:41:38,176 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:38,177 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:41:38,203 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:38,204 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:41:38,225 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq" UNIQUE ("tenant_id", "metric_id"); (params None)
2024-08-05 23:41:38,228 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_tenant_id_5a9de228" ON "metrics_movingaverage" ("tenant_id"); (params None)
2024-08-05 23:41:38,230 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_tenant_id_16a6ba09" ON "metrics_networkanalysisresult" ("tenant_id"); (params None)
2024-08-05 23:41:38,232 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_tenant_id_ca2da3fd" ON "metrics_seasonalityresult" ("tenant_id"); (params None)
2024-08-05 23:41:38,234 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_tenant_id_da10d898" ON "metrics_trendchangepoint" ("tenant_id"); (params None)
2024-08-05 23:41:38,264 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:38,266 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:41:38,267 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_metric_id_c86f5720" ON "metrics_report" ("metric_id"); (params None)
2024-08-05 23:41:38,291 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "analysis_result" jsonb NULL; (params None)
2024-08-05 23:41:38,311 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "anomaly_result" jsonb NULL; (params None)
2024-08-05 23:41:38,333 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:41:38.333118+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:41:38,334 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:41:38,356 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "forecast_result" jsonb NULL; (params None)
2024-08-05 23:41:38,376 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "relationship_result" jsonb NULL; (params None)
2024-08-05 23:41:38,527 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "report" text DEFAULT '1' NOT NULL; (params None)
2024-08-05 23:41:38,527 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "report" DROP DEFAULT; (params None)
2024-08-05 23:41:38,549 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "updated_at" timestamp with time zone DEFAULT '2024-08-05T23:41:38.549206+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:41:38,550 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "updated_at" DROP DEFAULT; (params None)
2024-08-05 23:41:38,604 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_trendchangepoint" DROP CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c"; (params None)
2024-08-05 23:41:38,605 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:41:38,624 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "significance" DROP NOT NULL; (params None)
2024-08-05 23:41:38,642 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" RENAME COLUMN "change_type" TO "direction"; (params None)
2024-08-05 23:41:38,685 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:41:38.685060+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:41:38,686 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:41:38,710 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq"; (params None)
2024-08-05 23:41:38,711 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresul_metric_id_seasonality_ty_d3492b78_uniq" UNIQUE ("metric_id", "seasonality_type"); (params None)
2024-08-05 23:41:38,741 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c"; (params None)
2024-08-05 23:41:38,742 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:41:38,744 - django.db.backends.schema - DEBUG - CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:38,749 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" ("session_key" varchar_pattern_ops); (params None)
2024-08-05 23:41:38,751 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date"); (params None)
2024-08-05 23:41:39,764 - metrics.computations.data_preparation - INFO - Loaded metric 7 for tenant 4 and project 4
2024-08-05 23:41:39,764 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 7
2024-08-05 23:41:39,765 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:39,765 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:39,766 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 7
2024-08-05 23:41:39,770 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:39,770 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:39,773 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  131.887062          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:39,773 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:39,776 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  131.887062          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:39,776 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:39,779 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:41,615 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 7
2024-08-05 23:41:41,617 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:41,618 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:41,619 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:41,621 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  123.449046          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:41,621 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:41,623 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  123.449046          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:41,626 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36309268522831883, Timeliness: nan
2024-08-05 23:41:41,626 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.43642284094396
2024-08-05 23:41:41,630 - metrics.computations.data_preparation - INFO - Data quality score: 45.43642284094396
2024-08-05 23:41:41,645 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 7, 'tenant_id': 4, 'project_id': 4, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.43642284094396, 'outliers_handled': True, 'profile': {'mean': 99.59544866288086, 'median': 99.52411271024293, 'std': 10.134825958722937, 'min': 76.29438017533805, 'max': 123.4490463702239, 'skewness': 0.07540678228924934, 'kurtosis': -0.41656644647887164, 'missing_percentage': 0.0}}
2024-08-05 23:41:41,651 - metrics.computations.data_preparation - INFO - Loaded metric 7 for tenant 4 and project 4
2024-08-05 23:41:41,651 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 7
2024-08-05 23:41:41,652 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:41,652 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:41,654 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 7
2024-08-05 23:41:41,662 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:41,662 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:41,665 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  131.887062          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:41,665 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:41,667 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  131.887062          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:41,668 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:41,673 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:43,397 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 7
2024-08-05 23:41:43,400 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:43,401 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:43,402 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:43,404 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  123.449046          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:43,404 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:43,406 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  123.449046          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:43,408 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36309268522831883, Timeliness: nan
2024-08-05 23:41:43,408 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.43642284094396
2024-08-05 23:41:43,411 - metrics.computations.data_preparation - INFO - Data quality score: 45.43642284094396
2024-08-05 23:41:43,475 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 7, 'tenant_id': 4, 'project_id': 4, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.43642284094396, 'outliers_handled': True, 'profile': {'mean': 99.59544866288086, 'median': 99.52411271024293, 'std': 10.134825958722937, 'min': 76.29438017533805, 'max': 123.4490463702239, 'skewness': 0.07540678228924934, 'kurtosis': -0.41656644647887164, 'missing_percentage': 0.0}}
2024-08-05 23:41:43,475 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:41:43,475 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 7
2024-08-05 23:41:43,486 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=3, strength=0.01
2024-08-05 23:41:43,500 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=3, strength=0.01
2024-08-05 23:41:43,505 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 7
2024-08-05 23:41:43,505 - metrics.computations.feature_engineering - INFO - Parameters for metric 7: dynamic
2024-08-05 23:41:43,505 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 7: {'seasonality_period': 3, 'forecast_horizon': 3, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:41:43,509 - metrics.computations.data_preparation - INFO - Loaded metric 7 for tenant 4 and project 4
2024-08-05 23:41:43,509 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 7
2024-08-05 23:41:43,511 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:43,512 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:43,520 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 7
2024-08-05 23:41:43,531 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:43,532 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:43,536 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  131.887062          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:43,536 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:43,540 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  131.887062          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:43,541 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:43,545 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:45,292 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 7
2024-08-05 23:41:45,294 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:45,296 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:45,296 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:45,299 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  123.449046          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:45,299 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:45,301 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  123.449046          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:45,303 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36309268522831883, Timeliness: nan
2024-08-05 23:41:45,303 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.43642284094396
2024-08-05 23:41:45,306 - metrics.computations.data_preparation - INFO - Data quality score: 45.43642284094396
2024-08-05 23:41:45,321 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 7, 'tenant_id': 4, 'project_id': 4, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.43642284094396, 'outliers_handled': True, 'profile': {'mean': 99.59544866288086, 'median': 99.52411271024293, 'std': 10.134825958722937, 'min': 76.29438017533805, 'max': 123.4490463702239, 'skewness': 0.07540678228924934, 'kurtosis': -0.41656644647887164, 'missing_percentage': 0.0}}
2024-08-05 23:41:45,325 - metrics.computations.data_preparation - INFO - Loaded metric 7 for tenant 4 and project 4
2024-08-05 23:41:45,325 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 7
2024-08-05 23:41:45,326 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:45,326 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:45,329 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 7
2024-08-05 23:41:45,336 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:45,336 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:45,339 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  131.887062          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:45,340 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:45,342 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  131.887062          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:45,343 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:45,346 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:47,092 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 7
2024-08-05 23:41:47,094 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:47,096 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:47,096 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:47,099 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  123.449046          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:47,099 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:47,101 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  123.449046          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:47,103 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36309268522831883, Timeliness: nan
2024-08-05 23:41:47,103 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.43642284094396
2024-08-05 23:41:47,106 - metrics.computations.data_preparation - INFO - Data quality score: 45.43642284094396
2024-08-05 23:41:47,120 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 7, 'tenant_id': 4, 'project_id': 4, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.43642284094396, 'outliers_handled': True, 'profile': {'mean': 99.59544866288086, 'median': 99.52411271024293, 'std': 10.134825958722937, 'min': 76.29438017533805, 'max': 123.4490463702239, 'skewness': 0.07540678228924934, 'kurtosis': -0.41656644647887164, 'missing_percentage': 0.0}}
2024-08-05 23:41:47,120 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:41:47,120 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 7
2024-08-05 23:41:47,126 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=3, strength=0.01
2024-08-05 23:41:47,131 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=3, strength=0.01
2024-08-05 23:41:47,135 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 7
2024-08-05 23:41:47,135 - metrics.computations.feature_engineering - INFO - Parameters for metric 7: dynamic
2024-08-05 23:41:47,135 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 7: {'seasonality_period': 3, 'forecast_horizon': 3, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:41:47,136 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Setup completed
2024-08-05 23:41:47,139 - metrics.computations.data_preparation - INFO - Loaded metric 7 for tenant 4 and project 4
2024-08-05 23:41:47,139 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 7
2024-08-05 23:41:47,140 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:47,140 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:47,146 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 7
2024-08-05 23:41:47,154 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:47,155 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:47,158 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  131.887062          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:47,158 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:47,161 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  131.887062          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:47,162 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:47,165 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:48,900 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 7
2024-08-05 23:41:48,902 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:48,904 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:48,904 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:48,906 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  123.449046          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:48,907 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:48,909 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  123.449046          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:48,911 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36309268522831883, Timeliness: nan
2024-08-05 23:41:48,911 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.43642284094396
2024-08-05 23:41:48,914 - metrics.computations.data_preparation - INFO - Data quality score: 45.43642284094396
2024-08-05 23:41:48,930 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 7, 'tenant_id': 4, 'project_id': 4, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.43642284094396, 'outliers_handled': True, 'profile': {'mean': 99.59544866288086, 'median': 99.52411271024293, 'std': 10.134825958722937, 'min': 76.29438017533805, 'max': 123.4490463702239, 'skewness': 0.07540678228924934, 'kurtosis': -0.41656644647887164, 'missing_percentage': 0.0}}
2024-08-05 23:41:48,934 - metrics.computations.data_preparation - INFO - Loaded metric 7 for tenant 4 and project 4
2024-08-05 23:41:48,934 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 7
2024-08-05 23:41:48,935 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:48,935 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 7 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:48,940 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 7
2024-08-05 23:41:48,950 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:48,950 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:48,953 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  131.887062          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:48,953 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:48,956 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  131.887062          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:48,956 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:48,959 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:50,716 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 7
2024-08-05 23:41:50,718 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:50,719 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:50,720 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:50,722 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  123.449046          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:50,722 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:50,724 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   83.136814          4
2023-01-02   95.122493          4
2023-01-03  123.449046          4
2023-01-04  109.090695          4
2023-01-05  100.630200          4
2024-08-05 23:41:50,726 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36309268522831883, Timeliness: nan
2024-08-05 23:41:50,727 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.43642284094396
2024-08-05 23:41:50,730 - metrics.computations.data_preparation - INFO - Data quality score: 45.43642284094396
2024-08-05 23:41:50,744 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 7, 'tenant_id': 4, 'project_id': 4, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.43642284094396, 'outliers_handled': True, 'profile': {'mean': 99.59544866288086, 'median': 99.52411271024293, 'std': 10.134825958722937, 'min': 76.29438017533805, 'max': 123.4490463702239, 'skewness': 0.07540678228924934, 'kurtosis': -0.41656644647887164, 'missing_percentage': 0.0}}
2024-08-05 23:41:50,746 - metrics.computations.computations_anomalies - INFO - Initialized AnomalyDetector for metric 7
2024-08-05 23:41:50,746 - metrics.computations.computations_anomalies - INFO - Seasonality period: 7
2024-08-05 23:41:50,747 - metrics.computations.computations_anomalies - INFO - Window size: 30
2024-08-05 23:41:50,747 - metrics.computations.computations_anomalies - INFO - Base threshold: 3.0
2024-08-05 23:41:50,747 - metrics.computations.computations_anomalies - INFO - Context window: 5
2024-08-05 23:41:50,747 - metrics.computations.computations_anomalies - INFO - Global threshold: 4.0
2024-08-05 23:41:50,747 - metrics.computations.computations_anomalies - WARNING - Not enough data for anomaly detection for metric 7
2024-08-05 23:41:50,878 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Teardown completed
```

## test_forecast_computation_robustness (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
Status: error
Duration: 16.734 seconds

### Error
```
Traceback (most recent call last):
  File "/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/unittest/mock.py", line 1369, in patched
    return func(*newargs, **newkeywargs)
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_permanent_computations_robustness.py", line 102, in test_forecast_computation_robustness
    self.assertEqual(forecaster.params['forecast_horizon'], self.params['forecast_horizon'])
AttributeError: 'Forecaster' object has no attribute 'params'
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
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
2024-08-05 23:41:50,893 - metrics - DEBUG - Starting test: test_forecast_computation_robustness (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
2024-08-05 23:41:50,897 - django.db.backends.schema - DEBUG - CREATE TABLE "django_migrations" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:50,911 - django.db.backends.schema - DEBUG - CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
2024-08-05 23:41:50,915 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params None)
2024-08-05 23:41:50,920 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL, "codename" varchar(100) NOT NULL); (params None)
2024-08-05 23:41:50,925 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(80) NOT NULL UNIQUE); (params None)
2024-08-05 23:41:50,930 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:41:50,936 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NOT NULL, "is_superuser" boolean NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:50,941 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:41:50,944 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:41:50,947 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename"); (params None)
2024-08-05 23:41:50,949 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:50,950 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id"); (params None)
2024-08-05 23:41:50,952 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_name_a6ea08ec_like" ON "auth_group" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:50,954 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id"); (params None)
2024-08-05 23:41:50,957 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:50,958 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:50,959 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id"); (params None)
2024-08-05 23:41:50,961 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id"); (params None)
2024-08-05 23:41:50,963 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_username_6821ab7c_like" ON "auth_user" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:41:50,965 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id"); (params None)
2024-08-05 23:41:50,967 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:50,969 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:50,969 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id"); (params None)
2024-08-05 23:41:50,972 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id"); (params None)
2024-08-05 23:41:50,973 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id"); (params None)
2024-08-05 23:41:50,975 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:50,976 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:50,977 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id"); (params None)
2024-08-05 23:41:50,979 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id"); (params None)
2024-08-05 23:41:50,988 - django.db.backends.schema - DEBUG - CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "action_time" timestamp with time zone NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL, "user_id" integer NOT NULL); (params None)
2024-08-05 23:41:50,994 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:50,995 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:50,996 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id"); (params None)
2024-08-05 23:41:50,999 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id"); (params None)
2024-08-05 23:41:51,018 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ALTER COLUMN "name" DROP NOT NULL; (params None)
2024-08-05 23:41:51,025 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" DROP COLUMN "name" CASCADE; (params None)
2024-08-05 23:41:51,032 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ALTER COLUMN "name" TYPE varchar(255); (params None)
2024-08-05 23:41:51,040 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "email" TYPE varchar(254); (params None)
2024-08-05 23:41:51,055 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_login" DROP NOT NULL; (params None)
2024-08-05 23:41:51,066 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "username" TYPE varchar(150); (params None)
2024-08-05 23:41:51,075 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_name" TYPE varchar(150); (params None)
2024-08-05 23:41:51,081 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group" ALTER COLUMN "name" TYPE varchar(150); (params None)
2024-08-05 23:41:51,094 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "first_name" TYPE varchar(150); (params None)
2024-08-05 23:41:51,126 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_client" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "schema_name" varchar(63) NOT NULL UNIQUE, "name" varchar(100) NOT NULL, "created_on" date NOT NULL); (params None)
2024-08-05 23:41:51,132 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_category" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,137 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dashboard" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "layout" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,144 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_domain" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "domain" varchar(253) NOT NULL UNIQUE, "is_primary" boolean NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,152 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "type" varchar(50) NOT NULL, "confidence" varchar(50) NOT NULL, "value_type" varchar(20) NOT NULL, "rhythm" varchar(20) NOT NULL, "description" text NOT NULL, "hypothesis" text NOT NULL, "technical_description" text NOT NULL, "last_updated" timestamp with time zone NOT NULL, "source" varchar(100) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL, "category_id" bigint NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,161 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_historicaldata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "value" double precision NOT NULL, "forecasted_value" double precision NULL, "anomaly_detected" boolean NOT NULL, "trend_component" varchar(50) NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,168 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_forecast" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "forecast_date" date NOT NULL, "forecast_value" double precision NOT NULL, "model_used" varchar(100) NOT NULL, "accuracy" double precision NULL, "confidence_interval" jsonb NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,181 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "status" varchar(50) NOT NULL, "results" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,187 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment_metrics" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "experiment_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,196 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_connection" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "relationship" varchar(100) NOT NULL, "correlation_coefficient" double precision NULL, "tenant_id" bigint NOT NULL, "from_metric_id" bigint NOT NULL, "to_metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,206 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_anomaly" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "detection_date" date NOT NULL, "anomaly_value" double precision NOT NULL, "anomaly_score" double precision NOT NULL, "notes" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,222 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_actionremark" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NULL, "description" text NOT NULL, "impact" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,234 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_project" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "created_on" date NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,244 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_report" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "configuration" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,258 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tag" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "project_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,271 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric_tags" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "metric_id" bigint NOT NULL, "tag_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,283 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_target" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "remarks" text NOT NULL, "target_kpi" varchar(100) NOT NULL, "target_date" date NULL, "target_value" double precision NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,300 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trend" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "trend_type" varchar(50) NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "trend_value" double precision NOT NULL, "notes" text NOT NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:41:51,306 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_schema_name_87d6fbb5_like" ON "metrics_client" ("schema_name" varchar_pattern_ops); (params None)
2024-08-05 23:41:51,308 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_category" ADD CONSTRAINT "metrics_category_tenant_id_67d98cc6_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,309 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_tenant_id_67d98cc6" ON "metrics_category" ("tenant_id"); (params None)
2024-08-05 23:41:51,311 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ADD CONSTRAINT "metrics_dashboard_tenant_id_50099a7d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,312 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_tenant_id_50099a7d" ON "metrics_dashboard" ("tenant_id"); (params None)
2024-08-05 23:41:51,315 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_domain" ADD CONSTRAINT "metrics_domain_tenant_id_259fb21f_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,316 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_domain_bdc97b86_like" ON "metrics_domain" ("domain" varchar_pattern_ops); (params None)
2024-08-05 23:41:51,318 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_is_primary_ac9d2eaf" ON "metrics_domain" ("is_primary"); (params None)
2024-08-05 23:41:51,321 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_tenant_id_259fb21f" ON "metrics_domain" ("tenant_id"); (params None)
2024-08-05 23:41:51,324 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_category_id_8793f683_fk_metrics_category_id" FOREIGN KEY ("category_id") REFERENCES "metrics_category" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,325 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_9606b577_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,327 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_category_id_8793f683" ON "metrics_metric" ("category_id"); (params None)
2024-08-05 23:41:51,330 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tenant_id_9606b577" ON "metrics_metric" ("tenant_id"); (params None)
2024-08-05 23:41:51,333 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_tenant_id_438c5ad4_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,334 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_metric_id_3f9e8174_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,335 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_tenant_id_438c5ad4" ON "metrics_historicaldata" ("tenant_id"); (params None)
2024-08-05 23:41:51,338 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_metric_id_3f9e8174" ON "metrics_historicaldata" ("metric_id"); (params None)
2024-08-05 23:41:51,340 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_tenant_id_92d37185_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,342 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_metric_id_e05f23a8_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,343 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_tenant_id_92d37185" ON "metrics_forecast" ("tenant_id"); (params None)
2024-08-05 23:41:51,345 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_metric_id_e05f23a8" ON "metrics_forecast" ("metric_id"); (params None)
2024-08-05 23:41:51,347 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD CONSTRAINT "metrics_experiment_tenant_id_10fa364a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,348 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_tenant_id_10fa364a" ON "metrics_experiment" ("tenant_id"); (params None)
2024-08-05 23:41:51,351 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_metri_experiment_id_metric_id_a9d54b29_uniq" UNIQUE ("experiment_id", "metric_id"); (params None)
2024-08-05 23:41:51,353 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_experiment_id_372c6b59_fk_metrics_e" FOREIGN KEY ("experiment_id") REFERENCES "metrics_experiment" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,354 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_metric_id_c8f84167_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,355 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_experiment_id_372c6b59" ON "metrics_experiment_metrics" ("experiment_id"); (params None)
2024-08-05 23:41:51,358 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_metric_id_c8f84167" ON "metrics_experiment_metrics" ("metric_id"); (params None)
2024-08-05 23:41:51,360 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_2e1e5750_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,361 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_from_metric_id_33b50521_fk_metrics_metric_id" FOREIGN KEY ("from_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,361 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_to_metric_id_94489c1c_fk_metrics_metric_id" FOREIGN KEY ("to_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,362 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_tenant_id_2e1e5750" ON "metrics_connection" ("tenant_id"); (params None)
2024-08-05 23:41:51,364 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_from_metric_id_33b50521" ON "metrics_connection" ("from_metric_id"); (params None)
2024-08-05 23:41:51,367 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_to_metric_id_94489c1c" ON "metrics_connection" ("to_metric_id"); (params None)
2024-08-05 23:41:51,369 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_tenant_id_9e474130_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,370 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_metric_id_1b3c3295_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,371 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_tenant_id_9e474130" ON "metrics_anomaly" ("tenant_id"); (params None)
2024-08-05 23:41:51,374 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_metric_id_1b3c3295" ON "metrics_anomaly" ("metric_id"); (params None)
2024-08-05 23:41:51,377 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_tenant_id_86ffa3a9_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,378 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_metric_id_c1b270f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,379 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_tenant_id_86ffa3a9" ON "metrics_actionremark" ("tenant_id"); (params None)
2024-08-05 23:41:51,381 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_metric_id_c1b270f2" ON "metrics_actionremark" ("metric_id"); (params None)
2024-08-05 23:41:51,384 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_project" ADD CONSTRAINT "metrics_project_tenant_id_db4a1170_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,385 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_tenant_id_db4a1170" ON "metrics_project" ("tenant_id"); (params None)
2024-08-05 23:41:51,387 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD CONSTRAINT "metrics_report_tenant_id_d1cf4812_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,388 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_tenant_id_d1cf4812" ON "metrics_report" ("tenant_id"); (params None)
2024-08-05 23:41:51,390 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_name_project_id_2d57d4da_uniq" UNIQUE ("name", "project_id"); (params None)
2024-08-05 23:41:51,392 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_project_id_b7ac5c8e_fk_metrics_project_id" FOREIGN KEY ("project_id") REFERENCES "metrics_project" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,393 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_tenant_id_c286653b_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,394 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_project_id_b7ac5c8e" ON "metrics_tag" ("project_id"); (params None)
2024-08-05 23:41:51,397 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_tenant_id_c286653b" ON "metrics_tag" ("tenant_id"); (params None)
2024-08-05 23:41:51,399 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_tag_id_a8e1a165_uniq" UNIQUE ("metric_id", "tag_id"); (params None)
2024-08-05 23:41:51,401 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_b2a068f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,402 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_tag_id_61869f56_fk_metrics_tag_id" FOREIGN KEY ("tag_id") REFERENCES "metrics_tag" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,403 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_metric_id_b2a068f2" ON "metrics_metric_tags" ("metric_id"); (params None)
2024-08-05 23:41:51,405 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_tag_id_61869f56" ON "metrics_metric_tags" ("tag_id"); (params None)
2024-08-05 23:41:51,408 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,409 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,410 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_metric_id_181e8748" ON "metrics_target" ("metric_id"); (params None)
2024-08-05 23:41:51,412 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_tenant_id_118eb54a" ON "metrics_target" ("tenant_id"); (params None)
2024-08-05 23:41:51,414 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_metric_id_25179b98_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,415 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_tenant_id_4cb1485d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:51,416 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_metric_id_25179b98" ON "metrics_trend" ("metric_id"); (params None)
2024-08-05 23:41:51,418 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_tenant_id_4cb1485d" ON "metrics_trend" ("tenant_id"); (params None)
2024-08-05 23:41:51,708 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_date_33d1e0bd" ON "metrics_actionremark" ("date"); (params None)
2024-08-05 23:41:51,720 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_detection_date_ee75a187" ON "metrics_anomaly" ("detection_date"); (params None)
2024-08-05 23:41:51,735 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c" ON "metrics_category" ("name"); (params None)
2024-08-05 23:41:51,737 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c_like" ON "metrics_category" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:51,749 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d" ON "metrics_client" ("name"); (params None)
2024-08-05 23:41:51,752 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d_like" ON "metrics_client" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:51,765 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET DEFAULT '{}'; (params None)
2024-08-05 23:41:51,766 - django.db.backends.schema - DEBUG - UPDATE "metrics_dashboard" SET "layout" = '{}' WHERE "layout" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:41:51,767 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET NOT NULL; (params None)
2024-08-05 23:41:51,768 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" DROP DEFAULT; (params None)
2024-08-05 23:41:51,780 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e" ON "metrics_dashboard" ("name"); (params None)
2024-08-05 23:41:51,783 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e_like" ON "metrics_dashboard" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:51,794 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_end_date_31af6c05" ON "metrics_experiment" ("end_date"); (params None)
2024-08-05 23:41:51,806 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7" ON "metrics_experiment" ("name"); (params None)
2024-08-05 23:41:51,809 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7_like" ON "metrics_experiment" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:51,821 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET DEFAULT '{}'; (params None)
2024-08-05 23:41:51,822 - django.db.backends.schema - DEBUG - UPDATE "metrics_experiment" SET "results" = '{}' WHERE "results" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:41:51,822 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET NOT NULL; (params None)
2024-08-05 23:41:51,823 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" DROP DEFAULT; (params None)
2024-08-05 23:41:51,834 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_start_date_a6deff13" ON "metrics_experiment" ("start_date"); (params None)
2024-08-05 23:41:51,846 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET DEFAULT '{}'; (params None)
2024-08-05 23:41:51,847 - django.db.backends.schema - DEBUG - UPDATE "metrics_forecast" SET "confidence_interval" = '{}' WHERE "confidence_interval" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:41:51,848 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET NOT NULL; (params None)
2024-08-05 23:41:51,848 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" DROP DEFAULT; (params None)
2024-08-05 23:41:51,858 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_forecast_date_71750ae8" ON "metrics_forecast" ("forecast_date"); (params None)
2024-08-05 23:41:51,872 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_date_f27e0e6a" ON "metrics_historicaldata" ("date"); (params None)
2024-08-05 23:41:51,885 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_last_updated_3e38a760" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:41:51,898 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5" ON "metrics_metric" ("name"); (params None)
2024-08-05 23:41:51,901 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5_like" ON "metrics_metric" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:51,914 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e" ON "metrics_metric" ("type"); (params None)
2024-08-05 23:41:51,916 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e_like" ON "metrics_metric" ("type" varchar_pattern_ops); (params None)
2024-08-05 23:41:51,938 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80" ON "metrics_project" ("name"); (params None)
2024-08-05 23:41:51,942 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80_like" ON "metrics_project" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:51,954 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET DEFAULT '{}'; (params None)
2024-08-05 23:41:51,955 - django.db.backends.schema - DEBUG - UPDATE "metrics_report" SET "configuration" = '{}' WHERE "configuration" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:41:51,956 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET NOT NULL; (params None)
2024-08-05 23:41:51,956 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" DROP DEFAULT; (params None)
2024-08-05 23:41:51,966 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34" ON "metrics_report" ("name"); (params None)
2024-08-05 23:41:51,969 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34_like" ON "metrics_report" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:51,984 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a" ON "metrics_tag" ("name"); (params None)
2024-08-05 23:41:51,987 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a_like" ON "metrics_tag" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:41:51,999 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_target_date_81507ff5" ON "metrics_target" ("target_date"); (params None)
2024-08-05 23:41:52,016 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_end_date_8444ef38" ON "metrics_trend" ("end_date"); (params None)
2024-08-05 23:41:52,031 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_start_date_7b1a850f" ON "metrics_trend" ("start_date"); (params None)
2024-08-05 23:41:52,044 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_act_metric__be3429_idx" ON "metrics_actionremark" ("metric_id", "date"); (params None)
2024-08-05 23:41:52,056 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ano_metric__84982d_idx" ON "metrics_anomaly" ("metric_id", "detection_date"); (params None)
2024-08-05 23:41:52,068 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_con_from_me_9411ea_idx" ON "metrics_connection" ("from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:41:52,082 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_exp_start_d_04716a_idx" ON "metrics_experiment" ("start_date", "end_date"); (params None)
2024-08-05 23:41:52,093 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_for_metric__4c9ae2_idx" ON "metrics_forecast" ("metric_id", "forecast_date"); (params None)
2024-08-05 23:41:52,105 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_his_metric__a2923a_idx" ON "metrics_historicaldata" ("metric_id", "date"); (params None)
2024-08-05 23:41:52,118 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_name_c9d100_idx" ON "metrics_metric" ("name", "type"); (params None)
2024-08-05 23:41:52,130 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_7984a6_idx" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:41:52,142 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1bdb27_idx" ON "metrics_tag" ("name", "project_id"); (params None)
2024-08-05 23:41:52,154 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tar_metric__234682_idx" ON "metrics_target" ("metric_id", "target_date"); (params None)
2024-08-05 23:41:52,168 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tre_metric__d386bb_idx" ON "metrics_trend" ("metric_id", "start_date", "end_date"); (params None)
2024-08-05 23:41:52,182 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_con_from_me_9411ea_idx"; (params None)
2024-08-05 23:41:52,192 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:41:52,194 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:41:52,206 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_from_metric_id_aa131d91_uniq" UNIQUE ("tenant_id", "from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:41:52,210 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_project_id_4c1b22ec" ON "metrics_connection" ("project_id"); (params None)
2024-08-05 23:41:52,226 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; ALTER TABLE "metrics_connection" DROP CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id"; (params None)
2024-08-05 23:41:52,227 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "project_id" CASCADE; (params None)
2024-08-05 23:41:52,238 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:41:52,240 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:41:52,250 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:41:52,253 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_project_id_36bdbe46" ON "metrics_metric" ("project_id"); (params None)
2024-08-05 23:41:52,257 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_correlation" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "lag" integer NOT NULL, "pearson_correlation" double precision NOT NULL, "spearman_correlation" double precision NOT NULL); (params None)
2024-08-05 23:41:52,261 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:52,269 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dataqualityscore" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_entry" varchar(255) NOT NULL, "completeness_score" double precision NOT NULL, "accuracy_score" double precision NOT NULL, "consistency_score" double precision NOT NULL, "timeliness_score" double precision NOT NULL, "overall_score" double precision NOT NULL); (params None)
2024-08-05 23:41:52,272 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_impactanalysis" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "before_value" double precision NOT NULL, "after_value" double precision NOT NULL, "percentage_change" double precision NOT NULL, "confidence" double precision NOT NULL, "artifact_link" varchar(200) NOT NULL); (params None)
2024-08-05 23:41:52,278 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_insight" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "title" varchar(200) NOT NULL, "content" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:52,285 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metricmetadata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_source" varchar(100) NOT NULL, "source_url" varchar(200) NOT NULL, "rhythm" varchar(20) NOT NULL, "last_updated" timestamp with time zone NOT NULL, "technical_description" text NOT NULL, "description" text NOT NULL, "artifacts_url" varchar(200) NOT NULL, "hypothesis" text NOT NULL, "confidence" varchar(20) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL); (params None)
2024-08-05 23:41:52,290 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metrictarget" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "target_kpi" varchar(100) NOT NULL, "target_remarks" text NOT NULL, "target_date" date NULL, "target_value" double precision NULL); (params None)
2024-08-05 23:41:52,296 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_strategy" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "estimated_time" interval NOT NULL, "artifacts_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:52,302 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tacticalsolution" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "artifact_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:52,307 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_team" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:52,313 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_technicalindicator" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "stochastic_value" double precision NOT NULL, "rsi_value" double precision NOT NULL, "percent_change" double precision NOT NULL, "moving_average" double precision NOT NULL); (params None)
2024-08-05 23:41:52,317 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_timedimension" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL UNIQUE, "day" integer NOT NULL, "day_of_week" integer NOT NULL, "day_name" varchar(10) NOT NULL, "week" integer NOT NULL, "month" integer NOT NULL, "month_name" varchar(10) NOT NULL, "quarter" integer NOT NULL, "year" integer NOT NULL, "is_weekend" boolean NOT NULL, "is_holiday" boolean NOT NULL); (params None)
2024-08-05 23:41:52,323 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_userprofile" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY); (params None)
2024-08-05 23:41:52,337 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_metric_id_181e8748_fk_metrics_metric_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id"; (params None)
2024-08-05 23:41:52,338 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "metric_id" CASCADE; (params None)
2024-08-05 23:41:52,350 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id"; (params None)
2024-08-05 23:41:52,351 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:41:52,363 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_name_c9d100_idx"; (params None)
2024-08-05 23:41:52,374 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_last_up_7984a6_idx"; (params None)
2024-08-05 23:41:52,384 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" RENAME COLUMN "description" TO "summary"; (params None)
2024-08-05 23:41:52,396 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq"; (params None)
2024-08-05 23:41:52,408 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "correlation_coefficient" CASCADE; (params None)
2024-08-05 23:41:52,418 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" DROP COLUMN "results" CASCADE; (params None)
2024-08-05 23:41:52,428 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "anomaly_detected" CASCADE; (params None)
2024-08-05 23:41:52,438 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "forecasted_value" CASCADE; (params None)
2024-08-05 23:41:52,449 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "trend_component" CASCADE; (params None)
2024-08-05 23:41:52,459 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "importance" varchar(20) DEFAULT 'MEDIUM' NOT NULL; (params None)
2024-08-05 23:41:52,459 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "importance" DROP DEFAULT; (params None)
2024-08-05 23:41:52,470 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:41:52.470041+00:00' NOT NULL; (params None)
2024-08-05 23:41:52,471 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:41:52,480 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "anomaly_type" varchar(20) DEFAULT 'IGNORE' NOT NULL; (params None)
2024-08-05 23:41:52,481 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "anomaly_type" DROP DEFAULT; (params None)
2024-08-05 23:41:52,493 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "quality" varchar(20) DEFAULT 'LOW' NOT NULL; (params None)
2024-08-05 23:41:52,494 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "quality" DROP DEFAULT; (params None)
2024-08-05 23:41:52,504 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "impact_description" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:41:52,505 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "impact_description" DROP DEFAULT; (params None)
2024-08-05 23:41:52,515 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "objective" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:41:52,516 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "objective" DROP DEFAULT; (params None)
2024-08-05 23:41:52,526 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_date" date NULL; (params None)
2024-08-05 23:41:52,537 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_files" varchar(100) NULL; (params None)
2024-08-05 23:41:52,547 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_summary" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:41:52,548 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "result_summary" DROP DEFAULT; (params None)
2024-08-05 23:41:52,558 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_value" double precision NULL; (params None)
2024-08-05 23:41:52,570 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:41:52.569822+00:00' NOT NULL; (params None)
2024-08-05 23:41:52,571 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:41:52,580 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "variance" double precision NULL; (params None)
2024-08-05 23:41:52,591 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD COLUMN "forecast_id" bigint NULL CONSTRAINT "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" REFERENCES "metrics_forecast"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" IMMEDIATE; (params None)
2024-08-05 23:41:52,603 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "impact" TYPE varchar(20) USING "impact"::varchar(20); (params None)
2024-08-05 23:41:52,813 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "status" TYPE varchar(20); (params None)
2024-08-05 23:41:52,933 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric1_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:52,945 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric2_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:52,958 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:52,965 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:41:52,984 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,003 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:41:53,025 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:53,044 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "experiment_id" bigint NOT NULL CONSTRAINT "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" REFERENCES "metrics_experiment"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" IMMEDIATE; (params None)
2024-08-05 23:41:53,063 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,080 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,099 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,118 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,138 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "user_id" bigint NOT NULL CONSTRAINT "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,157 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "data_quality_score_id" bigint NULL UNIQUE CONSTRAINT "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" REFERENCES "metrics_dataqualityscore"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" IMMEDIATE; (params None)
2024-08-05 23:41:53,180 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "metric_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,203 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,222 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,244 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,397 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,417 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:41:53,439 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:53,460 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_team" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,482 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "team_id" bigint NOT NULL CONSTRAINT "metrics_strategy_team_id_f1781500_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_team_id_f1781500_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,505 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,528 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,550 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_experiment_team_id_537107e3_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_experiment_team_id_537107e3_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,574 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:41:53,598 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:53,621 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_timedimension" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,644 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,668 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "user_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:41:53,672 - django.db.backends.schema - DEBUG - DROP TABLE "metrics_target" CASCADE; (params None)
2024-08-05 23:41:53,692 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "confidence" CASCADE; (params None)
2024-08-05 23:41:53,710 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "description" CASCADE; (params None)
2024-08-05 23:41:53,730 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "hypothesis" CASCADE; (params None)
2024-08-05 23:41:53,748 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "last_updated" CASCADE; (params None)
2024-08-05 23:41:53,768 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_x" CASCADE; (params None)
2024-08-05 23:41:53,788 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_y" CASCADE; (params None)
2024-08-05 23:41:53,806 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "rhythm" CASCADE; (params None)
2024-08-05 23:41:53,949 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "source" CASCADE; (params None)
2024-08-05 23:41:53,968 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "technical_description" CASCADE; (params None)
2024-08-05 23:41:53,987 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD CONSTRAINT "metrics_correlation_tenant_id_metric1_id_met_49a4c34a_uniq" UNIQUE ("tenant_id", "metric1_id", "metric2_id", "lag"); (params None)
2024-08-05 23:41:54,008 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_metric__b85d3a_idx" ON "metrics_insight" ("metric_id", "date"); (params None)
2024-08-05 23:41:54,031 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_user_id_1ebb42_idx" ON "metrics_insight" ("user_id", "date"); (params None)
2024-08-05 23:41:54,053 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_metric__a2b705_idx" ON "metrics_metrictarget" ("metric_id", "target_date"); (params None)
2024-08-05 23:41:54,073 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_6e2e67_idx" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:41:54,096 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_date_53cb14_idx" ON "metrics_timedimension" ("date"); (params None)
2024-08-05 23:41:54,118 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_year_92da9e_idx" ON "metrics_timedimension" ("year", "month", "day"); (params None)
2024-08-05 23:41:54,121 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_username_6e55f358_like" ON "metrics_customuser" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:41:54,123 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_date_ded95ba1" ON "metrics_insight" ("date"); (params None)
2024-08-05 23:41:54,125 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_last_updated_76599a1b" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:41:54,127 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_target_date_38cd9191" ON "metrics_metrictarget" ("target_date"); (params None)
2024-08-05 23:41:54,129 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_forecast_id_29590c29" ON "metrics_historicaldata" ("forecast_id"); (params None)
2024-08-05 23:41:54,132 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric1_id_6e1c2404" ON "metrics_correlation" ("metric1_id"); (params None)
2024-08-05 23:41:54,135 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric2_id_f2cc46dd" ON "metrics_correlation" ("metric2_id"); (params None)
2024-08-05 23:41:54,137 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_tenant_id_a00a5169" ON "metrics_correlation" ("tenant_id"); (params None)
2024-08-05 23:41:54,139 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_customuser_id_group_id_1c5fc435_uniq" UNIQUE ("customuser_id", "group_id"); (params None)
2024-08-05 23:41:54,141 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_g_customuser_id_fc13f3af_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:54,143 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_group_id_6b097e12_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:54,144 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_customuser_id_fc13f3af" ON "metrics_customuser_groups" ("customuser_id"); (params None)
2024-08-05 23:41:54,146 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_group_id_6b097e12" ON "metrics_customuser_groups" ("group_id"); (params None)
2024-08-05 23:41:54,149 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_tenant_id_02b7403c" ON "metrics_customuser" ("tenant_id"); (params None)
2024-08-05 23:41:54,151 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_user__customuser_id_permission_68cc320f_uniq" UNIQUE ("customuser_id", "permission_id"); (params None)
2024-08-05 23:41:54,154 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_customuser_id_46e97f00_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:54,155 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_permission_id_d66d657c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:54,156 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_customuser_id_46e97f00" ON "metrics_customuser_user_permissions" ("customuser_id"); (params None)
2024-08-05 23:41:54,158 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_permission_id_d66d657c" ON "metrics_customuser_user_permissions" ("permission_id"); (params None)
2024-08-05 23:41:54,160 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_tenant_id_8e9f296d" ON "metrics_dataqualityscore" ("tenant_id"); (params None)
2024-08-05 23:41:54,163 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_experiment_id_1beae7fe" ON "metrics_impactanalysis" ("experiment_id"); (params None)
2024-08-05 23:41:54,165 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_metric_id_f4b9eeb6" ON "metrics_impactanalysis" ("metric_id"); (params None)
2024-08-05 23:41:54,167 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_tenant_id_126ca20d" ON "metrics_impactanalysis" ("tenant_id"); (params None)
2024-08-05 23:41:54,169 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_metric_id_26d3a9d8" ON "metrics_insight" ("metric_id"); (params None)
2024-08-05 23:41:54,172 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_tenant_id_724d7d85" ON "metrics_insight" ("tenant_id"); (params None)
2024-08-05 23:41:54,174 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_user_id_83d421e1" ON "metrics_insight" ("user_id"); (params None)
2024-08-05 23:41:54,176 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_tenant_id_3277f967" ON "metrics_metricmetadata" ("tenant_id"); (params None)
2024-08-05 23:41:54,178 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_metric_id_7876e2c8" ON "metrics_metrictarget" ("metric_id"); (params None)
2024-08-05 23:41:54,181 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_tenant_id_b26a17f8" ON "metrics_metrictarget" ("tenant_id"); (params None)
2024-08-05 23:41:54,184 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_tenant_id_1323395e" ON "metrics_strategy" ("tenant_id"); (params None)
2024-08-05 23:41:54,186 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_metric_id_9887ffa4" ON "metrics_tacticalsolution" ("metric_id"); (params None)
2024-08-05 23:41:54,188 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_tenant_id_cf9028f0" ON "metrics_tacticalsolution" ("tenant_id"); (params None)
2024-08-05 23:41:54,189 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_team_tenant_id_3a14c47d" ON "metrics_team" ("tenant_id"); (params None)
2024-08-05 23:41:54,191 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_team_id_f1781500" ON "metrics_strategy" ("team_id"); (params None)
2024-08-05 23:41:54,193 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_team_id_f140658d" ON "metrics_metricmetadata" ("team_id"); (params None)
2024-08-05 23:41:54,196 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_team_id_4c4ffc18" ON "metrics_customuser" ("team_id"); (params None)
2024-08-05 23:41:54,198 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_team_id_537107e3" ON "metrics_experiment" ("team_id"); (params None)
2024-08-05 23:41:54,200 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_metric_id_3e2eead6" ON "metrics_technicalindicator" ("metric_id"); (params None)
2024-08-05 23:41:54,202 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_tenant_id_f4de3b44" ON "metrics_technicalindicator" ("tenant_id"); (params None)
2024-08-05 23:41:54,204 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_timedimension_tenant_id_f375bb45" ON "metrics_timedimension" ("tenant_id"); (params None)
2024-08-05 23:41:54,206 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_userprofile_tenant_id_cca71dae" ON "metrics_userprofile" ("tenant_id"); (params None)
2024-08-05 23:41:54,228 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "strength" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:41:54,229 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "strength" DROP DEFAULT; (params None)
2024-08-05 23:41:54,248 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "lower_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:41:54,249 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "lower_bound" DROP DEFAULT; (params None)
2024-08-05 23:41:54,269 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "upper_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:41:54,270 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "upper_bound" DROP DEFAULT; (params None)
2024-08-05 23:41:54,289 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD COLUMN "slope" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:41:54,290 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ALTER COLUMN "slope" DROP DEFAULT; (params None)
2024-08-05 23:41:54,313 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_movingaverage" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "ma_type" varchar(10) NOT NULL, "period" integer NOT NULL, "value" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:54,340 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_networkanalysisresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "analysis_type" varchar(20) NOT NULL, "result" jsonb NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:54,369 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_seasonalityresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "seasonality_type" varchar(20) NOT NULL, "strength" double precision NOT NULL, "period" integer NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:54,398 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trendchangepoint" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "change_type" varchar(20) NOT NULL, "significance" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:41:54,402 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD CONSTRAINT "metrics_movingaverage_metric_id_7c61cebf_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:54,404 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_metric_id_7c61cebf" ON "metrics_movingaverage" ("metric_id"); (params None)
2024-08-05 23:41:54,406 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD CONSTRAINT "metrics_networkanaly_metric_id_a4c90102_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:54,407 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_metric_id_a4c90102" ON "metrics_networkanalysisresult" ("metric_id"); (params None)
2024-08-05 23:41:54,409 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityr_metric_id_6e494791_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:54,410 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_metric_id_6e494791" ON "metrics_seasonalityresult" ("metric_id"); (params None)
2024-08-05 23:41:54,412 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD CONSTRAINT "metrics_trendchangep_metric_id_f8eb9f76_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:41:54,413 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_metric_id_f8eb9f76" ON "metrics_trendchangepoint" ("metric_id"); (params None)
2024-08-05 23:41:54,442 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:41:54,443 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:41:54,468 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" IMMEDIATE; (params None)
2024-08-05 23:41:54,469 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:41:54,490 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ALTER COLUMN "value" DROP NOT NULL; (params None)
2024-08-05 23:41:54,642 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD CONSTRAINT "metrics_dataqualityscore_tenant_id_metric_id_proj_66b9fb01_uniq" UNIQUE ("tenant_id", "metric_id", "project_id"); (params None)
2024-08-05 23:41:54,645 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_metric_id_1b6367d1" ON "metrics_dataqualityscore" ("metric_id"); (params None)
2024-08-05 23:41:54,647 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_project_id_123a4f58" ON "metrics_dataqualityscore" ("project_id"); (params None)
2024-08-05 23:41:54,671 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:41:54,699 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:41:54,702 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:41:54,728 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:54,730 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:41:54,756 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:54,757 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:41:54,784 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:41:54,785 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:41:54,805 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq" UNIQUE ("tenant_id", "metric_id"); (params None)
2024-08-05 23:41:54,808 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_tenant_id_5a9de228" ON "metrics_movingaverage" ("tenant_id"); (params None)
2024-08-05 23:41:54,811 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_tenant_id_16a6ba09" ON "metrics_networkanalysisresult" ("tenant_id"); (params None)
2024-08-05 23:41:54,813 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_tenant_id_ca2da3fd" ON "metrics_seasonalityresult" ("tenant_id"); (params None)
2024-08-05 23:41:54,815 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_tenant_id_da10d898" ON "metrics_trendchangepoint" ("tenant_id"); (params None)
2024-08-05 23:41:54,844 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:41:54,845 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:41:54,846 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_metric_id_c86f5720" ON "metrics_report" ("metric_id"); (params None)
2024-08-05 23:41:54,870 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "analysis_result" jsonb NULL; (params None)
2024-08-05 23:41:54,891 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "anomaly_result" jsonb NULL; (params None)
2024-08-05 23:41:54,912 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:41:54.912225+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:41:54,913 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:41:54,934 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "forecast_result" jsonb NULL; (params None)
2024-08-05 23:41:54,954 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "relationship_result" jsonb NULL; (params None)
2024-08-05 23:41:54,977 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "report" text DEFAULT '1' NOT NULL; (params None)
2024-08-05 23:41:54,977 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "report" DROP DEFAULT; (params None)
2024-08-05 23:41:54,999 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "updated_at" timestamp with time zone DEFAULT '2024-08-05T23:41:54.999128+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:41:55,000 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "updated_at" DROP DEFAULT; (params None)
2024-08-05 23:41:55,053 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_trendchangepoint" DROP CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c"; (params None)
2024-08-05 23:41:55,054 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:41:55,071 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "significance" DROP NOT NULL; (params None)
2024-08-05 23:41:55,088 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" RENAME COLUMN "change_type" TO "direction"; (params None)
2024-08-05 23:41:55,263 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:41:55.263138+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:41:55,264 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:41:55,287 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq"; (params None)
2024-08-05 23:41:55,288 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresul_metric_id_seasonality_ty_d3492b78_uniq" UNIQUE ("metric_id", "seasonality_type"); (params None)
2024-08-05 23:41:55,318 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c"; (params None)
2024-08-05 23:41:55,318 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:41:55,321 - django.db.backends.schema - DEBUG - CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:41:55,326 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" ("session_key" varchar_pattern_ops); (params None)
2024-08-05 23:41:55,329 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date"); (params None)
2024-08-05 23:41:56,314 - metrics.computations.data_preparation - INFO - Loaded metric 9 for tenant 5 and project 5
2024-08-05 23:41:56,314 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 9
2024-08-05 23:41:56,315 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:56,315 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:56,317 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 9
2024-08-05 23:41:56,321 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:56,321 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:56,324 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:41:56,324 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:56,326 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:41:56,327 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:56,329 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:58,059 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 9
2024-08-05 23:41:58,061 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:58,063 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:58,063 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:58,065 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:41:58,066 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:58,068 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:41:58,070 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36486427633847696, Timeliness: nan
2024-08-05 23:41:58,070 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.495475877949225
2024-08-05 23:41:58,073 - metrics.computations.data_preparation - INFO - Data quality score: 45.495475877949225
2024-08-05 23:41:58,088 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 9, 'tenant_id': 5, 'project_id': 5, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.495475877949225, 'outliers_handled': True, 'profile': {'mean': 100.04796801166025, 'median': 100.24069673689053, 'std': 9.667635986981242, 'min': 76.40225273057015, 'max': 122.38579800765001, 'skewness': 0.0012665307812521232, 'kurtosis': -0.354407201469491, 'missing_percentage': 0.0}}
2024-08-05 23:41:58,094 - metrics.computations.data_preparation - INFO - Loaded metric 9 for tenant 5 and project 5
2024-08-05 23:41:58,094 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 9
2024-08-05 23:41:58,095 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:58,096 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:58,097 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 9
2024-08-05 23:41:58,103 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:58,103 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:58,106 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:41:58,106 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:58,109 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:41:58,110 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:58,113 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:41:59,854 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 9
2024-08-05 23:41:59,856 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:41:59,857 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:41:59,858 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:41:59,860 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:41:59,860 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:41:59,863 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:41:59,865 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36486427633847696, Timeliness: nan
2024-08-05 23:41:59,865 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.495475877949225
2024-08-05 23:41:59,868 - metrics.computations.data_preparation - INFO - Data quality score: 45.495475877949225
2024-08-05 23:41:59,886 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 9, 'tenant_id': 5, 'project_id': 5, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.495475877949225, 'outliers_handled': True, 'profile': {'mean': 100.04796801166025, 'median': 100.24069673689053, 'std': 9.667635986981242, 'min': 76.40225273057015, 'max': 122.38579800765001, 'skewness': 0.0012665307812521232, 'kurtosis': -0.354407201469491, 'missing_percentage': 0.0}}
2024-08-05 23:41:59,886 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:41:59,886 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 9
2024-08-05 23:41:59,893 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:41:59,898 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:41:59,902 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 9
2024-08-05 23:41:59,902 - metrics.computations.feature_engineering - INFO - Parameters for metric 9: dynamic
2024-08-05 23:41:59,902 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 9: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:41:59,905 - metrics.computations.data_preparation - INFO - Loaded metric 9 for tenant 5 and project 5
2024-08-05 23:41:59,905 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 9
2024-08-05 23:41:59,906 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:59,906 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:41:59,908 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 9
2024-08-05 23:41:59,915 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:59,915 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:41:59,920 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:41:59,920 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:41:59,923 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:41:59,923 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:41:59,926 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:01,683 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 9
2024-08-05 23:42:01,685 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:01,686 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:01,686 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:01,689 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:01,689 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:01,692 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:01,694 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36486427633847696, Timeliness: nan
2024-08-05 23:42:01,694 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.495475877949225
2024-08-05 23:42:01,697 - metrics.computations.data_preparation - INFO - Data quality score: 45.495475877949225
2024-08-05 23:42:01,715 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 9, 'tenant_id': 5, 'project_id': 5, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.495475877949225, 'outliers_handled': True, 'profile': {'mean': 100.04796801166025, 'median': 100.24069673689053, 'std': 9.667635986981242, 'min': 76.40225273057015, 'max': 122.38579800765001, 'skewness': 0.0012665307812521232, 'kurtosis': -0.354407201469491, 'missing_percentage': 0.0}}
2024-08-05 23:42:01,719 - metrics.computations.data_preparation - INFO - Loaded metric 9 for tenant 5 and project 5
2024-08-05 23:42:01,720 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 9
2024-08-05 23:42:01,720 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:01,721 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:01,734 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 9
2024-08-05 23:42:01,741 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:01,741 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:01,744 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:01,744 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:01,747 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:01,747 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:01,751 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:03,560 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 9
2024-08-05 23:42:03,562 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:03,563 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:03,564 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:03,566 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:03,566 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:03,568 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:03,570 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36486427633847696, Timeliness: nan
2024-08-05 23:42:03,570 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.495475877949225
2024-08-05 23:42:03,573 - metrics.computations.data_preparation - INFO - Data quality score: 45.495475877949225
2024-08-05 23:42:03,589 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 9, 'tenant_id': 5, 'project_id': 5, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.495475877949225, 'outliers_handled': True, 'profile': {'mean': 100.04796801166025, 'median': 100.24069673689053, 'std': 9.667635986981242, 'min': 76.40225273057015, 'max': 122.38579800765001, 'skewness': 0.0012665307812521232, 'kurtosis': -0.354407201469491, 'missing_percentage': 0.0}}
2024-08-05 23:42:03,589 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:42:03,589 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 9
2024-08-05 23:42:03,594 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:42:03,600 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:42:03,604 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 9
2024-08-05 23:42:03,604 - metrics.computations.feature_engineering - INFO - Parameters for metric 9: dynamic
2024-08-05 23:42:03,604 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 9: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:42:03,605 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Setup completed
2024-08-05 23:42:03,607 - metrics.computations.data_preparation - INFO - Loaded metric 9 for tenant 5 and project 5
2024-08-05 23:42:03,607 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 9
2024-08-05 23:42:03,608 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:03,609 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:03,612 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 9
2024-08-05 23:42:03,621 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:03,621 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:03,624 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:03,625 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:03,629 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:03,629 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:03,632 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:05,415 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 9
2024-08-05 23:42:05,417 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:05,419 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:05,419 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:05,421 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:05,422 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:05,424 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:05,426 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36486427633847696, Timeliness: nan
2024-08-05 23:42:05,427 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.495475877949225
2024-08-05 23:42:05,430 - metrics.computations.data_preparation - INFO - Data quality score: 45.495475877949225
2024-08-05 23:42:05,569 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 9, 'tenant_id': 5, 'project_id': 5, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.495475877949225, 'outliers_handled': True, 'profile': {'mean': 100.04796801166025, 'median': 100.24069673689053, 'std': 9.667635986981242, 'min': 76.40225273057015, 'max': 122.38579800765001, 'skewness': 0.0012665307812521232, 'kurtosis': -0.354407201469491, 'missing_percentage': 0.0}}
2024-08-05 23:42:05,575 - metrics.computations.data_preparation - INFO - Loaded metric 9 for tenant 5 and project 5
2024-08-05 23:42:05,577 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 9
2024-08-05 23:42:05,579 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:05,579 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 9 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:05,586 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 9
2024-08-05 23:42:05,597 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:05,597 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:05,602 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:05,602 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:05,606 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:05,607 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:05,610 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:07,380 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 9
2024-08-05 23:42:07,382 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:07,384 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:07,385 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:07,387 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:07,387 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:07,390 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  105.074250          5
2023-01-02  103.214568          5
2023-01-03   95.290846          5
2023-01-04  103.356410          5
2023-01-05   91.521906          5
2024-08-05 23:42:07,392 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.36486427633847696, Timeliness: nan
2024-08-05 23:42:07,392 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.495475877949225
2024-08-05 23:42:07,395 - metrics.computations.data_preparation - INFO - Data quality score: 45.495475877949225
2024-08-05 23:42:07,479 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 9, 'tenant_id': 5, 'project_id': 5, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.495475877949225, 'outliers_handled': True, 'profile': {'mean': 100.04796801166025, 'median': 100.24069673689053, 'std': 9.667635986981242, 'min': 76.40225273057015, 'max': 122.38579800765001, 'skewness': 0.0012665307812521232, 'kurtosis': -0.354407201469491, 'missing_percentage': 0.0}}
2024-08-05 23:42:07,623 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Teardown completed
```

## test_permanent_computations_robustness (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
Status: failure
Duration: 48.715 seconds

### Failure
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_permanent_computations_robustness.py", line 156, in test_permanent_computations_robustness
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
23:42:34 - cmdstanpy - INFO - Chain [1] start processing
23:42:34 - cmdstanpy - INFO - Chain [1] done processing
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
23:42:52 - cmdstanpy - INFO - Chain [1] start processing
23:42:52 - cmdstanpy - INFO - Chain [1] done processing
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/computations/data_preparation.py:182: RuntimeWarning: invalid value encountered in log1p
  timeliness = safe_divide(1, 1 + np.log1p((pd.Timestamp.now() - self.cleaned_df.index.max()).days)) if not self.cleaned_df.empty else 0
2024-08-05 23:42:07,640 - metrics - DEBUG - Starting test: test_permanent_computations_robustness (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
2024-08-05 23:42:07,644 - django.db.backends.schema - DEBUG - CREATE TABLE "django_migrations" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:07,658 - django.db.backends.schema - DEBUG - CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
2024-08-05 23:42:07,662 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params None)
2024-08-05 23:42:07,668 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL, "codename" varchar(100) NOT NULL); (params None)
2024-08-05 23:42:07,673 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(80) NOT NULL UNIQUE); (params None)
2024-08-05 23:42:07,677 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:42:07,685 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NOT NULL, "is_superuser" boolean NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:07,690 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:42:07,693 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:42:07,697 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename"); (params None)
2024-08-05 23:42:07,699 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:07,700 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id"); (params None)
2024-08-05 23:42:07,702 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_name_a6ea08ec_like" ON "auth_group" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:07,704 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id"); (params None)
2024-08-05 23:42:07,707 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:07,708 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:07,709 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id"); (params None)
2024-08-05 23:42:07,712 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id"); (params None)
2024-08-05 23:42:07,714 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_username_6821ab7c_like" ON "auth_user" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:42:07,716 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id"); (params None)
2024-08-05 23:42:07,718 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:07,719 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:07,720 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id"); (params None)
2024-08-05 23:42:07,723 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id"); (params None)
2024-08-05 23:42:07,725 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id"); (params None)
2024-08-05 23:42:07,728 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:07,729 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:07,730 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id"); (params None)
2024-08-05 23:42:07,732 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id"); (params None)
2024-08-05 23:42:07,742 - django.db.backends.schema - DEBUG - CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "action_time" timestamp with time zone NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL, "user_id" integer NOT NULL); (params None)
2024-08-05 23:42:07,748 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:07,749 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:07,750 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id"); (params None)
2024-08-05 23:42:07,752 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id"); (params None)
2024-08-05 23:42:07,775 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ALTER COLUMN "name" DROP NOT NULL; (params None)
2024-08-05 23:42:07,781 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" DROP COLUMN "name" CASCADE; (params None)
2024-08-05 23:42:07,787 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ALTER COLUMN "name" TYPE varchar(255); (params None)
2024-08-05 23:42:07,794 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "email" TYPE varchar(254); (params None)
2024-08-05 23:42:07,808 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_login" DROP NOT NULL; (params None)
2024-08-05 23:42:07,821 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "username" TYPE varchar(150); (params None)
2024-08-05 23:42:07,829 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_name" TYPE varchar(150); (params None)
2024-08-05 23:42:07,836 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group" ALTER COLUMN "name" TYPE varchar(150); (params None)
2024-08-05 23:42:07,848 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "first_name" TYPE varchar(150); (params None)
2024-08-05 23:42:07,884 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_client" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "schema_name" varchar(63) NOT NULL UNIQUE, "name" varchar(100) NOT NULL, "created_on" date NOT NULL); (params None)
2024-08-05 23:42:07,890 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_category" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:07,896 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dashboard" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "layout" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:07,904 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_domain" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "domain" varchar(253) NOT NULL UNIQUE, "is_primary" boolean NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:07,913 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "type" varchar(50) NOT NULL, "confidence" varchar(50) NOT NULL, "value_type" varchar(20) NOT NULL, "rhythm" varchar(20) NOT NULL, "description" text NOT NULL, "hypothesis" text NOT NULL, "technical_description" text NOT NULL, "last_updated" timestamp with time zone NOT NULL, "source" varchar(100) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL, "category_id" bigint NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:07,923 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_historicaldata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "value" double precision NOT NULL, "forecasted_value" double precision NULL, "anomaly_detected" boolean NOT NULL, "trend_component" varchar(50) NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:07,931 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_forecast" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "forecast_date" date NOT NULL, "forecast_value" double precision NOT NULL, "model_used" varchar(100) NOT NULL, "accuracy" double precision NULL, "confidence_interval" jsonb NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:07,944 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "status" varchar(50) NOT NULL, "results" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:07,951 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment_metrics" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "experiment_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:07,961 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_connection" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "relationship" varchar(100) NOT NULL, "correlation_coefficient" double precision NULL, "tenant_id" bigint NOT NULL, "from_metric_id" bigint NOT NULL, "to_metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:07,971 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_anomaly" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "detection_date" date NOT NULL, "anomaly_value" double precision NOT NULL, "anomaly_score" double precision NOT NULL, "notes" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:07,985 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_actionremark" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NULL, "description" text NOT NULL, "impact" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:07,998 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_project" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "created_on" date NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:08,010 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_report" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "configuration" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:08,027 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tag" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "project_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:08,040 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric_tags" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "metric_id" bigint NOT NULL, "tag_id" bigint NOT NULL); (params None)
2024-08-05 23:42:08,054 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_target" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "remarks" text NOT NULL, "target_kpi" varchar(100) NOT NULL, "target_date" date NULL, "target_value" double precision NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:08,072 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trend" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "trend_type" varchar(50) NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "trend_value" double precision NOT NULL, "notes" text NOT NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:08,077 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_schema_name_87d6fbb5_like" ON "metrics_client" ("schema_name" varchar_pattern_ops); (params None)
2024-08-05 23:42:08,079 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_category" ADD CONSTRAINT "metrics_category_tenant_id_67d98cc6_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,080 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_tenant_id_67d98cc6" ON "metrics_category" ("tenant_id"); (params None)
2024-08-05 23:42:08,083 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ADD CONSTRAINT "metrics_dashboard_tenant_id_50099a7d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,084 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_tenant_id_50099a7d" ON "metrics_dashboard" ("tenant_id"); (params None)
2024-08-05 23:42:08,086 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_domain" ADD CONSTRAINT "metrics_domain_tenant_id_259fb21f_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,087 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_domain_bdc97b86_like" ON "metrics_domain" ("domain" varchar_pattern_ops); (params None)
2024-08-05 23:42:08,089 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_is_primary_ac9d2eaf" ON "metrics_domain" ("is_primary"); (params None)
2024-08-05 23:42:08,091 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_tenant_id_259fb21f" ON "metrics_domain" ("tenant_id"); (params None)
2024-08-05 23:42:08,093 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_category_id_8793f683_fk_metrics_category_id" FOREIGN KEY ("category_id") REFERENCES "metrics_category" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,095 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_9606b577_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,096 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_category_id_8793f683" ON "metrics_metric" ("category_id"); (params None)
2024-08-05 23:42:08,098 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tenant_id_9606b577" ON "metrics_metric" ("tenant_id"); (params None)
2024-08-05 23:42:08,101 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_tenant_id_438c5ad4_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,102 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_metric_id_3f9e8174_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,103 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_tenant_id_438c5ad4" ON "metrics_historicaldata" ("tenant_id"); (params None)
2024-08-05 23:42:08,105 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_metric_id_3f9e8174" ON "metrics_historicaldata" ("metric_id"); (params None)
2024-08-05 23:42:08,107 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_tenant_id_92d37185_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,109 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_metric_id_e05f23a8_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,110 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_tenant_id_92d37185" ON "metrics_forecast" ("tenant_id"); (params None)
2024-08-05 23:42:08,112 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_metric_id_e05f23a8" ON "metrics_forecast" ("metric_id"); (params None)
2024-08-05 23:42:08,114 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD CONSTRAINT "metrics_experiment_tenant_id_10fa364a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,115 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_tenant_id_10fa364a" ON "metrics_experiment" ("tenant_id"); (params None)
2024-08-05 23:42:08,118 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_metri_experiment_id_metric_id_a9d54b29_uniq" UNIQUE ("experiment_id", "metric_id"); (params None)
2024-08-05 23:42:08,120 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_experiment_id_372c6b59_fk_metrics_e" FOREIGN KEY ("experiment_id") REFERENCES "metrics_experiment" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,122 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_metric_id_c8f84167_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,123 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_experiment_id_372c6b59" ON "metrics_experiment_metrics" ("experiment_id"); (params None)
2024-08-05 23:42:08,125 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_metric_id_c8f84167" ON "metrics_experiment_metrics" ("metric_id"); (params None)
2024-08-05 23:42:08,127 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_2e1e5750_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,128 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_from_metric_id_33b50521_fk_metrics_metric_id" FOREIGN KEY ("from_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,129 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_to_metric_id_94489c1c_fk_metrics_metric_id" FOREIGN KEY ("to_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,130 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_tenant_id_2e1e5750" ON "metrics_connection" ("tenant_id"); (params None)
2024-08-05 23:42:08,132 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_from_metric_id_33b50521" ON "metrics_connection" ("from_metric_id"); (params None)
2024-08-05 23:42:08,135 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_to_metric_id_94489c1c" ON "metrics_connection" ("to_metric_id"); (params None)
2024-08-05 23:42:08,138 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_tenant_id_9e474130_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,139 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_metric_id_1b3c3295_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,140 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_tenant_id_9e474130" ON "metrics_anomaly" ("tenant_id"); (params None)
2024-08-05 23:42:08,142 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_metric_id_1b3c3295" ON "metrics_anomaly" ("metric_id"); (params None)
2024-08-05 23:42:08,144 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_tenant_id_86ffa3a9_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,145 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_metric_id_c1b270f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,146 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_tenant_id_86ffa3a9" ON "metrics_actionremark" ("tenant_id"); (params None)
2024-08-05 23:42:08,149 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_metric_id_c1b270f2" ON "metrics_actionremark" ("metric_id"); (params None)
2024-08-05 23:42:08,151 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_project" ADD CONSTRAINT "metrics_project_tenant_id_db4a1170_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,153 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_tenant_id_db4a1170" ON "metrics_project" ("tenant_id"); (params None)
2024-08-05 23:42:08,155 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD CONSTRAINT "metrics_report_tenant_id_d1cf4812_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,156 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_tenant_id_d1cf4812" ON "metrics_report" ("tenant_id"); (params None)
2024-08-05 23:42:08,158 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_name_project_id_2d57d4da_uniq" UNIQUE ("name", "project_id"); (params None)
2024-08-05 23:42:08,160 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_project_id_b7ac5c8e_fk_metrics_project_id" FOREIGN KEY ("project_id") REFERENCES "metrics_project" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,162 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_tenant_id_c286653b_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,163 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_project_id_b7ac5c8e" ON "metrics_tag" ("project_id"); (params None)
2024-08-05 23:42:08,165 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_tenant_id_c286653b" ON "metrics_tag" ("tenant_id"); (params None)
2024-08-05 23:42:08,167 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_tag_id_a8e1a165_uniq" UNIQUE ("metric_id", "tag_id"); (params None)
2024-08-05 23:42:08,169 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_b2a068f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,170 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_tag_id_61869f56_fk_metrics_tag_id" FOREIGN KEY ("tag_id") REFERENCES "metrics_tag" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,171 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_metric_id_b2a068f2" ON "metrics_metric_tags" ("metric_id"); (params None)
2024-08-05 23:42:08,174 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_tag_id_61869f56" ON "metrics_metric_tags" ("tag_id"); (params None)
2024-08-05 23:42:08,176 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,178 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,179 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_metric_id_181e8748" ON "metrics_target" ("metric_id"); (params None)
2024-08-05 23:42:08,181 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_tenant_id_118eb54a" ON "metrics_target" ("tenant_id"); (params None)
2024-08-05 23:42:08,183 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_metric_id_25179b98_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,185 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_tenant_id_4cb1485d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:08,186 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_metric_id_25179b98" ON "metrics_trend" ("metric_id"); (params None)
2024-08-05 23:42:08,188 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_tenant_id_4cb1485d" ON "metrics_trend" ("tenant_id"); (params None)
2024-08-05 23:42:08,351 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_date_33d1e0bd" ON "metrics_actionremark" ("date"); (params None)
2024-08-05 23:42:08,363 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_detection_date_ee75a187" ON "metrics_anomaly" ("detection_date"); (params None)
2024-08-05 23:42:08,377 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c" ON "metrics_category" ("name"); (params None)
2024-08-05 23:42:08,379 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c_like" ON "metrics_category" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:08,392 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d" ON "metrics_client" ("name"); (params None)
2024-08-05 23:42:08,394 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d_like" ON "metrics_client" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:08,406 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET DEFAULT '{}'; (params None)
2024-08-05 23:42:08,407 - django.db.backends.schema - DEBUG - UPDATE "metrics_dashboard" SET "layout" = '{}' WHERE "layout" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:42:08,408 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET NOT NULL; (params None)
2024-08-05 23:42:08,408 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" DROP DEFAULT; (params None)
2024-08-05 23:42:08,418 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e" ON "metrics_dashboard" ("name"); (params None)
2024-08-05 23:42:08,421 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e_like" ON "metrics_dashboard" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:08,435 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_end_date_31af6c05" ON "metrics_experiment" ("end_date"); (params None)
2024-08-05 23:42:08,447 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7" ON "metrics_experiment" ("name"); (params None)
2024-08-05 23:42:08,449 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7_like" ON "metrics_experiment" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:08,462 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET DEFAULT '{}'; (params None)
2024-08-05 23:42:08,463 - django.db.backends.schema - DEBUG - UPDATE "metrics_experiment" SET "results" = '{}' WHERE "results" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:42:08,463 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET NOT NULL; (params None)
2024-08-05 23:42:08,464 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" DROP DEFAULT; (params None)
2024-08-05 23:42:08,476 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_start_date_a6deff13" ON "metrics_experiment" ("start_date"); (params None)
2024-08-05 23:42:08,488 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET DEFAULT '{}'; (params None)
2024-08-05 23:42:08,489 - django.db.backends.schema - DEBUG - UPDATE "metrics_forecast" SET "confidence_interval" = '{}' WHERE "confidence_interval" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:42:08,489 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET NOT NULL; (params None)
2024-08-05 23:42:08,490 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" DROP DEFAULT; (params None)
2024-08-05 23:42:08,500 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_forecast_date_71750ae8" ON "metrics_forecast" ("forecast_date"); (params None)
2024-08-05 23:42:08,513 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_date_f27e0e6a" ON "metrics_historicaldata" ("date"); (params None)
2024-08-05 23:42:08,527 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_last_updated_3e38a760" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:42:08,540 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5" ON "metrics_metric" ("name"); (params None)
2024-08-05 23:42:08,542 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5_like" ON "metrics_metric" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:08,555 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e" ON "metrics_metric" ("type"); (params None)
2024-08-05 23:42:08,558 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e_like" ON "metrics_metric" ("type" varchar_pattern_ops); (params None)
2024-08-05 23:42:08,583 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80" ON "metrics_project" ("name"); (params None)
2024-08-05 23:42:08,586 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80_like" ON "metrics_project" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:08,600 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET DEFAULT '{}'; (params None)
2024-08-05 23:42:08,601 - django.db.backends.schema - DEBUG - UPDATE "metrics_report" SET "configuration" = '{}' WHERE "configuration" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:42:08,601 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET NOT NULL; (params None)
2024-08-05 23:42:08,602 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" DROP DEFAULT; (params None)
2024-08-05 23:42:08,612 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34" ON "metrics_report" ("name"); (params None)
2024-08-05 23:42:08,616 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34_like" ON "metrics_report" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:08,629 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a" ON "metrics_tag" ("name"); (params None)
2024-08-05 23:42:08,631 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a_like" ON "metrics_tag" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:08,769 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_target_date_81507ff5" ON "metrics_target" ("target_date"); (params None)
2024-08-05 23:42:08,780 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_end_date_8444ef38" ON "metrics_trend" ("end_date"); (params None)
2024-08-05 23:42:08,792 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_start_date_7b1a850f" ON "metrics_trend" ("start_date"); (params None)
2024-08-05 23:42:08,805 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_act_metric__be3429_idx" ON "metrics_actionremark" ("metric_id", "date"); (params None)
2024-08-05 23:42:08,817 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ano_metric__84982d_idx" ON "metrics_anomaly" ("metric_id", "detection_date"); (params None)
2024-08-05 23:42:08,828 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_con_from_me_9411ea_idx" ON "metrics_connection" ("from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:42:08,841 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_exp_start_d_04716a_idx" ON "metrics_experiment" ("start_date", "end_date"); (params None)
2024-08-05 23:42:08,853 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_for_metric__4c9ae2_idx" ON "metrics_forecast" ("metric_id", "forecast_date"); (params None)
2024-08-05 23:42:08,865 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_his_metric__a2923a_idx" ON "metrics_historicaldata" ("metric_id", "date"); (params None)
2024-08-05 23:42:08,877 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_name_c9d100_idx" ON "metrics_metric" ("name", "type"); (params None)
2024-08-05 23:42:08,891 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_7984a6_idx" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:42:08,904 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1bdb27_idx" ON "metrics_tag" ("name", "project_id"); (params None)
2024-08-05 23:42:08,916 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tar_metric__234682_idx" ON "metrics_target" ("metric_id", "target_date"); (params None)
2024-08-05 23:42:08,928 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tre_metric__d386bb_idx" ON "metrics_trend" ("metric_id", "start_date", "end_date"); (params None)
2024-08-05 23:42:08,945 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_con_from_me_9411ea_idx"; (params None)
2024-08-05 23:42:08,956 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:42:08,958 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:42:08,969 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_from_metric_id_aa131d91_uniq" UNIQUE ("tenant_id", "from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:42:08,987 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_project_id_4c1b22ec" ON "metrics_connection" ("project_id"); (params None)
2024-08-05 23:42:09,006 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; ALTER TABLE "metrics_connection" DROP CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id"; (params None)
2024-08-05 23:42:09,007 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "project_id" CASCADE; (params None)
2024-08-05 23:42:09,020 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:42:09,022 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:42:09,033 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:42:09,036 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_project_id_36bdbe46" ON "metrics_metric" ("project_id"); (params None)
2024-08-05 23:42:09,040 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_correlation" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "lag" integer NOT NULL, "pearson_correlation" double precision NOT NULL, "spearman_correlation" double precision NOT NULL); (params None)
2024-08-05 23:42:09,045 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:09,052 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dataqualityscore" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_entry" varchar(255) NOT NULL, "completeness_score" double precision NOT NULL, "accuracy_score" double precision NOT NULL, "consistency_score" double precision NOT NULL, "timeliness_score" double precision NOT NULL, "overall_score" double precision NOT NULL); (params None)
2024-08-05 23:42:09,056 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_impactanalysis" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "before_value" double precision NOT NULL, "after_value" double precision NOT NULL, "percentage_change" double precision NOT NULL, "confidence" double precision NOT NULL, "artifact_link" varchar(200) NOT NULL); (params None)
2024-08-05 23:42:09,060 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_insight" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "title" varchar(200) NOT NULL, "content" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:09,065 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metricmetadata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_source" varchar(100) NOT NULL, "source_url" varchar(200) NOT NULL, "rhythm" varchar(20) NOT NULL, "last_updated" timestamp with time zone NOT NULL, "technical_description" text NOT NULL, "description" text NOT NULL, "artifacts_url" varchar(200) NOT NULL, "hypothesis" text NOT NULL, "confidence" varchar(20) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL); (params None)
2024-08-05 23:42:09,072 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metrictarget" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "target_kpi" varchar(100) NOT NULL, "target_remarks" text NOT NULL, "target_date" date NULL, "target_value" double precision NULL); (params None)
2024-08-05 23:42:09,078 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_strategy" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "estimated_time" interval NOT NULL, "artifacts_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:09,087 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tacticalsolution" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "artifact_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:09,094 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_team" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:09,102 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_technicalindicator" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "stochastic_value" double precision NOT NULL, "rsi_value" double precision NOT NULL, "percent_change" double precision NOT NULL, "moving_average" double precision NOT NULL); (params None)
2024-08-05 23:42:09,105 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_timedimension" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL UNIQUE, "day" integer NOT NULL, "day_of_week" integer NOT NULL, "day_name" varchar(10) NOT NULL, "week" integer NOT NULL, "month" integer NOT NULL, "month_name" varchar(10) NOT NULL, "quarter" integer NOT NULL, "year" integer NOT NULL, "is_weekend" boolean NOT NULL, "is_holiday" boolean NOT NULL); (params None)
2024-08-05 23:42:09,111 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_userprofile" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY); (params None)
2024-08-05 23:42:09,127 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_metric_id_181e8748_fk_metrics_metric_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id"; (params None)
2024-08-05 23:42:09,128 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "metric_id" CASCADE; (params None)
2024-08-05 23:42:09,140 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id"; (params None)
2024-08-05 23:42:09,141 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:42:09,151 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_name_c9d100_idx"; (params None)
2024-08-05 23:42:09,162 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_last_up_7984a6_idx"; (params None)
2024-08-05 23:42:09,171 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" RENAME COLUMN "description" TO "summary"; (params None)
2024-08-05 23:42:09,183 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq"; (params None)
2024-08-05 23:42:09,193 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "correlation_coefficient" CASCADE; (params None)
2024-08-05 23:42:09,204 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" DROP COLUMN "results" CASCADE; (params None)
2024-08-05 23:42:09,214 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "anomaly_detected" CASCADE; (params None)
2024-08-05 23:42:09,224 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "forecasted_value" CASCADE; (params None)
2024-08-05 23:42:09,234 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "trend_component" CASCADE; (params None)
2024-08-05 23:42:09,246 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "importance" varchar(20) DEFAULT 'MEDIUM' NOT NULL; (params None)
2024-08-05 23:42:09,247 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "importance" DROP DEFAULT; (params None)
2024-08-05 23:42:09,257 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:42:09.257644+00:00' NOT NULL; (params None)
2024-08-05 23:42:09,258 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:42:09,268 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "anomaly_type" varchar(20) DEFAULT 'IGNORE' NOT NULL; (params None)
2024-08-05 23:42:09,269 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "anomaly_type" DROP DEFAULT; (params None)
2024-08-05 23:42:09,280 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "quality" varchar(20) DEFAULT 'LOW' NOT NULL; (params None)
2024-08-05 23:42:09,281 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "quality" DROP DEFAULT; (params None)
2024-08-05 23:42:09,291 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "impact_description" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:42:09,292 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "impact_description" DROP DEFAULT; (params None)
2024-08-05 23:42:09,302 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "objective" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:42:09,303 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "objective" DROP DEFAULT; (params None)
2024-08-05 23:42:09,313 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_date" date NULL; (params None)
2024-08-05 23:42:09,325 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_files" varchar(100) NULL; (params None)
2024-08-05 23:42:09,335 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_summary" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:42:09,336 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "result_summary" DROP DEFAULT; (params None)
2024-08-05 23:42:09,345 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_value" double precision NULL; (params None)
2024-08-05 23:42:09,356 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:42:09.355881+00:00' NOT NULL; (params None)
2024-08-05 23:42:09,357 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:42:09,368 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "variance" double precision NULL; (params None)
2024-08-05 23:42:09,379 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD COLUMN "forecast_id" bigint NULL CONSTRAINT "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" REFERENCES "metrics_forecast"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" IMMEDIATE; (params None)
2024-08-05 23:42:09,391 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "impact" TYPE varchar(20) USING "impact"::varchar(20); (params None)
2024-08-05 23:42:09,486 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "status" TYPE varchar(20); (params None)
2024-08-05 23:42:09,605 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric1_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:42:09,617 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric2_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:42:09,628 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:09,637 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:42:09,655 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:09,804 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:42:09,823 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:42:09,842 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "experiment_id" bigint NOT NULL CONSTRAINT "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" REFERENCES "metrics_experiment"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" IMMEDIATE; (params None)
2024-08-05 23:42:09,860 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:42:09,879 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:09,898 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:42:09,917 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:09,937 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "user_id" bigint NOT NULL CONSTRAINT "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:42:09,956 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "data_quality_score_id" bigint NULL UNIQUE CONSTRAINT "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" REFERENCES "metrics_dataqualityscore"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" IMMEDIATE; (params None)
2024-08-05 23:42:09,978 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "metric_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:42:09,999 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:10,019 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:42:10,040 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:10,061 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:10,083 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:42:10,105 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:42:10,127 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_team" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:10,151 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "team_id" bigint NOT NULL CONSTRAINT "metrics_strategy_team_id_f1781500_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_team_id_f1781500_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:42:10,173 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:42:10,195 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:42:10,218 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_experiment_team_id_537107e3_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_experiment_team_id_537107e3_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:42:10,370 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:42:10,392 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:42:10,415 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_timedimension" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:10,439 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:10,464 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "user_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:42:10,468 - django.db.backends.schema - DEBUG - DROP TABLE "metrics_target" CASCADE; (params None)
2024-08-05 23:42:10,488 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "confidence" CASCADE; (params None)
2024-08-05 23:42:10,507 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "description" CASCADE; (params None)
2024-08-05 23:42:10,526 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "hypothesis" CASCADE; (params None)
2024-08-05 23:42:10,545 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "last_updated" CASCADE; (params None)
2024-08-05 23:42:10,565 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_x" CASCADE; (params None)
2024-08-05 23:42:10,583 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_y" CASCADE; (params None)
2024-08-05 23:42:10,602 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "rhythm" CASCADE; (params None)
2024-08-05 23:42:10,621 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "source" CASCADE; (params None)
2024-08-05 23:42:10,641 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "technical_description" CASCADE; (params None)
2024-08-05 23:42:10,660 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD CONSTRAINT "metrics_correlation_tenant_id_metric1_id_met_49a4c34a_uniq" UNIQUE ("tenant_id", "metric1_id", "metric2_id", "lag"); (params None)
2024-08-05 23:42:10,682 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_metric__b85d3a_idx" ON "metrics_insight" ("metric_id", "date"); (params None)
2024-08-05 23:42:10,704 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_user_id_1ebb42_idx" ON "metrics_insight" ("user_id", "date"); (params None)
2024-08-05 23:42:10,725 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_metric__a2b705_idx" ON "metrics_metrictarget" ("metric_id", "target_date"); (params None)
2024-08-05 23:42:10,746 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_6e2e67_idx" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:42:10,766 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_date_53cb14_idx" ON "metrics_timedimension" ("date"); (params None)
2024-08-05 23:42:10,788 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_year_92da9e_idx" ON "metrics_timedimension" ("year", "month", "day"); (params None)
2024-08-05 23:42:10,791 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_username_6e55f358_like" ON "metrics_customuser" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:42:10,793 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_date_ded95ba1" ON "metrics_insight" ("date"); (params None)
2024-08-05 23:42:10,794 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_last_updated_76599a1b" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:42:10,797 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_target_date_38cd9191" ON "metrics_metrictarget" ("target_date"); (params None)
2024-08-05 23:42:10,799 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_forecast_id_29590c29" ON "metrics_historicaldata" ("forecast_id"); (params None)
2024-08-05 23:42:10,801 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric1_id_6e1c2404" ON "metrics_correlation" ("metric1_id"); (params None)
2024-08-05 23:42:10,804 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric2_id_f2cc46dd" ON "metrics_correlation" ("metric2_id"); (params None)
2024-08-05 23:42:10,806 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_tenant_id_a00a5169" ON "metrics_correlation" ("tenant_id"); (params None)
2024-08-05 23:42:10,808 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_customuser_id_group_id_1c5fc435_uniq" UNIQUE ("customuser_id", "group_id"); (params None)
2024-08-05 23:42:10,810 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_g_customuser_id_fc13f3af_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:10,811 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_group_id_6b097e12_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:10,812 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_customuser_id_fc13f3af" ON "metrics_customuser_groups" ("customuser_id"); (params None)
2024-08-05 23:42:10,814 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_group_id_6b097e12" ON "metrics_customuser_groups" ("group_id"); (params None)
2024-08-05 23:42:10,816 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_tenant_id_02b7403c" ON "metrics_customuser" ("tenant_id"); (params None)
2024-08-05 23:42:10,818 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_user__customuser_id_permission_68cc320f_uniq" UNIQUE ("customuser_id", "permission_id"); (params None)
2024-08-05 23:42:10,820 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_customuser_id_46e97f00_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:10,821 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_permission_id_d66d657c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:10,822 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_customuser_id_46e97f00" ON "metrics_customuser_user_permissions" ("customuser_id"); (params None)
2024-08-05 23:42:10,824 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_permission_id_d66d657c" ON "metrics_customuser_user_permissions" ("permission_id"); (params None)
2024-08-05 23:42:10,826 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_tenant_id_8e9f296d" ON "metrics_dataqualityscore" ("tenant_id"); (params None)
2024-08-05 23:42:10,828 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_experiment_id_1beae7fe" ON "metrics_impactanalysis" ("experiment_id"); (params None)
2024-08-05 23:42:10,831 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_metric_id_f4b9eeb6" ON "metrics_impactanalysis" ("metric_id"); (params None)
2024-08-05 23:42:10,833 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_tenant_id_126ca20d" ON "metrics_impactanalysis" ("tenant_id"); (params None)
2024-08-05 23:42:10,835 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_metric_id_26d3a9d8" ON "metrics_insight" ("metric_id"); (params None)
2024-08-05 23:42:10,837 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_tenant_id_724d7d85" ON "metrics_insight" ("tenant_id"); (params None)
2024-08-05 23:42:10,839 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_user_id_83d421e1" ON "metrics_insight" ("user_id"); (params None)
2024-08-05 23:42:10,841 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_tenant_id_3277f967" ON "metrics_metricmetadata" ("tenant_id"); (params None)
2024-08-05 23:42:10,844 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_metric_id_7876e2c8" ON "metrics_metrictarget" ("metric_id"); (params None)
2024-08-05 23:42:10,846 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_tenant_id_b26a17f8" ON "metrics_metrictarget" ("tenant_id"); (params None)
2024-08-05 23:42:10,848 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_tenant_id_1323395e" ON "metrics_strategy" ("tenant_id"); (params None)
2024-08-05 23:42:10,850 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_metric_id_9887ffa4" ON "metrics_tacticalsolution" ("metric_id"); (params None)
2024-08-05 23:42:10,852 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_tenant_id_cf9028f0" ON "metrics_tacticalsolution" ("tenant_id"); (params None)
2024-08-05 23:42:10,854 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_team_tenant_id_3a14c47d" ON "metrics_team" ("tenant_id"); (params None)
2024-08-05 23:42:10,857 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_team_id_f1781500" ON "metrics_strategy" ("team_id"); (params None)
2024-08-05 23:42:10,859 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_team_id_f140658d" ON "metrics_metricmetadata" ("team_id"); (params None)
2024-08-05 23:42:10,860 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_team_id_4c4ffc18" ON "metrics_customuser" ("team_id"); (params None)
2024-08-05 23:42:10,862 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_team_id_537107e3" ON "metrics_experiment" ("team_id"); (params None)
2024-08-05 23:42:10,864 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_metric_id_3e2eead6" ON "metrics_technicalindicator" ("metric_id"); (params None)
2024-08-05 23:42:10,866 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_tenant_id_f4de3b44" ON "metrics_technicalindicator" ("tenant_id"); (params None)
2024-08-05 23:42:10,869 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_timedimension_tenant_id_f375bb45" ON "metrics_timedimension" ("tenant_id"); (params None)
2024-08-05 23:42:10,872 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_userprofile_tenant_id_cca71dae" ON "metrics_userprofile" ("tenant_id"); (params None)
2024-08-05 23:42:11,023 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "strength" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:42:11,024 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "strength" DROP DEFAULT; (params None)
2024-08-05 23:42:11,042 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "lower_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:42:11,043 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "lower_bound" DROP DEFAULT; (params None)
2024-08-05 23:42:11,062 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "upper_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:42:11,063 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "upper_bound" DROP DEFAULT; (params None)
2024-08-05 23:42:11,082 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD COLUMN "slope" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:42:11,083 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ALTER COLUMN "slope" DROP DEFAULT; (params None)
2024-08-05 23:42:11,109 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_movingaverage" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "ma_type" varchar(10) NOT NULL, "period" integer NOT NULL, "value" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:11,137 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_networkanalysisresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "analysis_type" varchar(20) NOT NULL, "result" jsonb NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:11,167 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_seasonalityresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "seasonality_type" varchar(20) NOT NULL, "strength" double precision NOT NULL, "period" integer NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:11,195 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trendchangepoint" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "change_type" varchar(20) NOT NULL, "significance" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:11,198 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD CONSTRAINT "metrics_movingaverage_metric_id_7c61cebf_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:11,199 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_metric_id_7c61cebf" ON "metrics_movingaverage" ("metric_id"); (params None)
2024-08-05 23:42:11,201 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD CONSTRAINT "metrics_networkanaly_metric_id_a4c90102_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:11,203 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_metric_id_a4c90102" ON "metrics_networkanalysisresult" ("metric_id"); (params None)
2024-08-05 23:42:11,205 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityr_metric_id_6e494791_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:11,206 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_metric_id_6e494791" ON "metrics_seasonalityresult" ("metric_id"); (params None)
2024-08-05 23:42:11,208 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD CONSTRAINT "metrics_trendchangep_metric_id_f8eb9f76_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:11,208 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_metric_id_f8eb9f76" ON "metrics_trendchangepoint" ("metric_id"); (params None)
2024-08-05 23:42:11,237 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:42:11,239 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:42:11,264 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" IMMEDIATE; (params None)
2024-08-05 23:42:11,266 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:42:11,287 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ALTER COLUMN "value" DROP NOT NULL; (params None)
2024-08-05 23:42:11,306 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD CONSTRAINT "metrics_dataqualityscore_tenant_id_metric_id_proj_66b9fb01_uniq" UNIQUE ("tenant_id", "metric_id", "project_id"); (params None)
2024-08-05 23:42:11,310 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_metric_id_1b6367d1" ON "metrics_dataqualityscore" ("metric_id"); (params None)
2024-08-05 23:42:11,312 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_project_id_123a4f58" ON "metrics_dataqualityscore" ("project_id"); (params None)
2024-08-05 23:42:11,337 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:42:11,365 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:11,367 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:42:11,395 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:42:11,396 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:42:11,420 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:42:11,422 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:42:11,447 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:42:11,448 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:42:11,469 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq" UNIQUE ("tenant_id", "metric_id"); (params None)
2024-08-05 23:42:11,472 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_tenant_id_5a9de228" ON "metrics_movingaverage" ("tenant_id"); (params None)
2024-08-05 23:42:11,474 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_tenant_id_16a6ba09" ON "metrics_networkanalysisresult" ("tenant_id"); (params None)
2024-08-05 23:42:11,476 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_tenant_id_ca2da3fd" ON "metrics_seasonalityresult" ("tenant_id"); (params None)
2024-08-05 23:42:11,478 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_tenant_id_da10d898" ON "metrics_trendchangepoint" ("tenant_id"); (params None)
2024-08-05 23:42:11,633 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:42:11,635 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:42:11,636 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_metric_id_c86f5720" ON "metrics_report" ("metric_id"); (params None)
2024-08-05 23:42:11,659 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "analysis_result" jsonb NULL; (params None)
2024-08-05 23:42:11,679 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "anomaly_result" jsonb NULL; (params None)
2024-08-05 23:42:11,700 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:42:11.700400+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:42:11,701 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:42:11,721 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "forecast_result" jsonb NULL; (params None)
2024-08-05 23:42:11,742 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "relationship_result" jsonb NULL; (params None)
2024-08-05 23:42:11,765 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "report" text DEFAULT '1' NOT NULL; (params None)
2024-08-05 23:42:11,766 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "report" DROP DEFAULT; (params None)
2024-08-05 23:42:11,787 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "updated_at" timestamp with time zone DEFAULT '2024-08-05T23:42:11.786738+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:42:11,788 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "updated_at" DROP DEFAULT; (params None)
2024-08-05 23:42:11,842 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_trendchangepoint" DROP CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c"; (params None)
2024-08-05 23:42:11,843 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:42:11,859 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "significance" DROP NOT NULL; (params None)
2024-08-05 23:42:11,878 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" RENAME COLUMN "change_type" TO "direction"; (params None)
2024-08-05 23:42:11,919 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:42:11.919136+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:42:11,920 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:42:11,945 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq"; (params None)
2024-08-05 23:42:11,946 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresul_metric_id_seasonality_ty_d3492b78_uniq" UNIQUE ("metric_id", "seasonality_type"); (params None)
2024-08-05 23:42:11,976 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c"; (params None)
2024-08-05 23:42:11,977 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:42:11,980 - django.db.backends.schema - DEBUG - CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:11,984 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" ("session_key" varchar_pattern_ops); (params None)
2024-08-05 23:42:11,986 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date"); (params None)
2024-08-05 23:42:12,968 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:42:12,968 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:42:12,969 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:12,969 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:12,970 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:42:12,974 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:12,975 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:12,978 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:12,978 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:12,980 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:12,980 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:12,983 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:14,725 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:42:14,727 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:14,728 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:14,729 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:14,731 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:14,731 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:14,734 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:14,736 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:14,736 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:14,740 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:14,755 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 99.5134376048471, 'median': 99.80407153956804, 'std': 9.971245828956478, 'min': 75.7198204616319, 'max': 121.7580024948425, 'skewness': -0.07319630419864269, 'kurtosis': -0.3752845959539659, 'missing_percentage': 0.0}}
2024-08-05 23:42:14,761 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:42:14,761 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:42:14,764 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:14,764 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:14,766 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:42:14,772 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:14,773 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:14,776 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:14,776 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:14,780 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:14,780 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:14,783 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:16,574 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:42:16,576 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:16,577 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:16,578 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:16,580 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:16,580 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:16,582 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:16,584 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:16,585 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:16,587 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:16,610 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 99.5134376048471, 'median': 99.80407153956804, 'std': 9.971245828956478, 'min': 75.7198204616319, 'max': 121.7580024948425, 'skewness': -0.07319630419864269, 'kurtosis': -0.3752845959539659, 'missing_percentage': 0.0}}
2024-08-05 23:42:16,611 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:42:16,611 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 11
2024-08-05 23:42:16,620 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:42:16,626 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:42:16,630 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 11
2024-08-05 23:42:16,631 - metrics.computations.feature_engineering - INFO - Parameters for metric 11: dynamic
2024-08-05 23:42:16,631 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 11: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:42:16,634 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:42:16,635 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:42:16,635 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:16,636 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:16,638 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:42:16,648 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:16,648 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:16,651 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:16,651 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:16,655 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:16,656 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:16,661 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:18,372 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:42:18,374 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:18,376 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:18,376 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:18,378 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:18,378 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:18,381 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:18,383 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:18,383 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:18,386 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:18,400 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 99.5134376048471, 'median': 99.80407153956804, 'std': 9.971245828956478, 'min': 75.7198204616319, 'max': 121.7580024948425, 'skewness': -0.07319630419864269, 'kurtosis': -0.3752845959539659, 'missing_percentage': 0.0}}
2024-08-05 23:42:18,406 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:42:18,406 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:42:18,407 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:18,407 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:18,410 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:42:18,421 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:18,421 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:18,424 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:18,425 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:18,428 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:18,429 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:18,434 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:20,271 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:42:20,273 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:20,275 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:20,275 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:20,277 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:20,278 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:20,280 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:20,282 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:20,282 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:20,285 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:20,302 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 99.5134376048471, 'median': 99.80407153956804, 'std': 9.971245828956478, 'min': 75.7198204616319, 'max': 121.7580024948425, 'skewness': -0.07319630419864269, 'kurtosis': -0.3752845959539659, 'missing_percentage': 0.0}}
2024-08-05 23:42:20,302 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:42:20,302 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 11
2024-08-05 23:42:20,307 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:42:20,313 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:42:20,318 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 11
2024-08-05 23:42:20,318 - metrics.computations.feature_engineering - INFO - Parameters for metric 11: dynamic
2024-08-05 23:42:20,318 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 11: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:42:20,319 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Setup completed
2024-08-05 23:42:20,319 - metrics.computations.permanent_computations - INFO - Starting all computations for metrics: [11, 12]
2024-08-05 23:42:20,319 - metrics.computations.permanent_computations - INFO - Starting computations for metric 11
2024-08-05 23:42:20,320 - metrics.computations.permanent_computations - INFO - Starting data preparation for metric 11
2024-08-05 23:42:20,320 - metrics.computations.permanent_computations - INFO - Starting data preparation for metric 11
2024-08-05 23:42:20,322 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:42:20,322 - metrics.computations.permanent_computations - INFO - DataPreparation object created: <metrics.computations.data_preparation.DataPreparation object at 0x7fccbf75ca30>
2024-08-05 23:42:20,322 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:42:20,323 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:20,323 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:20,328 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:42:20,337 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:20,337 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:20,341 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:20,341 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:20,345 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:20,345 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:20,348 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:22,110 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:42:22,113 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:22,114 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:22,115 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:22,117 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:22,117 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:22,119 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:22,121 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:22,122 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:22,125 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:22,139 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 99.5134376048471, 'median': 99.80407153956804, 'std': 9.971245828956478, 'min': 75.7198204616319, 'max': 121.7580024948425, 'skewness': -0.07319630419864269, 'kurtosis': -0.3752845959539659, 'missing_percentage': 0.0}}
2024-08-05 23:42:22,139 - metrics.computations.permanent_computations - INFO - prepare_data() called, returned DataFrame of shape (1000, 2)
2024-08-05 23:42:22,139 - metrics.computations.permanent_computations - INFO - Data preparation statistics for metric 11:
2024-08-05 23:42:22,139 - metrics.computations.permanent_computations - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:22,139 - metrics.computations.permanent_computations - INFO - Number of data points: 1000
2024-08-05 23:42:22,140 - metrics.computations.permanent_computations - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:22,140 - metrics.computations.permanent_computations - INFO - Metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 99.5134376048471, 'median': 99.80407153956804, 'std': 9.971245828956478, 'min': 75.7198204616319, 'max': 121.7580024948425, 'skewness': -0.07319630419864269, 'kurtosis': -0.3752845959539659, 'missing_percentage': 0.0}}
2024-08-05 23:42:22,140 - metrics.computations.permanent_computations - INFO - Date range: 2023-01-01 00:00:00 to 2025-09-26 00:00:00
2024-08-05 23:42:22,140 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:42:22,141 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:22,142 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:22,147 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:42:22,159 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:22,159 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:22,162 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:22,162 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:22,165 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:22,166 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:22,168 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:23,931 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:42:23,933 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:23,935 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:23,935 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:23,937 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:23,937 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:23,940 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:23,942 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:23,942 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:23,945 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:23,963 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 99.5134376048471, 'median': 99.80407153956804, 'std': 9.971245828956478, 'min': 75.7198204616319, 'max': 121.7580024948425, 'skewness': -0.07319630419864269, 'kurtosis': -0.3752845959539659, 'missing_percentage': 0.0}}
2024-08-05 23:42:23,964 - metrics.computations.permanent_computations - INFO - Data preparation completed for metric 11
2024-08-05 23:42:23,964 - metrics.computations.permanent_computations - INFO - Starting feature engineering for metric 11
2024-08-05 23:42:23,969 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:42:23,969 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:42:23,970 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:23,970 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:23,975 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:42:23,985 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:23,985 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:23,988 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:23,988 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:23,991 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:23,991 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:23,994 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:25,764 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:42:25,766 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:25,768 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:25,768 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:25,770 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:25,771 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:25,773 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:25,775 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:25,775 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:25,778 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:25,792 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 99.5134376048471, 'median': 99.80407153956804, 'std': 9.971245828956478, 'min': 75.7198204616319, 'max': 121.7580024948425, 'skewness': -0.07319630419864269, 'kurtosis': -0.3752845959539659, 'missing_percentage': 0.0}}
2024-08-05 23:42:25,792 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:42:25,793 - metrics.computations.feature_engineering - ERROR - Error in profile_data: 'date'
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - Data profile for metric 11:
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - count: 0
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - mean: nan
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - median: nan
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - std: nan
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - min: nan
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - max: nan
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - range: nan
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - skewness: nan
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - kurtosis: nan
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - variance: nan
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - coefficient_of_variation: nan
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - percentiles: {'1%': nan, '5%': nan, '25%': nan, '75%': nan, '95%': nan, '99%': nan}
2024-08-05 23:42:25,793 - metrics.computations.permanent_computations - INFO - missing_values: 0
2024-08-05 23:42:25,794 - metrics.computations.permanent_computations - INFO - missing_percentage: 0
2024-08-05 23:42:25,794 - metrics.computations.permanent_computations - INFO - unique_values: 0
2024-08-05 23:42:25,794 - metrics.computations.permanent_computations - INFO - time_range: {'start': None, 'end': None, 'duration_days': 0}
2024-08-05 23:42:25,794 - metrics.computations.permanent_computations - INFO - frequency: None
2024-08-05 23:42:25,794 - metrics.computations.permanent_computations - INFO - trend: None
2024-08-05 23:42:25,794 - metrics.computations.permanent_computations - INFO - stationarity: None
2024-08-05 23:42:25,794 - metrics.computations.permanent_computations - INFO - outliers: {'count': 0, 'percentage': 0}
2024-08-05 23:42:25,794 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 11
2024-08-05 23:42:25,799 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:42:25,804 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:42:25,808 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 11
2024-08-05 23:42:25,808 - metrics.computations.feature_engineering - INFO - Parameters for metric 11: dynamic
2024-08-05 23:42:25,808 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 11: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:42:25,808 - metrics.computations.permanent_computations - INFO - Feature engineering completed for metric 11
2024-08-05 23:42:25,808 - metrics.computations.permanent_computations - INFO - Starting analysis for metric 11
2024-08-05 23:42:25,812 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:42:25,812 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:42:25,813 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:25,813 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:25,818 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:42:25,829 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:25,829 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:25,832 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:25,832 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:25,835 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:25,836 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:25,838 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:27,630 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:42:27,632 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:27,634 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:27,634 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:27,637 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:27,637 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:27,639 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:27,641 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:27,641 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:27,644 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:27,659 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 99.5134376048471, 'median': 99.80407153956804, 'std': 9.971245828956478, 'min': 75.7198204616319, 'max': 121.7580024948425, 'skewness': -0.07319630419864269, 'kurtosis': -0.3752845959539659, 'missing_percentage': 0.0}}
2024-08-05 23:42:27,665 - metrics.computations.computations_analyzer - INFO - Analyzed trend for metric 11
2024-08-05 23:42:27,689 - metrics.computations.computations_analyzer - INFO - Calculated moving averages for metric 11
2024-08-05 23:42:27,689 - metrics.computations.computations_analyzer - INFO - Calculated technical indicators for metric 11
2024-08-05 23:42:27,692 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:42:27,693 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:42:27,693 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:27,694 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:27,700 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:42:27,711 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:27,711 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:27,714 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:27,715 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:27,717 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:27,718 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:27,721 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:29,494 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:42:29,496 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:29,497 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:29,497 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:29,500 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:29,500 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:29,502 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:29,505 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:29,505 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:29,508 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:29,535 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 99.5134376048471, 'median': 99.80407153956804, 'std': 9.971245828956478, 'min': 75.7198204616319, 'max': 121.7580024948425, 'skewness': -0.07319630419864269, 'kurtosis': -0.3752845959539659, 'missing_percentage': 0.0}}
2024-08-05 23:42:29,540 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:42:29,540 - metrics.computations.computations_analyzer - ERROR - Error detecting seasonality for metric 11: 'dict' object has no attribute 'strength'
2024-08-05 23:42:29,973 - metrics.computations.computations_analyzer - INFO - Detected trend change point for metric 11
2024-08-05 23:42:29,978 - metrics.computations.permanent_computations - ERROR - Unexpected error saving analysis results for metric 11: string indices must be integers
2024-08-05 23:42:29,978 - metrics.computations.permanent_computations - INFO - Analysis completed for metric 11
2024-08-05 23:42:29,978 - metrics.computations.permanent_computations - INFO - Starting forecasting for metric 11
2024-08-05 23:42:29,981 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:42:29,981 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:42:29,982 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:29,983 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:29,988 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:42:29,997 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:29,997 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:30,000 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:30,000 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:30,002 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:30,003 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:30,005 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:31,821 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:42:31,823 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:31,825 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:31,825 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:31,827 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:31,827 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:31,830 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:31,832 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:31,832 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:31,835 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:31,852 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 99.5134376048471, 'median': 99.80407153956804, 'std': 9.971245828956478, 'min': 75.7198204616319, 'max': 121.7580024948425, 'skewness': -0.07319630419864269, 'kurtosis': -0.3752845959539659, 'missing_percentage': 0.0}}
2024-08-05 23:42:31,854 - metrics.computations.computations_forecaster - WARNING - SARIMA model not recommended for metric 11. Using it anyway.
2024-08-05 23:42:33,920 - metrics.computations.computations_forecaster - INFO - Generated SARIMA forecast for metric 11
2024-08-05 23:42:33,921 - metrics.computations.computations_forecaster - WARNING - Prophet model not recommended for metric 11. Using it anyway.
2024-08-05 23:42:33,921 - prophet - DEBUG - Trying to load backend: CMDSTANPY
2024-08-05 23:42:33,940 - prophet - DEBUG - Loaded stan backend: CMDSTANPY
2024-08-05 23:42:33,946 - prophet - INFO - Disabling daily seasonality. Run prophet with daily_seasonality=True to override this.
2024-08-05 23:42:33,960 - cmdstanpy - DEBUG - input tempfile: /tmp/tmpsp01_789/hb2gfgrm.json
2024-08-05 23:42:34,146 - cmdstanpy - DEBUG - input tempfile: /tmp/tmpsp01_789/kxb8k7ap.json
2024-08-05 23:42:34,147 - cmdstanpy - DEBUG - idx 0
2024-08-05 23:42:34,147 - cmdstanpy - DEBUG - running CmdStan, num_threads: None
2024-08-05 23:42:34,147 - cmdstanpy - DEBUG - CmdStan args: ['/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/prophet/stan_model/prophet_model.bin', 'random', 'seed=73245', 'data', 'file=/tmp/tmpsp01_789/hb2gfgrm.json', 'init=/tmp/tmpsp01_789/kxb8k7ap.json', 'output', 'file=/tmp/tmpsp01_789/prophet_modeluip3sjtv/prophet_model-20240805234234.csv', 'method=optimize', 'algorithm=lbfgs', 'iter=10000']
2024-08-05 23:42:34,147 - cmdstanpy - INFO - Chain [1] start processing
2024-08-05 23:42:34,192 - cmdstanpy - INFO - Chain [1] done processing
2024-08-05 23:42:34,324 - metrics.computations.computations_forecaster - INFO - Generated Prophet forecast for metric 11
2024-08-05 23:42:34,325 - metrics.computations.permanent_computations - ERROR - Error in forecasting for metric 11: string indices must be integers
2024-08-05 23:42:34,325 - metrics.computations.permanent_computations - INFO - Starting anomaly detection for metric 11
2024-08-05 23:42:34,328 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:42:34,328 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:42:34,328 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:34,329 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:34,335 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:42:34,343 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:34,344 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:34,346 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:34,347 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:34,349 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:34,349 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:34,351 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:36,180 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:42:36,182 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:36,184 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:36,184 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:36,187 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:36,187 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:36,189 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:36,191 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:36,191 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:36,194 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:36,221 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 99.5134376048471, 'median': 99.80407153956804, 'std': 9.971245828956478, 'min': 75.7198204616319, 'max': 121.7580024948425, 'skewness': -0.07319630419864269, 'kurtosis': -0.3752845959539659, 'missing_percentage': 0.0}}
2024-08-05 23:42:36,222 - metrics.computations.computations_anomalies - INFO - Initialized AnomalyDetector for metric 11
2024-08-05 23:42:36,223 - metrics.computations.computations_anomalies - INFO - Seasonality period: 2
2024-08-05 23:42:36,223 - metrics.computations.computations_anomalies - INFO - Window size: 1000
2024-08-05 23:42:36,223 - metrics.computations.computations_anomalies - INFO - Base threshold: 5.0
2024-08-05 23:42:36,223 - metrics.computations.computations_anomalies - INFO - Context window: 15
2024-08-05 23:42:36,223 - metrics.computations.computations_anomalies - INFO - Global threshold: 5.0
2024-08-05 23:42:36,223 - metrics.computations.computations_anomalies - INFO - Starting anomaly detection for metric 11
2024-08-05 23:42:36,223 - metrics.computations.computations_anomalies - INFO - Data shape: (1000, 2)
2024-08-05 23:42:36,225 - metrics.computations.computations_anomalies - INFO - Data summary: count    1000.000000
mean       99.513438
std         9.971246
min        75.719820
25%        92.934074
50%        99.804072
75%       106.314417
max       121.758002
Name: value, dtype: float64
2024-08-05 23:42:36,229 - metrics.computations.computations_anomalies - INFO - Deseasonalized data summary: count    1000.000000
mean       99.507822
std         9.973753
min        75.719820
25%        92.912414
50%        99.804072
75%       106.314417
max       121.758002
Name: value, dtype: float64
2024-08-05 23:42:36,230 - metrics.computations.computations_anomalies - INFO - Modified z-scores range: 0.2489252043304685 to 0.2489252043304685
2024-08-05 23:42:36,232 - metrics.computations.computations_anomalies - INFO - Modified z-scores summary: count    1.000000
mean     0.248925
std           NaN
min      0.248925
25%      0.248925
50%      0.248925
75%      0.248925
max      0.248925
Name: value, dtype: float64
2024-08-05 23:42:36,233 - metrics.computations.computations_anomalies - INFO - Adaptive threshold range: 6.01825031334684 to 6.01825031334684
2024-08-05 23:42:36,235 - metrics.computations.computations_anomalies - INFO - Adaptive threshold summary: count    1.00000
mean     6.01825
std          NaN
min      6.01825
25%      6.01825
50%      6.01825
75%      6.01825
max      6.01825
Name: value, dtype: float64
2024-08-05 23:42:36,236 - metrics.computations.computations_anomalies - INFO - Contextual z-scores range: nan to nan
2024-08-05 23:42:36,237 - metrics.computations.computations_anomalies - INFO - Contextual z-scores summary: count    0.0
mean     NaN
std      NaN
min      NaN
25%      NaN
50%      NaN
75%      NaN
max      NaN
Name: value, dtype: float64
2024-08-05 23:42:36,238 - metrics.computations.computations_anomalies - INFO - Global mean: 99.5078222510172, Global std: 9.973752894286704
2024-08-05 23:42:36,238 - metrics.computations.computations_anomalies - INFO - Number of anomalies detected: 0
2024-08-05 23:42:36,241 - metrics.computations.computations_anomalies - INFO - Detected 0 anomalies for metric 11
2024-08-05 23:42:36,243 - metrics.computations.permanent_computations - ERROR - Error in anomaly detection for metric 11: 'anomalies'
2024-08-05 23:42:36,243 - metrics.computations.permanent_computations - INFO - Starting relationship analysis for metric 11
2024-08-05 23:42:36,246 - metrics.computations.data_preparation - INFO - Loaded metric 11 for tenant 6 and project 6
2024-08-05 23:42:36,246 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 11
2024-08-05 23:42:36,247 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:36,247 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 11 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:36,256 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 11
2024-08-05 23:42:36,270 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:36,270 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:36,273 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:36,273 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:36,276 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:36,277 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:36,280 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:38,097 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 11
2024-08-05 23:42:38,099 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:38,100 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:38,101 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:38,103 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:38,103 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:38,106 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01   92.726057          6
2023-01-02   91.115881          6
2023-01-03  116.283678          6
2023-01-04  110.606026          6
2023-01-05   93.833799          6
2024-08-05 23:42:38,108 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:38,108 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:38,111 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:38,127 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 11, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 99.5134376048471, 'median': 99.80407153956804, 'std': 9.971245828956478, 'min': 75.7198204616319, 'max': 121.7580024948425, 'skewness': -0.07319630419864269, 'kurtosis': -0.3752845959539659, 'missing_percentage': 0.0}}
2024-08-05 23:42:38,129 - metrics.computations.permanent_computations - ERROR - Error in relationship analysis for metric 11: RelationshipAnalyzer.analyze_relationships() missing 1 required positional argument: 'other_metric_ids'
2024-08-05 23:42:38,129 - metrics.computations.permanent_computations - INFO - Generating report for metric 11
2024-08-05 23:42:38,130 - metrics.computations.permanent_computations - ERROR - Error generating or saving report for metric 11: -1
2024-08-05 23:42:38,130 - metrics.computations.permanent_computations - INFO - All computations completed for metric 11
2024-08-05 23:42:38,130 - metrics.computations.permanent_computations - INFO - Starting computations for metric 12
2024-08-05 23:42:38,131 - metrics.computations.permanent_computations - INFO - Starting data preparation for metric 12
2024-08-05 23:42:38,131 - metrics.computations.permanent_computations - INFO - Starting data preparation for metric 12
2024-08-05 23:42:38,133 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:42:38,133 - metrics.computations.permanent_computations - INFO - DataPreparation object created: <metrics.computations.data_preparation.DataPreparation object at 0x7fccbf754bb0>
2024-08-05 23:42:38,133 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:42:38,134 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:38,134 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:38,136 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:42:38,142 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:38,142 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:38,147 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:38,147 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:38,150 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:38,151 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:38,153 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:40,023 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:42:40,026 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:40,027 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:40,028 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:40,030 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:40,031 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:40,033 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:40,035 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:40,035 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:40,039 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:40,065 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 109.46478136533182, 'median': 109.78447869352485, 'std': 10.968370411852126, 'min': 83.2918025077951, 'max': 133.93380274432675, 'skewness': -0.07319630419864273, 'kurtosis': -0.375284595953965, 'missing_percentage': 0.0}}
2024-08-05 23:42:40,065 - metrics.computations.permanent_computations - INFO - prepare_data() called, returned DataFrame of shape (1000, 2)
2024-08-05 23:42:40,066 - metrics.computations.permanent_computations - INFO - Data preparation statistics for metric 12:
2024-08-05 23:42:40,066 - metrics.computations.permanent_computations - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:40,066 - metrics.computations.permanent_computations - INFO - Number of data points: 1000
2024-08-05 23:42:40,066 - metrics.computations.permanent_computations - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:40,066 - metrics.computations.permanent_computations - INFO - Metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 109.46478136533182, 'median': 109.78447869352485, 'std': 10.968370411852126, 'min': 83.2918025077951, 'max': 133.93380274432675, 'skewness': -0.07319630419864273, 'kurtosis': -0.375284595953965, 'missing_percentage': 0.0}}
2024-08-05 23:42:40,066 - metrics.computations.permanent_computations - INFO - Date range: 2023-01-01 00:00:00 to 2025-09-26 00:00:00
2024-08-05 23:42:40,066 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:42:40,067 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:40,068 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:40,070 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:42:40,076 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:40,077 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:40,087 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:40,087 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:40,091 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:40,091 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:40,095 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:41,968 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:42:41,970 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:41,972 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:41,972 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:41,974 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:41,974 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:41,977 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:41,979 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:41,979 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:41,982 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:41,999 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 109.46478136533182, 'median': 109.78447869352485, 'std': 10.968370411852126, 'min': 83.2918025077951, 'max': 133.93380274432675, 'skewness': -0.07319630419864273, 'kurtosis': -0.375284595953965, 'missing_percentage': 0.0}}
2024-08-05 23:42:41,999 - metrics.computations.permanent_computations - INFO - Data preparation completed for metric 12
2024-08-05 23:42:42,000 - metrics.computations.permanent_computations - INFO - Starting feature engineering for metric 12
2024-08-05 23:42:42,004 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:42:42,004 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:42:42,004 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:42,005 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:42,008 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:42:42,016 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:42,016 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:42,019 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:42,019 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:42,022 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:42,023 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:42,026 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:43,791 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:42:43,793 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:43,795 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:43,795 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:43,798 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:43,798 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:43,800 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:43,802 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:43,802 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:43,806 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:43,820 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 109.46478136533182, 'median': 109.78447869352485, 'std': 10.968370411852126, 'min': 83.2918025077951, 'max': 133.93380274432675, 'skewness': -0.07319630419864273, 'kurtosis': -0.375284595953965, 'missing_percentage': 0.0}}
2024-08-05 23:42:43,820 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:42:43,821 - metrics.computations.feature_engineering - ERROR - Error in profile_data: 'date'
2024-08-05 23:42:43,821 - metrics.computations.permanent_computations - INFO - Data profile for metric 12:
2024-08-05 23:42:43,821 - metrics.computations.permanent_computations - INFO - count: 0
2024-08-05 23:42:43,821 - metrics.computations.permanent_computations - INFO - mean: nan
2024-08-05 23:42:43,821 - metrics.computations.permanent_computations - INFO - median: nan
2024-08-05 23:42:43,821 - metrics.computations.permanent_computations - INFO - std: nan
2024-08-05 23:42:43,821 - metrics.computations.permanent_computations - INFO - min: nan
2024-08-05 23:42:43,821 - metrics.computations.permanent_computations - INFO - max: nan
2024-08-05 23:42:43,821 - metrics.computations.permanent_computations - INFO - range: nan
2024-08-05 23:42:43,821 - metrics.computations.permanent_computations - INFO - skewness: nan
2024-08-05 23:42:43,821 - metrics.computations.permanent_computations - INFO - kurtosis: nan
2024-08-05 23:42:43,821 - metrics.computations.permanent_computations - INFO - variance: nan
2024-08-05 23:42:43,821 - metrics.computations.permanent_computations - INFO - coefficient_of_variation: nan
2024-08-05 23:42:43,822 - metrics.computations.permanent_computations - INFO - percentiles: {'1%': nan, '5%': nan, '25%': nan, '75%': nan, '95%': nan, '99%': nan}
2024-08-05 23:42:43,822 - metrics.computations.permanent_computations - INFO - missing_values: 0
2024-08-05 23:42:43,822 - metrics.computations.permanent_computations - INFO - missing_percentage: 0
2024-08-05 23:42:43,822 - metrics.computations.permanent_computations - INFO - unique_values: 0
2024-08-05 23:42:43,822 - metrics.computations.permanent_computations - INFO - time_range: {'start': None, 'end': None, 'duration_days': 0}
2024-08-05 23:42:43,822 - metrics.computations.permanent_computations - INFO - frequency: None
2024-08-05 23:42:43,822 - metrics.computations.permanent_computations - INFO - trend: None
2024-08-05 23:42:43,822 - metrics.computations.permanent_computations - INFO - stationarity: None
2024-08-05 23:42:43,822 - metrics.computations.permanent_computations - INFO - outliers: {'count': 0, 'percentage': 0}
2024-08-05 23:42:43,822 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 12
2024-08-05 23:42:43,830 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:42:43,835 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:42:43,839 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 12
2024-08-05 23:42:43,839 - metrics.computations.feature_engineering - INFO - Parameters for metric 12: dynamic
2024-08-05 23:42:43,839 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 12: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:42:43,839 - metrics.computations.permanent_computations - INFO - Feature engineering completed for metric 12
2024-08-05 23:42:43,839 - metrics.computations.permanent_computations - INFO - Starting analysis for metric 12
2024-08-05 23:42:43,842 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:42:43,842 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:42:43,843 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:43,844 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:43,847 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:42:43,856 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:43,856 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:43,859 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:43,859 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:43,862 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:43,862 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:43,865 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:45,628 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:42:45,630 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:45,631 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:45,632 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:45,634 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:45,634 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:45,636 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:45,638 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:45,639 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:45,642 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:45,657 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 109.46478136533182, 'median': 109.78447869352485, 'std': 10.968370411852126, 'min': 83.2918025077951, 'max': 133.93380274432675, 'skewness': -0.07319630419864273, 'kurtosis': -0.375284595953965, 'missing_percentage': 0.0}}
2024-08-05 23:42:45,662 - metrics.computations.computations_analyzer - INFO - Analyzed trend for metric 12
2024-08-05 23:42:45,685 - metrics.computations.computations_analyzer - INFO - Calculated moving averages for metric 12
2024-08-05 23:42:45,685 - metrics.computations.computations_analyzer - INFO - Calculated technical indicators for metric 12
2024-08-05 23:42:45,688 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:42:45,688 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:42:45,689 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:45,689 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:45,693 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:42:45,703 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:45,703 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:45,709 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:45,709 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:45,712 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:45,713 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:45,716 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:47,463 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:42:47,466 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:47,467 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:47,467 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:47,470 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:47,470 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:47,472 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:47,474 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:47,474 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:47,477 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:47,492 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 109.46478136533182, 'median': 109.78447869352485, 'std': 10.968370411852126, 'min': 83.2918025077951, 'max': 133.93380274432675, 'skewness': -0.07319630419864273, 'kurtosis': -0.375284595953965, 'missing_percentage': 0.0}}
2024-08-05 23:42:47,501 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:42:47,501 - metrics.computations.computations_analyzer - ERROR - Error detecting seasonality for metric 12: 'dict' object has no attribute 'strength'
2024-08-05 23:42:47,931 - metrics.computations.computations_analyzer - INFO - Detected trend change point for metric 12
2024-08-05 23:42:47,936 - metrics.computations.permanent_computations - ERROR - Unexpected error saving analysis results for metric 12: string indices must be integers
2024-08-05 23:42:47,936 - metrics.computations.permanent_computations - INFO - Analysis completed for metric 12
2024-08-05 23:42:47,936 - metrics.computations.permanent_computations - INFO - Starting forecasting for metric 12
2024-08-05 23:42:47,939 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:42:47,939 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:42:47,940 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:47,940 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:47,944 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:42:47,951 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:47,951 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:47,954 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:47,954 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:47,956 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:47,957 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:47,959 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:49,705 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:42:49,707 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:49,709 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:49,709 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:49,712 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:49,712 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:49,714 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:49,716 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:49,716 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:49,719 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:49,734 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 109.46478136533182, 'median': 109.78447869352485, 'std': 10.968370411852126, 'min': 83.2918025077951, 'max': 133.93380274432675, 'skewness': -0.07319630419864273, 'kurtosis': -0.375284595953965, 'missing_percentage': 0.0}}
2024-08-05 23:42:49,736 - metrics.computations.computations_forecaster - WARNING - SARIMA model not recommended for metric 12. Using it anyway.
2024-08-05 23:42:52,256 - metrics.computations.computations_forecaster - INFO - Generated SARIMA forecast for metric 12
2024-08-05 23:42:52,257 - metrics.computations.computations_forecaster - WARNING - Prophet model not recommended for metric 12. Using it anyway.
2024-08-05 23:42:52,257 - prophet - DEBUG - Trying to load backend: CMDSTANPY
2024-08-05 23:42:52,258 - prophet - DEBUG - Loaded stan backend: CMDSTANPY
2024-08-05 23:42:52,263 - prophet - INFO - Disabling daily seasonality. Run prophet with daily_seasonality=True to override this.
2024-08-05 23:42:52,273 - cmdstanpy - DEBUG - input tempfile: /tmp/tmpsp01_789/xa4ju8sv.json
2024-08-05 23:42:52,317 - cmdstanpy - DEBUG - input tempfile: /tmp/tmpsp01_789/bxb00q9a.json
2024-08-05 23:42:52,318 - cmdstanpy - DEBUG - idx 0
2024-08-05 23:42:52,318 - cmdstanpy - DEBUG - running CmdStan, num_threads: None
2024-08-05 23:42:52,318 - cmdstanpy - DEBUG - CmdStan args: ['/home/nadeemramli/.pyenv/versions/3.10.7/lib/python3.10/site-packages/prophet/stan_model/prophet_model.bin', 'random', 'seed=94387', 'data', 'file=/tmp/tmpsp01_789/xa4ju8sv.json', 'init=/tmp/tmpsp01_789/bxb00q9a.json', 'output', 'file=/tmp/tmpsp01_789/prophet_modelh5vqoysx/prophet_model-20240805234252.csv', 'method=optimize', 'algorithm=lbfgs', 'iter=10000']
2024-08-05 23:42:52,319 - cmdstanpy - INFO - Chain [1] start processing
2024-08-05 23:42:52,342 - cmdstanpy - INFO - Chain [1] done processing
2024-08-05 23:42:52,474 - metrics.computations.computations_forecaster - INFO - Generated Prophet forecast for metric 12
2024-08-05 23:42:52,475 - metrics.computations.permanent_computations - ERROR - Error in forecasting for metric 12: string indices must be integers
2024-08-05 23:42:52,475 - metrics.computations.permanent_computations - INFO - Starting anomaly detection for metric 12
2024-08-05 23:42:52,478 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:42:52,478 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:42:52,478 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:52,479 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:52,483 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:42:52,489 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:52,489 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:52,492 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:52,492 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:52,494 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:52,494 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:52,497 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:54,238 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:42:54,240 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:54,241 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:54,242 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:54,244 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:54,244 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:54,247 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:54,249 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:54,249 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:54,252 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:54,277 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 109.46478136533182, 'median': 109.78447869352485, 'std': 10.968370411852126, 'min': 83.2918025077951, 'max': 133.93380274432675, 'skewness': -0.07319630419864273, 'kurtosis': -0.375284595953965, 'missing_percentage': 0.0}}
2024-08-05 23:42:54,279 - metrics.computations.computations_anomalies - INFO - Initialized AnomalyDetector for metric 12
2024-08-05 23:42:54,279 - metrics.computations.computations_anomalies - INFO - Seasonality period: 2
2024-08-05 23:42:54,279 - metrics.computations.computations_anomalies - INFO - Window size: 1000
2024-08-05 23:42:54,279 - metrics.computations.computations_anomalies - INFO - Base threshold: 5.0
2024-08-05 23:42:54,279 - metrics.computations.computations_anomalies - INFO - Context window: 15
2024-08-05 23:42:54,279 - metrics.computations.computations_anomalies - INFO - Global threshold: 5.0
2024-08-05 23:42:54,279 - metrics.computations.computations_anomalies - INFO - Starting anomaly detection for metric 12
2024-08-05 23:42:54,279 - metrics.computations.computations_anomalies - INFO - Data shape: (1000, 2)
2024-08-05 23:42:54,281 - metrics.computations.computations_anomalies - INFO - Data summary: count    1000.000000
mean      109.464781
std        10.968370
min        83.291803
25%       102.227481
50%       109.784479
75%       116.945859
max       133.933803
Name: value, dtype: float64
2024-08-05 23:42:54,285 - metrics.computations.computations_anomalies - INFO - Deseasonalized data summary: count    1000.000000
mean      109.458604
std        10.971128
min        83.291803
25%       102.203656
50%       109.784479
75%       116.945859
max       133.933803
Name: value, dtype: float64
2024-08-05 23:42:54,287 - metrics.computations.computations_anomalies - INFO - Modified z-scores range: 0.24892520433046914 to 0.24892520433046914
2024-08-05 23:42:54,289 - metrics.computations.computations_anomalies - INFO - Modified z-scores summary: count    1.000000
mean     0.248925
std           NaN
min      0.248925
25%      0.248925
50%      0.248925
75%      0.248925
max      0.248925
Name: value, dtype: float64
2024-08-05 23:42:54,290 - metrics.computations.computations_anomalies - INFO - Adaptive threshold range: 6.0599388295715 to 6.0599388295715
2024-08-05 23:42:54,292 - metrics.computations.computations_anomalies - INFO - Adaptive threshold summary: count    1.000000
mean     6.059939
std           NaN
min      6.059939
25%      6.059939
50%      6.059939
75%      6.059939
max      6.059939
Name: value, dtype: float64
2024-08-05 23:42:54,292 - metrics.computations.computations_anomalies - INFO - Contextual z-scores range: nan to nan
2024-08-05 23:42:54,294 - metrics.computations.computations_anomalies - INFO - Contextual z-scores summary: count    0.0
mean     NaN
std      NaN
min      NaN
25%      NaN
50%      NaN
75%      NaN
max      NaN
Name: value, dtype: float64
2024-08-05 23:42:54,294 - metrics.computations.computations_anomalies - INFO - Global mean: 109.45860447611892, Global std: 10.971128183715376
2024-08-05 23:42:54,295 - metrics.computations.computations_anomalies - INFO - Number of anomalies detected: 0
2024-08-05 23:42:54,297 - metrics.computations.computations_anomalies - INFO - Detected 0 anomalies for metric 12
2024-08-05 23:42:54,301 - metrics.computations.permanent_computations - ERROR - Error in anomaly detection for metric 12: 'anomalies'
2024-08-05 23:42:54,301 - metrics.computations.permanent_computations - INFO - Starting relationship analysis for metric 12
2024-08-05 23:42:54,305 - metrics.computations.data_preparation - INFO - Loaded metric 12 for tenant 6 and project 6
2024-08-05 23:42:54,305 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 12
2024-08-05 23:42:54,306 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:54,307 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 12 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:42:54,312 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 12
2024-08-05 23:42:54,323 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:54,324 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:42:54,328 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:54,328 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:42:54,332 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:54,332 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:42:54,336 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:42:56,140 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 12
2024-08-05 23:42:56,142 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:42:56,144 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:42:56,144 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:42:56,146 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:56,147 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:42:56,149 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  101.998663          6
2023-01-02  100.227470          6
2023-01-03  127.912045          6
2023-01-04  121.666628          6
2023-01-05  103.217179          6
2024-08-05 23:42:56,151 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.37249584856878226, Timeliness: nan
2024-08-05 23:42:56,151 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.7498616189594
2024-08-05 23:42:56,154 - metrics.computations.data_preparation - INFO - Data quality score: 45.7498616189594
2024-08-05 23:42:56,168 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 12, 'tenant_id': 6, 'project_id': 6, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.7498616189594, 'outliers_handled': True, 'profile': {'mean': 109.46478136533182, 'median': 109.78447869352485, 'std': 10.968370411852126, 'min': 83.2918025077951, 'max': 133.93380274432675, 'skewness': -0.07319630419864273, 'kurtosis': -0.375284595953965, 'missing_percentage': 0.0}}
2024-08-05 23:42:56,170 - metrics.computations.permanent_computations - ERROR - Error in relationship analysis for metric 12: RelationshipAnalyzer.analyze_relationships() missing 1 required positional argument: 'other_metric_ids'
2024-08-05 23:42:56,170 - metrics.computations.permanent_computations - INFO - Generating report for metric 12
2024-08-05 23:42:56,172 - metrics.computations.permanent_computations - ERROR - Error generating or saving report for metric 12: -1
2024-08-05 23:42:56,172 - metrics.computations.permanent_computations - INFO - All computations completed for metric 12
2024-08-05 23:42:56,176 - metrics.computations.permanent_computations - ERROR - Error storing results for metric 11: -1
2024-08-05 23:42:56,177 - metrics.computations.permanent_computations - ERROR - Error storing results for metric 12: -1
2024-08-05 23:42:56,352 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Teardown completed
```

## test_relationships_robustness (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
Status: failure
Duration: 27.882 seconds

### Failure
```
Traceback (most recent call last):
  File "/home/nadeemramli/workspace/github.com/nadeemramli/mapping-of-metrics/metric-map-app/backend/metricMapAPI/metrics/tests/test_permanent_computations/test_permanent_computations_robustness.py", line 227, in test_relationships_robustness
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
Relationship Analyzer Computation time: 3.675377130508423 seconds
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
2024-08-05 23:42:56,368 - metrics - DEBUG - Starting test: test_relationships_robustness (metrics.tests.test_permanent_computations.test_permanent_computations_robustness.TestComputationsRobustness)
2024-08-05 23:42:56,373 - django.db.backends.schema - DEBUG - CREATE TABLE "django_migrations" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:56,386 - django.db.backends.schema - DEBUG - CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
2024-08-05 23:42:56,390 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params None)
2024-08-05 23:42:56,395 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL, "codename" varchar(100) NOT NULL); (params None)
2024-08-05 23:42:56,400 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(80) NOT NULL UNIQUE); (params None)
2024-08-05 23:42:56,404 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_group_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:42:56,411 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NOT NULL, "is_superuser" boolean NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:56,416 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:42:56,418 - django.db.backends.schema - DEBUG - CREATE TABLE "auth_user_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "user_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:42:56,425 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename"); (params None)
2024-08-05 23:42:56,427 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,428 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id"); (params None)
2024-08-05 23:42:56,430 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_name_a6ea08ec_like" ON "auth_group" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:56,432 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id"); (params None)
2024-08-05 23:42:56,435 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,436 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,437 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id"); (params None)
2024-08-05 23:42:56,439 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id"); (params None)
2024-08-05 23:42:56,442 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_username_6821ab7c_like" ON "auth_user" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:42:56,443 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id"); (params None)
2024-08-05 23:42:56,445 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,447 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,448 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id"); (params None)
2024-08-05 23:42:56,450 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id"); (params None)
2024-08-05 23:42:56,452 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id"); (params None)
2024-08-05 23:42:56,455 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,456 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,456 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id"); (params None)
2024-08-05 23:42:56,458 - django.db.backends.schema - DEBUG - CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id"); (params None)
2024-08-05 23:42:56,467 - django.db.backends.schema - DEBUG - CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "action_time" timestamp with time zone NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL, "user_id" integer NOT NULL); (params None)
2024-08-05 23:42:56,471 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,472 - django.db.backends.schema - DEBUG - ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,473 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id"); (params None)
2024-08-05 23:42:56,476 - django.db.backends.schema - DEBUG - CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id"); (params None)
2024-08-05 23:42:56,493 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" ALTER COLUMN "name" DROP NOT NULL; (params None)
2024-08-05 23:42:56,499 - django.db.backends.schema - DEBUG - ALTER TABLE "django_content_type" DROP COLUMN "name" CASCADE; (params None)
2024-08-05 23:42:56,507 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_permission" ALTER COLUMN "name" TYPE varchar(255); (params None)
2024-08-05 23:42:56,513 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "email" TYPE varchar(254); (params None)
2024-08-05 23:42:56,524 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_login" DROP NOT NULL; (params None)
2024-08-05 23:42:56,537 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "username" TYPE varchar(150); (params None)
2024-08-05 23:42:56,546 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "last_name" TYPE varchar(150); (params None)
2024-08-05 23:42:56,551 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_group" ALTER COLUMN "name" TYPE varchar(150); (params None)
2024-08-05 23:42:56,565 - django.db.backends.schema - DEBUG - ALTER TABLE "auth_user" ALTER COLUMN "first_name" TYPE varchar(150); (params None)
2024-08-05 23:42:56,594 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_client" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "schema_name" varchar(63) NOT NULL UNIQUE, "name" varchar(100) NOT NULL, "created_on" date NOT NULL); (params None)
2024-08-05 23:42:56,601 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_category" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,605 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dashboard" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "layout" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,613 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_domain" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "domain" varchar(253) NOT NULL UNIQUE, "is_primary" boolean NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,623 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "type" varchar(50) NOT NULL, "confidence" varchar(50) NOT NULL, "value_type" varchar(20) NOT NULL, "rhythm" varchar(20) NOT NULL, "description" text NOT NULL, "hypothesis" text NOT NULL, "technical_description" text NOT NULL, "last_updated" timestamp with time zone NOT NULL, "source" varchar(100) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL, "category_id" bigint NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,631 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_historicaldata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "value" double precision NOT NULL, "forecasted_value" double precision NULL, "anomaly_detected" boolean NOT NULL, "trend_component" varchar(50) NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,638 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_forecast" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "forecast_date" date NOT NULL, "forecast_value" double precision NOT NULL, "model_used" varchar(100) NOT NULL, "accuracy" double precision NULL, "confidence_interval" jsonb NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,648 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "status" varchar(50) NOT NULL, "results" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,653 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_experiment_metrics" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "experiment_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,662 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_connection" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "relationship" varchar(100) NOT NULL, "correlation_coefficient" double precision NULL, "tenant_id" bigint NOT NULL, "from_metric_id" bigint NOT NULL, "to_metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,672 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_anomaly" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "detection_date" date NOT NULL, "anomaly_value" double precision NOT NULL, "anomaly_score" double precision NOT NULL, "notes" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,684 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_actionremark" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NULL, "description" text NOT NULL, "impact" text NOT NULL, "tenant_id" bigint NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,699 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_project" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "created_on" date NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,710 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_report" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "configuration" jsonb NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,724 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tag" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "project_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,736 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metric_tags" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "metric_id" bigint NOT NULL, "tag_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,750 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_target" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "remarks" text NOT NULL, "target_kpi" varchar(100) NOT NULL, "target_date" date NULL, "target_value" double precision NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,766 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trend" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "trend_type" varchar(50) NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "trend_value" double precision NOT NULL, "notes" text NOT NULL, "metric_id" bigint NOT NULL, "tenant_id" bigint NOT NULL); (params None)
2024-08-05 23:42:56,771 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_schema_name_87d6fbb5_like" ON "metrics_client" ("schema_name" varchar_pattern_ops); (params None)
2024-08-05 23:42:56,773 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_category" ADD CONSTRAINT "metrics_category_tenant_id_67d98cc6_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,774 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_tenant_id_67d98cc6" ON "metrics_category" ("tenant_id"); (params None)
2024-08-05 23:42:56,776 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ADD CONSTRAINT "metrics_dashboard_tenant_id_50099a7d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,777 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_tenant_id_50099a7d" ON "metrics_dashboard" ("tenant_id"); (params None)
2024-08-05 23:42:56,779 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_domain" ADD CONSTRAINT "metrics_domain_tenant_id_259fb21f_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,780 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_domain_bdc97b86_like" ON "metrics_domain" ("domain" varchar_pattern_ops); (params None)
2024-08-05 23:42:56,783 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_is_primary_ac9d2eaf" ON "metrics_domain" ("is_primary"); (params None)
2024-08-05 23:42:56,785 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_domain_tenant_id_259fb21f" ON "metrics_domain" ("tenant_id"); (params None)
2024-08-05 23:42:56,787 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_category_id_8793f683_fk_metrics_category_id" FOREIGN KEY ("category_id") REFERENCES "metrics_category" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,788 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_9606b577_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,788 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_category_id_8793f683" ON "metrics_metric" ("category_id"); (params None)
2024-08-05 23:42:56,791 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tenant_id_9606b577" ON "metrics_metric" ("tenant_id"); (params None)
2024-08-05 23:42:56,794 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_tenant_id_438c5ad4_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,795 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD CONSTRAINT "metrics_historicaldata_metric_id_3f9e8174_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,796 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_tenant_id_438c5ad4" ON "metrics_historicaldata" ("tenant_id"); (params None)
2024-08-05 23:42:56,798 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_metric_id_3f9e8174" ON "metrics_historicaldata" ("metric_id"); (params None)
2024-08-05 23:42:56,800 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_tenant_id_92d37185_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,801 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD CONSTRAINT "metrics_forecast_metric_id_e05f23a8_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,802 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_tenant_id_92d37185" ON "metrics_forecast" ("tenant_id"); (params None)
2024-08-05 23:42:56,804 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_metric_id_e05f23a8" ON "metrics_forecast" ("metric_id"); (params None)
2024-08-05 23:42:56,807 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD CONSTRAINT "metrics_experiment_tenant_id_10fa364a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,808 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_tenant_id_10fa364a" ON "metrics_experiment" ("tenant_id"); (params None)
2024-08-05 23:42:56,810 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_metri_experiment_id_metric_id_a9d54b29_uniq" UNIQUE ("experiment_id", "metric_id"); (params None)
2024-08-05 23:42:56,812 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_experiment_id_372c6b59_fk_metrics_e" FOREIGN KEY ("experiment_id") REFERENCES "metrics_experiment" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,814 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment_metrics" ADD CONSTRAINT "metrics_experiment_m_metric_id_c8f84167_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,815 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_experiment_id_372c6b59" ON "metrics_experiment_metrics" ("experiment_id"); (params None)
2024-08-05 23:42:56,817 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_metrics_metric_id_c8f84167" ON "metrics_experiment_metrics" ("metric_id"); (params None)
2024-08-05 23:42:56,819 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_2e1e5750_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,821 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_from_metric_id_33b50521_fk_metrics_metric_id" FOREIGN KEY ("from_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,822 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_to_metric_id_94489c1c_fk_metrics_metric_id" FOREIGN KEY ("to_metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,823 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_tenant_id_2e1e5750" ON "metrics_connection" ("tenant_id"); (params None)
2024-08-05 23:42:56,825 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_from_metric_id_33b50521" ON "metrics_connection" ("from_metric_id"); (params None)
2024-08-05 23:42:56,827 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_to_metric_id_94489c1c" ON "metrics_connection" ("to_metric_id"); (params None)
2024-08-05 23:42:56,829 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_tenant_id_9e474130_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,830 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD CONSTRAINT "metrics_anomaly_metric_id_1b3c3295_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,831 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_tenant_id_9e474130" ON "metrics_anomaly" ("tenant_id"); (params None)
2024-08-05 23:42:56,833 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_metric_id_1b3c3295" ON "metrics_anomaly" ("metric_id"); (params None)
2024-08-05 23:42:56,836 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_tenant_id_86ffa3a9_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,837 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD CONSTRAINT "metrics_actionremark_metric_id_c1b270f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,837 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_tenant_id_86ffa3a9" ON "metrics_actionremark" ("tenant_id"); (params None)
2024-08-05 23:42:56,840 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_metric_id_c1b270f2" ON "metrics_actionremark" ("metric_id"); (params None)
2024-08-05 23:42:56,841 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_project" ADD CONSTRAINT "metrics_project_tenant_id_db4a1170_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,842 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_tenant_id_db4a1170" ON "metrics_project" ("tenant_id"); (params None)
2024-08-05 23:42:56,844 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD CONSTRAINT "metrics_report_tenant_id_d1cf4812_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,845 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_tenant_id_d1cf4812" ON "metrics_report" ("tenant_id"); (params None)
2024-08-05 23:42:56,847 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_name_project_id_2d57d4da_uniq" UNIQUE ("name", "project_id"); (params None)
2024-08-05 23:42:56,850 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_project_id_b7ac5c8e_fk_metrics_project_id" FOREIGN KEY ("project_id") REFERENCES "metrics_project" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,851 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tag" ADD CONSTRAINT "metrics_tag_tenant_id_c286653b_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,852 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_project_id_b7ac5c8e" ON "metrics_tag" ("project_id"); (params None)
2024-08-05 23:42:56,854 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_tenant_id_c286653b" ON "metrics_tag" ("tenant_id"); (params None)
2024-08-05 23:42:56,856 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_tag_id_a8e1a165_uniq" UNIQUE ("metric_id", "tag_id"); (params None)
2024-08-05 23:42:56,858 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_metric_id_b2a068f2_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,859 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric_tags" ADD CONSTRAINT "metrics_metric_tags_tag_id_61869f56_fk_metrics_tag_id" FOREIGN KEY ("tag_id") REFERENCES "metrics_tag" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,861 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_metric_id_b2a068f2" ON "metrics_metric_tags" ("metric_id"); (params None)
2024-08-05 23:42:56,863 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_tags_tag_id_61869f56" ON "metrics_metric_tags" ("tag_id"); (params None)
2024-08-05 23:42:56,866 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,867 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" ADD CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,868 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_metric_id_181e8748" ON "metrics_target" ("metric_id"); (params None)
2024-08-05 23:42:56,869 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_tenant_id_118eb54a" ON "metrics_target" ("tenant_id"); (params None)
2024-08-05 23:42:56,871 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_metric_id_25179b98_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,872 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD CONSTRAINT "metrics_trend_tenant_id_4cb1485d_fk_metrics_client_id" FOREIGN KEY ("tenant_id") REFERENCES "metrics_client" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:56,874 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_metric_id_25179b98" ON "metrics_trend" ("metric_id"); (params None)
2024-08-05 23:42:56,876 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_tenant_id_4cb1485d" ON "metrics_trend" ("tenant_id"); (params None)
2024-08-05 23:42:57,035 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_actionremark_date_33d1e0bd" ON "metrics_actionremark" ("date"); (params None)
2024-08-05 23:42:57,048 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_anomaly_detection_date_ee75a187" ON "metrics_anomaly" ("detection_date"); (params None)
2024-08-05 23:42:57,059 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c" ON "metrics_category" ("name"); (params None)
2024-08-05 23:42:57,062 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_category_name_a4b75e5c_like" ON "metrics_category" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:57,074 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d" ON "metrics_client" ("name"); (params None)
2024-08-05 23:42:57,076 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_client_name_dcd9893d_like" ON "metrics_client" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:57,089 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET DEFAULT '{}'; (params None)
2024-08-05 23:42:57,090 - django.db.backends.schema - DEBUG - UPDATE "metrics_dashboard" SET "layout" = '{}' WHERE "layout" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:42:57,091 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" SET NOT NULL; (params None)
2024-08-05 23:42:57,091 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dashboard" ALTER COLUMN "layout" DROP DEFAULT; (params None)
2024-08-05 23:42:57,101 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e" ON "metrics_dashboard" ("name"); (params None)
2024-08-05 23:42:57,104 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dashboard_name_ab41129e_like" ON "metrics_dashboard" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:57,116 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_end_date_31af6c05" ON "metrics_experiment" ("end_date"); (params None)
2024-08-05 23:42:57,127 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7" ON "metrics_experiment" ("name"); (params None)
2024-08-05 23:42:57,129 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_name_d1b9e1f7_like" ON "metrics_experiment" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:57,142 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET DEFAULT '{}'; (params None)
2024-08-05 23:42:57,143 - django.db.backends.schema - DEBUG - UPDATE "metrics_experiment" SET "results" = '{}' WHERE "results" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:42:57,144 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" SET NOT NULL; (params None)
2024-08-05 23:42:57,144 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "results" DROP DEFAULT; (params None)
2024-08-05 23:42:57,154 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_start_date_a6deff13" ON "metrics_experiment" ("start_date"); (params None)
2024-08-05 23:42:57,166 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET DEFAULT '{}'; (params None)
2024-08-05 23:42:57,167 - django.db.backends.schema - DEBUG - UPDATE "metrics_forecast" SET "confidence_interval" = '{}' WHERE "confidence_interval" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:42:57,168 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" SET NOT NULL; (params None)
2024-08-05 23:42:57,168 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "confidence_interval" DROP DEFAULT; (params None)
2024-08-05 23:42:57,180 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_forecast_forecast_date_71750ae8" ON "metrics_forecast" ("forecast_date"); (params None)
2024-08-05 23:42:57,192 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_date_f27e0e6a" ON "metrics_historicaldata" ("date"); (params None)
2024-08-05 23:42:57,204 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_last_updated_3e38a760" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:42:57,217 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5" ON "metrics_metric" ("name"); (params None)
2024-08-05 23:42:57,221 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_name_9ab0aad5_like" ON "metrics_metric" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:57,234 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e" ON "metrics_metric" ("type"); (params None)
2024-08-05 23:42:57,237 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_type_8557d31e_like" ON "metrics_metric" ("type" varchar_pattern_ops); (params None)
2024-08-05 23:42:57,257 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80" ON "metrics_project" ("name"); (params None)
2024-08-05 23:42:57,260 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_project_name_612cab80_like" ON "metrics_project" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:57,272 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET DEFAULT '{}'; (params None)
2024-08-05 23:42:57,273 - django.db.backends.schema - DEBUG - UPDATE "metrics_report" SET "configuration" = '{}' WHERE "configuration" IS NULL; SET CONSTRAINTS ALL IMMEDIATE; (params None)
2024-08-05 23:42:57,274 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" SET NOT NULL; (params None)
2024-08-05 23:42:57,274 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "configuration" DROP DEFAULT; (params None)
2024-08-05 23:42:57,285 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34" ON "metrics_report" ("name"); (params None)
2024-08-05 23:42:57,288 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_name_4fc3ba34_like" ON "metrics_report" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:57,300 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a" ON "metrics_tag" ("name"); (params None)
2024-08-05 23:42:57,303 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1748f53a_like" ON "metrics_tag" ("name" varchar_pattern_ops); (params None)
2024-08-05 23:42:57,314 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_target_target_date_81507ff5" ON "metrics_target" ("target_date"); (params None)
2024-08-05 23:42:57,328 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_end_date_8444ef38" ON "metrics_trend" ("end_date"); (params None)
2024-08-05 23:42:57,340 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trend_start_date_7b1a850f" ON "metrics_trend" ("start_date"); (params None)
2024-08-05 23:42:57,352 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_act_metric__be3429_idx" ON "metrics_actionremark" ("metric_id", "date"); (params None)
2024-08-05 23:42:57,364 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ano_metric__84982d_idx" ON "metrics_anomaly" ("metric_id", "detection_date"); (params None)
2024-08-05 23:42:57,378 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_con_from_me_9411ea_idx" ON "metrics_connection" ("from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:42:57,391 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_exp_start_d_04716a_idx" ON "metrics_experiment" ("start_date", "end_date"); (params None)
2024-08-05 23:42:57,404 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_for_metric__4c9ae2_idx" ON "metrics_forecast" ("metric_id", "forecast_date"); (params None)
2024-08-05 23:42:57,416 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_his_metric__a2923a_idx" ON "metrics_historicaldata" ("metric_id", "date"); (params None)
2024-08-05 23:42:57,430 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_name_c9d100_idx" ON "metrics_metric" ("name", "type"); (params None)
2024-08-05 23:42:57,444 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_7984a6_idx" ON "metrics_metric" ("last_updated"); (params None)
2024-08-05 23:42:57,456 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tag_name_1bdb27_idx" ON "metrics_tag" ("name", "project_id"); (params None)
2024-08-05 23:42:57,470 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tar_metric__234682_idx" ON "metrics_target" ("metric_id", "target_date"); (params None)
2024-08-05 23:42:57,483 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tre_metric__d386bb_idx" ON "metrics_trend" ("metric_id", "start_date", "end_date"); (params None)
2024-08-05 23:42:57,497 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_con_from_me_9411ea_idx"; (params None)
2024-08-05 23:42:57,508 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:42:57,509 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:42:57,638 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD CONSTRAINT "metrics_connection_tenant_id_from_metric_id_aa131d91_uniq" UNIQUE ("tenant_id", "from_metric_id", "to_metric_id"); (params None)
2024-08-05 23:42:57,641 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_connection_project_id_4c1b22ec" ON "metrics_connection" ("project_id"); (params None)
2024-08-05 23:42:57,656 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id" IMMEDIATE; ALTER TABLE "metrics_connection" DROP CONSTRAINT "metrics_connection_project_id_4c1b22ec_fk_metrics_project_id"; (params None)
2024-08-05 23:42:57,656 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "project_id" CASCADE; (params None)
2024-08-05 23:42:57,667 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metric_project_id_36bdbe46_fk_metrics_project_id" IMMEDIATE; (params None)
2024-08-05 23:42:57,668 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:42:57,680 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:42:57,683 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metric_project_id_36bdbe46" ON "metrics_metric" ("project_id"); (params None)
2024-08-05 23:42:57,688 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_correlation" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "lag" integer NOT NULL, "pearson_correlation" double precision NOT NULL, "spearman_correlation" double precision NOT NULL); (params None)
2024-08-05 23:42:57,693 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:57,702 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_dataqualityscore" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_entry" varchar(255) NOT NULL, "completeness_score" double precision NOT NULL, "accuracy_score" double precision NOT NULL, "consistency_score" double precision NOT NULL, "timeliness_score" double precision NOT NULL, "overall_score" double precision NOT NULL); (params None)
2024-08-05 23:42:57,707 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_impactanalysis" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "before_value" double precision NOT NULL, "after_value" double precision NOT NULL, "percentage_change" double precision NOT NULL, "confidence" double precision NOT NULL, "artifact_link" varchar(200) NOT NULL); (params None)
2024-08-05 23:42:57,711 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_insight" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "title" varchar(200) NOT NULL, "content" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:57,718 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metricmetadata" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "data_source" varchar(100) NOT NULL, "source_url" varchar(200) NOT NULL, "rhythm" varchar(20) NOT NULL, "last_updated" timestamp with time zone NOT NULL, "technical_description" text NOT NULL, "description" text NOT NULL, "artifacts_url" varchar(200) NOT NULL, "hypothesis" text NOT NULL, "confidence" varchar(20) NOT NULL, "position_x" double precision NOT NULL, "position_y" double precision NOT NULL); (params None)
2024-08-05 23:42:57,725 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_metrictarget" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "target_kpi" varchar(100) NOT NULL, "target_remarks" text NOT NULL, "target_date" date NULL, "target_value" double precision NULL); (params None)
2024-08-05 23:42:57,731 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_strategy" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "estimated_time" interval NOT NULL, "artifacts_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:57,737 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_tacticalsolution" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "description" text NOT NULL, "artifact_url" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:57,744 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_team" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "description" text NOT NULL, "created_at" timestamp with time zone NOT NULL, "updated_at" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:42:57,750 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_technicalindicator" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL, "stochastic_value" double precision NOT NULL, "rsi_value" double precision NOT NULL, "percent_change" double precision NOT NULL, "moving_average" double precision NOT NULL); (params None)
2024-08-05 23:42:57,755 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_timedimension" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" date NOT NULL UNIQUE, "day" integer NOT NULL, "day_of_week" integer NOT NULL, "day_name" varchar(10) NOT NULL, "week" integer NOT NULL, "month" integer NOT NULL, "month_name" varchar(10) NOT NULL, "quarter" integer NOT NULL, "year" integer NOT NULL, "is_weekend" boolean NOT NULL, "is_holiday" boolean NOT NULL); (params None)
2024-08-05 23:42:57,761 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_userprofile" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY); (params None)
2024-08-05 23:42:57,782 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_metric_id_181e8748_fk_metrics_metric_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_metric_id_181e8748_fk_metrics_metric_id"; (params None)
2024-08-05 23:42:57,783 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "metric_id" CASCADE; (params None)
2024-08-05 23:42:57,797 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_target_tenant_id_118eb54a_fk_metrics_client_id" IMMEDIATE; ALTER TABLE "metrics_target" DROP CONSTRAINT "metrics_target_tenant_id_118eb54a_fk_metrics_client_id"; (params None)
2024-08-05 23:42:57,798 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_target" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:42:57,809 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_name_c9d100_idx"; (params None)
2024-08-05 23:42:57,819 - django.db.backends.schema - DEBUG - DROP INDEX IF EXISTS "metrics_met_last_up_7984a6_idx"; (params None)
2024-08-05 23:42:57,830 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" RENAME COLUMN "description" TO "summary"; (params None)
2024-08-05 23:42:57,843 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq"; (params None)
2024-08-05 23:42:57,853 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" DROP COLUMN "correlation_coefficient" CASCADE; (params None)
2024-08-05 23:42:57,863 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" DROP COLUMN "results" CASCADE; (params None)
2024-08-05 23:42:57,872 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "anomaly_detected" CASCADE; (params None)
2024-08-05 23:42:57,885 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "forecasted_value" CASCADE; (params None)
2024-08-05 23:42:57,895 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" DROP COLUMN "trend_component" CASCADE; (params None)
2024-08-05 23:42:57,905 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "importance" varchar(20) DEFAULT 'MEDIUM' NOT NULL; (params None)
2024-08-05 23:42:57,906 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "importance" DROP DEFAULT; (params None)
2024-08-05 23:42:57,915 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:42:57.915609+00:00' NOT NULL; (params None)
2024-08-05 23:42:57,916 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:42:57,927 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "anomaly_type" varchar(20) DEFAULT 'IGNORE' NOT NULL; (params None)
2024-08-05 23:42:57,928 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "anomaly_type" DROP DEFAULT; (params None)
2024-08-05 23:42:57,938 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ADD COLUMN "quality" varchar(20) DEFAULT 'LOW' NOT NULL; (params None)
2024-08-05 23:42:57,939 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_anomaly" ALTER COLUMN "quality" DROP DEFAULT; (params None)
2024-08-05 23:42:57,950 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "impact_description" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:42:57,951 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "impact_description" DROP DEFAULT; (params None)
2024-08-05 23:42:57,963 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "objective" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:42:57,964 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "objective" DROP DEFAULT; (params None)
2024-08-05 23:42:57,974 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_date" date NULL; (params None)
2024-08-05 23:42:57,984 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_files" varchar(100) NULL; (params None)
2024-08-05 23:42:57,994 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_summary" text DEFAULT '' NOT NULL; (params None)
2024-08-05 23:42:57,995 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "result_summary" DROP DEFAULT; (params None)
2024-08-05 23:42:58,007 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "result_value" double precision NULL; (params None)
2024-08-05 23:42:58,017 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "title" varchar(200) DEFAULT '2024-08-05 23:42:58.017623+00:00' NOT NULL; (params None)
2024-08-05 23:42:58,018 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "title" DROP DEFAULT; (params None)
2024-08-05 23:42:58,029 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "variance" double precision NULL; (params None)
2024-08-05 23:42:58,039 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ADD COLUMN "forecast_id" bigint NULL CONSTRAINT "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" REFERENCES "metrics_forecast"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_historicalda_forecast_id_29590c29_fk_metrics_f" IMMEDIATE; (params None)
2024-08-05 23:42:58,052 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_actionremark" ALTER COLUMN "impact" TYPE varchar(20) USING "impact"::varchar(20); (params None)
2024-08-05 23:42:58,143 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ALTER COLUMN "status" TYPE varchar(20); (params None)
2024-08-05 23:42:58,263 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric1_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric1_id_6e1c2404_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,276 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "metric2_id" bigint NOT NULL CONSTRAINT "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_metric2_id_f2cc46dd_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,287 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_correlation_tenant_id_a00a5169_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,295 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_groups" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "group_id" integer NOT NULL); (params None)
2024-08-05 23:42:58,314 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_tenant_id_02b7403c_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,332 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_customuser_user_permissions" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "customuser_id" bigint NOT NULL, "permission_id" integer NOT NULL); (params None)
2024-08-05 23:42:58,352 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_tenant_id_8e9f296d_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:42:58,369 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "experiment_id" bigint NOT NULL CONSTRAINT "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" REFERENCES "metrics_experiment"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalys_experiment_id_1beae7fe_fk_metrics_e" IMMEDIATE; (params None)
2024-08-05 23:42:58,389 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_metric_id_f4b9eeb6_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,406 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_impactanalysis" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_impactanalysis_tenant_id_126ca20d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,564 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_metric_id_26d3a9d8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,582 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_tenant_id_724d7d85_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,602 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_insight" ADD COLUMN "user_id" bigint NOT NULL CONSTRAINT "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_insight_user_id_83d421e1_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,622 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "data_quality_score_id" bigint NULL UNIQUE CONSTRAINT "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" REFERENCES "metrics_dataqualityscore"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetada_data_quality_score_i_dae35c78_fk_metrics_d" IMMEDIATE; (params None)
2024-08-05 23:42:58,644 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "metric_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_metric_id_1d44b650_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,668 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_tenant_id_3277f967_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,689 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_metric_id_7876e2c8_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,710 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metrictarget" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metrictarget_tenant_id_b26a17f8_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,731 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_tenant_id_1323395e_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,753 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_metric_id_9887ffa4_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:42:58,775 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_tacticalsolution" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_tacticalsolu_tenant_id_cf9028f0_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:42:58,798 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_team" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_team_tenant_id_3a14c47d_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,820 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_strategy" ADD COLUMN "team_id" bigint NOT NULL CONSTRAINT "metrics_strategy_team_id_f1781500_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_strategy_team_id_f1781500_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,842 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metricmetadata" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_metricmetadata_team_id_f140658d_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,865 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_customuser_team_id_4c4ffc18_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,889 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_experiment" ADD COLUMN "team_id" bigint NULL CONSTRAINT "metrics_experiment_team_id_537107e3_fk_metrics_team_id" REFERENCES "metrics_team"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_experiment_team_id_537107e3_fk_metrics_team_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,911 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "metric_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_metric_id_3e2eead6_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:42:58,935 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_technicalindicator" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_technicalind_tenant_id_f4de3b44_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:42:58,958 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_timedimension" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_timedimension_tenant_id_f375bb45_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:58,981 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "tenant_id" bigint NOT NULL CONSTRAINT "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_tenant_id_cca71dae_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:42:59,132 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_userprofile" ADD COLUMN "user_id" bigint NOT NULL UNIQUE CONSTRAINT "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" REFERENCES "metrics_customuser"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_userprofile_user_id_c7dada8d_fk_metrics_customuser_id" IMMEDIATE; (params None)
2024-08-05 23:42:59,136 - django.db.backends.schema - DEBUG - DROP TABLE "metrics_target" CASCADE; (params None)
2024-08-05 23:42:59,155 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "confidence" CASCADE; (params None)
2024-08-05 23:42:59,174 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "description" CASCADE; (params None)
2024-08-05 23:42:59,193 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "hypothesis" CASCADE; (params None)
2024-08-05 23:42:59,212 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "last_updated" CASCADE; (params None)
2024-08-05 23:42:59,231 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_x" CASCADE; (params None)
2024-08-05 23:42:59,251 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "position_y" CASCADE; (params None)
2024-08-05 23:42:59,269 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "rhythm" CASCADE; (params None)
2024-08-05 23:42:59,288 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "source" CASCADE; (params None)
2024-08-05 23:42:59,308 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" DROP COLUMN "technical_description" CASCADE; (params None)
2024-08-05 23:42:59,326 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_correlation" ADD CONSTRAINT "metrics_correlation_tenant_id_metric1_id_met_49a4c34a_uniq" UNIQUE ("tenant_id", "metric1_id", "metric2_id", "lag"); (params None)
2024-08-05 23:42:59,349 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_metric__b85d3a_idx" ON "metrics_insight" ("metric_id", "date"); (params None)
2024-08-05 23:42:59,372 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_ins_user_id_1ebb42_idx" ON "metrics_insight" ("user_id", "date"); (params None)
2024-08-05 23:42:59,394 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_metric__a2b705_idx" ON "metrics_metrictarget" ("metric_id", "target_date"); (params None)
2024-08-05 23:42:59,415 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_met_last_up_6e2e67_idx" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:42:59,436 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_date_53cb14_idx" ON "metrics_timedimension" ("date"); (params None)
2024-08-05 23:42:59,457 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tim_year_92da9e_idx" ON "metrics_timedimension" ("year", "month", "day"); (params None)
2024-08-05 23:42:59,460 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_username_6e55f358_like" ON "metrics_customuser" ("username" varchar_pattern_ops); (params None)
2024-08-05 23:42:59,463 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_date_ded95ba1" ON "metrics_insight" ("date"); (params None)
2024-08-05 23:42:59,465 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_last_updated_76599a1b" ON "metrics_metricmetadata" ("last_updated"); (params None)
2024-08-05 23:42:59,467 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_target_date_38cd9191" ON "metrics_metrictarget" ("target_date"); (params None)
2024-08-05 23:42:59,469 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_historicaldata_forecast_id_29590c29" ON "metrics_historicaldata" ("forecast_id"); (params None)
2024-08-05 23:42:59,471 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric1_id_6e1c2404" ON "metrics_correlation" ("metric1_id"); (params None)
2024-08-05 23:42:59,474 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_metric2_id_f2cc46dd" ON "metrics_correlation" ("metric2_id"); (params None)
2024-08-05 23:42:59,477 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_correlation_tenant_id_a00a5169" ON "metrics_correlation" ("tenant_id"); (params None)
2024-08-05 23:42:59,479 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_customuser_id_group_id_1c5fc435_uniq" UNIQUE ("customuser_id", "group_id"); (params None)
2024-08-05 23:42:59,481 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_g_customuser_id_fc13f3af_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:59,482 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_groups" ADD CONSTRAINT "metrics_customuser_groups_group_id_6b097e12_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:59,483 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_customuser_id_fc13f3af" ON "metrics_customuser_groups" ("customuser_id"); (params None)
2024-08-05 23:42:59,485 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_groups_group_id_6b097e12" ON "metrics_customuser_groups" ("group_id"); (params None)
2024-08-05 23:42:59,486 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_tenant_id_02b7403c" ON "metrics_customuser" ("tenant_id"); (params None)
2024-08-05 23:42:59,489 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_user__customuser_id_permission_68cc320f_uniq" UNIQUE ("customuser_id", "permission_id"); (params None)
2024-08-05 23:42:59,492 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_customuser_id_46e97f00_fk_metrics_c" FOREIGN KEY ("customuser_id") REFERENCES "metrics_customuser" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:59,493 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_customuser_user_permissions" ADD CONSTRAINT "metrics_customuser_u_permission_id_d66d657c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:59,493 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_customuser_id_46e97f00" ON "metrics_customuser_user_permissions" ("customuser_id"); (params None)
2024-08-05 23:42:59,495 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_user_permissions_permission_id_d66d657c" ON "metrics_customuser_user_permissions" ("permission_id"); (params None)
2024-08-05 23:42:59,497 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_tenant_id_8e9f296d" ON "metrics_dataqualityscore" ("tenant_id"); (params None)
2024-08-05 23:42:59,499 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_experiment_id_1beae7fe" ON "metrics_impactanalysis" ("experiment_id"); (params None)
2024-08-05 23:42:59,502 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_metric_id_f4b9eeb6" ON "metrics_impactanalysis" ("metric_id"); (params None)
2024-08-05 23:42:59,505 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_impactanalysis_tenant_id_126ca20d" ON "metrics_impactanalysis" ("tenant_id"); (params None)
2024-08-05 23:42:59,507 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_metric_id_26d3a9d8" ON "metrics_insight" ("metric_id"); (params None)
2024-08-05 23:42:59,509 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_tenant_id_724d7d85" ON "metrics_insight" ("tenant_id"); (params None)
2024-08-05 23:42:59,511 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_insight_user_id_83d421e1" ON "metrics_insight" ("user_id"); (params None)
2024-08-05 23:42:59,513 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_tenant_id_3277f967" ON "metrics_metricmetadata" ("tenant_id"); (params None)
2024-08-05 23:42:59,515 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_metric_id_7876e2c8" ON "metrics_metrictarget" ("metric_id"); (params None)
2024-08-05 23:42:59,518 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metrictarget_tenant_id_b26a17f8" ON "metrics_metrictarget" ("tenant_id"); (params None)
2024-08-05 23:42:59,520 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_tenant_id_1323395e" ON "metrics_strategy" ("tenant_id"); (params None)
2024-08-05 23:42:59,522 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_metric_id_9887ffa4" ON "metrics_tacticalsolution" ("metric_id"); (params None)
2024-08-05 23:42:59,524 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_tacticalsolution_tenant_id_cf9028f0" ON "metrics_tacticalsolution" ("tenant_id"); (params None)
2024-08-05 23:42:59,526 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_team_tenant_id_3a14c47d" ON "metrics_team" ("tenant_id"); (params None)
2024-08-05 23:42:59,528 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_strategy_team_id_f1781500" ON "metrics_strategy" ("team_id"); (params None)
2024-08-05 23:42:59,531 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_metricmetadata_team_id_f140658d" ON "metrics_metricmetadata" ("team_id"); (params None)
2024-08-05 23:42:59,533 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_customuser_team_id_4c4ffc18" ON "metrics_customuser" ("team_id"); (params None)
2024-08-05 23:42:59,535 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_experiment_team_id_537107e3" ON "metrics_experiment" ("team_id"); (params None)
2024-08-05 23:42:59,537 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_metric_id_3e2eead6" ON "metrics_technicalindicator" ("metric_id"); (params None)
2024-08-05 23:42:59,539 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_technicalindicator_tenant_id_f4de3b44" ON "metrics_technicalindicator" ("tenant_id"); (params None)
2024-08-05 23:42:59,542 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_timedimension_tenant_id_f375bb45" ON "metrics_timedimension" ("tenant_id"); (params None)
2024-08-05 23:42:59,544 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_userprofile_tenant_id_cca71dae" ON "metrics_userprofile" ("tenant_id"); (params None)
2024-08-05 23:42:59,566 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ADD COLUMN "strength" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:42:59,567 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_connection" ALTER COLUMN "strength" DROP DEFAULT; (params None)
2024-08-05 23:42:59,587 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "lower_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:42:59,588 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "lower_bound" DROP DEFAULT; (params None)
2024-08-05 23:42:59,607 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ADD COLUMN "upper_bound" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:42:59,608 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_forecast" ALTER COLUMN "upper_bound" DROP DEFAULT; (params None)
2024-08-05 23:42:59,629 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ADD COLUMN "slope" double precision DEFAULT 0.0 NOT NULL; (params None)
2024-08-05 23:42:59,630 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trend" ALTER COLUMN "slope" DROP DEFAULT; (params None)
2024-08-05 23:42:59,784 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_movingaverage" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "ma_type" varchar(10) NOT NULL, "period" integer NOT NULL, "value" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:59,813 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_networkanalysisresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "analysis_type" varchar(20) NOT NULL, "result" jsonb NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:59,845 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_seasonalityresult" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "seasonality_type" varchar(20) NOT NULL, "strength" double precision NOT NULL, "period" integer NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:59,877 - django.db.backends.schema - DEBUG - CREATE TABLE "metrics_trendchangepoint" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date" timestamp with time zone NOT NULL, "change_type" varchar(20) NOT NULL, "significance" double precision NOT NULL, "metric_id" bigint NOT NULL); (params None)
2024-08-05 23:42:59,881 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD CONSTRAINT "metrics_movingaverage_metric_id_7c61cebf_fk_metrics_metric_id" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:59,882 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_metric_id_7c61cebf" ON "metrics_movingaverage" ("metric_id"); (params None)
2024-08-05 23:42:59,884 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD CONSTRAINT "metrics_networkanaly_metric_id_a4c90102_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:59,885 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_metric_id_a4c90102" ON "metrics_networkanalysisresult" ("metric_id"); (params None)
2024-08-05 23:42:59,888 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityr_metric_id_6e494791_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:59,889 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_metric_id_6e494791" ON "metrics_seasonalityresult" ("metric_id"); (params None)
2024-08-05 23:42:59,891 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD CONSTRAINT "metrics_trendchangep_metric_id_f8eb9f76_fk_metrics_m" FOREIGN KEY ("metric_id") REFERENCES "metrics_metric" ("id") DEFERRABLE INITIALLY DEFERRED; (params None)
2024-08-05 23:42:59,893 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_metric_id_f8eb9f76" ON "metrics_trendchangepoint" ("metric_id"); (params None)
2024-08-05 23:42:59,926 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_metric_id_1b6367d1_fk_metrics_m" IMMEDIATE; (params None)
2024-08-05 23:42:59,928 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:42:59,955 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD COLUMN "project_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" REFERENCES "metrics_project"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_dataqualitys_project_id_123a4f58_fk_metrics_p" IMMEDIATE; (params None)
2024-08-05 23:42:59,957 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ALTER COLUMN "project_id" DROP DEFAULT; (params None)
2024-08-05 23:42:59,977 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_historicaldata" ALTER COLUMN "value" DROP NOT NULL; (params None)
2024-08-05 23:42:59,998 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_dataqualityscore" ADD CONSTRAINT "metrics_dataqualityscore_tenant_id_metric_id_proj_66b9fb01_uniq" UNIQUE ("tenant_id", "metric_id", "project_id"); (params None)
2024-08-05 23:43:00,000 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_metric_id_1b6367d1" ON "metrics_dataqualityscore" ("metric_id"); (params None)
2024-08-05 23:43:00,002 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_dataqualityscore_project_id_123a4f58" ON "metrics_dataqualityscore" ("project_id"); (params None)
2024-08-05 23:43:00,027 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_metric" ADD CONSTRAINT "metrics_metric_tenant_id_project_id_name_77eab572_uniq" UNIQUE ("tenant_id", "project_id", "name"); (params None)
2024-08-05 23:43:00,056 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_movingaverage_tenant_id_5a9de228_fk_metrics_client_id" IMMEDIATE; (params None)
2024-08-05 23:43:00,057 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_movingaverage" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:43:00,085 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_networkanaly_tenant_id_16a6ba09_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:43:00,086 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_networkanalysisresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:43:00,113 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:43:00,115 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:43:00,141 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ADD COLUMN "tenant_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" REFERENCES "metrics_client"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; (params None)
2024-08-05 23:43:00,143 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "tenant_id" DROP DEFAULT; (params None)
2024-08-05 23:43:00,163 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq" UNIQUE ("tenant_id", "metric_id"); (params None)
2024-08-05 23:43:00,166 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_movingaverage_tenant_id_5a9de228" ON "metrics_movingaverage" ("tenant_id"); (params None)
2024-08-05 23:43:00,168 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_networkanalysisresult_tenant_id_16a6ba09" ON "metrics_networkanalysisresult" ("tenant_id"); (params None)
2024-08-05 23:43:00,170 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_seasonalityresult_tenant_id_ca2da3fd" ON "metrics_seasonalityresult" ("tenant_id"); (params None)
2024-08-05 23:43:00,172 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_trendchangepoint_tenant_id_da10d898" ON "metrics_trendchangepoint" ("tenant_id"); (params None)
2024-08-05 23:43:00,201 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "metric_id" bigint DEFAULT 1 NOT NULL CONSTRAINT "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" REFERENCES "metrics_metric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "metrics_report_metric_id_c86f5720_fk_metrics_metric_id" IMMEDIATE; (params None)
2024-08-05 23:43:00,203 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "metric_id" DROP DEFAULT; (params None)
2024-08-05 23:43:00,203 - django.db.backends.schema - DEBUG - CREATE INDEX "metrics_report_metric_id_c86f5720" ON "metrics_report" ("metric_id"); (params None)
2024-08-05 23:43:00,227 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "analysis_result" jsonb NULL; (params None)
2024-08-05 23:43:00,248 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "anomaly_result" jsonb NULL; (params None)
2024-08-05 23:43:00,276 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:43:00.276318+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:43:00,277 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:43:00,452 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "forecast_result" jsonb NULL; (params None)
2024-08-05 23:43:00,473 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "relationship_result" jsonb NULL; (params None)
2024-08-05 23:43:00,494 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "report" text DEFAULT '1' NOT NULL; (params None)
2024-08-05 23:43:00,495 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "report" DROP DEFAULT; (params None)
2024-08-05 23:43:00,517 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ADD COLUMN "updated_at" timestamp with time zone DEFAULT '2024-08-05T23:43:00.517630+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:43:00,518 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_report" ALTER COLUMN "updated_at" DROP DEFAULT; (params None)
2024-08-05 23:43:00,575 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_trendchangepoint" DROP CONSTRAINT "metrics_trendchangep_tenant_id_da10d898_fk_metrics_c"; (params None)
2024-08-05 23:43:00,576 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:43:00,592 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" ALTER COLUMN "significance" DROP NOT NULL; (params None)
2024-08-05 23:43:00,611 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_trendchangepoint" RENAME COLUMN "change_type" TO "direction"; (params None)
2024-08-05 23:43:00,655 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD COLUMN "created_at" timestamp with time zone DEFAULT '2024-08-05T23:43:00.655027+00:00'::timestamptz NOT NULL; (params None)
2024-08-05 23:43:00,656 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ALTER COLUMN "created_at" DROP DEFAULT; (params None)
2024-08-05 23:43:00,680 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityresult_tenant_id_metric_id_21fa3448_uniq"; (params None)
2024-08-05 23:43:00,681 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" ADD CONSTRAINT "metrics_seasonalityresul_metric_id_seasonality_ty_d3492b78_uniq" UNIQUE ("metric_id", "seasonality_type"); (params None)
2024-08-05 23:43:00,711 - django.db.backends.schema - DEBUG - SET CONSTRAINTS "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c" IMMEDIATE; ALTER TABLE "metrics_seasonalityresult" DROP CONSTRAINT "metrics_seasonalityr_tenant_id_ca2da3fd_fk_metrics_c"; (params None)
2024-08-05 23:43:00,712 - django.db.backends.schema - DEBUG - ALTER TABLE "metrics_seasonalityresult" DROP COLUMN "tenant_id" CASCADE; (params None)
2024-08-05 23:43:00,715 - django.db.backends.schema - DEBUG - CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" timestamp with time zone NOT NULL); (params None)
2024-08-05 23:43:00,721 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" ("session_key" varchar_pattern_ops); (params None)
2024-08-05 23:43:00,724 - django.db.backends.schema - DEBUG - CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date"); (params None)
2024-08-05 23:43:01,844 - metrics.computations.data_preparation - INFO - Loaded metric 13 for tenant 7 and project 7
2024-08-05 23:43:01,844 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 13
2024-08-05 23:43:01,844 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:01,845 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:01,846 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 13
2024-08-05 23:43:01,850 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:01,850 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:43:01,853 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:01,854 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:01,856 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:01,857 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:43:01,859 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:43:03,608 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 13
2024-08-05 23:43:03,610 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:43:03,612 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:43:03,612 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:43:03,615 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:03,615 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:43:03,617 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:03,619 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3644886295173909, Timeliness: nan
2024-08-05 23:43:03,619 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48295431724636
2024-08-05 23:43:03,623 - metrics.computations.data_preparation - INFO - Data quality score: 45.48295431724636
2024-08-05 23:43:03,637 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 13, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48295431724636, 'outliers_handled': True, 'profile': {'mean': 100.26981825500415, 'median': 100.2360212504316, 'std': 9.795495670695658, 'min': 78.20700148292758, 'max': 123.00587899285291, 'skewness': -0.0015939833400606452, 'kurtosis': -0.4541465371251978, 'missing_percentage': 0.0}}
2024-08-05 23:43:03,645 - metrics.computations.data_preparation - INFO - Loaded metric 13 for tenant 7 and project 7
2024-08-05 23:43:03,645 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 13
2024-08-05 23:43:03,646 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:03,647 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:03,648 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 13
2024-08-05 23:43:03,654 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:03,655 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:43:03,658 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:03,659 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:03,663 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:03,664 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:43:03,667 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:43:05,477 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 13
2024-08-05 23:43:05,480 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:43:05,483 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:43:05,483 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:43:05,486 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:05,486 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:43:05,491 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:05,494 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3644886295173909, Timeliness: nan
2024-08-05 23:43:05,495 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48295431724636
2024-08-05 23:43:05,499 - metrics.computations.data_preparation - INFO - Data quality score: 45.48295431724636
2024-08-05 23:43:05,587 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 13, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48295431724636, 'outliers_handled': True, 'profile': {'mean': 100.26981825500415, 'median': 100.2360212504316, 'std': 9.795495670695658, 'min': 78.20700148292758, 'max': 123.00587899285291, 'skewness': -0.0015939833400606452, 'kurtosis': -0.4541465371251978, 'missing_percentage': 0.0}}
2024-08-05 23:43:05,587 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:43:05,587 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 13
2024-08-05 23:43:05,598 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:43:05,603 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:43:05,608 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 13
2024-08-05 23:43:05,610 - metrics.computations.feature_engineering - INFO - Parameters for metric 13: dynamic
2024-08-05 23:43:05,610 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 13: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:43:05,616 - metrics.computations.data_preparation - INFO - Loaded metric 13 for tenant 7 and project 7
2024-08-05 23:43:05,616 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 13
2024-08-05 23:43:05,617 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:05,618 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:05,621 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 13
2024-08-05 23:43:05,631 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:05,631 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:43:05,635 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:05,635 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:05,638 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:05,638 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:43:05,643 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:43:07,409 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 13
2024-08-05 23:43:07,411 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:43:07,412 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:43:07,413 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:43:07,415 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:07,415 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:43:07,417 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:07,419 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3644886295173909, Timeliness: nan
2024-08-05 23:43:07,419 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48295431724636
2024-08-05 23:43:07,422 - metrics.computations.data_preparation - INFO - Data quality score: 45.48295431724636
2024-08-05 23:43:07,436 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 13, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48295431724636, 'outliers_handled': True, 'profile': {'mean': 100.26981825500415, 'median': 100.2360212504316, 'std': 9.795495670695658, 'min': 78.20700148292758, 'max': 123.00587899285291, 'skewness': -0.0015939833400606452, 'kurtosis': -0.4541465371251978, 'missing_percentage': 0.0}}
2024-08-05 23:43:07,442 - metrics.computations.data_preparation - INFO - Loaded metric 13 for tenant 7 and project 7
2024-08-05 23:43:07,442 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 13
2024-08-05 23:43:07,443 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:07,444 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 13 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:07,447 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 13
2024-08-05 23:43:07,454 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:07,454 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:43:07,457 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:07,457 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:07,462 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:07,462 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:43:07,465 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:43:09,241 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 13
2024-08-05 23:43:09,244 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:43:09,245 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:43:09,246 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:43:09,248 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:09,248 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:43:09,251 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  114.908410          7
2023-01-02  107.060369          7
2023-01-03  104.198116          7
2023-01-04  105.666149          7
2023-01-05  108.862153          7
2024-08-05 23:43:09,253 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3644886295173909, Timeliness: nan
2024-08-05 23:43:09,253 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48295431724636
2024-08-05 23:43:09,256 - metrics.computations.data_preparation - INFO - Data quality score: 45.48295431724636
2024-08-05 23:43:09,271 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 13, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 1', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48295431724636, 'outliers_handled': True, 'profile': {'mean': 100.26981825500415, 'median': 100.2360212504316, 'std': 9.795495670695658, 'min': 78.20700148292758, 'max': 123.00587899285291, 'skewness': -0.0015939833400606452, 'kurtosis': -0.4541465371251978, 'missing_percentage': 0.0}}
2024-08-05 23:43:09,271 - metrics.computations.feature_engineering - ERROR - Error in engineer_features: 'NoneType' object is not callable
2024-08-05 23:43:09,271 - metrics.computations.feature_engineering - DEBUG - Starting _compute_seasonality_period for metric 13
2024-08-05 23:43:09,276 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:43:09,283 - metrics.computations.feature_engineering - INFO - Seasonality detected: type=daily, period=2, strength=0.00
2024-08-05 23:43:09,287 - metrics.computations.feature_engineering - INFO - Using dynamic parameters for metric 13
2024-08-05 23:43:09,287 - metrics.computations.feature_engineering - INFO - Parameters for metric 13: dynamic
2024-08-05 23:43:09,287 - metrics.computations.feature_engineering - DEBUG - Parameter values for metric 13: {'seasonality_period': 2, 'forecast_horizon': 2, 'correlation_window': 7, 'trend_window': 100, 'anomaly_detection_window': 7, 'base_threshold': 5.0, 'window_size': 1000, 'context_window': 15, 'global_threshold': 5.0, 'imputation_method': 'mean'}
2024-08-05 23:43:09,288 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Setup completed
2024-08-05 23:43:09,291 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:43:09,291 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:43:09,292 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:09,292 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:09,295 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:43:09,300 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:09,301 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:43:09,304 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:09,304 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:09,307 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:09,307 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:43:09,310 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:43:11,162 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:43:11,164 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:43:11,166 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:43:11,166 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:43:11,169 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:11,169 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:43:11,171 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:11,173 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3644886295173909, Timeliness: nan
2024-08-05 23:43:11,174 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48295431724636
2024-08-05 23:43:11,177 - metrics.computations.data_preparation - INFO - Data quality score: 45.48295431724636
2024-08-05 23:43:11,247 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48295431724636, 'outliers_handled': True, 'profile': {'mean': 110.29680008050457, 'median': 110.25962337547477, 'std': 10.775045237765225, 'min': 86.02770163122035, 'max': 135.3064668921382, 'skewness': -0.0015939833400581429, 'kurtosis': -0.45414653712519915, 'missing_percentage': 0.0}}
2024-08-05 23:43:11,249 - metrics.computations.computations_relationships - INFO - Calculated pearson correlation between metrics 13 and 14
2024-08-05 23:43:11,251 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:43:11,254 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:43:11,255 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:11,256 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:11,265 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:43:11,273 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:11,274 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:43:11,278 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:11,278 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:11,281 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:11,284 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:43:11,288 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:43:13,069 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:43:13,071 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:43:13,073 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:43:13,073 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:43:13,075 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:13,075 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:43:13,078 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:13,080 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3644886295173909, Timeliness: nan
2024-08-05 23:43:13,080 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48295431724636
2024-08-05 23:43:13,083 - metrics.computations.data_preparation - INFO - Data quality score: 45.48295431724636
2024-08-05 23:43:13,098 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48295431724636, 'outliers_handled': True, 'profile': {'mean': 110.29680008050457, 'median': 110.25962337547477, 'std': 10.775045237765225, 'min': 86.02770163122035, 'max': 135.3064668921382, 'skewness': -0.0015939833400581429, 'kurtosis': -0.45414653712519915, 'missing_percentage': 0.0}}
2024-08-05 23:43:13,101 - metrics.computations.computations_relationships - INFO - Calculated spearman correlation between metrics 13 and 14
2024-08-05 23:43:13,124 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:43:13,124 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:43:13,125 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:13,126 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:13,128 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:43:13,138 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:13,138 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:43:13,141 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:13,142 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:13,144 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:13,145 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:43:13,148 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:43:14,945 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:43:14,947 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:43:14,949 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:43:14,949 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:43:14,952 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:14,952 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:43:14,954 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:14,956 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3644886295173909, Timeliness: nan
2024-08-05 23:43:14,956 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48295431724636
2024-08-05 23:43:14,959 - metrics.computations.data_preparation - INFO - Data quality score: 45.48295431724636
2024-08-05 23:43:14,973 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48295431724636, 'outliers_handled': True, 'profile': {'mean': 110.29680008050457, 'median': 110.25962337547477, 'std': 10.775045237765225, 'min': 86.02770163122035, 'max': 135.3064668921382, 'skewness': -0.0015939833400581429, 'kurtosis': -0.45414653712519915, 'missing_percentage': 0.0}}
2024-08-05 23:43:14,976 - metrics.computations.computations_relationships - INFO - Calculated pearson correlation between metrics 13 and 14
2024-08-05 23:43:14,978 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:43:14,978 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:43:14,979 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:14,979 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:14,983 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:43:14,990 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:14,990 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:43:14,994 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:14,994 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:14,997 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:14,997 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:43:15,000 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:43:16,778 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:43:16,780 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:43:16,782 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:43:16,782 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:43:16,784 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:16,784 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:43:16,787 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:16,789 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3644886295173909, Timeliness: nan
2024-08-05 23:43:16,789 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48295431724636
2024-08-05 23:43:16,792 - metrics.computations.data_preparation - INFO - Data quality score: 45.48295431724636
2024-08-05 23:43:16,823 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48295431724636, 'outliers_handled': True, 'profile': {'mean': 110.29680008050457, 'median': 110.25962337547477, 'std': 10.775045237765225, 'min': 86.02770163122035, 'max': 135.3064668921382, 'skewness': -0.0015939833400581429, 'kurtosis': -0.45414653712519915, 'missing_percentage': 0.0}}
2024-08-05 23:43:16,826 - metrics.computations.computations_relationships - INFO - Calculated spearman correlation between metrics 13 and 14
2024-08-05 23:43:16,834 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:43:16,834 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:43:16,835 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:16,836 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:16,839 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:43:16,847 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:16,848 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:43:16,851 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:16,851 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:16,858 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:16,858 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:43:16,861 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:43:18,591 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:43:18,594 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:43:18,595 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:43:18,595 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:43:18,598 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:18,598 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:43:18,600 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:18,602 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3644886295173909, Timeliness: nan
2024-08-05 23:43:18,603 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48295431724636
2024-08-05 23:43:18,606 - metrics.computations.data_preparation - INFO - Data quality score: 45.48295431724636
2024-08-05 23:43:18,624 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48295431724636, 'outliers_handled': True, 'profile': {'mean': 110.29680008050457, 'median': 110.25962337547477, 'std': 10.775045237765225, 'min': 86.02770163122035, 'max': 135.3064668921382, 'skewness': -0.0015939833400581429, 'kurtosis': -0.45414653712519915, 'missing_percentage': 0.0}}
2024-08-05 23:43:18,626 - metrics.computations.computations_relationships - INFO - Calculated pearson correlation between metrics 13 and 14
2024-08-05 23:43:18,629 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:43:18,630 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:43:18,631 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:18,631 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:18,636 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:43:18,645 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:18,645 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:43:18,648 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:18,648 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:18,651 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:18,651 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:43:18,655 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:43:20,395 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:43:20,397 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:43:20,398 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:43:20,398 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:43:20,401 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:20,401 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:43:20,403 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:20,405 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3644886295173909, Timeliness: nan
2024-08-05 23:43:20,405 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48295431724636
2024-08-05 23:43:20,408 - metrics.computations.data_preparation - INFO - Data quality score: 45.48295431724636
2024-08-05 23:43:20,424 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48295431724636, 'outliers_handled': True, 'profile': {'mean': 110.29680008050457, 'median': 110.25962337547477, 'std': 10.775045237765225, 'min': 86.02770163122035, 'max': 135.3064668921382, 'skewness': -0.0015939833400581429, 'kurtosis': -0.45414653712519915, 'missing_percentage': 0.0}}
2024-08-05 23:43:20,426 - metrics.computations.computations_relationships - INFO - Calculated spearman correlation between metrics 13 and 14
2024-08-05 23:43:20,429 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:43:20,429 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:43:20,430 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:20,430 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:20,437 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:43:20,447 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:20,447 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:43:20,450 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:20,450 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:20,453 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:20,454 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:43:20,456 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:43:22,260 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:43:22,262 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:43:22,263 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:43:22,264 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:43:22,266 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:22,266 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:43:22,268 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:22,271 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3644886295173909, Timeliness: nan
2024-08-05 23:43:22,271 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48295431724636
2024-08-05 23:43:22,274 - metrics.computations.data_preparation - INFO - Data quality score: 45.48295431724636
2024-08-05 23:43:22,288 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48295431724636, 'outliers_handled': True, 'profile': {'mean': 110.29680008050457, 'median': 110.25962337547477, 'std': 10.775045237765225, 'min': 86.02770163122035, 'max': 135.3064668921382, 'skewness': -0.0015939833400581429, 'kurtosis': -0.45414653712519915, 'missing_percentage': 0.0}}
2024-08-05 23:43:22,290 - metrics.computations.computations_relationships - INFO - Calculated pearson correlation between metrics 13 and 14
2024-08-05 23:43:22,293 - metrics.computations.data_preparation - INFO - Loaded metric 14 for tenant 7 and project 7
2024-08-05 23:43:22,293 - metrics.computations.data_preparation - INFO - Fetching historical data for metric 14
2024-08-05 23:43:22,294 - metrics.computations.data_preparation - INFO - Query: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:22,294 - metrics.computations.data_preparation - INFO - SQL: SELECT "metrics_historicaldata"."id", "metrics_historicaldata"."tenant_id", "metrics_historicaldata"."metric_id", "metrics_historicaldata"."date", "metrics_historicaldata"."value", "metrics_historicaldata"."forecast_id" FROM "metrics_historicaldata" WHERE "metrics_historicaldata"."metric_id" = 14 ORDER BY "metrics_historicaldata"."date" ASC
2024-08-05 23:43:22,300 - metrics.computations.data_preparation - INFO - Found 1000 historical data points for metric 14
2024-08-05 23:43:22,310 - metrics.computations.data_preparation - INFO - DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:22,310 - metrics.computations.data_preparation - INFO - DataFrame columns: Index(['value', 'tenant_id'], dtype='object')
2024-08-05 23:43:22,314 - metrics.computations.data_preparation - INFO - DataFrame head: 
                 value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:22,314 - metrics.computations.data_preparation - INFO - Raw DataFrame shape after loading: (1000, 2)
2024-08-05 23:43:22,316 - metrics.computations.data_preparation - INFO - Raw DataFrame head after loading:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:22,317 - metrics.computations.data_preparation - INFO - Found 0.00% missing values in the data
2024-08-05 23:43:22,320 - metrics.computations.data_preparation - INFO - Handled missing values using mean method
2024-08-05 23:43:24,070 - metrics.computations.data_preparation - INFO - Updated database with imputed values for metric 14
2024-08-05 23:43:24,072 - metrics.computations.data_preparation - INFO - Handled outliers using IQR method
2024-08-05 23:43:24,074 - metrics.computations.data_preparation - INFO - Handled extreme values by capping at 1st and 99th percentiles
2024-08-05 23:43:24,074 - metrics.computations.data_preparation - INFO - Cleaned DataFrame shape: (1000, 2)
2024-08-05 23:43:24,076 - metrics.computations.data_preparation - INFO - Cleaned DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:24,076 - metrics.computations.data_preparation - INFO - Raw DataFrame shape: (1000, 2)
2024-08-05 23:43:24,079 - metrics.computations.data_preparation - INFO - Raw DataFrame head:                  value  tenant_id
date                             
2023-01-01  126.399251          7
2023-01-02  117.766406          7
2023-01-03  114.617928          7
2023-01-04  116.232763          7
2023-01-05  119.748368          7
2024-08-05 23:43:24,080 - metrics.computations.data_preparation - INFO - Completeness: 1.0, Accuracy: 0.0, Consistency: 0.3644886295173909, Timeliness: nan
2024-08-05 23:43:24,081 - metrics.computations.data_preparation - INFO - Overall data quality score: 45.48295431724636
2024-08-05 23:43:24,084 - metrics.computations.data_preparation - INFO - Data quality score: 45.48295431724636
2024-08-05 23:43:24,099 - metrics.computations.data_preparation - INFO - Final metadata: {'metric_id': 14, 'tenant_id': 7, 'project_id': 7, 'metric_name': 'Test Metric 2', 'value_type': 'COUNT', 'imputation_method': 'mean', 'is_stationary': True, 'data_quality_score': 45.48295431724636, 'outliers_handled': True, 'profile': {'mean': 110.29680008050457, 'median': 110.25962337547477, 'std': 10.775045237765225, 'min': 86.02770163122035, 'max': 135.3064668921382, 'skewness': -0.0015939833400581429, 'kurtosis': -0.45414653712519915, 'missing_percentage': 0.0}}
2024-08-05 23:43:24,102 - metrics.computations.computations_relationships - INFO - Calculated spearman correlation between metrics 13 and 14
2024-08-05 23:43:24,102 - metrics.computations.computations_relationships - ERROR - Error analyzing connections for metric 13: 'Metric' object has no attribute 'connections_from'
2024-08-05 23:43:24,248 - metrics.tests.test_permanent_computations.test_permanent_computations_robustness - INFO - Teardown completed
```

