from django.contrib.auth import authenticate
from django.http.response import HttpResponse
from django.shortcuts import render
from PhotoSharingApplication.models import Categories
from django.template import RequestContext, loader


def index(request):
    if request.user.is_authenticated():
        go_to_home(request)
    return render(request, 'views/login.html')


def login(request):
    if request.user.is_authenticated():
        go_to_home(request)
    return render(request, 'views/login.html')


def home(request):
    if request.user.is_authenticated():
        go_to_home(request)
    return render(request, 'views/login.html')


def register(request):
    if request.user.is_authenticated():
        go_to_home(request)
    return render(request, 'views/templates/register.html')


def profile(request):
    if request.user.is_authenticated():
        return render(request, 'views/profile.html')
    return render(request, 'views/login.html')


def category_list(request):
    if request.user.is_authenticated():
        categories = Categories.objects.all()
        # serializer = CategorySerializer(queryset, many=True)

        # return JSONResponse(get_response_data("", serializer.data))
        template = loader.get_template('views/category_list.html')
        context = RequestContext(request, {'categories': categories, })
        return HttpResponse(template.render(context))
    else:
        categories = Categories.objects.all()
        # serializer = CategorySerializer(queryset, many=True)

        # return JSONResponse(get_response_data("", serializer.data))
        template = loader.get_template('views/category_list.html')
        context = RequestContext(request, {'categories': categories, })
        return HttpResponse(template.render(context))

def go_to_home(request):
    categories = Categories.objects.all()
    # serializer = CategorySerializer(queryset, many=True)

    # return JSONResponse(get_response_data("", serializer.data))
    template = loader.get_template('views/category_list.html')
    context = RequestContext(request, {'categories': categories, })
    return HttpResponse(template.render(context))
