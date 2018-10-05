from django.contrib.auth.decorators import login_required
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


def homepage(request):
    posts = Post.all_posts()
    comments=Comment.objects.all()




    return render(request, 'images/homepage.html', { "posts":posts , "comments":comments})


def add_comment(request, id):
    post = Post.objects.get(id=id)

    if request.GET.get("id"):
        posts = Post.show_by_id(request.GET.get("id"))

    comments=Comment.get_comments(id=id)

    return render(request, 'images/ind_post.html', {  "comments":comments , "posts":post})


def like_post(request, id):



    return render(request, )