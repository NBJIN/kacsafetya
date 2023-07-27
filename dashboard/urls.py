from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('purchase_records/<purchase_no>',
         views.purchase_records,
         name='purchase_records'),
]
