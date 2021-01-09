from django import forms
from .models import Application

class WorkshopsForm(forms.ModelForm):
    class Meta:
        model = Application

        fields = (

            'name',
            'email',

            'phone',
            'country',

            )