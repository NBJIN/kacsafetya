from django import forms
from .models import Courses, Group_By, Location


class CoursesForm(forms.ModelForm):

    class Meta:
        model = Courses
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     locations = Location.objects.all()
    #     friendly_names = [(l.id, l.get_friendly_name()) for l in locations]

    #     self.fields['location'].choices = friendly_names
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'border-black rounded-0'
