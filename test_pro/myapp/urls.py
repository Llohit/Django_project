from django.urls import path,include
from rest_framework import routers
from .views import account_views,user_views,user_login_views,user_transaction_llm_views,check_api

router = routers.DefaultRouter()
router.register(r'/account', account_views.Sample, basename="upload")
urlpatterns = [
    path("api/lohit",include(router.urls)),
    path("api/lohit/register_user",user_views.UserView.as_view(),name="register_user"),
    path("api/lohit/login",user_login_views.UserLoginView.as_view(), name = "login"),
    path("api/lohit/financial_info",user_transaction_llm_views.FinancialInfoView.as_view(),name="financial_info"),

    path("api/v1/adduser", check_api.CheckView.as_view(), name="check")
]