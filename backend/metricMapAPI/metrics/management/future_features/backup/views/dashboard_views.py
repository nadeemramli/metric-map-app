from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Dashboard, Metric, HistoricalData, Report
from ..serializers import DashboardSerializer
from rest_framework.pagination import PageNumberPagination
import logging
from metrics.tasks.utils_tasks import decision_support_dashboard_task, performance_dashboard_task

logger = logging.getLogger(__name__)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = [permissions.IsAuthenticated]

class PerformanceDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, metric_id):
        try:
            metric = Metric.objects.get(id=metric_id)
            historical_data = list(HistoricalData.objects.filter(metric=metric).order_by('date').values('date', 'value'))

            task = performance_dashboard_task.delay(historical_data)
            result = task.get()

            return Response(result)
        except ObjectDoesNotExist:
            return Response({"error": "Metric not found"}, status=status.HTTP_404_NOT_FOUND)

class DecisionSupportDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Assuming you have a way to get all relevant data for the dashboard
        all_data = self.get_all_dashboard_data()
        
        task = decision_support_dashboard_task.delay(all_data)
        result = task.get()
        
        return Response(result)

    def get_all_dashboard_data(self):
        # Implement logic to fetch all necessary data for the dashboard
        pass

class InspirationGalleryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dashboards = Dashboard.objects.all()[:5]  # Get top 5 dashboards
        reports = Report.objects.all()[:5]  # Get top 5 reports

        gallery_items = {
            'dashboards': [
                {
                    'name': dashboard.name,
                    'layout': dashboard.layout
                } for dashboard in dashboards
            ],
            'reports': [
                {
                    'name': report.name,
                    'configuration': report.configuration
                } for report in reports
            ]
        }

        return Response(gallery_items)

class StakeholderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        role = request.query_params.get('role', 'default')
        
        if role == 'executive':
            data = self.get_executive_view()
        elif role == 'manager':
            data = self.get_manager_view()
        elif role == 'analyst':
            data = self.get_analyst_view()
        else:
            data = self.get_default_view()

        return Response(data)

    def get_executive_view(self):
        # Fetch high-level KPIs and summary data
        pass

    def get_manager_view(self):
        # Fetch team-specific metrics and performance data
        pass

    def get_analyst_view(self):
        # Fetch detailed metrics and raw data
        pass

    def get_default_view(self):
        # Fetch general overview of metrics
        pass