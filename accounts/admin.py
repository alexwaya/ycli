from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [

    		'username',
            'email',
            'org_name',
    ]

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.unregister(Group)
