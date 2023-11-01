from django.contrib import admin
from .models import Mailchimp


class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'fullname',
        'company',
        'email'
        )

    list_filter = (
        'fullname',
        'company',
        'email'
    )

    ordering = ('fullname',)


admin.site.register(Mailchimp)
