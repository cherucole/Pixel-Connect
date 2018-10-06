from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import datetime as dt
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .email import *

# def add_comment(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required(login_url='/accounts/login/')
def homepage(request):
    posts = Post.all_posts()
    # post = Post.one_image(id)
    comments=Comment.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        post = Post.one_image(posts)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            # comment.imagecommented=post
            comment.save()
        return redirect('homepage')

    else:
        form = CommentForm()


    form=CommentForm
    context =  {
        "form": form,
        "posts":posts ,
        "comments":comments
    }
    return render(request, 'images/homepage.html', context)


@login_required
def profile(request,profile_id):

    users = User.objects.get(pk = profile_id)
    posts = Post.objects.filter(profile_id=profile).all()

    return render(request,"profile.html",{"users":users,"posts":posts})

def add_comment(request, id):
    post = Post.objects.get(id=id)

    if request.GET.get("id"):
        posts = Post.show_by_id(request.GET.get("id"))

    comments=Comment.get_comments(id=id)

    return render(request, 'images/ind_post.html', {  "comments":comments , "posts":post})


def like_post(request, id):

    return render(request, )


@login_required(login_url='/accounts/login/')
def upload_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('homepage')

    else:
        form = UploadForm()
    return render(request, 'images/upload.html', {"form": form})

# @login_required(login_url='/accounts/login/')
# def add_profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.editor = current_user
#             profile.save()
#         return redirect('home')
#
#     else:
#         form = NewProfileForm()
#     return render(request, 'new_profile.html', {"form": form})


def profile(request, username):
    profile = User.objects.get(username=username)
    try:
        profile_info = Profile.get_profile(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)
    images = Post.get_profile_image(profile.id)
    title = f'@{profile.username}'
    return render(request, 'images/profile.html', {'title':title, 'profile':profile, 'profile_info':profile_info, 'images':images})


@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()
        return redirect('homepage')

    else:
        form = NewProfileForm()
    return render(request, 'images/new_profile.html', {"form": form})
#
# @login_required(login_url='/accounts/login/')
# def update_image(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.save(commit=False)
#             image.name = current_user
#             image.save()
#         return redirect('home')
#
#     else:
#         form = UploadForm()
#     return render(request, 'upload.html', {"form": form})
#

#
# @login_required(login_url='/accounts/login/')
# def add_comment(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.editor = current_user
#             comment.save()
#         return redirect('homepage')
#
#     else:
#         form = CommentForm()
#     return render(request, 'images/homepage.html', {"form": form})








# def add_comment(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/add_comment_to_post.html', {'form': form})
#

#
# def add_comment(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form=CommentForm()
#
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('homepage', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'image/homepage.html', {'form': form})
#
#
