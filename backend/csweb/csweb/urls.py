from django.contrib import admin

admin.site.site_header = "csweb后台管理系统"
admin.site.site_title = "后台管理"
admin.site.index_title = "我在后台首页"
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("interview/", include("interview.urls")),

]
