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
        }
        # labels = {
        #     'title',
        #     'location',
        #     'details',
        #     'image',
        #     'group_by',
        #     'fee',
        #     'image_url',
        # }

    # Group_By = forms.ModelChoiceField(queryset=Group_By.objects.all(), empty_label=None)
    # Location = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label=None)
    # def __init__(self, *args, **kwargs):
    """
    Add placeholders and classes, remove auto-generated
    labels and set autofocus on first field
    """
        # super().__init__(*args, **kwargs)
        # print(self.fields.keys())
        # self.fields = OrderedDict(
        #     (field_name, self.fields[field_name])

        #     for field_name in [
        #         'title',
        #         'group_by',
        #         'location',
        #         'image',
        #         'image_url',
        #         'details',
                # 'date_of_course', 'fee',
            # ]
            # )

    # def __init__(self, *args, **kwargs):
    """
    Add placeholders and classes, remove auto-generated
    labels and set autofocus on first field
        """
        # super().__init__(*args, **kwargs)

        # self.fields['group_by'].widget = forms.Select()

        # group_by = [
        #     ('health', 'Health'),
        #     ('Safety', 'Safety'),
        # ]
        # self.fields['location'].widget = forms.Select()
        # location = [
        #     ('online', 'Online'),
        #     ('classroom', 'Classroom'),
        # ]
