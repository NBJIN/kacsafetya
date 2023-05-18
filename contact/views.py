from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import ContactForm


def view_contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, 'Your inquiry has been submitted, we will get back to you shortly.')
    else: 
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
