from rest_framework.decorators import api_view
from PhotoSharingApplication.APIS.helpers.api_helper import JSONResponse, get_response_data
from PhotoSharingApplication.models import PictureLikes, PictureAbuseReports


@api_view(['POST'])
def like(request):
    if request.method == 'POST':
        picture_id = request.data['picture_id']
        user_id = request.data["user_id"]
        try:
            like = PictureLikes.objects.get(user=user_id,picture=picture_id)
        except PictureLikes.DoesNotExist:
            like = None

        if like is None:
            picture_like = PictureLikes()
            picture_like.picture_id = picture_id
            picture_like.user_id = user_id
            picture_like.save()
            return JSONResponse(get_response_data("", "Success"))
        else:
            return JSONResponse(get_response_data("User already liked this picture", ""))

    else:
        return JSONResponse(get_response_data("bad request", ""))


@api_view(['POST'])
def abuse_picture(request):
    if request.method == 'POST':
        picture_id = request.data['picture_id']
        user_id = request.data['user_id']
        subject = request.data['subject']
        comment = request.data['comment']
        picture_abuse_report = PictureAbuseReports()
        picture_abuse_report.user_id = user_id
        picture_abuse_report.picture_id = picture_id
        picture_abuse_report.subject = subject
        picture_abuse_report.comment = comment
        picture_abuse_report.save()
        return JSONResponse(get_response_data("", "Success"))

