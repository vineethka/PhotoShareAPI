from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from django.contrib.auth import login as auth_login

# Create your views here.
from PhotoSharingApplication.APIS.helpers import authentication_helper
from PhotoSharingApplication.APIS.helpers.api_helper import JSONResponse, get_response_data
from PhotoSharingApplication.APIS.helpers.serializers import UserSerializer
from PhotoSharingApplication.models import UserProfile


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        user = authentication_helper.login_authenticate(request)
        if user is not None:
            if user.is_active:
                # return success response
                authenticated_user = authenticate(username=user.username, password=request.data['password'])
                auth_login(request, authenticated_user)
                serializer = UserSerializer(authenticated_user)
                return JSONResponse(get_response_data("", serializer.data))
            else:
                return JSONResponse(get_response_data("Invalid user name and password", ""))

        else:
            return JSONResponse(get_response_data("Invalid user name and password", ""))

    else:
        return JSONResponse(get_response_data("bad request", ""))


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        if authentication_helper.is_user_already_exists(request.data['email']):
            return JSONResponse(get_response_data("User already exists", ""))
        else:
            user = UserProfile.objects.create_user(request.data['username'], request.data['email'],
                                                   request.data['password'], request.data['firstName'],
                                                   request.data['lastName'])
            user.save()
            return JSONResponse(get_response_data("", "Success"))

    else:
        return JSONResponse(get_response_data("bad request", ""))






