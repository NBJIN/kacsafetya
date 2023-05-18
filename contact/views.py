from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404


def view_contact(request):
    """ A view to return the contact page """
    return render(request, 'contact/contact.html')
