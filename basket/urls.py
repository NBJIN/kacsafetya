from django.urls import path, reverse
from . import views
# from .views import add_to_basket, view_basket


# app_name = 'basket'


urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<int:item_id>/', views.add_to_basket, name='add_to_basket'),
]
