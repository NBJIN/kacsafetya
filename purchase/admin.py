from django.contrib import admin
from .models import Purchase, PurchaseOrderItem


class PurchaseOrderItemAdminInline(admin.TabularInline):
    model = PurchaseOrderItem
    readonly_fields = ('orderitem_total', 'course_title', 'quantity',)


class PurchaseAdmin(admin.ModelAdmin):
    inlines = (PurchaseOrderItemAdminInline,)

    readonly_fields = ('purchase_no', 'date_added',
                        'total', 'discount',
                       'grand_total', 'original_basket',
                       'stripe_pid')

    fields = ('purchase_no', 'user_dashboard', 'fullname',
              'company', 'address1', 'address2',
              'address3', 'postcode', 'telephone',
              'email', 'date_added',  'total', 'discount',
              'grand_total', 'original_basket',
              'stripe_pid')

    list_display = ('purchase_no', 'date_added', 'fullname',
                    'total', 'grand_total',)

    ordering = ('date_added',)


admin.site.register(Purchase, PurchaseAdmin)
