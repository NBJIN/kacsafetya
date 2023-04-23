from django.urls import path
from . import views


urlpatterns = [
    path('courses/', views.all_courses, name='all_courses'),
]
