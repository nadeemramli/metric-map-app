import sys
import time
from io import StringIO
from django.test.runner import DiscoverRunner
from django.conf import settings
import os

class FileOutputTestRunner(DiscoverRunner):
    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        self.setup_test_environment()
        suite = self.build_suite(test_labels)
        if extra_tests:
            for test in extra_tests:
                suite.addTest(test)
        old_config = self.setup_databases()
        
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
        
        return self.suite_result(suite, result)

__test__ = False  # This tells Django not to treat this file as a test file