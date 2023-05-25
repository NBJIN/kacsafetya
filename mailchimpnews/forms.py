# from django.forms import ModelForm
# from django import forms
# from Mailchimp.models import Mailchimp


# # Create Contact Form
# class MailchimpForm(forms.ModelForm):
#     class Meta:
#         model = Mailchimp
#         fields = ('fullname',
#                   'company',
#                   'email',)

#     def __init__(self, *args, **kwargs):
#         """
#         Add placeholders and classes, remove auto-generated
#         labels and set autofocus on first field
#         """
#         super().__init__(*args, **kwargs)
#         placeholders = {
#             'fullname': 'Full Name',
#             'company': 'Company',
         
#             'email': 'Email',
           
#         }
#         labels = {
#             'fullname': 'Full Name',
#             'company': 'Company',
       
#             'email': 'Email',
           
#         }
