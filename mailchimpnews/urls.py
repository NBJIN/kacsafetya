from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.subscribe, name="subscribe"),
    path("success", views.success, name="success"),
    path("failure", views.failure, name="failure"),
]
