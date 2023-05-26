from django.shortcuts import redirect, render, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from django.contrib import messages
from .models import Mailchimp
from .forms import SubscribeForm
import os

MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY', '')
MAILCHIMP_DATA_CENTER = os.getenv('MAILCHIMP_DATA_CENTER', '')
MAILCHIMP_EMAIL_LIST_ID = os.getenv('MAILCHIMP_EMAIL_LIST_ID', '')


def subscribe_view(request):
    """ A view to return the contact page """

    if request.method == 'POST':
        form = SubscribeForm(data=request.POST)
        # print("in post")
        form = SubscribeForm(request.POST)
        if form.is_valid():
            # print("in post valid")
            fullname = form.cleaned_data['fullname']
            company = form.cleaned_data['company']
            email = form.cleaned_data['email']
            form.save()
            return redirect('success')
    else:
        form = SubscribeForm()
    return render(request, 'mailchimpnews/subscribe.html', {'form': form})

# def subscribe_view(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         Mailchimp.objects.create(email=email)
#         # print(email)
#         messages.success(request, "You details have been received. Thank You")

#     return render(request, "mailchimpnews/subscribe.html")


def success(request):
    return render(request, 'mailchimpnews/success.html')


def error(request):
    return render(request, 'error.html')

# ********

    #     fullname = form.cleaned_data['fullname']
    #     company = form.cleaned_data['company']
        #   email = form.cleaned_data['email']

    # return render(request, 'subscribe.html')
# ********
#  def contact_view(request):
#     """ A view to return the contact page """

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # fullname = form.cleaned_data['fullname']
#             # company = form.cleaned_data['company']
#             # telephone = form.cleaned_data['telephone']
#             # email = form.cleaned_data['email']
#             # # 'date_added': 'Date',
#             # course_title = form.cleaned_data['course_title']
#             # message = form.cleaned_data['message']
#             form.save()
#             return redirect(reverse('contact_approved'))
#     else:
#         form = ContactForm()
#     return render(request, 'contact/contact.html', {'form': form})


# def contact_approved(request):
#     return render(request, 'contact/contact_approved.html')

#         mailchimpClient = Client()
#         mailchimpClient.set_config({
#             "MAILCHIMP_API_KEY": MAILCHIMP_API_KEY,
#         })

#         userinfo = {
#             "email": email,
#             "company": "company",
#             "fullname": fullname
#         }

#         try:
#             mailchimpClient.lists.add_list_member(list_id, userinfo)
#             return redirect("success")
#         except ApiClientError as error:
#             print(error.text)
#             return redirect("error")

#     return redner(request, "index.html")
