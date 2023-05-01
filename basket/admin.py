from django.contrib import admin
from .models import Basket


class BasketAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'quantity', 'fee', 'total', 'discount', 'grand_total',
    )

    ordering = ('title',)


admin.site.register(Basket, BasketAdmin)
