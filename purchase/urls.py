from django.urls import path
from . import views


urlpatterns = [
    path('', views.purchase, name='purchase'),
    path('purchase_success/<purchase_no>', views.purchase_success, name='purchase_success'),
]
