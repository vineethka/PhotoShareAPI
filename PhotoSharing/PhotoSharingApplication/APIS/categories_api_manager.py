from django.core.serializers import serialize
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from PhotoSharingApplication.APIS.helpers.api_helper import JSONResponse, get_response_data
from PhotoSharingApplication.APIS.helpers.serializers import PictureSerializer, CategorySerializer
from PhotoSharingApplication.models import Categories, Pictures, PictureCategories
from django.template import RequestContext, loader


@api_view(['GET'])
def get_all_categories(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        # serializer = CategorySerializer(queryset, many=True)

        # return JSONResponse(get_response_data("", serializer.data))
        template = loader.get_template('views/category_list.html')
        context = RequestContext(request, {'categories': categories, })
        return HttpResponse(template.render(context))
    else:
        return JSONResponse(get_response_data("bad request", ""))

@api_view(['POST'])
def get_pictures_for_category(request):
    if request.method == 'POST':
        queryset = Pictures.objects.all()
        serializer = PictureSerializer(queryset, many=True)

        return JSONResponse(get_response_data("", serializer.data))
    else:
        return JSONResponse(get_response_data("bad request", ""))


