from django.shortcuts import render

from accounts.models import CustomUser
# Create your views here.

def members_directory(request):
    posts = CustomUser.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "members.html", context)
    

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')
