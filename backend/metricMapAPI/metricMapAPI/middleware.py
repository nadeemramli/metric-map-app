# backend/metricMapAPI/middleware.py
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore
from django.http import Http404, JsonResponse
from django_tenants.utils import get_tenant_model, get_public_schema_name, schema_context, tenant_context
from metrics.models import Client
from django.db import connection
from django_tenants.middleware.main import TenantMainMiddleware
import json
from metrics import logger

class LoggingMiddleware:
       def __init__(self, get_response):
           self.get_response = get_response

       def __call__(self, request):
           logger.info(f"Incoming request: {request.method} {request.path}")
           response = self.get_response(request)
           logger.info(f"Outgoing response: {response.status_code}")
           return response

class CustomTenantMiddleware(TenantMainMiddleware):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.get_response = get_response

    def __call__(self, request):
        hostname = self.hostname_from_request(request)
        logger.debug(f"[CustomTenantMiddleware: __call__] Processing request for hostname: {hostname}")
        logger.debug(f"[CustomTenantMiddleware: __call__] Request path: {request.path}")
        logger.debug(f"[CustomTenantMiddleware: __call__] Initial schema: {connection.schema_name}")
        
        # Identify tenant as early as possible
        tenant = self.get_tenant(request, hostname)

        if tenant:
            logger.info(f"[CustomTenantMiddleware: __call__] Identified tenant: {tenant.schema_name}")
            # Ensure entire request processing happens within the correct tenant context
            with tenant_context(tenant):
                logger.debug(f"[CustomTenantMiddleware: __call__] Entered tenant context: {connection.schema_name}")
                request.tenant = tenant
                logger.info(f"[CustomTenantMiddleware: __call__] Set active tenant: {tenant.schema_name}")

                # Check if it's an admin request
                if request.path.startswith('/admin/'):
                    logger.info(f"[CustomTenantMiddleware: __call__] Admin request detected for tenant: {tenant.schema_name}")

                logger.debug(f"[CustomTenantMiddleware: __call__] Before get_response, schema: {connection.schema_name}")
                response = self.get_response(request)
                logger.debug(f"[CustomTenantMiddleware: __call__] After get_response, schema: {connection.schema_name}")

                # Update session with correct schema name
                if hasattr(request, 'session'):
                    session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME)
                    logger.debug(f"[CustomTenantMiddleware: __call__] Session key from cookie: {session_key}")
                    logger.debug(f"[CustomTenantMiddleware: __call__] Current schema before session handling: {connection.schema_name}")
                    if not session_key:
                        logger.debug(f"[CustomTenantMiddleware: __call__] No session key in cookie, creating new session")
                        request.session = SessionStore()
                    else:
                        logger.debug(f"[CustomTenantMiddleware: __call__] Existing session key found")
                    request.session['schema_name'] = tenant.schema_name
                    try:
                        logger.debug(f"[CustomTenantMiddleware: __call__] Attempting to save session in schema: {connection.schema_name}")
                        request.session.save()
                        logger.debug(f"[CustomTenantMiddleware: __call__] Session saved successfully")
                    except Exception as e:
                        logger.error(f"[CustomTenantMiddleware: __call__] Failed to save session: {str(e)}", exc_info=True)
                
                logger.debug(f"[CustomTenantMiddleware: __call__] Exiting tenant context")
                logger.debug(f"[CustomTenantMiddleware: __call__] Final schema for request: {connection.schema_name}")
                return response
        else:
            logger.warning(f"[CustomTenantMiddleware: __call__] No tenant found for {hostname}, using public schema")
            request.tenant = None
            connection.set_schema_to_public()
            logger.debug(f"[CustomTenantMiddleware: __call__] Set to public schema: {connection.schema_name}")
            return self.get_response(request)

    def get_tenant(self, request, hostname):
        TenantModel = get_tenant_model()
        logger.debug(f"[CustomTenantMiddleware: get_tenant] Attempting to identify tenant for hostname: {hostname}")
        logger.debug(f"[CustomTenantMiddleware: get_tenant] Attempting to identify the tenant: {TenantModel}")

        # 1. Check domain
        try:
            tenant = TenantModel.objects.get(domain_url=hostname)
            logger.info(f"[CustomTenantMiddleware: get_tenant] Tenant identified from domain_url: {tenant.schema_name}")
            return tenant
        except TenantModel.DoesNotExist:
            logger.warning(f"[CustomTenantMiddleware: get_tenant] No tenant found for hostname: {hostname}")

        # 2. Check header
        tenant_name = request.headers.get("Tenant-Header")
        if tenant_name:
            logger.debug(f"[CustomTenantMiddleware: get_tenant] Found Tenant-Header: {tenant_name}")
            try:
                tenant = TenantModel.objects.get(name__iexact=tenant_name)
                logger.info(f"[CustomTenantMiddleware: get_tenant] Tenant identified from header: {tenant.schema_name}")
                return tenant
            except TenantModel.DoesNotExist:
                logger.error(f"[CustomTenantMiddleware: get_tenant] Tenant not found for header: {tenant_name}")

        # 3. Check sessio
        session_schema = self.get_session_schema(request)
        if session_schema:
            logger.debug(f"[CustomTenantMiddleware: get_tenant] Found schema in session: {session_schema}")
            try:
                tenant = TenantModel.objects.get(schema_name=session_schema)
                logger.info(f"[CustomTenantMiddleware: get_tenant] Tenant identified from session: {tenant.schema_name}")
                return tenant
            except TenantModel.DoesNotExist:
                logger.warning(f"[CustomTenantMiddleware: get_tenant] Session schema {session_schema} not found in database")
        
        # 4. Check for public domain
        public_tenant = self.get_tenant_for_public_domain(hostname)
        if public_tenant:
            logger.info(f"[CustomTenantMiddleware: get_tenant] Using public tenant: {public_tenant.schema_name}")
            return public_tenant

        logger.error(f"[CustomTenantMiddleware: get_tenant] No tenant could be identified for hostname: {hostname}")
        return None

    def get_tenant_for_public_domain(self, hostname):
        if hostname in ['localhost', '127.0.0.1']:
            public_schema_name = get_public_schema_name()
            TenantModel = get_tenant_model()
            try:
                public_tenant = TenantModel.objects.get(schema_name=public_schema_name)
                logger.info(f"[CustomTenantMiddleware: get_public_tenant] Found public tenant: {public_schema_name}")
                return public_tenant
            except TenantModel.DoesNotExist:
                logger.error(f"[CustomTenantMiddleware: get_public_tenant] Public tenant not found: {public_schema_name}")
        return None

    def get_session_schema(self, request):
        if hasattr(request, 'session') and 'schema_name' in request.session:
            return request.session['schema_name']
        return get_public_schema_name()
    
    def setup_url_routing(self, request):
        if (not hasattr(request, 'tenant') or 
            request.tenant is None or 
            request.tenant.schema_name == get_public_schema_name()):
            request.urlconf = settings.PUBLIC_SCHEMA_URLCONF
            logger.debug(f"[CustomTenantMiddleware: setup_url_routing] Set urlconf to PUBLIC_SCHEMA_URLCONF")
        return None

    def process_request(self, request):
        hostname = self.hostname_from_request(request)
        logger.debug(f"[CustomTenantMiddleware: process_request] Processing request for hostname: {hostname}")

        tenant = self.get_tenant(request, hostname)

        if tenant:
            with schema_context(tenant.schema_name):
                request.tenant = tenant
                connection.set_tenant(tenant)
                logger.info(f"[CustomTenantMiddleware: process_request] Set tenant: {tenant.schema_name}")
                logger.debug(f"[CustomTenantMiddleware: process_request] Current schema: {connection.schema_name}")
                
                # Ensure the session is associated with the correct schema
                if hasattr(request, 'session'):
                    request.session['schema_name'] = tenant.schema_name
                    request.session.save()
        else:
            logger.warning(f"[CustomTenantMiddleware: process_request] No tenant found, using public schema")
            request.tenant = None
            connection.set_schema_to_public()

        logger.debug(f"[CustomTenantMiddleware: process_request] Final schema for request: {connection.schema_name}")
        return self.setup_url_routing(request)


class RequestResponseLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log request
        #logger.info(f"Request: {request.method} {request.path}")
        #logger.debug(f"Request headers: {dict(request.headers)}")
        #logger.debug(f"Request body: {request.body.decode('utf-8')}")

        response = self.get_response(request)

        # Log response
        #logger.info(f"Response status: {response.status_code}")
        #logger.debug(f"Response headers: {dict(response.headers)}")
        
        # Be careful with logging response content, as it might be sensitive
        #if response['Content-Type'] == 'application/json':
            # logger.debug(f"Response content: {json.loads(response.content)}")

        return response