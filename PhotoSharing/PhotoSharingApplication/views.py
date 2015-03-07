from django.db.models import Sum
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from PhotoSharingApplication.APIS.helpers.upload_images import ImageForm
from PhotoSharingApplication.models import Categories, UserProfile, Pictures, PictureLikes
from django.template import RequestContext, loader
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

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
        return HttpResponseRedirect("/")
    return render(request, 'views/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')


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
        return HttpResponseRedirect("/")

    return render(request, 'views/register.html')


def profile(request):
    if request.user.is_authenticated():
        try:
            user_profile = UserProfile.objects.get(id=request.user.id)
        except UserProfile.DoesNotExist:
            user_profile = request.user

        try:
            like_pic_count = Pictures.objects.filter(picturelikes__user_id=request.user.id).distinct().count()
        except Pictures.DoesNotExist:
            like_pic_count = 0
        uploaded_pic_count = Pictures.objects.filter(user_id=request.user.id).count()

        return render(request, 'views/profile.html', {'user_profile': user_profile, 'like_pic_count': like_pic_count, 'uploaded_pic_count': uploaded_pic_count})
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

    if request.user.is_authenticated():
        pictures = Pictures.objects.filter(category_id=category_id).exclude(picturelikes__user_id=request.user.id)
        template = loader.get_template('views/category_image_list.html')
        context = RequestContext(request, {'pictures': pictures, })
        return HttpResponse(template.render(context))
    return render(request, 'views/login.html')


def likes(request):

    if request.user.is_authenticated():
        pictures = Pictures.objects.filter(picturelikes__user_id=request.user.id).distinct()
        template = loader.get_template('views/like.html')
        context = RequestContext(request, {'pictures': pictures, })
        return HttpResponse(template.render(context))
    return render(request, 'views/login.html')


def uploaded(request):
    if request.user.is_authenticated():
        pictures = Pictures.objects.filter(user_id=request.user.id)
        template = loader.get_template('views/category_image_list.html')
        context = RequestContext(request, {'pictures': pictures, })
        return HttpResponse(template.render(context))
    return render(request, 'views/login.html')


def report_a_pic(request, picture_id):

    if request.user.is_authenticated():
        picture = Pictures.objects.get(id=picture_id)
        template = loader.get_template('views/report_a_pic.html')
        context = RequestContext(request, {'picture': picture, })
        return HttpResponse(template.render(context))
    return render(request, 'views/login.html')


def image_details(request, picture_id):

    if request.user.is_authenticated():
        picture = Pictures.objects.get(id=picture_id)
        like_count_agg = PictureLikes.objects.filter(picture_id=picture_id).aggregate(Sum('like_count'))
        like_count = 0
        if like_count_agg['like_count__sum'] != None:
            like_count = like_count_agg['like_count__sum']
        template = loader.get_template('views/image_details.html')
        context = RequestContext(request, {'picture': picture, 'like_count': like_count})
        return HttpResponse(template.render(context))
    return render(request, 'views/login.html')


def upload(request):
    if request.user.is_authenticated():
        return render(request, 'views/upload.html')

    return render(request, 'views/login.html')