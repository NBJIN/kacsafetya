from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'fullname', 'company', 'telephone',
        'email', 'date_added', 'course_title', 'truncated_message',
    )

    ordering = ('email',)

    def truncated_message(self, obj):
        max_length = 25
        return (obj.message[:max_length]
                if len(obj.message) > max_length
                else obj.message)


admin.site.register(Contact, ContactAdmin)
