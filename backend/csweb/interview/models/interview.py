from django.db import models
from rest_framework import serializers
from interview.models.company import Company
from interview.models.job import Job
from user.models.user import User


class Interview(models.Model):
    title = models.CharField(max_length=255, verbose_name="标题")
    body = models.TextField(verbose_name="正文", default="", blank=True, null=True)
    keywords = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="关键字"
    )
    created_at = models.DateField(
        auto_now_add=True, verbose_name="创建时间", blank=True, null=True
    )
    modified_at = models.DateField(auto_now=True, verbose_name="修改时间")
    interview_at = models.DateField(auto_now=True, verbose_name="考察时间")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=7, verbose_name="作者"
    )
    read_count = models.IntegerField(default=2, verbose_name="阅读数量")
    badge = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="标签",
        default="互联网 后端",
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="公司",
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="工作类型",
    )
    classification_choices = ((1, "实习"), (2, "校招"), (3, "社招"))  # 使用int类型
    classification = models.IntegerField(choices=classification_choices, default=2,verbose_name="分类")
    def __str__(self):
        return str(self.created_at) + " : " + self.title

    class Meta:
        verbose_name = "面经"
        verbose_name_plural = "面经"


from rest_framework import serializers


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"


class InterviewSerializer_list(serializers.ModelSerializer):
    classification_display = serializers.SerializerMethodField()

    class Meta:
        model = Interview
        exclude = ["body", "classification"]

    def get_classification_display(self, obj):
        # 使用Django的get_FOO_display方法来获取可读的选项
        return obj.get_classification_display()
