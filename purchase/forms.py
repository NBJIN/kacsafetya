from django import forms
from .models import Purchase


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('fname', 'lname',
                  'company', 'address1', 'address2',
                  'address3', 'postcode', 'telephone',
                  'email', 'course_title',
                  'quantity', 'fee', 'total', 'discount',
                  'grand_total',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'purchase_no': 'Purchase Order Number',
            'fname': 'First Name',
            'lname': 'Last Name',
            'company': 'Company',
            'address1': 'Address 1',
            'address2': 'Address 2',
            'address3': 'Address 3',
            'postcode': 'Postcode',
            'telephone': 'Telephone',
            'email': 'Email',
            'date_added': 'Date Added',
            'course_title': 'Course Title',
            'quantity': 'Quantity',
            'fee': 'Fee',
            'total': 'Total',
            'discount': 'Discount',
            'grand_total': 'Grand Total',
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
