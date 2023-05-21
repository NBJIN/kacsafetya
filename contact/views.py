from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import ContactForm


def view_contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            # lname = form.cleaned_data['lname']
            company = form.cleaned_data['company']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']
            # 'date_added': 'Date',
            course_title = form.cleaned_data['course_title']
            message = form.cleaned_data['message']
            return redirect('contact_approved')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def contact_approved(request):
    """
    A veiw to return the contact approved  page
    """
    return render(request, 'contact/contact_approved.html')
