# metrics/management/commands/stress_test.py
from django.core.management.base import BaseCommand
from django.test import Client
from django.urls import reverse
from metrics.models import Metric
import time
import multiprocessing

def make_request(url):
    client = Client()
    start_time = time.time()
    response = client.get(url)
    end_time = time.time()
    return end_time - start_time

class Command(BaseCommand):
    help = 'Runs a stress test on the API'

    def handle(self, *args, **options):
        metric = Metric.objects.first()
        url = reverse('anomaly-detection', kwargs={'metric_id': metric.id})
        
        num_requests = 1000
        num_processes = 4
        
        pool = multiprocessing.Pool(processes=num_processes)
        results = pool.map(make_request, [url] * num_requests)
        
        avg_time = sum(results) / len(results)
        self.stdout.write(self.style.SUCCESS(f'Average response time: {avg_time:.4f} seconds'))