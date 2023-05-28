from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Courses, Location, Group_By
from .forms import CoursesForm


def all_courses(request):
    """ A view to show list of all courses """

    courses = Courses.objects.all()
    Locations = None
    lookup = None

    if request.GET:
        if 'Location' in request.GET:
            Locations = request.GET['Location'].split(',')
            courses = all_courses.filter(Location__name__in=Locations)
            Locations = Location.objects.filter(name__in=Locations)

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
        'current_Locations': Locations,

    }

    return render(request, 'courses/all_courses.html', context)


def detailed_courses(request, course_id):
    """ A view to show each course in more detail """
    course_id = int(course_id)
    courses = get_object_or_404(Courses, pk=int(course_id))

    context = {
        'courses': courses,

    }

    return render(request, 'courses/detailed_courses.html', context)


@login_required
def edit_courses(request, courses_id):
    """ A view to show each course in more detail """
    if not request.user.is_superuser:
        messages.error(request, 'This is a restricted view for the admin user.')
        return redirect(reverse('index'))

    courses = get_object_or_404(Courses, pk=courses_id)

    if request.method == 'POST':
        form = CoursesForm(request.POST, request.FILES, instance=courses)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course has been edited.')
            return redirect(reverse('detailed_courses', args=[courses.id]))
        else:
            messages.error(request, 'Course has not been edited please check your form.')
    else:
        form = CoursesForm(instance=courses)
        messages.info(request, f'You are editing {courses.title}')

    template = 'courses/edit_courses.html'

    context = {
        'form': form,
        'courses': courses,

    }

    return render(request, 'courses/edit_courses.html', context)


@login_required
def add_courses(request):
    """
    Add Courses
    """
    if not request.user.is_superuser:
        messages.error(request, 'This is a restricted view for the admin user.')
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = CoursesForm(request.POST, request.FILES)
        if form.is_valid():
            courses = form.save()
            messages.success(request, 'Course added.')
            return redirect(reverse('detailed_courses', args=[courses.id]))
        else:
            messages.error(request, 'Course has not been added please check your form.')
    else:
        form = CoursesForm()

    template = 'courses/add_courses.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def delete_courses(request, courses_id):
    """
    A view to show that course is deleted
    """
    if not request.user.is_superuser:
        messages.error(request, 'This is a restricted view for the admin user.')
        return redirect(reverse('index'))

    courses = get_object_or_404(Courses, pk=courses_id)
    courses.delete()
    messages.success(request, 'The course has been deleted')
    return redirect(reverse('all_courses'))
