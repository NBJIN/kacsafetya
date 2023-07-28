from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.purchase, name='purchase'),
    path('purchase/purchase_success/<purchase_no>',
         views.purchase_success, name='purchase_success'),
    path('cache_purchase_data/', views.cache_purchase_data,
         name='cache_purchase_data'),
    path('wh/', webhook, name='webhook'),
]
