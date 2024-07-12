from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "工作类型"
        verbose_name_plural = "工作类型"


from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["id", "name", "description"]
