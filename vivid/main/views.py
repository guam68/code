from django.shortcuts import render, redirect
from .forms import LoginForm 
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, get_user_model
from django.urls import reverse

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('user-home')
        else:
            messages.error(request, 'There are problems with your form')
            return render(request, 'main/home.html')
    return render(request, 'main/home.html')