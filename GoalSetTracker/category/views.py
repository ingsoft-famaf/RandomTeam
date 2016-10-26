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
            return HttpResponse("El usuario no existe")
        context = {'category_all': category_all,}
        return render(request,'category/category.html',context)
    else:
        return HttpResponseRedirect("/login")

def category_info(request,category_id):
    if request.user.is_authenticated:
       catego = get_object_or_404(Category, pk=category_id)
       return render(request,'category/category_info.html',{'catego' : catego})
    else:
        return HttpResponseRedirect("/login")

def category_new(request):
   if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
        except Exception as e:
            return HttpResponse("El usuario no existe")
<<<<<<< HEAD
        return HttpResponse("estas en categorias")
=======
        if request.method == "POST":
             user.category_set.create(categoria_tipo=request.POST.get("categoria_tipo"))
             return redirect_home(request.user.username)
        else:
            return render(request,'category/category_new.html')
   else:
        return HttpResponseRedirect("/login")

def category_edit(request,category_id):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
            catego = get_object_or_404(Category, pk=category_id)
        except Exception as e:
            return HttpResponse("El usuario no existe")
        if request.method == "POST":
             catego.categoria_tipo = categoria_tipo=request.POST.get("categoria_tipo")
             return redirect_home(request.user.username)
        else:
            return render(request,'category/category_edit.html',{'catego' : catego})
>>>>>>> categorias agregadas, faltan relacionar categoria goals
    else:
        return HttpResponseRedirect("/login")




