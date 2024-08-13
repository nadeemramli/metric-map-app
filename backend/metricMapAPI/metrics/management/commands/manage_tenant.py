from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from django.db import transaction
from django_tenants.utils import schema_context
from metrics.models import Client, Project, CustomUser
import re
from django.utils import timezone

class Command(BaseCommand):
    help = 'Creates or edits a tenant'

    def add_arguments(self, parser):
        parser.add_argument('action', type=str, choices=['create', 'edit'], help="Action to perform: 'create' or 'edit'")

    def handle(self, *args, **options):
        action = options['action'].lower()

        if action == 'create':
            name = options.get('name') or input("Enter the tenant name: ")
            domain_url = options.get('domain_url') or input("Enter the domain URL: ")
            result = self.create_tenant(name, domain_url)
            self.stdout.write(self.style.SUCCESS(result))
        elif action == 'edit':
            self.edit_tenant()
        else:
            self.stdout.write(self.style.ERROR("Invalid action. Please choose 'create' or 'edit'."))

    def create_tenant(self, name, domain_url):
        schema_name = name.lower().replace(' ', '_')

        if not re.match(r'^[a-z0-9.-]+$', domain_url):
            raise ValidationError('Domain URL can only contain lowercase letters, numbers, dots, and hyphens')

        try:
            with transaction.atomic():
                with schema_context('public'):
                    if Client.objects.filter(schema_name=schema_name).exists():
                        raise ValidationError(f'Tenant {schema_name} already exists')

                    client = Client(schema_name=schema_name, name=name, domain_url=domain_url)
                    client.save()

            return f'Successfully created tenant {schema_name} with domain {domain_url}'
        except Exception as e:
            raise ValidationError(f'Error creating tenant: {str(e)}')

    def edit_tenant(self):
        with schema_context('public'):
            clients = Client.objects.all()
            self.stdout.write("Available clients:")
            for client in clients:
                with schema_context(client.schema_name):
                    projects_count = Project.objects.filter(tenant=client).count()
                    users_count = CustomUser.objects.filter(tenant=client).count()
                self.stdout.write(f"- {client.name} (Schema: {client.schema_name})")
                self.stdout.write(f"  Domain URL: {client.domain_url}")
                self.stdout.write(f"  Created: {client.created_on}")
                self.stdout.write(f"  Projects: {projects_count}")
                self.stdout.write(f"  Users: {users_count}")
                self.stdout.write("")

        schema_name = input("Enter the schema name of the tenant you want to edit: ")

        try:
            with schema_context('public'):
                client = Client.objects.get(schema_name=schema_name)
                
                new_name = input(f"Enter new name (current: {client.name}, press enter to keep current): ")
                if new_name:
                    client.name = new_name

                new_domain_url = input(f"Enter new domain URL (current: {client.domain_url}, press enter to keep current): ")
                if new_domain_url:
                    if not re.match(r'^[a-z0-9.-]+$', new_domain_url):
                        raise ValidationError('Domain URL can only contain lowercase letters, numbers, dots, and hyphens')
                    client.domain_url = new_domain_url

                client.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully updated tenant {schema_name}'))
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Tenant {schema_name} does not exist'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error editing tenant: {str(e)}'))