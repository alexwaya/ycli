from django import forms

from .models import Chat


class RaiseIssueForm(forms.ModelForm):
    class Meta:
        model = Chat

        fields = (

            'title',
            'body',

            )























class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )