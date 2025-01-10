from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'/upload', views.Sample, basename="upload")
urlpatterns = [
    path("api/lohit",include(router.urls)),
]