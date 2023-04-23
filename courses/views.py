from django.shortcuts import render
from .models import Courses, Location, Group_By

def courses(request):
    """ A view to show list of all courses """

    courses = Courses.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses_list.html', context)
