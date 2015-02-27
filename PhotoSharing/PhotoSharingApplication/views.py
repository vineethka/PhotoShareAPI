from django.contrib.auth import authenticate
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    if request.user.is_authenticated():
        return HttpResponse("Home screen")
    return render(request, 'views/login.html')
