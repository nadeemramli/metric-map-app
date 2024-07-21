from django.core.management.base import BaseCommand
from django.core.cache import cache

class Command(BaseCommand):
    help = 'Clears the entire cache'

    def handle(self, *args, **kwargs):
        cache.clear()
        self.stdout.write(self.style.SUCCESS('Successfully cleared cache'))

# Save this in a file named 'clear_cache.py' in one of your app's management/commands/ directory
# Then run: python manage.py clear_cache