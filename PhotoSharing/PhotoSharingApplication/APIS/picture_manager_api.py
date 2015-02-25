from datetime import date
from rest_framework.decorators import api_view
from PhotoSharingApplication.models import PictureLikes


@api_view(['GET'])
def like(request):
    if request.method == 'POST':
        picture_id = request.data['picture_id']
        user_id = request.data["user_id"]

        picture_like = PictureLikes()
        picture_like.picture_id = picture_id
        picture_like.user_id = user_id
        picture_like.created_at = date.ctime()
        picture_like.updated_at = date.ctime()
        picture_like.save()



