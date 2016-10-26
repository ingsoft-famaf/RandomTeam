# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from login.views import redirect_home
from goal.models import Goal
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
       return render(request,'category/category_info.html',{'category' : category})
    else:
        return HttpResponseRedirect("/login")

def category_new(request):
   if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
        except Exception as e:
<<<<<<< HEAD
            return HttpResponse("El usuario no existe")
<<<<<<< HEAD
        return HttpResponse("estas en categorias")
=======
=======
            return HttpResponse("The user do not exist")
>>>>>>> Congruencia de idioma en Category
        if request.method == "POST":
             user.category_set.create(category_tipo=request.POST.get("category_tipo"))
             return redirect_home(request.user.username)
        else:
            return render(request,'category/category_new.html')
   else:
        return HttpResponseRedirect("/login")

def category_edit(request,category_id):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
            category = get_object_or_404(Category, pk=category_id)
        except Exception as e:
            return HttpResponse("The user do not exist")
        if request.method == "POST":
             if request.POST.get("category_tipo"):
                  category.category_tipo = request.POST.get("category_tipo")
             category.save()
             return redirect_home(request.user.username)
        else:
<<<<<<< HEAD
            return render(request,'category/category_edit.html',{'catego' : catego})
>>>>>>> categorias agregadas, faltan relacionar categoria goals
=======
            return render(request,'category/category_edit.html',{'category' : category})
>>>>>>> Congruencia de idioma en Category
    else:
        return HttpResponseRedirect("/login")




