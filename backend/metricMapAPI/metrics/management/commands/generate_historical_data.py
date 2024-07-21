import random
from datetime import datetime, timedelta
import numpy as np
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import connection, transaction
from django_tenants.utils import schema_context
from tqdm import tqdm
import logging

from metrics.models import (
    Metric, HistoricalData, Project, Category, Tag, Connection, 
    Target, ActionRemark, Experiment, Dashboard, Report, Forecast, Client
)

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Generate robust historical data for testing in public schema'

    def add_arguments(self, parser):
        parser.add_argument(
            '--reset',
            action='store_true',
            help='Reset all data before generating new data',
        )
        parser.add_argument(
            '--metrics',
            type=int,
            default=5,
            help='Number of metrics to generate',
        )
        parser.add_argument(
            '--start-date',
            type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
            default=datetime(2020, 1, 1),
            help='Start date for historical data (YYYY-MM-DD)',
        )
        parser.add_argument(
            '--end-date',
            type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
            default=datetime(2023, 12, 31),
            help='End date for historical data (YYYY-MM-DD)',
        )

    def handle(self, *args, **options):
        try:
            with schema_context('public'):
                with transaction.atomic():
                    if options['reset']:
                        self.reset_data()
                        self.stdout.write(self.style.SUCCESS('All data has been reset'))
                        return
                    
                    client = self.get_or_create_client()
                    project = self.get_or_create_project(client)

                    categories = self.create_categories(client)
                    tags = self.create_tags(client, project)
                    metrics = self.create_metrics(client, project, categories, tags, options['metrics'])

                    self.generate_historical_data(metrics, client, options['start_date'], options['end_date'])
                    self.create_connections(metrics, client)
                    self.create_targets(metrics, client)
                    self.create_action_remarks(metrics, client)
                    self.create_experiments(metrics, client)
                    self.create_dashboards_and_reports(metrics, client)
                    self.create_forecasts(metrics, client)
                    self.create_users(client)

                    self.stdout.write(self.style.SUCCESS('Successfully generated comprehensive test data'))
        except Exception as e:
            logger.error(f"An error occurred while generating data: {str(e)}")
            self.stdout.write(self.style.ERROR(f'Failed to generate data: {str(e)}'))

    def get_or_create_client(self):
        client = Client.objects.first()
        if not client:
            client = Client.objects.create(name="Test Client", schema_name="test_client")
            logger.info(f"Created new client: {client.name}")
        return client

    def get_or_create_project(self, client):
        project = Project.objects.filter(tenant=client).first()
        if not project:
            project = Project.objects.create(name="Test Project", tenant=client)
            logger.info(f"Created new project: {project.name}")
        return project

    def create_categories(self, tenant):
        category_names = ["Financial", "Marketing", "Operations", "Customer", "Product", "HR", "Sales", "Technology"]
        categories = []
        for name in tqdm(category_names, desc="Creating categories"):
            category, created = Category.objects.get_or_create(name=name, tenant=tenant)
            categories.append(category)
            if created:
                logger.info(f"Created new category: {category.name}")
        return categories

    def create_tags(self, tenant, project):
        tag_names = ["Important", "Growth", "Efficiency", "Customer Satisfaction", "Revenue", "Cost", "Quality", "Innovation", "Productivity", "Retention"]
        tags = []
        for name in tqdm(tag_names, desc="Creating tags"):
            tag, created = Tag.objects.get_or_create(name=name, tenant=tenant, project=project)
            tags.append(tag)
            if created:
                logger.info(f"Created new tag: {tag.name}")
        return tags

    def create_metrics(self, tenant, project, categories, tags, num_metrics):
        metrics_data = [
            {
                "name": "Customer Acquisition Cost (CAC)",
                "type": "KPI",
                "value_type": "Currency",
                "rhythm": "Monthly",
                "category": categories[0],  # Financial
                "description": "Cost of acquiring a new customer",
                "hypothesis": "Reducing CAC will improve profitability",
                "technical_description": "Total marketing spend / New customers acquired",
                "source": "Finance and Marketing departments",
                "confidence": "Above Average",
            },
            {
                "name": "Conversion Rate",
                "type": "KPI",
                "value_type": "Percentage",
                "rhythm": "Daily",
                "category": categories[1],  # Marketing
                "description": "Percentage of visitors who make a purchase",
                "hypothesis": "Improving website UX will increase conversion rate",
                "technical_description": "(Conversions / Total Visitors) * 100",
                "source": "Web Analytics",
                "confidence": "Very High",
            },
            {
                "name": "Customer Lifetime Value (CLV)",
                "type": "KPI",
                "value_type": "Currency",
                "rhythm": "Quarterly",
                "category": categories[3],  # Customer
                "description": "Total value a customer brings over their lifetime",
                "hypothesis": "Increasing CLV leads to higher long-term profitability",
                "technical_description": "Average purchase value * Purchase frequency * Average customer lifespan",
                "source": "CRM and Sales data",
                "confidence": "Above Average",
            },
            {
                "name": "Net Promoter Score (NPS)",
                "type": "North Star",
                "value_type": "Number",
                "rhythm": "Monthly",
                "category": categories[3],  # Customer
                "description": "Measure of customer satisfaction and loyalty",
                "hypothesis": "Higher NPS correlates with higher customer retention and referrals",
                "technical_description": "% Promoters - % Detractors",
                "source": "Customer surveys",
                "confidence": "High",
            },
            {
                "name": "Monthly Recurring Revenue (MRR)",
                "type": "KPI",
                "value_type": "Currency",
                "rhythm": "Monthly",
                "category": categories[0],  # Financial
                "description": "Predictable revenue generated each month",
                "hypothesis": "Increasing MRR leads to more stable and scalable growth",
                "technical_description": "Sum of all recurring revenue for the month",
                "source": "Billing system",
                "confidence": "Very High",
            },
        ]

        created_metrics = []
        for metric_data in tqdm(metrics_data[:num_metrics], desc="Creating metrics"):
            metric, created = Metric.objects.get_or_create(
                name=metric_data["name"],
                tenant=tenant,
                defaults={
                    "type": metric_data["type"],
                    "value_type": metric_data["value_type"],
                    "rhythm": metric_data["rhythm"],
                    "category": metric_data["category"],
                    "description": metric_data["description"],
                    "hypothesis": metric_data["hypothesis"],
                    "technical_description": metric_data["technical_description"],
                    "source": metric_data["source"],
                    "confidence": metric_data["confidence"],
                    "position_x": random.uniform(0, 1000),
                    "position_y": random.uniform(0, 1000),
                }
            )
            metric.tags.add(*random.sample(tags, k=random.randint(1, 3)))
            created_metrics.append(metric)
            if created:
                logger.info(f"Created new metric: {metric.name}")
        return created_metrics

    def generate_historical_data(self, metrics, tenant, start_date, end_date):
        for metric in tqdm(metrics, desc="Generating historical data"):
            current_date = start_date
            base_value = random.uniform(100, 1000)
            trend = random.uniform(0.8, 1.2)
            while current_date <= end_date:
                if metric.value_type == "Currency":
                    value = base_value * (1 + 0.1 * np.sin(current_date.month / 12 * 2 * np.pi))  # Seasonality
                elif metric.value_type == "Percentage":
                    value = min(100, max(0, base_value))
                else:
                    value = int(base_value)
                
                value *= random.uniform(0.9, 1.1)  # Add some randomness
                value *= trend ** ((current_date - start_date).days / 365)  # Apply trend
                
                HistoricalData.objects.create(
                    metric=metric,
                    date=current_date,
                    value=value,
                    tenant=tenant
                )
                current_date += timedelta(days=1)
                
                if random.random() < 0.01:  # Occasionally add an anomaly
                    HistoricalData.objects.create(
                        metric=metric,
                        date=current_date,
                        value=value * random.uniform(1.5, 2.0),
                        tenant=tenant
                    )
                
                base_value = value  # For the next iteration

    def create_connections(self, metrics, tenant):
        for i in tqdm(range(len(metrics)), desc="Creating connections"):
            for j in range(i+1, len(metrics)):
                if random.random() < 0.3:  # 30% chance of connection
                    Connection.objects.create(
                        from_metric=metrics[i],
                        to_metric=metrics[j],
                        relationship=f"Affects {metrics[j].name}",
                        correlation_coefficient=random.uniform(-1, 1),
                        tenant=tenant
                    )

    def create_targets(self, metrics, tenant):
        for metric in tqdm(metrics, desc="Creating targets"):
            last_value = HistoricalData.objects.filter(metric=metric).order_by('-date').first().value
            Target.objects.create(
                metric=metric,
                target_value=last_value * random.uniform(1.1, 1.5),
                target_date=datetime.now() + timedelta(days=random.randint(30, 365)),
                tenant=tenant
            )

    def create_action_remarks(self, metrics, tenant):
        for metric in tqdm(metrics, desc="Creating action remarks"):
            for _ in range(random.randint(1, 5)):
                ActionRemark.objects.create(
                    metric=metric,
                    date=datetime.now() - timedelta(days=random.randint(1, 365)),
                    description=f"Action taken for {metric.name}",
                    impact="Positive impact observed",
                    tenant=tenant
                )

    def create_experiments(self, metrics, tenant):
        for _ in tqdm(range(5), desc="Creating experiments"):
            experiment = Experiment.objects.create(
                name=f"Experiment {random.randint(1, 100)}",
                description="Testing impact on metrics",
                start_date=datetime.now() - timedelta(days=random.randint(30, 180)),
                end_date=datetime.now() + timedelta(days=random.randint(1, 30)),
                status=random.choice(['Ongoing', 'Completed', 'Planned']),
                tenant=tenant
            )
            experiment.metrics.set(random.sample(metrics, k=random.randint(1, 3)))

    def create_dashboards_and_reports(self, metrics, tenant):
        for _ in tqdm(range(3), desc="Creating dashboards and reports"):
            Dashboard.objects.create(
                name=f"Dashboard {random.randint(1, 100)}",
                layout={"layout": "example_layout"},
                tenant=tenant
            )
            Report.objects.create(
                name=f"Report {random.randint(1, 100)}",
                configuration={"config": "example_config"},
                tenant=tenant
            )

    def create_forecasts(self, metrics, tenant):
        for metric in tqdm(metrics, desc="Creating forecasts"):
            last_value = HistoricalData.objects.filter(metric=metric).order_by('-date').first().value
            Forecast.objects.create(
                metric=metric,
                forecast_date=datetime.now() + timedelta(days=30),
                forecast_value=last_value * random.uniform(0.9, 1.1),
                model_used="ARIMA",
                accuracy=random.uniform(0.7, 0.95),
                tenant=tenant
            )

    def create_users(self, tenant):
        for username, email in tqdm([('analyst', 'analyst@example.com'), ('manager', 'manager@example.com'), ('admin', 'admin@example.com')], desc="Creating users"):
            user, created = User.objects.get_or_create(username=username, email=email)
            if created:
                user.set_password('password')
                user.is_superuser = (username == 'admin')
                user.is_staff = (username == 'admin')
                user.save()
                logger.info(f"Created new user: {username}")

    def reset_data(self):
        models = [Forecast, Report, Dashboard, Experiment, ActionRemark, Target, Connection, HistoricalData, Metric, Tag, Category, Project, Client, User]
        for model in tqdm(models, desc="Resetting data"):
            model.objects.all().delete()
            logger.info(f"Deleted all {model.__name__} objects")