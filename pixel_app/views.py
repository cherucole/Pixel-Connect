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

@login_required(login_url='/accounts/login/')
def homepage(request):
    posts = Post.all_posts()
    profile = Profile.get_all_profiles()
    comments=Comment.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('homepage')

    else:
        form=CommentForm
    context =  {
        "profile": profile,
        "form": form,
        "posts":posts ,
        "comments":comments,
    }
    return render(request, 'images/homepage.html', context)


@login_required(login_url='/accounts/login/')
def upload_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile = current_user
            post.save()
        return redirect('homepage')

    else:
        form = UploadForm()
    return render(request, 'images/upload.html', {"form": form})


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
            profile.user = current_user
            profile.save()
        return redirect('homepage')

    else:
        form = NewProfileForm()
    return render(request, 'images/new_profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def search_results(request):
    current_user = request.user
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        profiles = Profile.find_profile(search_term)
        message = search_term

        return render(request,'images/search_profile.html',{"message":message,
                                             "profiles":profiles,
                                             "user":current_user,
                                             "username":profiles})
    else:
        message = "You haven't searched for any user"
        return render(request,'images/search_profile.html',{"message":message})



def like(request,operation,pk):
    image = get_object_or_404(Post,pk=pk)
    if operation == 'like':
        image.likes += 1
        image.save()
    elif operation =='unlike':
        image.likes -= 1
        image.save()
    return redirect('homepage')


@login_required(login_url='/accounts/login/')
def add_comment(request,pk):
    image = get_object_or_404(Post, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.imagecommented = image
            comment.poster = current_user
            comment.save()
            return redirect('homepage')
    else:
        form = CommentForm()
        return render(request,'comment.html',{"user":current_user,"comment_form":form})

def follow(request,operation,id):
    user=User.objects.get(id=id)
    if operation=='follow':
        Follow.follow(request.user,user)
        return redirect('homepage')
    elif operation=='unfollow':
        Follow.unfollow(request.user,user)
        return redirect('homepage')
