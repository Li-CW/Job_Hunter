from user.models.user import User
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models.user import UserSerializer
from django.conf import settings
import time
from django_redis import get_redis_connection
from django.core.cache import cache
from utils.base_view import BaseView
class UserPhotoView(BaseView, APIView):
    @staticmethod
    def save_photo(user_id, photo):
        image_type = ""
        for i in range(len(photo._name) - 1, 0, -1):
            if photo._name[i] == ".":
                break
            image_type = photo._name[i] + image_type
        image_type = "." + image_type
        path = settings.PHOTO_PATH + str(user_id)  + "_" + image_type
        
        with open(path, 'wb+') as destination:
            for chunk in photo.chunks():
                destination.write(chunk)
        
        return settings.PHOTO + str(user_id) + "_" + image_type

    def put(self, request, pk):
        
        new_photo = UserPhotoView.save_photo(pk, request.data["photo"])
        user = User.objects.get(id=int(pk))
        user_dict = user.__dict__
        user_dict["photo"] = new_photo
        serialize = UserSerializer(instance=user, data=user_dict)
        if serialize.is_valid():
            user = serialize.save()
            cache.delete("user:id:" + str(user.id))
            cache.delete("user:username:" + str(user.username))
            return Response({
                'result': "更改成功",
                'photo': user.photo
            })
        return Response({
                'result': "更新失败",
            })
    


class UserView(BaseView, APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)   
        if user_serializer.is_valid():
            try:
                user_serializer.save()
            except:
                return Response({
                    'result': "用户名重复",
                })
            return Response({
            'result': "注册成功",
        })
        return Response({
            'result': "注册失败",
        })
