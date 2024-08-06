from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import HistoricalData, Connection, Metric
from .computations.permanent_computations import PermanentComputations

@receiver([post_save, post_delete], sender=HistoricalData)
def trigger_computations_on_historical_data_change(sender, instance, **kwargs):
    PermanentComputations([instance.metric_id], instance.tenant).run_all_computations()

@receiver([post_save, post_delete], sender=Connection)
def trigger_computations_on_connection_change(sender, instance, **kwargs):
    metrics = [instance.from_metric_id, instance.to_metric_id]
    PermanentComputations(metrics, instance.tenant).run_all_computations()

@receiver(post_save, sender=Metric)
def trigger_computations_on_metric_creation(sender, instance, created, **kwargs):
    if created:
        PermanentComputations([instance.id], instance.tenant).run_all_computations()