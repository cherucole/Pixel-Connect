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


    return render(request, 'images/homepage.html', { "posts":posts })