from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Metric, HistoricalData
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.pagination import PageNumberPagination
import logging
from metrics.tasks.forecasting_tasks import advanced_trend_analysis_task
from metrics.tasks.impact_tasks import detect_anomalies_task, ab_test_analysis_task
from metrics.tasks.relationships_tasks import pearson_correlation_task
from metrics.tasks.statistics_tasks import probability_analysis_task

logger = logging.getLogger(__name__)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class TrendAnalysisView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, metric_id):
        try:
            metric = Metric.objects.get(id=metric_id)
            historical_data = HistoricalData.objects.filter(metric=metric).order_by('date').values('date', 'value')
            
            task = advanced_trend_analysis_task.delay(list(historical_data))
            result = task.get()  # This will wait for the task to complete. In production, you might want to handle this asynchronously.
            
            return Response({
                'metric': metric.name,
                'trend': result['trend'],
                'seasonal': result['seasonal'],
                'residual': result['residual']
            })
        except ObjectDoesNotExist:
            return Response({"error": "Metric not found"}, status=status.HTTP_404_NOT_FOUND)

class AnomalyDetectionView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, metric_id):
        try:
            metric = Metric.objects.get(id=metric_id)
            historical_data = HistoricalData.objects.filter(metric=metric).order_by('date').values('date', 'value')
            
            task = detect_anomalies_task.delay(list(historical_data))
            result = task.get()
            
            return Response({
                'metric': metric.name,
                'anomalies': result['anomalies']
            })
        except ObjectDoesNotExist:
            return Response({"error": "Metric not found"}, status=status.HTTP_404_NOT_FOUND)

class CorrelationAnalysisView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        metric_a_id = request.data.get('metric_a')
        metric_b_id = request.data.get('metric_b')

        try:
            metric_a = Metric.objects.get(id=metric_a_id)
            metric_b = Metric.objects.get(id=metric_b_id)

            data_a = list(HistoricalData.objects.filter(metric=metric_a).order_by('date').values_list('value', flat=True))
            data_b = list(HistoricalData.objects.filter(metric=metric_b).order_by('date').values_list('value', flat=True))

            task = pearson_correlation_task.delay(data_a, data_b)
            result = task.get()

            return Response({
                'metric_a': metric_a.name,
                'metric_b': metric_b.name,
                'correlation': result['correlation'],
                'data_points': result['data_points']
            })
        except ObjectDoesNotExist:
            return Response({"error": "One or both metrics not found"}, status=status.HTTP_404_NOT_FOUND)

class ProbabilityAnalysisView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, metric_id):
        try:
            metric = Metric.objects.get(id=metric_id)
            historical_data = list(HistoricalData.objects.filter(metric=metric).order_by('date').values('date', 'value'))

            task = probability_analysis_task.delay(historical_data)
            result = task.get()

            return Response(result)
        except ObjectDoesNotExist:
            return Response({"error": "Metric not found"}, status=status.HTTP_404_NOT_FOUND)

