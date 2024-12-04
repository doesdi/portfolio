from django import forms
from .models import *


class AddReviewFrom(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['title', 'rating', 'content']
