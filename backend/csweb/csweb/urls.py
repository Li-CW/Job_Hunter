from django.contrib import admin

admin.site.site_header = "csweb后台管理系统"
admin.site.site_title = "后台管理"
admin.site.index_title = "我在后台首页"
from django.urls import path, include, re_path
from csweb.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("interview/", include("interview.urls")),
    re_path(r"^[a-zA-Z]*", index),
]
