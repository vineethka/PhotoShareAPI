from django.contrib.auth import authenticate, logout
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import login as auth_login

# Create your views here.
from PhotoSharingApplication.APIS.helpers import authentication_helper
from PhotoSharingApplication.APIS.helpers.api_helper import JSONResponse, get_response_data
from PhotoSharingApplication.APIS.helpers.serializers import UserSerializer
from PhotoSharingApplication.APIS.helpers.upload_images import ImageForm
from PhotoSharingApplication.models import UserProfile, Categories
from django.template import RequestContext, loader


@api_view(['POST', 'GET'])
def do_login(request):
    if request.method == 'POST':
        user = UserProfile.objects.get(username='aptwei')

        # user = authentication_helper.login_authenticate(request)
        if user is not None:
            if user.is_active:
                # return success response
                authenticated_user = authenticate(username=user.username)
                auth_login(request, authenticated_user)
                # serializer = UserSerializer(authenticated_user)
                return HttpResponseRedirect("/")
            else:
                return render(request, 'views/login.html', {'error_message': "Invalid username / password.", })
        else:
            return render(request, 'views/login.html', {'error_message': "Invalid username / password.", })

    else:
        return HttpResponseRedirect("/")


@api_view(['POST', 'GET'])
def do_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


@api_view(['POST', 'GET'])
def do_register(request):
    register_template = loader.get_template('views/register.html')
    if request.method == 'POST':
        if authentication_helper.get_user_with_email_address(request.data['email']) is not None:
            context = RequestContext(request, {'error_message': "Email Already exists", })
            return HttpResponse(register_template.render(context))
        elif authentication_helper.get_user_with_username(request.data['username']) is not None:
            context = RequestContext(request, {'error_message': "Username Already exists", })
            return HttpResponse(register_template.render(context))
        else:
            user = UserProfile.objects.create_user(request.data['username'], request.data['email'],
                                                   request.data['password'])
            user.first_name = request.data['firstName']
            user.last_name = request.data['lastName']
            user.dob = request.data['dob']
            user.is_active = True
            # user.backend = 'django.contrib.auth.backends.ModelBackend'

            user.save()
            if user is not None:
                if user.is_active:
                    # return success response
                    authenticated_user = authenticate(username=request.data['username'])
                    auth_login(request, authenticated_user)
                    # serializer = UserSerializer(authenticated_user)

                    return HttpResponseRedirect("/")
                else:
                    context = RequestContext(request, {'error_message': "Invalid email / password", })
                    return HttpResponse(register_template.render(context))
            else:
                context = RequestContext(request, {'error_message': "Unable to create the user"
                                                                    "Please check the username, email", })
                return HttpResponse(register_template.render(context))

    else:
        return HttpResponseRedirect("/register")


@api_view(['POST'])
def facebook_login(request):
    if request.method == 'POST':
        user = authentication_helper.get_user_with_email_address(request.data['email'])
        if user is not None:
            auth_user = authenticate(username=user.username)
            auth_login(request, auth_user)
            serializer = UserSerializer(user)
            return JSONResponse(get_response_data("", serializer.data))
        else:
            facebook_user = UserProfile.objects.create_facebook_user(request.data["fb_user_id"],
                                                                     request.data["fb_access_token"],
                                                                     request.data["email"], request.data["firstName"],
                                                                     request.data['lastName'])
            facebook_user.save()
            auth_user = authenticate(username=facebook_user.user.username)
            auth_login(request, auth_user)
            serializer = UserSerializer(facebook_user.user)
            return JSONResponse(get_response_data("", serializer.data))

    else:
        return JSONResponse(get_response_data("bad request", ""))


@api_view(['POST', 'GET'])
def upload_profile_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = UserProfile.objects.get(id=request.user.id)
            user_profile.profile_image = form.cleaned_data['image']
            user_profile.save()
            return HttpResponseRedirect("/profile")
    return HttpResponseRedirect("/profile")




