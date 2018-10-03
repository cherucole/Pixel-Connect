from django.shortcuts import render
from django.http import HttpResponse
from .models import  *
# Create your views here.

def sample_display(request):
    message="This is to confirm my page is displaying shit"

    return render(request, 'images/homepage.html', {"message":message })