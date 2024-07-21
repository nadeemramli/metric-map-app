from django.core.management.base import BaseCommand
from metrics.models import Client

class Command(BaseCommand):
    help = 'List all tenants and their attributes'

    def handle(self, *args, **kwargs):
        tenants = Client.objects.all()
        for tenant in tenants:
            self.stdout.write(f"Name: {tenant.name}, Domain: {tenant.domain_url}")
