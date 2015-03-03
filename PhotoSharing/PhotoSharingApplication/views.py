from django.contrib.auth import authenticate
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from scipy.integrate.tests.test_integrate import Pi
from PhotoSharingApplication.APIS.helpers.upload_images import ImageForm
from PhotoSharingApplication.models import Categories, UserProfile, Pictures, PictureLikes
from django.template import RequestContext, loader


def index(request):
    if request.user.is_authenticated():
        categories = Categories.objects.all()
        # serializer = CategorySerializer(queryset, many=True)

        # return JSONResponse(get_response_data("", serializer.data))
        template = loader.get_template('views/home.html')
        context = RequestContext(request, {'categories': categories, })
        return HttpResponse(template.render(context))

    return render(request, 'views/login.html')


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/photoshare")
    return render(request, 'views/login.html')


def home(request):
    if request.user.is_authenticated():
        categories = Categories.objects.all()
        # serializer = CategorySerializer(queryset, many=True)

        # return JSONResponse(get_response_data("", serializer.data))
        template = loader.get_template('views/home.html')
        context = RequestContext(request, {'categories': categories, })
        return HttpResponse(template.render(context))
    return render(request, 'views/login.html')


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/photoshare")

    return render(request, 'views/register.html')


def profile(request):
    if request.user.is_authenticated():
        user_profile = UserProfile.objects.get(user_id=request.user.id)
        try:
            pic_count = Pictures.objects.filter(user=request.user).count()
        except Pictures.DoesNotExist:
            pic_count = 0

        return render(request, 'views/profile.html', {'user_profile': user_profile, 'pic_count': pic_count,})
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


def upload_profile_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        # if form.is_valid():
        #     newdoc = Document(docfile = request.FILES['docfile'])
        #     newdoc.save()
        #
        #     # Redirect to the document list after POST
        #     return HttpResponseRedirect(reverse('myapp.views.list'))


def category_detail(request, category_id):
    picture_list = Pictures.objects.filter(category_id=category_id)
    liked_pictures = PictureLikes.objects.filter(user_id=request.user.id, category_id=category_id).picture
    if picture_list is not None and liked_pictures is not None:
        for liked_picture in liked_pictures:
            if liked_picture in picture_list:
                picture_list.remove(liked_picture)

