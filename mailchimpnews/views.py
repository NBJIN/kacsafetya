from django.shortcuts import redirect, render
from .forms import SubscribeForm
import os

MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY', '')
MAILCHIMP_DATA_CENTER = os.getenv('MAILCHIMP_DATA_CENTER', '')
MAILCHIMP_EMAIL_LIST_ID = os.getenv('MAILCHIMP_EMAIL_LIST_ID', '')


def subscribe_view(request):
    """ A view to return the contact page """

    if request.method == 'POST':
        form = SubscribeForm(data=request.POST)
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.cleaned_data['fullname']
            form.cleaned_data['company']
            form.cleaned_data['email']
            form.save()
            return redirect('success')
    else:
        form = SubscribeForm()
    return render(request, 'mailchimpnews/subscribe.html', {'form': form})


def success(request):
    return render(request, 'mailchimpnews/success.html')


def error(request):
    return render(request, 'error.html')
