from django import forms
from mailchimpnews.models import Mailchimp


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Mailchimp
        fields = ('fullname',
                  'company',
                  'email',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
