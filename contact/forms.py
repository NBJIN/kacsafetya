from django.forms import ModelForm
from django import forms
from contact.models import Contact


# Create Contact Form
class ContactForm(forms.ModelForm):
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
        # labels = {
        #     'fullname': 'Full Name',
        #     'company': 'Company',
        #     'telephone': 'Telephone',
        #     'email': 'Email',
        #     'date_added': 'Date',
        #     'course_title': 'Course Title',
        #     'message': 'Message',
        # }

        # for field_name, field in self.fields.items():
        #     field.widget.attrs['placeholder'] = placeholders.get(field_name, '')
        #     field.label = labels.get(field_name, field.label)
