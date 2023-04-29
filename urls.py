from django.urls import path, reverse
from . import views
from .views import add_to_basket, view_basket


urlpatterns = [
    path('basket/', views.view_basket, name='basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
]
