from rest_framework import permissions
from rest_framework.response import Response
from ..models import Metric, HistoricalData
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
import logging
from metrics.tasks.forecasting_tasks import (
    generate_daily_forecast_task, 
    forecast_vs_actual_task, 
    performance_scenario_modeling_task,
    goal_cascading_task,
    predictive_goal_setting_task
)

logger = logging.getLogger(__name__)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ComparativePerformanceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        metric_ids = request.GET.getlist('metric_ids')
        try:
            metrics = Metric.objects.filter(id__in=metric_ids)
            data = {}
            for metric in metrics:
                historical_data = list(HistoricalData.objects.filter(metric=metric).order_by('date').values('date', 'value'))
                data[metric.name] = historical_data

            # Assuming you have a task for comparative performance
            task = comparative_performance_task.delay(data)
            result = task.get()

            return Response(result)
        except ObjectDoesNotExist:
            return Response({"error": "One or more metrics not found"}, status=status.HTTP_404_NOT_FOUND)

class ForecastVsActualView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, metric_id):
        try:
            metric = Metric.objects.get(id=metric_id)
            historical_data = list(HistoricalData.objects.filter(metric=metric).order_by('date').values('date', 'value'))

            task = forecast_vs_actual_task.delay(historical_data)
            result = task.get()

            return Response({
                'metric': metric.name,
                'forecast_vs_actual': result
            })
        except ObjectDoesNotExist:
            return Response({"error": "Metric not found"}, status=status.HTTP_404_NOT_FOUND)

class PerformanceScenarioModelingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        scenario_data = request.data
        task = performance_scenario_modeling_task.delay(scenario_data)
        result = task.get()
        return Response(result)

class GoalCascadingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        organization_goal = request.data
        task = goal_cascading_task.delay(organization_goal)
        result = task.get()
        return Response(result)

class PredictiveGoalSettingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, metric_id):
        try:
            metric = Metric.objects.get(id=metric_id)
            historical_data = list(HistoricalData.objects.filter(metric=metric).order_by('date').values('date', 'value'))
            task = predictive_goal_setting_task.delay(historical_data)
            result = task.get()
            return Response(result)
        except ObjectDoesNotExist:
            return Response({"error": "Metric not found"}, status=status.HTTP_404_NOT_FOUND)

class DailyForecastView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, metric_id):
        try:
            metric = Metric.objects.get(id=metric_id)
            historical_data = list(HistoricalData.objects.filter(metric=metric).order_by('date').values('date', 'value'))

            task = generate_daily_forecast_task.delay(historical_data)
            result = task.get()

            return Response({
                'metric': metric.name,
                'forecast': result
            })
        except ObjectDoesNotExist:
            return Response({"error": "Metric not found"}, status=status.HTTP_404_NOT_FOUND)