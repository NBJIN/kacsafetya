from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import PurchaseOrderItem


@receiver(post_save, sender=PurchaseOrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on PurchaseOrderItem when creating and updating
    """
    instance.purchase.update_total()


@receiver(post_delete, sender=PurchaseOrderItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on PurchaseOrderItem when deleting a record
    """
    instance.purchase.update_total()
