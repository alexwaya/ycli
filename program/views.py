from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Program, Post, Comment
from .forms import CommentForm, PostForm, ApplicationForm


@login_required
def apply_program(request, pk):
    program = Program.objects.get(pk=pk)
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.program = program
            application.created_by = request.user
            application.save()
            return redirect('dashboard')
        else:
            form = ApplicationForm()
    context = {
        "program": program,
        "form": form,
        }
    return render(request, 'program/apply_for_program.html', context)


# def apply_program(request, pk):
#     program = Program.objects.get(pk=pk)

#     form = CommentForm()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = Comment(author=form.cleaned_data["author"], body=form.cleaned_data["body"], post=post)
#             comment.save()

#     comments = Comment.objects.filter(post=post)

#     context = {
#         "post": post,
#         "comments": comments,
#         "form": form,
#     }
#     return render(request, "news/blog_detail.html", context)




def program_view(request):
    programs = Program.objects.all()[0:3]

    context = {
        "programs": programs,
        }

    return render(request, 'program/program.html', context)



def program_detail(request, pk):
    program = Program.objects.get(pk=pk)
    context = {
        "program": program,
        }

    return render(request, 'program/program_detail.html', context)


















def add_program(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = PostForm()
    return render(request, "program/add_program.html", {'form': form})




def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "program/blog_index.html", context)



def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "program/blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

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
    return render(request, "program/blog_detail.html", context)