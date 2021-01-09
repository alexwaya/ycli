from django import forms
from .models import Application, Post, Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application

        fields = (

            'full_name',
            'company',
            'email',
            'website',

            'country',
            'city',

            'description',
            'importance',

            'photo',

            )



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 
            'body',
            # 'categories',
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