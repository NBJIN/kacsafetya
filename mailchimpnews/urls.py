from django.contrib import admin
from django.urls import path, reverse
from . import views


urlpatterns = [
    path("subscribe/", views.subscribe_view, name="subscribe_view"),
    path("success/", views.success, name="success"),
    # path("failure", views.failure, name="failure"),
]
# path("admin/", admin.site.urls),
# 