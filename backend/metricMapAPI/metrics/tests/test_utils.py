import os
import sys
import time
from io import StringIO
from django.db import connection
from django.test.runner import DiscoverRunner
from django.conf import settings
#from django_tenants.test.cases import TenantTestCase
#from django_tenants.utils import get_public_schema_name, schema_context, get_tenant_model, get_tenant_domain_model
from rest_framework.test import APIClient
#from ..models import *
#from .test_permanent_computations.factories import ClientFactory, DomainFactory
import logging
# from django.db import transaction
# import uuid

logger = logging.getLogger(__name__)

class TestOutputCapture:
    def __init__(self):
        self.output = StringIO()
        self.error = StringIO()
        self.log_capture = StringIO()
        self.handler = None
        self.root_logger = None

    def __enter__(self):
        # Capture stdout and stderr
        self.stdout_capture = sys.stdout
        self.stderr_capture = sys.stderr
        sys.stdout = self.output
        sys.stderr = self.error
        
        # Set up root logger to capture all logs
        self.root_logger = logging.getLogger('')
        self.previous_handlers = self.root_logger.handlers[:]
        self.previous_level = self.root_logger.level
        self.root_logger.setLevel(logging.DEBUG)
        
        # Force all loggers to DEBUG level
        for name in logging.root.manager.loggerDict:
            logger = logging.getLogger(name)
            logger.setLevel(logging.DEBUG)
            logger.propagate = True

        # Create a handler that writes to our StringIO
        self.handler = logging.StreamHandler(self.log_capture)
        self.handler.setLevel(logging.DEBUG)
        
        # Create a formatter that includes the logger name
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)
        
        # Ensure immediate flushing of logs
        self.handler.flush = lambda: None
        
        # Add our handler to the root logger
        self.root_logger.addHandler(self.handler)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.stdout_capture
        sys.stderr = self.stderr_capture
        
        # Remove our handler from the root logger
        if self.root_logger and self.handler:
            self.root_logger.removeHandler(self.handler)
        
        # Restore previous logging configuration
        if self.root_logger:
            self.root_logger.setLevel(self.previous_level)
            for handler in self.previous_handlers:
                self.root_logger.addHandler(handler)
        
        if self.handler:
            self.handler.flush()
        self.log_capture.flush()

    def get_output(self):
        if self.handler:
            self.handler.flush()
        output = self.output.getvalue() + self.error.getvalue() + self.log_capture.getvalue()
        print("Captured output:", output)  # Debug print
        return output

class CustomTestResult(DiscoverRunner.test_runner.resultclass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_results = []
        self.current_test = None
        self.test_run_name = None
        self.show_full_output = False

    def startTest(self, test):
        super().startTest(test)
        self.current_test = {
            'name': self.getDescription(test),
            'start_time': time.time(),
            'output_capture': TestOutputCapture(),
            'status': 'passed',
            'details': '',
            'error': ''
        }
        self.current_test['output_capture'].__enter__()
        logging.getLogger('metrics').debug(f"Starting test: {self.current_test['name']}")

    def stopTest(self, test):
        super().stopTest(test)
        self.current_test['end_time'] = time.time()
        self.current_test['output'] = self.current_test['output_capture'].get_output()
        self.current_test['output_capture'].__exit__(None, None, None)
        self.test_results.append(self.current_test)
        logging.getLogger('metrics').debug(f"Finished test: {self.current_test['name']}")

    def addSuccess(self, test):
        super().addSuccess(test)
        self.current_test['details'] = "All assertions passed successfully."

    def addError(self, test, err):
        super().addError(test, err)
        self.current_test['status'] = 'error'
        self.current_test['error'] = self._exc_info_to_string(err, test)

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.current_test['status'] = 'failure'
        self.current_test['error'] = self._exc_info_to_string(err, test)

    def generate_report(self):
        if self.show_full_output:
            return self.generate_full_report()
        else:
            return self.generate_concise_report()

    def generate_full_report(self):
        total_tests = len(self.test_results)
        passed_tests = sum(1 for test in self.test_results if test['status'] == 'passed')
        failed_tests = sum(1 for test in self.test_results if test['status'] == 'failure')
        error_tests = sum(1 for test in self.test_results if test['status'] == 'error')

        report = f"# Test Run: {self.test_run_name}\n\n"
        report += f"Total tests: {total_tests}\n"
        report += f"Passed: {passed_tests}\n"
        report += f"Failed: {failed_tests}\n"
        report += f"Errors: {error_tests}\n\n"

        for test in self.test_results:
            report += f"## {test['name']}\n"
            report += f"Status: {test['status']}\n"
            report += f"Duration: {test['end_time'] - test['start_time']:.3f} seconds\n\n"
            
            if test['status'] in ['failure', 'error']:
                report += f"### {test['status'].capitalize()}\n"
                report += "```\n"
                report += test['error']
                report += "```\n\n"
            
            report += "### Details\n"
            report += test['details'] + "\n\n"
            
            report += "### Output\n"
            report += "```\n"
            report += test['output']
            report += "```\n\n"

        return report

    def generate_concise_report(self):
        total_tests = len(self.test_results)
        passed_tests = sum(1 for test in self.test_results if test['status'] == 'passed')
        failed_tests = sum(1 for test in self.test_results if test['status'] == 'failure')
        error_tests = sum(1 for test in self.test_results if test['status'] == 'error')

        report = f"# Test Run: {self.test_run_name}\n\n"
        report += f"Total tests: {total_tests}\n"
        report += f"Passed: {passed_tests}\n"
        report += f"Failed: {failed_tests}\n"
        report += f"Errors: {error_tests}\n\n"

        for test in self.test_results:
            if test['status'] in ['failure', 'error']:
                report += f"## {test['name']}\n"
                report += f"Status: {test['status']}\n"
                report += f"Duration: {test['end_time'] - test['start_time']:.3f} seconds\n\n"
                report += f"### {test['status'].capitalize()}\n"
                report += "```\n"
                report += test['error']
                report += "```\n\n"
                report += "### Output\n"
                report += "```\n"
                report += test['output']
                report += "```\n\n"

        return report

class CustomTenantTestRunner(DiscoverRunner):
    def __init__(self, *args, **kwargs):
        self.show_full_output = kwargs.pop('show_full_output', False)
        super().__init__(*args, **kwargs)

    def run_suite(self, suite, **kwargs):
        runner = self.test_runner(
            verbosity=self.verbosity,
            failfast=self.failfast,
            resultclass=CustomTestResult,
        )
        result = runner.run(suite)
        result.test_run_name = kwargs.get('test_run_name')
        result.show_full_output = self.show_full_output
        return result

    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        self.setup_test_environment()
        suite = self.build_suite(test_labels)
        if extra_tests:
            for test in extra_tests:
                suite.addTest(test)
        
        test_run_name = test_labels[0] if test_labels else None
        
        connection.set_schema_to_public()
        
        old_config = self.setup_databases()

        result = self.run_suite(suite, test_run_name=test_run_name)
        
        self.teardown_databases(old_config)
        self.teardown_test_environment()
        
        report = result.generate_report()
        output_dir = getattr(settings, 'TEST_OUTPUT_DIR', '.')
        os.makedirs(output_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        test_name = getattr(result, 'test_run_name', None) or 'unknown'
        filename = os.path.join(output_dir, f'test_report_{test_name}_{timestamp}.md')
        with open(filename, 'w') as f:
            f.write(report)

        print(f"Test report written to {filename}")
        
        return result

'''
class MetricsTestCase(TenantTestCase):
    @classmethod
    def setUpClass(cls):
        logger.info("MetricsTestCase.setUpClass: Starting")
        super().setUpClass()
        connection.set_schema_to_public()
        logger.info(f"MetricsTestCase.setUpClass: Set schema to public. Current schema: {connection.schema_name}")
        
    def setUp(self):
        logger.info("MetricsTestCase.setUp: Starting")
        super().setUp()
        self.schema_name = f"test_{uuid.uuid4().hex[:10]}"
        logger.info(f"MetricsTestCase.setUp: Generated schema name: {self.schema_name}")
        with schema_context('public'):
            logger.info("MetricsTestCase.setUp: Creating tenant in public schema")
            self.tenant_client = ClientFactory(schema_name=self.schema_name)
            self.domain = DomainFactory(tenant=self.tenant_client, domain=f'{self.schema_name}.test.com', is_primary=True)
        connection.set_tenant(self.tenant_client)
        logger.info(f"MetricsTestCase.setUp: Set tenant. Current schema: {connection.schema_name}")
        self.client = APIClient()
        logger.info("MetricsTestCase.setUp: Finished")
    
    def tearDown(self):
        logger.info("MetricsTestCase.tearDown: Starting")
        connection.set_schema_to_public()
        logger.info(f"MetricsTestCase.tearDown: Set schema to public. Current schema: {connection.schema_name}")
        super().tearDown()
        logger.info("MetricsTestCase.tearDown: Finished")

    @transaction.atomic
    def setup_tenant(self):
        self.tenant_client = ClientFactory(schema_name=get_public_schema_name())
        self.domain = DomainFactory(tenant=self.tenant_client, domain='test.com', is_primary=True)
        connection.set_tenant(self.tenant_client)
        self.tenant = self.tenant_client

    def run(self, result=None):
        with transaction.atomic():
            return super().run(result)
'''