from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
	path('multiple', views.upload_multiple_files, name='upload_multiple_files'),
]