from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def home(request):
    item = Items.objects.all()
    return render(request, 'main/home.html')


def about(request):
    item = Items.objects.all()
    return render(request, 'main/about.html')


def pageNotFound(request, exception):
    return render(request, 'main/404.html')