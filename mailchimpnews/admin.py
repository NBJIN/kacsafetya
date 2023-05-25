from django.contrib import admin
from .models import Mailchimp
from .views import subscribe


class Subscribe(admin.ModelAdmin):
    list_display = (
        'fullname', 'company', 'email',
        )

    ordering = ('fullname',)
    admin.site.register(Mailchimp)
