from django.core.serializers import serialize
from rest_framework.decorators import api_view
from PhotoSharingApplication.APIS.helpers.api_helper import JSONResponse, get_response_data
from PhotoSharingApplication.APIS.helpers.serializers import PictureSerializer, CategorySerializer
from PhotoSharingApplication.models import Categories, Pictures, PictureCategories

@api_view(['GET'])
def get_all_categories(request):
    if request.method == 'GET':
        queryset = Categories.objects.all()
        serializer = CategorySerializer(queryset, many=True)

        return JSONResponse(get_response_data("", serializer.data))
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


