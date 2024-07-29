from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import HistoricalData
from .permanent_computations import PermanentComputations

@receiver(post_save, sender=HistoricalData)
def update_permanent_computations(sender, instance, created, **kwargs):
    if created:
        pc = PermanentComputations(instance.metric_id)
        pc.update_all_computations()