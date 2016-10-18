# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login(request):
    # Si esta logueado lo redirecciono al home.
    if request.user.is_authenticated:
        # return redirect_home(request.user.username)
        return HttpResponse("Hola {}".format(request.user.username))
    # Si es una solicitud de login, checkeo que este bien.
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if is_valid(request):
            user = authenticate(username=username, password=password, email=email)
            if user is not None:
                login_user(request, user)
                # return redirect_home(username)
                return HttpResponse("Hola {}".format(username))

    return render(request, 'login/login.html')

@csrf_protect
def new_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if is_valid(request):
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email
                                            )
            # TODO: Comprobar que no redirecciona luego de crear cuenta
            # return redirect_home(username)
            return HttpResponseRedirect('/login')
    return render(request, 'login/new_user.html')

def logout(request):
    logout_user(request)
    return HttpResponseRedirect("/login")

def is_valid(request):
    return (request.POST.get("username")
            and request.POST.get("password")
            and request.POST.get("mail")
            ) is not ''

def redirect_home(username):
    return HttpResponseRedirect("/home/{}".format(username))
