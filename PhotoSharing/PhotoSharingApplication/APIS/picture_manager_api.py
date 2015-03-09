from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from rest_framework.decorators import api_view
from PhotoSharingApplication.APIS.helpers.api_helper import JSONResponse, get_response_data
from PhotoSharingApplication.APIS.helpers.serializers import PictureSerializer
from PhotoSharingApplication.APIS.helpers.upload_images import ImageForm
from PhotoSharingApplication.models import PictureLikes, PictureAbuseReports, Pictures, UserProfile


@api_view(['POST'])
def like(request):
    if request.method == 'POST':

        picture_id = request.data['picture_id']
        # user_profile = UserProfile.objects.get(user_id=request.user.id)

        user_id = request.user.id
        # is_power_vote = request.data['is_power_vote']
        is_power_vote = 0

        like_count = int(request.data['like_count'])

        if is_power_vote:
            try:
                picture_like = PictureLikes.objects.get(user=user_id, picture=picture_id, is_in_app_vote=True)
                picture_like.like_count = like_count + picture_like.like_count
                picture_like.save()
                return JSONResponse(get_response_data("", "Success"))
            except PictureLikes.DoesNotExist:
                save_picture_like(request)
                return JSONResponse(get_response_data("", "Success"))
        # dislike
        elif like_count < 0:
            try:
                get_list_or_404(PictureLikes, user=user_id, picture=picture_id)
                # PictureLikes.objects.get(user=user_id, picture=picture_id)
                return JSONResponse(get_response_data("You can not dislike the picture that you already liked", ""))
            except Http404:
                save_picture_like(request, user_id)
                return JSONResponse(get_response_data("", "Success"))
        # Normal like
        else:
            try:
                get_list_or_404(PictureLikes, user=user_id, picture=picture_id)
                return JSONResponse(get_response_data("User already liked this picture", ""))
            except Http404:
                save_picture_like(request, user_id)
                return JSONResponse(get_response_data("", "Success"))


@api_view(['POST', 'GET'])
def abuse_picture(request):

    if request.method == 'POST':
        picture = Pictures.objects.get(id=request.data['picture_id'])

        try:

            picture_id = request.data['picture_id']

            subject = request.data['subject']
            comment = request.data['comment']
            picture_abuse_report = PictureAbuseReports()
            picture_abuse_report.user_id = request.user.id
            picture_abuse_report.picture_id = picture_id
            picture_abuse_report.subject = subject
            picture_abuse_report.comment = comment
            picture_abuse_report.save()
            return render(request, 'views/report_a_pic.html',
                          {'error_message': "Reported abuse.", 'picture': picture, })
        except PictureAbuseReports.DoesNotExist:
            return render(request, 'views/report_a_pic.html',
                          {'error_message': "Failed to report abuse", 'picture': picture, })
    else:
        return HttpResponseRedirect("/")


def save_picture_like(request, user_id):
    picture_id = request.data['picture_id']
    # is_power_vote = request.data['is_power_vote']
    is_power_vote = 0
    like_count = int(request.data['like_count'])

    picture_like = PictureLikes()
    picture_like.picture_id = picture_id
    picture_like.user_id = user_id
    picture_like.is_in_app_vote = is_power_vote
    picture_like.like_count = like_count
    picture_like.save()


@api_view(['POST', 'GET'])
def upload_picture(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            picture = Pictures(user_id=request.user.id)
            picture.image = form.cleaned_data['image']
            picture.category_id = 1
            picture.save()
            serializer = PictureSerializer(picture)
            return JSONResponse(get_response_data("", serializer.data))

    return HttpResponseRedirect("/upload")

