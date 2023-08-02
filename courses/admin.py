from django.contrib import admin
from .models import Courses, Location, Group_By


class CoursesAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'location', 'group_by', 'fee',
    )

    list_filter = (
        'location', 'group_by',
    )

    ordering = ('title',)


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class Group_ByAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Courses, CoursesAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Group_By, Group_ByAdmin)
