from django import forms
from .models import Purchase


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('fname', 'lname',
                  'company', 'address1', 'address2',
                  'address3', 'postcode', 'telephone',
                  'email', 'course_title',
                  'quantity',)

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
            'address1': 'Address 1',
            'address2': 'Address 2',
            'address3': 'Address 3',
            'postcode': 'Postcode',
            'telephone': 'Telephone',
            'email': 'Email',
            'course_title': 'Course Title',
            'quantity': 'Quantity',

        }

        self.fields['fname'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False