from django.urls import path
from .views import FileUploadView

urlpatterns = [
path('api/lohit/file_upload', FileUploadView.as_view(),name='file_upload_view'),
]