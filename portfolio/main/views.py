from django.shortcuts import render, redirect
from .forms import *
from .models import Items


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')



def reviews(request):
    if request.method == 'POST':
        form = AddReviewFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = AddReviewFrom()
    items = Items.objects.all()
    return render(request, 'main/reviews.html', {'Items': items, 'form': form})


def pageNotFound(request, exception):
    return render(request, 'main/404.html')