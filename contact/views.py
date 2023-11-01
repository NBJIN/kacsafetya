from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
# from .models import Contact


def contact_view(request):
    """ A view to return the contact page """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('contact_approved'))
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def contact_approved(request):
    return render(request, 'contact/contact_approved.html')
