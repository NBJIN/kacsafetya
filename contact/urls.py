from django.contrib import admin
from django.urls import path
from . import views
from .views import contact_approved


urlpatterns = [
    path('', views.view_contact, name='view_contact'),
    path('contact/approved', views.contact_approved, name='contact_approved'),
]
