from django.core.management.base import BaseCommand
from django.test.utils import get_runner
from django.conf import settings
import sys

class Command(BaseCommand):
    help = 'Runs the test suite with option for full or concise output'

    def add_arguments(self, parser):
        parser.add_argument(
            '--full-output',
            action='store_true',
            help='Show full test output including passed tests',
        )
        parser.add_argument(
            'test_labels',
            nargs='*',
            help='Test labels to run',
        )

    def handle(self, *args, **options):
        TestRunner = get_runner(settings)
        test_runner = TestRunner(
            verbosity=2,  # Increase verbosity
            show_full_output=options['full_output']
        )
        test_labels = options['test_labels'] or ['metrics']
        failures = test_runner.run_tests(test_labels)
        sys.exit(bool(failures))