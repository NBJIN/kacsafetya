from django import forms
from .models import UserDashboard


class UserDashboardForm(forms.ModelForm):
    class Meta:
        model = UserDashboard
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_company': 'Company',
            'default_address1': 'Address 1',
            'default_address2': 'Address 2',
            'default_address3': 'Address 3',
            'default_postcode': 'Postcode',
            'default_telephone': 'Telephone',
            'default_email': 'Email',
        }

        self.fields['default_company'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 dashboard-form-input'
            self.fields[field].label = False
