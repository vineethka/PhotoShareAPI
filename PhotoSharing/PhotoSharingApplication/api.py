from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import login as auth_login

# Create your views here.
from PhotoSharingApplication import authentication_helper
from PhotoSharingApplication.serializers import UserSerializer
from PhotoSharingApplication.models import UserProfile

SUCCESS_STRING = "Success"
FAILED_STRING = "Failed"

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

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


def get_response_data(error_message, response_data):

    if error_message == "":
        response_code = SUCCESS_STRING
    else:
        response_code = FAILED_STRING

    content = {'responseCode': response_code, 'data': response_data, 'errorMessage': error_message}
    return content



