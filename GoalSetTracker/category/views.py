# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from login.views import redirect_home
from goal.models import AbstractGoal
from .models import Category
from django.template import loader

def category(request):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
            category_all = user.category_set.all()
        except Exception as a:
            return HttpResponse("The user do not exist")
        context = {'category_all': category_all,}
        return render(request,'category/category.html',context)
    else:
        return HttpResponseRedirect("/login")

def category_info(request,category_id):
    if request.user.is_authenticated:
       category = get_object_or_404(Category, pk=category_id)
       if request.user == category.owner:
          return render(request,'category/category_info.html',{'category' : category})
       else:
          return redirect_home(request.user)
    else:
       return HttpResponseRedirect("/login")

def category_new(request):
   if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
        except Exception as e:
            return HttpResponse("The user do not exist")
        if request.method == "POST" and request.POST.get("category_tipo") != "" :
             user.category_set.create(category_tipo=request.POST.get("category_tipo"))
             return HttpResponseRedirect("/category")
        else:
            return render(request,'category/category_new.html')
   else:
        return HttpResponseRedirect("/login")

def category_edit(request,category_id):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
            category = get_object_or_404(Category, pk=category_id)
            goals_all = user.abstractgoal_set.all()
        except Exception as e:
            return HttpResponse("The user do not exist")
        if request.method == "POST":
             if request.POST.get("category_tipo"):
                  category.category_tipo = request.POST.get("category_tipo")
             if request.POST.getlist('goal_add[]'):
                  add_goal_list = request.POST.getlist('goal_add[]')
                  for add_goal in add_goal_list:
                         category.goal.add(user.abstractgoal_set.get(pk=add_goal))
             if request.POST.getlist('goal_rem[]'):
                  rem_goal_list = request.POST.getlist('goal_rem[]')
                  for rem_goal in rem_goal_list:
                         category.goal.remove(user.abstractgoal_set.get(pk=rem_goal))
             category.save()
             if request.POST.get("deleted"):
                  category.delete()
             return HttpResponseRedirect("/category")
        else:
            if user == category.owner:
              return render(request,'category/category_edit.html',{'category' : category, 'goals_all' : goals_all})
            else:
              return redirect_home(request.user)
    else:
        return HttpResponseRedirect("/login")




