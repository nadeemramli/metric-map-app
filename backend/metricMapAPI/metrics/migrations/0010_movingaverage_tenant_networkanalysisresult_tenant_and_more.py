# Generated by Django 5.0.6 on 2024-07-25 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metrics", "0009_alter_metric_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="movingaverage",
            name="tenant",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tenant_%(class)ss",
                to="metrics.client",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="networkanalysisresult",
            name="tenant",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tenant_%(class)ss",
                to="metrics.client",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="seasonalityresult",
            name="tenant",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tenant_%(class)ss",
                to="metrics.client",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="trendchangepoint",
            name="tenant",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tenant_%(class)ss",
                to="metrics.client",
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="seasonalityresult",
            unique_together={("tenant", "metric")},
        ),
    ]