from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^upload_img', views.upload_img, name="upload_img"),
	url(r'^listar', views.archivo_list, name="listar"),
	url(r'^index', views.index, name="index"),
	url(r'^editar/(?P<id_archivo>\d+)/$', views.archivo_editar, name="archivo_editar"),
	url(r'^eliminar/(?P<id_archivo>\d+)/$', views.archivo_eliminar, name="archivo_eliminar"),
]
