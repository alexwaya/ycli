from django.shortcuts import render

# Create your views here.
from .models import Event

# def events_index(request):
#     return render(request, 'events/events_index.html')


def events_index(request):
    posts = Event.objects.all().order_by('-created_at')
    context = {
        "posts": posts,
    }
    return render(request, "events/events_index.html", context)

def event_detail(request, pk):
    post = Event.objects.get(pk=pk)
    context = {
        "post": post,
        }

    return render(request, 'events/events_detail.html', context)
