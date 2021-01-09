from django.shortcuts import render, redirect

from .models import Event

from .forms import EventsForm


def apply_event(request, pk):
    event = Event.objects.get(pk=pk)
    form = EventsForm()
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.event = event
            application.created_by = request.user
            application.save()
            return redirect('home')
        else:
            form = EventsForm()
    context = {
        "event": event,
        "form": form,
        }
    return render(request, 'events/apply_for_event.html', context)









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
