from django.urls import path
from . import views


urlpatterns = [
    path('all_courses/', views.all_courses, name='all_courses'),
    path('all_courses/location/<str:location>/', views.all_courses, name='courses_by_location'),
    path('all_courses/group_by/<str:group_by>/', views.all_courses, name='courses_by_group_by'),
    path('courses/detail/<int:course_id>/', views.detailed_courses, name='detailed_courses'),
    path('add/', views.add_courses, name='add_courses'),
    path('edit/<int:courses_id>/', views.edit_courses, name='edit_courses'),
    path('delete/<int:courses_id>/', views.delete_courses, name='delete_courses'),
]
