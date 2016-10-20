from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^upload_img', views.upload_img, name="upload_img"),
	url(r'^success_upload', views.seccess_upload, name="success_upload"),
	url(r'^index', views.index, name="index"),
	url(r'^', views.index, name="index"),
	
    
]
