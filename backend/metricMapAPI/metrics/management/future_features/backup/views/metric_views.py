import logging
from rest_framework import viewsets, status
from rest_framework.decorators import action 
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import HttpResponse
from ..models import Tag, Metric, Connection, HistoricalData, ActionRemark
from ..serializers import MetricSerializer, ConnectionSerializer, ActionRemarkSerializer
from rest_framework.pagination import PageNumberPagination
import logging
from rest_framework.views import APIView
from metrics.tasks.utils_tasks import generate_automated_suggestions, update_historical_data


logger = logging.getLogger(__name__)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

def home(request):
    return HttpResponse("Welcome to the Metric Map App API!")

class CustomTokenObtainPairView(TokenObtainPairView):
    pass

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class MetricViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        queryset = Metric.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(date__range=[start_date, end_date])
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        logger.info(f"Retrieving metric with pk: {kwargs.get('pk')}")
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        logger.info(f"Serialized data: {serializer.data}")
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        metric = serializer.save()
        tags_data = self.request.data.get('tags', [])
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            metric.tags.add(tag)
        metric.save()

    @action(detail=True, methods=['get'])
    def connections(self, request, pk=None):
        logger.info(f"Fetching connections for metric with pk: {pk}")
        metric = self.get_object()
        connections = Connection.objects.filter(from_metric=metric) | Connection.objects.filter(to_metric=metric)
        serializer = ConnectionSerializer(connections, many=True)
        logger.info(f"Connections data: {serializer.data}")
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)   

class MetricFeedbackView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, metric_id):
        feedback_data = request.data
        saved_feedback = self.save_feedback(metric_id, feedback_data)
        
        task = generate_automated_suggestions.delay(metric_id)
        automated_suggestions = task.get()  # In production, consider handling this asynchronously
        
        return Response({
            'saved_feedback': saved_feedback,
            'automated_suggestions': automated_suggestions
        })

    def save_feedback(self, metric_id, feedback_data):
        # Implement feedback saving logic
        pass

class SourceManagementView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        metric_id = request.data.get('metric_id')
        source = request.data.get('source')
        historical_data = request.data.get('historical_data')

        task = update_historical_data.delay(metric_id, source, historical_data)
        result = task.get()  # In production, consider handling this asynchronously

        return Response(result)