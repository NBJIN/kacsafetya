from django import forms
from .widgets import CustomClearableFileInput
from .models import Courses, Group_By, Location
from collections import OrderedDict


class CoursesForm(forms.ModelForm):

    class Meta:
        model = Courses
        fields = '__all__'
        widgets = {
            'image': CustomClearableFileInput,
            'date_of_course': forms.DateInput(
                attrs={
                    'type': 'datetime-local',
                        }
            ),
        }
