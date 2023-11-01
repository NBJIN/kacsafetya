from django import forms
from .widgets import CustomClearableFileInput
from .models import Courses


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
