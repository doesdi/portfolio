from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.cache import cache
from .forms import *
from .models import Items
from django.shortcuts import render





def home(request):
     return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')



# def reviews(request):
#     if request.method == 'POST':
#         form = AddReviewFrom(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('reviews')
#     else:
#         form = AddReviewFrom()
#     items = Items.objects.all()
#     return render(request, 'main/reviews.html', {'Items': items, 'form': form})

def reviews(request):
    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = AddReviewForm()
    items = cache.get('items_cache')
    if items is None:
        items = Items.objects.all()
        cache.set('items_cache', items, timeout=100)
    return render(request, 'main/reviews.html', {'Items': items, 'form': form})


def pageNotFound(request, exception):
    return render(request, 'main/404.html')



def Register(request):
    if request.method == 'POST':
        form = Reg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Reg()
    user = request.user
    us = User.objects.all()
    return render(request, 'main/registration.html', {'user': user, 'us': us, 'form': form})



class LoginUser(LoginView):
    form = Login
    template_name = 'main/login.html'

    def get_success_url(self):
        print(1)
        return reverse_lazy('home')


def Logout_user(request):
    logout(request)
    return redirect('home')
