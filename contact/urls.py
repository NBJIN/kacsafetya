from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact_view, name='contact_view'),
    path('contact_approved/', views.contact_approved, name='contact_approved'),
]
