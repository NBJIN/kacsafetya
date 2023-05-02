from django.contrib import admin
from .models import Purchase, PurchaseOrderItem


class PurchaseOrderItemAdminInline(admin.TabularInline):
    model = PurchaseOrderItem
    readonly_fields = ('orderitem_total',)


class PurchaseAdmin(admin.ModelAdmin):
    inlines = (PurchaseOrderItemAdminInline,)


    readonly_fields = ('purchase_no', 'date_added', 'fee', 'total', 'discount', 'grand_total')

    list_display = ('purchase_no', 'date_added', 'fname', 'lname',
                    'total', 'grand_total',)

    ordering = ('date_added',)

admin.site.register(Purchase, PurchaseAdmin)
