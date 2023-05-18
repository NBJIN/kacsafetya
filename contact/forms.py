from django.forms import ModelForm
from contact.models import Contact


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
            'date_added': 'Date',
            'course_title': 'Course Title',
            'message': 'Message',
        }
        # print('fields')
