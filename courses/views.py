from django.shortcuts import render
from .models import Courses


def courses(request):
    """ A view to show list of all courses """

    # course = Courses.details.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)
