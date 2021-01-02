from django.shortcuts import render

# Create your views here.
def blog_index(request):
    return render(request, 'workshops/blog_index.html')
