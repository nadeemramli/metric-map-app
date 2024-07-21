from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Experiment, Metric
from ..serializers import ExperimentSerializer
from ..tasks.impact_tasks import ab_test_analysis_task

class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer

    @action(detail=True, methods=['post'])
    def run_ab_test(self, request, pk=None):
        experiment = self.get_object()
        metric_a_id = request.data.get('metric_a_id')
        metric_b_id = request.data.get('metric_b_id')

        if not metric_a_id or not metric_b_id:
            return Response({"error": "Both metric_a_id and metric_b_id are required"}, status=status.HTTP_400_BAD_REQUEST)

        metric_a = Metric.objects.get(id=metric_a_id)
        metric_b = Metric.objects.get(id=metric_b_id)

        data_a = list(metric_a.historical_data.values_list('value', flat=True))
        data_b = list(metric_b.historical_data.values_list('value', flat=True))

        task = ab_test_analysis_task.delay(data_a, data_b)
        
        experiment.results = {'task_id': task.id}
        experiment.save()

        return Response({"message": "A/B test started", "task_id": task.id})

    @action(detail=True, methods=['get'])
    def get_ab_test_results(self, request, pk=None):
        experiment = self.get_object()
        task_id = experiment.results.get('task_id')

        if not task_id:
            return Response({"error": "No A/B test has been run for this experiment"}, status=status.HTTP_400_BAD_REQUEST)

        task = ab_test_analysis_task.AsyncResult(task_id)

        if task.ready():
            result = task.get()
            experiment.results = result
            experiment.save()
            return Response(result)
        else:
            return Response({"message": "A/B test is still running"}, status=status.HTTP_202_ACCEPTED)