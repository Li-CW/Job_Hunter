from user.views.user import UserView, UserPhotoView
from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenRefreshView
from utils.user.authentication import MyTokenObtainPairView

urlpatterns = [
    path("register/", UserView.as_view(), name="register"),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
