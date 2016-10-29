"""GoalSetTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from login import views as login_views
from goal import views as goal_views
from commentary import views as comment_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from upload import views as upload_views


urlpatterns = [
	url(r'^goal/(?P<goal_id>[0-9]+)/upload/', upload_views.archivo_list, name = 'list_uploads'),
    url(r'^goal/(?P<goal_id>[0-9]+)/editar/(?P<id_archivo>\d+)/$', upload_views.archivo_editar, name = 'edit_upload'),
    url(r'^goal/(?P<goal_id>[0-9]+)/remove_upload/(?P<id_archivo>\d+)/$', upload_views.archivo_eliminar, name = 'remove_upload'),
    url(r'^goal/(?P<goal_id>[0-9]+)/add_file/', upload_views.upload_img, name = 'add_file'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls')),
    url(r'^$', login_views.login, name='login'),
    url(r'^logout$', login_views.logout, name='logout'),
    url(r'^new_user$', login_views.new_user, name='new_user'),
    url(r'^home/(?P<username>[\w.@+-]+)/$', login_views.home, name='home'),
    url(r'^home/$', login_views.home, name='home'),
    url(r'^new_goal$', goal_views.new_goal, name='new_goal'),
    url(r'^goal/(?P<goal_id>[0-9]+)/delete$', goal_views.delete_goal, name='delete_goal'),
    url(r'^goal/(?P<goal_id>[0-9]+)/$', goal_views.detail_goal, name='detail'),
    url(r'^goal/(?P<goal_id>[0-9]+)/modify$', goal_views.modify_goal, name='modify_goal'),
    url(r'^goal/(?P<goal_id>[0-9]+)/new_sub_goal$', goal_views.new_sub_goal, name='new_sub_goal'),
    url(r'^goal/(?P<goal_id>[0-9]+)/subgoal/(?P<subgoal_id>[0-9]+)$', goal_views.detail_sub_goal, name='detail_sub_goal'),
<<<<<<< HEAD
    url(r'^goal/(?P<goal_id>[0-9]+)/subgoal/(?P<subgoal_id>[0-9]+)/modify$', goal_views.modify_sub_goal, name='modify_sub_goal'),
    url(r'^goal/(?P<goal_id>[0-9]+)/subgoal/(?P<subgoal_id>[0-9]+)/new_comment$', comment_views.new_comment, name='new_comment'),
    url(r'^goal/(?P<goal_id>[0-9]+)/subgoal/(?P<subgoal_id>[0-9]+)/modify_comment/(?P<comment_id>[0-9]+)/$', comment_views.modify_comment, name='modify_comment'),
    url(r'^goal/(?P<goal_id>[0-9]+)/subgoal/(?P<subgoal_id>[0-9]+)/delete_comment/(?P<comment_id>[0-9]+)/$', comment_views.delete_comment, name='delete_comment'),
    url(r'^category/',include('category.urls')),
    url(r'^admin/', admin.site.urls),
    # Allauth URLS
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', RedirectView.as_view(url='/upload/media/', permanent=True)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    #url(r'^upload_img', views.upload_img, name="upload_img"),
    #url(r'^listar', views.archivo_list, name="listar"),
    #url(r'^index', views.index, name="index"),
    #url(r'^editar/(?P<id_archivo>\d+)/$', views.archivo_editar, name="archivo_editar"),
    #url(r'^eliminar/(?P<id_archivo>\d+)/$', views.archivo_eliminar, name="archivo_eliminar"),
