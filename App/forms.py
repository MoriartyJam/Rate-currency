from django import forms
from .models import Post
from django.forms import ModelForm


class PostForm(forms.ModelForm):
    currency = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new date...'}))
    period1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new date...'}))
    period2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new date...'}))



    class Meta:
        model = Post
        fields = ('period1', 'period2', 'currency')
