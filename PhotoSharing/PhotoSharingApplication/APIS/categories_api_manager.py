from django.core.serializers import serialize
from rest_framework.decorators import api_view
from PhotoSharingApplication.APIS.helpers.api_helper import JSONResponse, get_response_data
from PhotoSharingApplication.models import Categories

__author__ = 'suslov'

@api_view(['GET'])
def get_all_categories(request):
    if request.method == 'GET':
        return JSONResponse(get_response_data("", serialize('python', Categories.objects.all())))
    else:
        return JSONResponse(get_response_data("bad request", ""))


