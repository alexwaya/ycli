from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = (
        	'fname', 
        	'lname',
        	'email', 
        	'phone', 
        	'type_of_donation', 
        	'amount', 
        	'comments',
        	)
