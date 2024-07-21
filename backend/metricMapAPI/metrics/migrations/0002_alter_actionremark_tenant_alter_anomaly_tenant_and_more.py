# Generated by Django 5.0.6 on 2024-07-20 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metrics", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actionremark",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
        migrations.AlterField(
            model_name="anomaly",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
        migrations.AlterField(
            model_name="connection",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
        migrations.AlterField(
            model_name="dashboard",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
        migrations.AlterField(
            model_name="forecast",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldata",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
        migrations.AlterField(
            model_name="metric",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="metrics",
                to="metrics.category",
            ),
        ),
        migrations.AlterField(
            model_name="metric",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
        migrations.AlterField(
            model_name="report",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tags",
                to="metrics.project",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
        migrations.AlterField(
            model_name="target",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
        migrations.AlterField(
            model_name="trend",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="metrics.client",
            ),
        ),
    ]