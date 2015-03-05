from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from rest_framework.decorators import api_view
from PhotoSharingApplication.APIS.helpers.api_helper import JSONResponse, get_response_data
from PhotoSharingApplication.models import PictureLikes, PictureAbuseReports


@api_view(['POST'])
def like(request):
    if request.method == 'POST':

        picture_id = request.data['picture_id']
        user_id = request.data["user_id"]
        is_power_vote = request.data['is_power_vote']
        like_count = request.data['like_count']

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
                get_list_or_404(PictureLikes,user=user_id, picture=picture_id)
                # PictureLikes.objects.get(user=user_id, picture=picture_id)
                return JSONResponse(get_response_data("You can not dislike the picture that you already liked", ""))
            except Http404:
                save_picture_like(request)
                return JSONResponse(get_response_data("", "Success"))
        #Normal like
        else:
            try:
                get_list_or_404(PictureLikes,user=user_id, picture=picture_id)
                return JSONResponse(get_response_data("User already liked this picture", ""))
            except Http404:
                save_picture_like(request)
                return JSONResponse(get_response_data("", "Success"))


@api_view(['POST'])
def abuse_picture(request, picture_id):
    if request.method == 'POST':
        try:
            picture_id = picture_id
            subject = request.data['subject']
            comment = request.data['comment']
            picture_abuse_report = PictureAbuseReports()
            picture_abuse_report.user_id = 1
            picture_abuse_report.picture_id = picture_id
            picture_abuse_report.subject = subject
            picture_abuse_report.comment = comment
            picture_abuse_report.save()
            return render(request, 'views/report_a_pic.html', {'error_message': "Reported abuse.", })
        except PictureAbuseReports.DoesNotExist:
            return render(request, 'views/report_a_pic.html', {'error_message': "Failed to report abuse", })
    else:
        return HttpResponseRedirect("/report_a_pic/" + picture_id)



def save_picture_like(request):
    picture_id = request.data['picture_id']
    user_id = request.data["user_id"]
    is_power_vote = request.data['is_power_vote']
    like_count = request.data['like_count']

    picture_like = PictureLikes()
    picture_like.picture_id = picture_id
    picture_like.user_id = user_id
    picture_like.is_in_app_vote = is_power_vote
    picture_like.like_count = like_count
    picture_like.save()