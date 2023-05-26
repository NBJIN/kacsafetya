from django.contrib import admin
from django.urls import path, reverse
from . import views
from .views import subscribe_view, success


urlpatterns = [
    path('subscribe/', views.subscribe_view, name='subscribe_view'),
    path('subscribe/success/', views.success, name='success'),
]
