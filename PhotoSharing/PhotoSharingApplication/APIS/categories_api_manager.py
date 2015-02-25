from django.core.serializers import serialize
from rest_framework.decorators import api_view
from PhotoSharingApplication.APIS.helpers.api_helper import JSONResponse, get_response_data
from PhotoSharingApplication.models import Categories, Pictures, PictureCategories

__author__ = 'suslov'

@api_view(['GET'])
def get_all_categories(request):
    if request.method == 'GET':
        return JSONResponse(get_response_data("", serialize('python', Categories.objects.all())))
    else:
        return JSONResponse(get_response_data("bad request", ""))

@api_view(['POST'])
def get_pictures_for_category(request):
    if request.method == 'POST':
        return JSONResponse(get_response_data("", serialize('python', Pictures.objects.filter(category_id=request.data['category_id']))))
    else:
        return JSONResponse(get_response_data("bad request", ""))


