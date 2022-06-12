from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']