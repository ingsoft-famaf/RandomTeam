# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from login.views import redirect_home
from goal.models import Goal

def category(request):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
        except Exception as e:
            return HttpResponse("El usuario no existe")
        return HttpResponse("estas en categorias")   
#        if request.method == "POST":
#            finish_date = request.POST.get("finish_date")
#            if finish_date == '':
#                finish_date = timezone.now()
#            user.goal_set.create(goal_text=request.POST.get("goal_text"),
#                                 finish_date=finish_date,
#                                 create_date=timezone.now(),
#                                 priority = request.POST.get("priority"),
#                                 state = request.POST.get("state")
#                                 )
#            return redirect_home(request.user.username)
#        else:
#            return render(request, 'goal/new_goal.html')
    else:
        return HttpResponseRedirect("/login")

