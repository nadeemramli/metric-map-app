# backend/metricMapAPI/utils/tenant_context.py
from threading import local

_thread_locals = local()

def set_current_tenant(tenant):
    _thread_locals.tenant = tenant

def get_current_tenant():
    return getattr(_thread_locals, 'tenant', None)
