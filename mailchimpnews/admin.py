from django.contrib import admin
from .models import Mailchimp
from .forms import SubscribeForm


class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'fullname', 'company', 'email',
        )

    ordering = ('fullname',)
    

admin.site.register(Mailchimp)
