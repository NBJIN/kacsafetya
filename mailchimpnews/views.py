from django.shortcuts import redirect, render, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from django.contrib import messages
import os

MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY', '')
MAILCHIMP_DATA_CENTER = os.getenv('MAILCHIMP_DATA_CENTER', '')
MAILCHIMP_EMAIL_LIST_ID = os.getenv('MAILCHIMP_EMAIL_LIST_ID', '')


def subscribe(request):
    if request.method == "POST":

        fullname = request.POST['fullname']
        company = request.POST['company']
        email = request.POST['email']
       
    return render(request, 'subscribe.html')

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


def success(request):
    return render(request, 'success.html')


def error(request):
    return render(request, 'error.html')
