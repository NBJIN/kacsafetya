from django.shortcuts import redirect, render
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

api_key = os.getenv('MAILCHIMP_KEY', '')
list_id = os.getenv('MAILCHIMP_AUDIENCE_ID', '')


def subscribe(request):
    if request.method == "POST":

        fullname = request.POST['fullname']
        company = request.POST['company']
        email = request.POST['email']

        mailchimpClient = Client()
        mailchimpClient.set_config({
            "api_key": api_key,
        })

        userinfo = {
            "email": email,
            "status": "subscribed",
            "fullname": fullname
        }

        try:
            mailchimpClient.lists.add_list_member(list_id, userinfo)
            return redirect("success")
        except ApiClientError as error:
            print(error.text)
            return redirect("error")

    return redner(request, "index.html")


def success(request):
    return render(request, 'success.html')


def error(request):
    return render(request, 'error.html')
