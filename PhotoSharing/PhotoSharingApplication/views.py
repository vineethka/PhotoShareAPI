from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from rest_framework import status

from django.contrib.auth import authenticate
# Create your views here.


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def login(request):
    if request.method == 'POST':
        return HttpResponse("login")
    else:
        return HttpResponse("not a post request")