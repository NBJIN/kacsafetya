from django.forms import ModelForm
from django import forms
from .models import Purchase, PurchaseOrderItem


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase

        fields = ('fullname',
                  'company',
                  'address1',
                  'address2',
                  'address3',
                  'postcode',
                  'telephone',
                  'email',
                #   'course_title',
                #   'quantity',
                  )

# class PurchaseOrderItem(ModelForm):
#     course_title = forms.CharField(label='Course Title', max_length=100)
#     quantity = forms.IntegerField(label='Quantity')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'fullname': 'Full Name',
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

        self.fields['fullname'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
