from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Item

def index(request):
    return render(request, 'user/index.html')


def user_login(request):
    if request.method != "POST": 
        return HttpResponseRedirect(reverse('user:index'))
    
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('user:profile'))

    return HttpResponseRedirect(reverse('user:index'))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:index'))


def signup_render(request):
    return render(request, 'user/signup.html')


def signup(request):
    if request.method != "POST":
        return render(request, 'user/signup.html')

    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.create_user(username, email, password)
    login(request, user)

    return HttpResponseRedirect(reverse('user:profile'))


@login_required
def profile(request):
    items = Item.objects.all()
    item_list = []
    for item in items:
        if str(item.user) == request.user.username:
            item_list.append(item)

    return render(request, 'user/profile.html', {'user_items': item_list})