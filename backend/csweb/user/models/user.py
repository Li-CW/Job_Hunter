from django.db import models
from rest_framework import serializers
from datetime import date
from rest_framework.exceptions import ValidationError
from django.utils import timezone


class User(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    username = models.CharField(max_length=200, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    photo = models.CharField(
        default="https://cdn.acwing.com/media/user/profile/photo/149733_md_15a86531ae.jpg",
        max_length=256,
    )
    state = models.IntegerField(default=0, verbose_name="状态")
    registere = models.DateField(auto_now_add=True, verbose_name="注册时间")
    login_time = models.DateField(default=timezone.now)

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def __str__(self):
        return str(self.id) + self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=256)
    email = serializers.CharField(
        max_length=256,
        default="anonymous@anonymous.com",
        required=False,
        allow_null=True,
    )
    photo = serializers.CharField(max_length=256, required=False, allow_null=True)
    state = serializers.IntegerField(default=0)
    login_time = serializers.DateField(required=False, allow_null=True)
    vip = serializers.IntegerField(default=0, required=False, allow_null=True)

    def create(self, validated_data):
        try:
            return User.objects.create(**validated_data)
        except:
            raise ValidationError("用户名重复")
