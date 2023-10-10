from django.urls import path
from . import views

urlpatterns = [
    path('files/', views.file_upload, name='file_upload'),
    path('files/success/', views.file_upload, name='file_upload_success'),
]
