import sys
import os
from pathlib import Path
import django
from django.conf import settings

# Get the absolute path of the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Add the project root and the app directory to the Python path
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / 'metrics'))

def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metricMapAPI.settings')
    django.setup()

    # Configure the test database
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }

    # Add any additional test-specific settings here
    settings.DEBUG = True
    settings.TENANT_DB_ALIAS = 'default'

import pytest

@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

pytest_plugins = [
    "pytest_django",
]

# Remove pytest-bdd if you're not using it
# If you are using it, make sure it's installed: pip install pytest-bdd
# pytest_plugins = [
#     "pytest_django",
#     "pytest_bdd",
# ]