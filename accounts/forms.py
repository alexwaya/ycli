from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (

            'org_name',
            'org_type',

            'org_email',
            'org_phone',

            'org_website',
            'org_address',

            'org_city',
            'org_country',

            'person_name',
            'person_org_title',

            'person_email',
            'person_phone',

            'staff_no',
            'area_of_focus',

            'mission',

            'username',
            # 'email',
            # 'org_name',

            # 'phone',

            
            )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (

        	'username',
            'email',
            'org_name',
            
        	)