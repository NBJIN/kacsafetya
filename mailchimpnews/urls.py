from django.contrib import admin
from django.urls import path, reverse
from . import views


urlpatterns = [
    path("", views.subscribe, name="subscribe"),
    # path("failure", views.failure, name="failure"),
]
# path("admin/", admin.site.urls),
# path("success/", views.success, name="success"),