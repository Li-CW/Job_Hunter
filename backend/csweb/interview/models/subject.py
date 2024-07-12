from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '科目类型'
        verbose_name_plural = '科目类型'

from rest_framework import serializers

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description']
