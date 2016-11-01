# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from goal.models import AbstractGoal, Goal, SubGoal


@csrf_protect
def login(request):
    # Si esta logueado lo redirecciono al home.
    if request.user.is_authenticated:
        return redirect_home(request.user.username)
    # Si es una solicitud de login, checkeo que este bien.
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if is_valid(request):
            user = authenticate(username=username,
                                password=password,
                                email=email)
            if user is not None:
                login_user(request, user)
                return redirect_home(username)

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
            user.save()
            user = authenticate(username=username, password=password, email=email)
            login_user(request, user)
            return redirect_home(username)
    return HttpResponseRedirect('/login')


def logout(request):
    logout_user(request)
    return HttpResponseRedirect("/login")


def is_valid(request):
    return (request.POST.get("username")
            and request.POST.get("password")
            and request.POST.get("mail")
            ) is not ''

def home(request, username="Anonymous"):
    if request.user.is_authenticated:
        # Si el usuario esta logueado y quiere ver su home, continuo
        if request.user.username == username:
            try:
                user = User.objects.get(username=username)
                goals = Goal.objects.filter(owner=user)
                categories = user.category_set.all()
            except Exception as e:
                return HttpResponse("El usuario no existe")
            actives = [goal for goal in goals if goal.is_active()]
            finished = [goal for goal in goals if not goal.is_active()]
            goals_f = goals
            if request.method == "POST":
                if request.POST.getlist('category_filter[]'):
                    goals_f = goals_f.filter(category__in = request.POST.getlist('category_filter[]')).distinct()
                if request.POST.get("sort"):
                    sort_o = request.POST.get("sort")
                    if sort_o == "Z-A":
                       goals_f = goals_f.order_by('-goal_text')
                    elif sort_o == "FECHA_N":
                       goals_f = goals_f.order_by('finish_date')
                    elif sort_o == "FECHA_L":
                       goals_f = goals_f.order_by('-finish_date')
                    else:
                       goals_f = goals_f.order_by('goal_text')
            return render(request, 'login/home.html', {
                'user': username,
                'goals': goals,
                'actives': actives,
                'finished': finished,
                'categories': categories,
                'goals_f': goals_f,
                })
        else:
            # El usuario quiere ingresar a otro home que no es el suyo.
            return redirect_home(request.user.username)
    else:
        return HttpResponseRedirect("/login")


def redirect_home(username):
    return HttpResponseRedirect("/home/{}".format(username))
