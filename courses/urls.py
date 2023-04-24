from django.urls import path
from . import views


urlpatterns = [
    path('all_courses/', views.all_courses, name='all_courses'),
    path('courses/<int:courses_id>/', views.detailed_courses, name='detailed_courses'),
]
