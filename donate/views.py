from django.shortcuts import render, redirect

from .forms import DonationForm

def blog_index(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = DonationForm()
    return render(request, 'donate/blog_index.html', {'form': form})