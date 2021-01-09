from django import forms
from .models import Application


class EventsForm(forms.ModelForm):
    class Meta:
        model = Application

        fields = (

            'name',
            'email',

            'phone',
            'country',

            )