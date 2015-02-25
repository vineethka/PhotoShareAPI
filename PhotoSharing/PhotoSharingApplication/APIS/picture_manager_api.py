from datetime import date
from rest_framework.decorators import api_view
from PhotoSharingApplication.APIS.helpers.api_helper import JSONResponse, get_response_data
from PhotoSharingApplication.models import PictureLikes


@api_view(['POST'])
def like(request):
    if request.method == 'POST':
        picture_id = request.data['picture_id']
        user_id = request.data["user_id"]

        picture_like = PictureLikes()
        picture_like.picture_id = picture_id
        picture_like.user_id = user_id
        picture_like.save()
        return JSONResponse(get_response_data("", "Success"))
    else:
        return JSONResponse(get_response_data("bad request", ""))



