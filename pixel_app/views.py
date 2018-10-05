from django.shortcuts import render,redirect
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

# def sample_display(request):
#     message="This is to confirm my page is displaying shit"
#
#     return render(request, 'images/homepage.html', {"message":message })

@login_required(login_url='/accounts/login/')

def homepage(request):
    posts = Post.all_posts()
    comments=Comment.objects.all()

    return render(request, 'images/homepage.html', { "posts":posts , "comments":comments})


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
# @login_required(login_url='/accounts/login/')
# def add_comment(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.save(commit=False)
#             image.name = current_user
#             image.save()
#         return redirect('home')
#
#     else:
#         form = CommentForm()
#     return render(request, 'comment.html', {"form": form})