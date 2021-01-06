from django.shortcuts import render

# Create your views here.
# def blog_index(request):
#     return render(request, 'workshops/blog_index.html')


from .models import Workshop

# def events_index(request):
#     return render(request, 'events/events_index.html')


def workshops_index(request):
    posts = Workshop.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "workshops/workshops_index.html", context)
