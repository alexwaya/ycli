from django.shortcuts import render

# Create your views here.
from .models import Event

# def events_index(request):
#     return render(request, 'events/events_index.html')


def events_index(request):
    posts = Event.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "events/events_index.html", context)
