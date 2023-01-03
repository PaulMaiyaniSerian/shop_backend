from django.urls import path
from . import views


# jwt token auth import
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)



urlpatterns = [
    # test urls
    # path("test/", views.TestApi.as_view(), name="testapi"),
    # auth urls
    # jwt views
    path('token', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    # register_view
    path("register_user", views.UserRegisterView.as_view(), name="register_normal_user"),



]