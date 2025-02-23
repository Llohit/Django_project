from django.urls import path,include
from rest_framework import routers
from .views import account_views,user_views,user_login_views

router = routers.DefaultRouter()
router.register(r'/upload', account_views.Sample, basename="upload")
urlpatterns = [
    path("api/lohit",include(router.urls)),
    path("api/lohit/register_user",user_views.UserView.as_view(),name="register_user"),
    path("api/lohit/login",user_login_views.UserLoginView.as_view(), name = "login"),
]