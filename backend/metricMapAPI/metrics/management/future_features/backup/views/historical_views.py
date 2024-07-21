from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import HistoricalData, Metric
from ..serializers import HistoricalDataSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
import logging
from django.core.exceptions import ObjectDoesNotExist
from metrics.tasks.statistics_tasks import calculate_aggregated_views, advanced_statistics_task

logger = logging.getLogger(__name__)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class HistoricalDataViewSet(viewsets.ModelViewSet):
    queryset = HistoricalData.objects.all()
    serializer_class = HistoricalDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    @action(detail=False, methods=['post'])
    def bulk_import(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def metric_history(self, request):
        metric_id = request.query_params.get('metric_id')
        if not metric_id:
            return Response({"error": "metric_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.get_queryset().filter(metric_id=metric_id).order_by('date')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        logger.info(f"GET request to HistoricalViewSet. Query params: {self.request.query_params}")
        queryset = HistoricalData.objects.all()
        metric_id = self.request.query_params.get('metric', None)
        if metric_id is not None:
            queryset = queryset.filter(metric_id=metric_id)
        return queryset

    def perform_create(self, serializer):
        logger.info(f"POST request to HistoricalViewSet. Data: {self.request.data}")
        serializer.save()

    def list(self, request, *args, **kwargs):
        logger.info(f"LIST request to HistoricalViewSet. Query params: {request.query_params}")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        logger.info(f"CREATE request to HistoricalViewSet. Data: {request.data}")
        return super().create(request, *args, **kwargs)

class AggregatedViewsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    @method_decorator(cache_page(60*60))
    def get(self, request, metric_id):
        try:
            metric = Metric.objects.get(id=metric_id)
            historical_data = list(HistoricalData.objects.filter(metric=metric).order_by('date').values('date', 'value'))
            
            task = calculate_aggregated_views.delay(historical_data)
            result = task.get()
            
            return Response({
                'metric': metric.name,
                'monthly_aggregation': result['monthly_aggregation'],
                'yearly_aggregation': result['yearly_aggregation']
            })
        except ObjectDoesNotExist:
            return Response({"error": "Metric not found"}, status=status.HTTP_404_NOT_FOUND)

class AdvancedStatisticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, metric_id):
        try:
            metric = Metric.objects.get(id=metric_id)
            historical_data = list(HistoricalData.objects.filter(metric=metric).order_by('date').values('date', 'value'))

            task = advanced_statistics_task.delay(historical_data)
            result = task.get()

            return Response(result)
        except ObjectDoesNotExist:
            return Response({"error": "Metric not found"}, status=status.HTTP_404_NOT_FOUND)