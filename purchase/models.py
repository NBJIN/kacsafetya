import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from courses.models import Courses
from dashboard.models import UserDashboard


class Purchase(models.Model):
    purchase_no = models.CharField(max_length=40, null=False, editable=False)
    user_dashboard = models.ForeignKey(UserDashboard, on_delete=models.SET_NULL,
                                       null=True, blank=True, related_name='purchase')
    fullname = models.CharField(max_length=150, null=False, blank=False, default='')
    company = models.CharField(max_length=200, null=False, blank=False)
    address1 = models.CharField(max_length=100, null=False, blank=False)
    address2 = models.CharField(max_length=100, null=False, blank=False)
    address3 = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=50, null=True, blank=True)
    telephone = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=300, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    fee = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    discount = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_purchase_no(self):
        """ create a purchase no using uuid """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Every time a new course is added update grand total """
        self.purchase_total = self.orderitems.aggregate(Sum('orderitem_total'))['orderitem_total__sum'] or 0
        if self.purchase_total < settings.FREE_DISCOUNT:
            self.discount = self.purchase_total * settings.STANDARD_DISCOUNT_PERCENTAGE * 10 / 100
        else:
            self.discount = 0
        self.grand_total = self.purchase_total + self.discount
        self.save()

    def save(self, *args, **kwargs):
        """ set purchase_no if its not set already by overiding the original save method """

        if not self.purchase_no:
            self.purchase_no = self._generate_purchase_no()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.purchase_no


class PurchaseOrderItem(models.Model):
    purchase_no = models.ForeignKey(Purchase, null=False, blank=False, on_delete=models.CASCADE, related_name='orderitem')
    date_added = models.DateTimeField(auto_now_add=True)
    course_title = models.ForeignKey(Courses, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    fee = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    orderitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """ set purchase_no if its not set already by overiding the original save method """
        self.orderitem_total = self.courses.fee * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.purchase_no
