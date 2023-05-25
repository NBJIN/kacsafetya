from django.contrib import admin
from .models import Mailchimp
from .views import subscribe_view


class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'fullname', 'company', 'email',
        )

    ordering = ('fullname',)
    admin.site.register(Mailchimp)
