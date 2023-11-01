from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserDashboard(models.Model):
    """
    User Dashboard to display users delivery
    and purchase details
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_company = models.CharField(max_length=200, null=True, blank=True)
    default_address1 = models.CharField(max_length=100, null=True, blank=True)
    default_address2 = models.CharField(max_length=100, null=True, blank=True)
    default_address3 = models.CharField(max_length=100, null=True, blank=True)
    default_postcode = models.CharField(max_length=50, null=True, blank=True)
    default_telephone = models.CharField(max_length=30, null=True, blank=True)
    default_email = models.EmailField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_dashboard(sender, instance, created, **kwargs):
    """
    Create or update user dashboard
    """
    if created:
        UserDashboard.objects.create(user=instance)
    instance.userdashboard.save()
