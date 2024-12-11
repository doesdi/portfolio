from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *
from captcha.fields import CaptchaField


class AddReviewForm(forms.ModelForm):
    captcha = CaptchaField(label='Код')
    class Meta:
        model = Items
        fields = ['title', 'rating', 'content']

class Reg(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'user_phone',
                  'password1', 'password2', ]

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'input'}))
    user_phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'input'}))

class Login(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input'}))





