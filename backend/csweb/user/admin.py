from django.contrib import admin
from user.models.user import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "registere",
    )
    date_hierarchy = "registere"
    ordering = ("id",)
    search_fields = ["username"]
    list_per_page = 10
    ordering = ("id",)
    list_display_links = ("username",)


admin.site.register(User, UserAdmin)
