from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('fname', 'lname',
                  'company', 'telephone',
                  'email', 'date_added', 'course_title',
                  'message',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'company': 'Company',
            'telephone': 'Telephone',
            'email': 'Email',
            'date_added': 'Date'
            'course_title': 'Course Title',
            'message': 'Message',
        }

        self.fields['fname'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
