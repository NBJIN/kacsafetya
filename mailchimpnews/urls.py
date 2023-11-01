from django.urls import path
from . import views


urlpatterns = [
    path('subscribe/', views.subscribe_view, name='subscribe_view'),
    path('subscribe/success/', views.success, name='success'),
]
