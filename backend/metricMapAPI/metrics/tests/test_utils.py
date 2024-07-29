import os
import sys
import time
import uuid
from io import StringIO
from django.db import connection
from django.test.runner import DiscoverRunner
from django.conf import settings
from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient
from django_tenants.utils import get_public_schema_name, schema_context, get_tenant_model, get_tenant_domain_model
from rest_framework.test import APIClient
from ..models import Client, Domain

class TenantAPIClient(TenantClient, APIClient):
    pass

class CustomTestResult(DiscoverRunner.test_runner.resultclass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_run_name = None

    def startTestRun(self):
        super().startTestRun()
        self._start_time = time.time()

    def stopTestRun(self):
        self._stop_time = time.time()
        super().stopTestRun()

    @property
    def run_time(self):
        return self._stop_time - self._start_time

class CustomTenantTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        connection.set_schema_to_public()
        return super().setup_databases(**kwargs)

    def run_suite(self, suite, **kwargs):
        test_run_name = kwargs.pop('test_run_name', None)
        runner = self.test_runner(
            verbosity=self.verbosity,
            failfast=self.failfast,
            resultclass=CustomTestResult,
        )
        result = runner.run(suite)
        result.test_run_name = test_run_name
        return result

    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        self.setup_test_environment()
        suite = self.build_suite(test_labels)
        if extra_tests:
            for test in extra_tests:
                suite.addTest(test)
        
        test_run_name = test_labels[0] if test_labels else None  # Use the first test label as the run name
        
        connection.set_schema_to_public()
        
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        output = StringIO()
        sys.stdout = sys.stderr = output
        
        old_config = self.setup_databases()
        result = self.run_suite(suite, test_run_name=test_run_name)
        
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        
        self.teardown_databases(old_config)
        self.teardown_test_environment()
        
        # Write output to file
        output_dir = getattr(settings, 'TEST_OUTPUT_DIR', '.')
        os.makedirs(output_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        test_name = getattr(result, 'test_run_name', None) or 'unknown'
        filename = os.path.join(output_dir, f'test_report_{test_name}_{timestamp}.txt')
        with open(filename, 'w') as f:
            f.write(f"Test Run: {test_name}\n")
            f.write(f"Ran {suite.countTestCases()} tests in {getattr(result, 'run_time', 0):.3f} seconds\n\n")
            f.write(output.getvalue())
            f.write(f"\nTest Result: {'Success' if result.wasSuccessful() else 'Failure'}\n")
            f.write(f"Errors: {len(result.errors)}\n")
            f.write(f"Failures: {len(result.failures)}\n")
        
        print(f"Test report written to {filename}")
        
        return result

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