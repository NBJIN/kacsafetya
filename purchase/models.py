import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from courses.models import Courses


class Purchase(models.Model):
    purchase_no = models.CharField(max_length=40, null=False, editable=False)
    fname = models.CharField(max_length=60, null=False, blank=False)
    lname = models.CharField(max_length=60, null=False, blank=False)
    company = models.CharField(max_length=200, null=False, blank=False)
    address1 = models.CharField(max_length=100, null=False, blank=False)
    address2 = models.CharField(max_length=100, null=False, blank=False)
    address3 = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=50, null=True, blank=True)
    telephone = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=300, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    course_title = models.CharField(max_length=250)
    quantity = models.PositiveIntegerField(default=0)
    fee = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    discount = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)


class Purchaseorderitem(models.Model):
    purchase_no = models.ForeignKey(Purchase, null=False, blank=False, on_delete=models.CASCADE, related_name='orderitem')
    date_added = models.DateTimeField(auto_now_add=True)
    course_title = models.ForeignKey(Courses, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    fee = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    orderitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
