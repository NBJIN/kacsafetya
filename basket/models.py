from django.db import models


class Basket(models.Model):
    title = models.CharField(max_length=250)
    quantity = models.PositiveIntegerField(default=0)
    fee = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title
