from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
	path('', views.upload_files, name='upload_files'),
	path('upload', views.upload_files, name='upload_files'),
]