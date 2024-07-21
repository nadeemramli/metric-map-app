import os
import sys
import time
import uuid
import time
from io import StringIO
from django.db import connection
from django.test.runner import DiscoverRunner
from django.conf import settings
from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient
from django_tenants.utils import get_public_schema_name, schema_context, get_tenant_model, get_tenant_domain_model
from rest_framework.test import APIClient
from django_tenants.test.client import TenantClient
from ..models import Client, Domain

class TenantAPIClient(TenantClient, APIClient):
    pass

class CustomTenantTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        connection.set_schema_to_public()
        return super().setup_databases(**kwargs)

    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        self.setup_test_environment()
        suite = self.build_suite(test_labels)
        if extra_tests:
            for test in extra_tests:
                suite.addTest(test)
        old_config = self.setup_databases()
        
        connection.set_schema_to_public()
        
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        output = StringIO()
        sys.stdout = sys.stderr = output
        
        start_time = time.time()
        result = self.run_suite(suite)
        time_taken = time.time() - start_time
        
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        
        self.teardown_databases(old_config)
        self.teardown_test_environment()
        
        # Write output to file
        output_dir = getattr(settings, 'TEST_OUTPUT_DIR', '.')
        os.makedirs(output_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = os.path.join(output_dir, f'test_report_{timestamp}.txt')
        with open(filename, 'w') as f:
            f.write(f"Ran {suite.countTestCases()} tests in {time_taken:.3f} seconds\n\n")
            f.write(output.getvalue())
            f.write(f"\nTest Result: {'Success' if result.wasSuccessful() else 'Failure'}\n")
            f.write(f"Errors: {len(result.errors)}\n")
            f.write(f"Failures: {len(result.failures)}\n")
        
        print(f"Test report written to {filename}")
        
        return result

""""
class MetricsTestCase(TenantTestCase):
    @classmethod
    def setUpClass(cls):
        cls.public_schema_name = get_public_schema_name()
        connection.set_schema_to_public()
        
        # Use a unique schema name for each test run
        cls.schema_name = f'test_{uuid.uuid4().hex[:10]}'
        
        # Create the tenant with the unique schema name
        cls.tenant = get_tenant_model()(schema_name=cls.schema_name)
        cls.tenant.save()

        # Create the tenant's domain
        domain = get_tenant_domain_model()(tenant=cls.tenant, domain=f'{cls.schema_name}.localhost', is_primary=True)
        domain.save()

        # Now call super().setUpClass()
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        connection.set_schema_to_public()
        # Make sure to delete the tenant and its related objects
        if hasattr(cls, 'tenant'):
            cls.tenant.delete(force_drop=True)
        super().tearDownClass()

    def setUp(self):
        self.client = TenantAPIClient(self.tenant)
        connection.set_tenant(self.tenant)
        super().setUp()
"""
class MetricsTestCase(TenantTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        connection.set_schema_to_public()
        
    def setUp(self):
        super().setUp()
        self.tenant_client = Client.objects.create(schema_name=get_public_schema_name(),
                                                   name='Test Client')
        self.domain = Domain.objects.create(domain='test.com', 
                                            tenant=self.tenant_client,
                                            is_primary=True)
        connection.set_tenant(self.tenant_client)
        self.client = APIClient()

    def tearDown(self):
        connection.set_schema_to_public()
        super().tearDown()