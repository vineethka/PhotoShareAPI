from django.contrib.auth import authenticate
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    if request.user.is_authenticated():
        return render(request, 'views/home.html')
    return render(request, 'views/login.html')


def login(request):
    if request.user.is_authenticated():
        return render(request, 'views/home.html')
    return render(request, 'views/login.html')


def home(request):
    if request.user.is_authenticated():
        return render(request, 'views/home.html')
    return render(request, 'views/login.html')


def register(request):
    if request.user.is_authenticated():
        return render(request, 'views/home.html')
    return render(request, 'views/register.html')
