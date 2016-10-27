from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.category, name='category'),
    url(r'^(?P<category_id>[0-9]+)/$',views.category_info,name='category_inf'),
    url(r'^(?P<category_id>[0-9]+)/edit/$',views.category_edit,name='category_edit'),
    url(r'^category_new/$',views.category_new,name='category_new'),
    
]

