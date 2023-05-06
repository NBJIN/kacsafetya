from django.urls import path
from . import views


urlpatterns = [
    path('all_courses/', views.all_courses, name='all_courses'),
    path('courses/detail/<course_id>', views.detailed_courses, name='detailed_courses'),
    path('courses/edit/<course_id>', views.edit_courses, name='edit_courses'),

]
