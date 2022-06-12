from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from .forms import Signupform

# Create your views here.
def signuppage (request):
    form = Signupform()
    if request.method == "POST":
        form = Signupform(request.POST)
        
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Hi ' + user + ', you signed up successfully')
            return redirect('login')

    context = {'form':form}
    return render(request,'logs/signup.html', context)

def loginpage (request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Wrong username or password')

    context = {}
    return render(request,'logs/login.html', context)

def logoutpage (request):
    logout(request)
    return redirect('login')