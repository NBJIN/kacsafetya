from django.contrib import admin
from django.urls import path, reverse
from . import views
from .views import contact_approved, contact_view


urlpatterns = [
    path('', views.contact_view, name='contact_view'),
    path('contact_approved/', views.contact_approved, name='contact_approved'),
]
