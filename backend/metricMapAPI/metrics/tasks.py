from celery import shared_task
from .models import ComputationStatus, Notification, Client
from .computations.permanent_computations import PermanentComputations

@shared_task
def run_computations(tenant_id, metric_ids):
    try:
        computation_status = ComputationStatus.objects.create(tenant_id=tenant_id, status='IN_PROGRESS')
        tenant = Client.objects.get(id=tenant_id)
        PermanentComputations(metric_ids, tenant).run_all_computations()
        computation_status.status = 'COMPLETED'
        computation_status.save()
        Notification.objects.create(
            tenant_id=tenant_id,
            message='Computations completed successfully.'
        )
    except Exception as e:
        computation_status.status = 'FAILED' 
        computation_status.error_message = str(e)
        computation_status.save()
        Notification.objects.create(
            tenant_id=tenant_id,
            message='Computations failed with error: {e}'.format(e=e)
        )