# management/commands/run_view_tests.py
from django.core.management.base import BaseCommand
from django.test.runner import DiscoverRunner
import os

class Command(BaseCommand):
    help = 'Runs all tests in the tests/test_views/ directory'

    def handle(self, *args, **options):
        test_dir = 'tests/test_views'
        suite = DiscoverRunner(verbosity=1).build_suite(test_dir)
        runner = DiscoverRunner(verbosity=1)
        runner.run_suite(suite)