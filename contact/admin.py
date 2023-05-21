from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'fullname', 'company', 'telephone',
        'email', 'date_added', 'course_title', 'message',
    )

    ordering = ('email',)


admin.site.register(Contact)
