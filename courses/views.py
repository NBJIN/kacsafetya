from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Courses, Location, Group_By
from .forms import CoursesForm
from django.core.paginator import Paginator


def all_courses(request):
    """ A view to show list of all courses """
    queryset = Courses.objects.all().order_by('title')
    paginate_by = 4

    selected_location = request.GET.get('location', '')

    if selected_location:
        queryset = queryset.filter(location__name=selected_location)

    group_by_options = Group_By.objects.all()

    selected_group_by = request.GET.get('group_by', '')

    if selected_group_by:
        queryset = queryset.filter(group_by__name=selected_group_by)

    paginator = Paginator(queryset, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    locations = Location.objects.all()

    context = {
        'page_obj': page_obj,
        'is_paginated': True,
        'selected_location': selected_location,
        'group_by_options': group_by_options,
        'selected_group_by': selected_group_by,
        'locations': locations,

    }

    return render(request, 'courses/all_courses.html', context)


def all_courses_location(request, location):
    lookup = None
    locations = Location.objects.all()

    if request.GET:
        if 'location' in request.GET:
            locations = request.GET.getlist('location')
            courses = Courses.objects.filter(Location__name__in=locations)
            locations = Location.objects.filter(name__in=locations)

        if 'lookup' in request.GET:
            lookup = request.GET['lookup']
            if not lookup:
                messages.error(request, "No details entered!")
                return redirect(reverse('landing'))

            lookup = Q(title__icontains=lookup) | Q(details__icontains=lookup)
            courses = courses.filter(lookup)
    else:
        courses = Courses.objects.all()

    paginator = Paginator(courses, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'locations': locations,
        'search_term': lookup,
        'selected_location': location,
    }

    return render(request, 'courses/all_courses.html', context)


def all_courses_group_by(request, group_by):

    courses = Courses.objects.all()
    lookup = None

    if 'group_by' in request.GET:
        group_by = request.GET['group_by']
        if group_by == 'health':
            courses = courses.filter(group='Health')
        elif group_by == 'safety':
            courses = courses.filter(group='Safety')

    paginator = Paginator(courses, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_term': lookup,
        'current_group': group_by,

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
    """
    A view to show each course in more detail
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            'This is a restricted view for the admin user.'
        )
        return redirect(reverse('index'))

    courses = get_object_or_404(Courses, pk=courses_id)

    if request.method == 'POST':
        form = CoursesForm(request.POST, request.FILES, instance=courses)
        if form.is_valid():
            form.save()
            messages.info(request, 'Course has been edited.')
            return redirect(reverse('detailed_courses', args=[courses.id]))
        else:
            messages.error(
                request,
                'Course has not been edited please check your form.'
            )
    else:
        form = CoursesForm(instance=courses)
        messages.info(request, f'You are editing {courses.title}')

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
        messages.error(
            request,
            'This is a restricted view for the admin user.'
        )
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = CoursesForm(request.POST, request.FILES)
        if form.is_valid():
            courses = form.save()
            messages.info(request, 'Course added.')
            return redirect(reverse('detailed_courses', args=[courses.id]))
        else:
            messages.error(
                request,
                'Course has not been added please check your form.'
            )
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
        messages.error(
            request,
            'This is a restricted view for the admin user.'
        )
        return redirect(reverse('index'))

    courses = get_object_or_404(Courses, pk=courses_id)
    courses.delete()
    messages.info(request, 'The course has been deleted')
    return redirect(reverse('all_courses'))
