from django.shortcuts import render, redirect

from .models import Workshop
from .forms import WorkshopsForm


def apply_workshop(request, pk):
    workshop = Workshop.objects.get(pk=pk)
    form = WorkshopsForm()
    if request.method == 'POST':
        form = WorkshopsForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.workshop = workshop
            application.created_by = request.user
            application.save()
            return redirect('home')
        else:
            form = WorkshopsForm()
    context = {
        "workshop": workshop,
        "form": form,
        }
    return render(request, 'workshops/apply_for_workshop.html', context)

# def apply_workshop(request, pk):
#     workshop = Workshop.objects.get(pk=pk)
#     form = WorkshopsForm()
#     if request.method == 'POST':
#         form = WorkshopsForm(request.POST)
#         if form.is_valid():
#             application = form.save(commit=False)
#             application.workshop = workshop
#             application.created_by = request.user
#             application.save()
#             return redirect('home')
#         else:
#             form = WorkshopsForm()
#     context = {
#         "workshop": workshop,
#         "form": form,
#         }
#     return render(request, 'workshops/apply_for_workshop.html', context)








def workshops_index(request):
    posts = Workshop.objects.all().order_by('-created_at')
    context = {
        "posts": posts,
    }
    return render(request, "workshops/workshops_index.html", context)

def workshops_detail(request, pk):
    post = Workshop.objects.get(pk=pk)
    context = {
        "post": post,
        }

    return render(request, 'workshops/workshops_detail.html', context)
