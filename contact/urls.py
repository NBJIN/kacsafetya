from django.contrib import admin
from django.urls import path, reverse
from . import views
from .views import contact_approved, contact


urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('contact_approved/', views.contact_approved, name='contact_approved'),
]
