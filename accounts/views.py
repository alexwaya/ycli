from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def my_dashboard_view(request):
	return render(request, 'accounts/dashboard_home.html')

@login_required
def my_applications_view(request):
	return render(request, 'accounts/my_applications.html')

