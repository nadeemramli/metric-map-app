# backend/metricMapAPI/middleware.py
from django_tenants.utils import get_tenant_model, get_tenant_database_alias, get_public_schema_name
from metrics.models import Domain
from django.db import connection
from django_tenants.middleware.main import TenantMainMiddleware
from django_tenants.middleware import TenantMiddleware
from django.http import Http404

class ProjectMiddleware(TenantMainMiddleware):
    def get_tenant(self, domain_model, hostname):
        project = domain_model.objects.get(domain=hostname).tenant
        return project

class TenantMiddleware(TenantMainMiddleware):
    def process_request(self, request):
        # This is necessary for django_tenants to set up the connection
        connection.set_schema_to_public()
        hostname = self.hostname_from_request(request)

        TenantModel = get_tenant_model()
        try:
            domain = Domain.objects.select_related('tenant').get(domain=hostname)
            tenant = domain.tenant
        except Domain.DoesNotExist:
            try:
                tenant = TenantModel.objects.get(schema_name=get_public_schema_name())
            except TenantModel.DoesNotExist:
                raise Http404("No tenant for hostname '%s'" % hostname)

        tenant.domain_url = hostname
        request.tenant = tenant
        connection.set_tenant(request.tenant)
        return None

class CustomTenantMiddleware(TenantMainMiddleware):
    def process_request(self, request):
        connection.set_schema_to_public()
        hostname = self.hostname_from_request(request)
        
        try:
            domain = Domain.objects.select_related('tenant').get(domain=hostname)
            tenant = domain.tenant
        except Domain.DoesNotExist:
            tenant = self.get_tenant_for_public_domain(hostname)

        if tenant:
            request.tenant = tenant
            connection.set_tenant(request.tenant)
        else:
            return self.no_tenant_found(request, hostname)

        return None

    def get_tenant_for_public_domain(self, hostname):
        public_schema_name = get_public_schema_name()
        TenantModel = get_tenant_model()
        try:
            return TenantModel.objects.get(schema_name=public_schema_name)
        except TenantModel.DoesNotExist:
            return None