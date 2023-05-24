from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from .models import Contact


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            company = form.cleaned_data['company']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']
            # 'date_added': 'Date',
            course_title = form.cleaned_data['course_title']
            message = form.cleaned_data['message']
            form.save()
            return redirect('contact_approved')

    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def contact_approved(request):
    return render(request, 'contact/contact_approved.html')








    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         fullname = form.cleaned_data['fullname']
    #         company = form.cleaned_data['company']
    #         telephone = form.cleaned_data['telephone']
    #         email = form.cleaned_data['email']
    #         # 'date_added': 'Date',
    #         course_title = form.cleaned_data['course_title']
    #         message = form.cleaned_data['message']
    #         return redirect('contact_approved')
    # else:
    #     form = ContactForm()

    # return render(request, 'contact/contact.html', {'form': form})

    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         return HttpResponseRedirect('/contact?submitted=True')
    #     else:
    #         form = ContactForm()
    #         if 'submitted' in request.GET:
    #             submitted = True

    #     return render(request, 'view_contact', {'form': form, 'submitted': submitted})


# def contact_approved(request):
#     """
#     A veiw to return the contact approved  page
#     """
#     return render(request, 'contact/contact_approved.html')
