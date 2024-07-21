from django.core.management.base import BaseCommand
from django_tenants.utils import schema_context
from metrics.models import Client, Domain

class Command(BaseCommand):
    help = 'Creates a new tenant'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the tenant')
        parser.add_argument('subdomain', type=str, help='Subdomain for the tenant')

    def handle(self, *args, **options):
        schema_name = options['name'].lower()
        subdomain = options['subdomain'].lower()

        with schema_context('public'):
            if Client.objects.filter(schema_name=schema_name).exists():
                self.stdout.write(self.style.ERROR(f'Tenant {schema_name} already exists'))
                return

            client = Client(schema_name=schema_name, name=options['name'])
            client.save()

            domain = Domain()
            domain.domain = f'{subdomain}.localhost'
            domain.tenant = client
            domain.is_primary = True
            domain.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created tenant {schema_name} with domain {subdomain}.localhost'))
        
"""
Now you can create a new tenant using:
Copy
python manage.py create_tenant "Tenant Name" subdomain
"""