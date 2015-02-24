from django.contrib.auth import  authenticate
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import login as auth_login

# Create your views here.
from PhotoSharingApplication import authentication_helper
from PhotoSharingApplication.serializers import UserSerializer


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


def get_response_data(error_message, response_data):
    content = {'data': response_data, 'errorMessage': error_message}
    return content



