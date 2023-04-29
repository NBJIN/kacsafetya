from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('basket/<course_id>', views.add_to_basket, name='add_to_basket'),
]
