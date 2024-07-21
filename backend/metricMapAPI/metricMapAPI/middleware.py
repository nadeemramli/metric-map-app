# backend/metricMapAPI/middleware.py
from django_tenants.middleware.main import TenantMainMiddleware
from metrics.models import Domain

class ProjectMiddleware(TenantMainMiddleware):
    def get_tenant(self, domain_model, hostname):
        project = domain_model.objects.get(domain=hostname).tenant
        return project

class TenantMiddleware(TenantMainMiddleware):
    def get_tenant(self, model, hostname, request):
        return model.objects.get(domain_url=hostname)
