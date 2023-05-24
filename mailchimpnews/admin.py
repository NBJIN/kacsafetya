from django.contrib import admin
from .models import Mailchimp


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'fullname', 'company', 'email',
    )

    ordering = ('fullname',)


admin.site.register(Mailchimp)
