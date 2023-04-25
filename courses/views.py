from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import Courses, Location, Group_By


def all_courses(request):
    """ A view to show list of all courses """

    courses = Courses.objects.all()
    lookup = None

    if request.GET:
        if 'group_by' in request.GET:
            group_by = request.GET['group_by'].split(',')
            courses = courses.filter(group_by__name__in=group_by)
            group_by = Group_By.objects.filter(name__in=group_by)

        # lookup is not working when i enter a word that is not on the website 
        if 'lookup' in request.GET:
            lookup = request.GET['lookup']
            if not lookup:
                messages.error(request, "No details entered!")
                return redirect(reverse('landing'))

            lookup = Q(title__icontains=lookup) | Q(details__icontains=lookup)
            courses = courses.filter(lookup)

    context = {
        'courses': courses,
        'search_term': lookup,
        'group': group_by,
    }

    return render(request, 'courses/all_courses.html', context)


def detailed_courses(request, course_id):
    """ A view to show each course in more detail """
    courses = get_object_or_404(Courses, pk=course_id)

    context = {
        'courses': courses,

    }

    return render(request, 'courses/detailed_courses.html', context)
