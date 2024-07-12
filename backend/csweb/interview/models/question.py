from django.db import models
from rest_framework import serializers
from interview.models.subject import Subject
from interview.models.company import Company

# from interview.models.interview import Interview
from interview.models.job import Job


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name="题目")
    answer = models.TextField(verbose_name="答案")
    keywords = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="关键字"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="创建时间")
    modified_at = models.DateField(auto_now=True, verbose_name="修改时间")
    interview_at = models.DateField(auto_now=True, verbose_name="考察时间")
    author = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, default=7, verbose_name="作者"
    )
    badge = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="标签",
        default="互联网 计算机 面试",
    )
    read_count = models.IntegerField(default=2, verbose_name="阅读数量")
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="科目"
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="科目",
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="工作类型",
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "问题"
        verbose_name_plural = "问题"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionSerializer_exclude_answer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ["answer"]
