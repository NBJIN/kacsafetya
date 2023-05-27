from django import forms
from .widgets import CustomClearableFileInput
from .models import Courses, Group_By, Location
from collections import OrderedDict


class CoursesForm(forms.ModelForm):

    class Meta:
        model = Courses
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        print(self.fields.keys())
        self.fields = OrderedDict(
            (field_name, self.fields[field_name])
            for field_name in [
                'title',
                'group_by',
                'location',
                'image',
                'image_url',
                'details',
                # 'date_of_course',
                'fee',
            ]
            )
