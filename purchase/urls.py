from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.purchase, name='purchase'),
    path('purchase_success/<purchase_no>', views.purchase_success, name='purchase_success'),
    path('wh/', webhook, name='webhook'),
]
