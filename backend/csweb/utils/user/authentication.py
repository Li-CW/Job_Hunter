from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
from user.models.user import User
from django.conf import settings


import re


# 生成token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    自定义登录认证，使用自有用户表
    """

    username_field = "username"
    PREX = "user:username:"

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            "password": attrs["password"],
        }
        try:
            user = User.objects.get(**authenticate_kwargs)
        except exceptions as e:
            raise exceptions.NotFound(e.args[0])
        refresh = self.get_token(user)
        data = {
            "userId": user.id,
            "username": user.username,
            "photo": user.photo,
            "token": str(refresh.access_token),
            "refresh": str(refresh),
        }
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# 根据token验证
class MyJWTAuthentication(JWTAuthentication):
    """
    修改JWT认证类，返回自定义User表对象
    """

    PREX = "user:id:"

    def get_user(self, validated_token):
        try:
            user_id = validated_token["user_id"]
        except KeyError:
            raise InvalidToken(_("Token contained no recognizable user identification"))
        try:
            user = User.objects.get(**{"id": user_id})
        except User.DoesNotExist:
            raise AuthenticationFailed(_("User not found"), code="user_not_found")
        return user


class MyPermission:
    def has_permission(self, request, view):
        for url_method in settings.PERMISSION_URL:
            if re.match(url_method[0], request.path_info):
                if (
                    len(url_method) == 1
                    or (len(url_method) == 2 and url_method[-1] == 0)
                    or request.method.lower() in url_method[1:]
                ):
                    permission = url_method[-1]
                    if type(permission) != type(0):
                        permission = 0
                    return bool(
                        request.user
                        and request.user.is_authenticated
                        and (int(request.user.vip) & permission) == permission
                    )
        return True

    def has_object_permission(self, request, view, obj):
        # 默认返回 True，表示所有对象级别的权限检查都通过
        return True


class MyAuthentication:
    @staticmethod
    def get_authenticators(request):

        for url_method in settings.AUTHENTICETORS_URL:
            if re.match(url_method[0], request.path_info):
                if len(url_method) == 1 or request.method.lower() in url_method[1:]:
                    return [MyJWTAuthentication()]

        return []

    @staticmethod
    def get_permissions(request):
        return [MyPermission()]
