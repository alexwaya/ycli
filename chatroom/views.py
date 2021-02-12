from django.shortcuts import render, redirect
from .models import Chat, Comment

from .forms import CommentForm, RaiseIssueForm

def raise_issue(request):
    if request.method == 'POST':
        form = RaiseIssueForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('chat_index')
    else:
        form = RaiseIssueForm()
    return render(request, 'chatroom/raise_issue.html', {'form': form})




def chat_index(request):
    posts = Chat.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "chatroom/chat_index.html", context)



def chat_detail(request, pk):
    post = Chat.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "chatroom/chat_detail.html", context)