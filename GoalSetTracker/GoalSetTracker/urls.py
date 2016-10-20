"""GoalSetTracker URL Configuration
>>>>>>> recibiendo el formulario

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
<<<<<<< HEAD
from django.conf.urls import include, url
from django.contrib import admin
from login import views as login_views
from goal import views as goal_views
from commentary import views as comment_views

urlpatterns = [
	url(r'^upload/', include("upload.urls")),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls')),
    url(r'^$', login_views.login, name='login'),
    url(r'^logout$', login_views.logout, name='logout'),
    url(r'^new_user$', login_views.new_user, name='new_user'),
    url(r'^home/(?P<username>[\w.@+-]+)/$', login_views.home, name='home'),
    url(r'^home/$', login_views.home, name='home'),
    url(r'^new_goal$', goal_views.new_goal, name='new_goal'),
    url(r'^goal/(?P<goal_id>[0-9]+)/$', goal_views.detail_goal, name='detail'),
    url(r'^goal/(?P<goal_id>[0-9]+)/modify$', goal_views.modify_goal, name='modify_goal'),
    url(r'^goal/(?P<goal_id>[0-9]+)/new_sub_goal$', goal_views.new_sub_goal, name='new_sub_goal'),
    url(r'^goal/(?P<goal_id>[0-9]+)/subgoal/(?P<subgoal_id>[0-9]+)$', goal_views.detail_sub_goal, name='detail_sub_goal'),
    url(r'^goal/(?P<goal_id>[0-9]+)/delete$', goal_views.delete_goal, name='delete_goal'),
    url(r'^goal/(?P<goal_id>[0-9]+)/new_comment$', comment_views.new_comment, name='new_comment'),
    url(r'^goal/(?P<goal_id>[0-9]+)/modify_comment/(?P<comment_id>[0-9]+)/$', comment_views.modify_comment, name='modify_comment'),
    url(r'^goal/(?P<goal_id>[0-9]+)/delete_comment/(?P<comment_id>[0-9]+)/$', comment_views.delete_comment, name='delete_comment'),
]
