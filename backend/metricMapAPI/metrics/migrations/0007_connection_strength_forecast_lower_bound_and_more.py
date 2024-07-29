# Generated by Django 5.0.6 on 2024-07-24 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metrics", "0006_correlation_customuser_dataqualityscore_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="connection",
            name="strength",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="forecast",
            name="lower_bound",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="forecast",
            name="upper_bound",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="trend",
            name="slope",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="MovingAverage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                ("ma_type", models.CharField(max_length=10)),
                ("period", models.IntegerField()),
                ("value", models.FloatField()),
                (
                    "metric",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="moving_averages",
                        to="metrics.metric",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NetworkAnalysisResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("analysis_type", models.CharField(max_length=20)),
                ("result", models.JSONField()),
                (
                    "metric",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="network_analysis_results",
                        to="metrics.metric",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SeasonalityResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("seasonality_type", models.CharField(max_length=20)),
                ("strength", models.FloatField()),
                ("period", models.IntegerField()),
                (
                    "metric",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seasonality_results",
                        to="metrics.metric",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TrendChangePoint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                ("change_type", models.CharField(max_length=20)),
                ("significance", models.FloatField()),
                (
                    "metric",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trend_change_points",
                        to="metrics.metric",
                    ),
                ),
            ],
        ),
    ]