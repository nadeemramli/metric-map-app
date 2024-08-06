import sys
import os
from pathlib import Path
import django
from django.conf import settings

# Get the absolute path of the project root (two levels up from the current directory)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent

# Add the project root and the app directory to the Python path
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / 'metricMapAPI'))

# Print the system path and project structure for debugging
print("Python sys.path:")
for path in sys.path:
    print(path)

print("\nProject structure:")
for root, dirs, files in os.walk(PROJECT_ROOT):
    level = root.replace(str(PROJECT_ROOT), '').count(os.sep)
    indent = ' ' * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    sub_indent = ' ' * 4 * (level + 1)
    for file in files:
        print(f"{sub_indent}{file}")

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