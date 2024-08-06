from .settings import *

import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Add the virtual environment site-packages to the Python path
venv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'venv')
site_packages_path = os.path.join(venv_path, 'lib', 'python3.10', 'site-packages')
sys.path.insert(0, site_packages_path)

print("Python path:", sys.path)
print("Installed apps:", INSTALLED_APPS)

# Check if django_tenants can be imported
try:
    import django_tenants
    print("django_tenants imported successfully from:", django_tenants.__file__)
except ImportError as e:
    print("Failed to import django_tenants:", str(e))
    print("Searching for django_tenants in sys.path:")
    for path in sys.path:
        if os.path.exists(os.path.join(path, 'django_tenants')):
            print("Found django_tenants in:", path)
        elif os.path.exists(os.path.join(path, 'django_tenants.py')):
            print("Found django_tenants.py in:", path)