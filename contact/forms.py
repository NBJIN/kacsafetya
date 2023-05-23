from django.forms import ModelForm
from django import forms
from contact.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('fullname',
                  'company', 'telephone',
                  'email', 'course_title',
                  'message',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'fullname': 'Full Name',
            'company': 'Company',
            'telephone': 'Telephone',
            'email': 'Email',
            'date_added': 'Date',
            'course_title': 'Course Title',
            'message': 'Message',
        }
        labels = {
            'fullname': 'Full Name',
            'company': 'Company',
            'telephone': 'Telephone',
            'email': 'Email',
            'date_added': 'Date',
            'course_title': 'Course Title',
            'message': 'Message',
        }
