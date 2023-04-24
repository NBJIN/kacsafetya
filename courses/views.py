from django.shortcuts import render, get_object_or_404
from .models import Courses, Location, Group_By


def all_courses(request):
    """ A view to show list of all courses """

    courses = Courses.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/all_courses.html', context)


def detailed_courses(request, course_id):
    """ A view to show each course in more detail """
    courses = get_object_or_404(Courses, pk=course_id)

    context = {
        'courses': courses,
    }

    return render(request, 'courses/detailed_courses.html', context)
