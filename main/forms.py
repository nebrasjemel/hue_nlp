from django.contrib.auth.models import User
from django import forms

__author__ = 'nebrasjemel'


class SignupForm(forms.ModelForm):
    password = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    username = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class SignInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    class Meta:
        model = User
        fields = ('username', 'password')
