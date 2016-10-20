from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from login.views import redirect_home
from .models import Goal

def new_goal(request):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
        except Exception as e:
            return HttpResponse("El usuario no existe")
        if request.method == "POST":
            finish_date = request.POST.get("finish_date")
            if finish_date == '':
                finish_date = timezone.now()
            user.goal_set.create(goal_text=request.POST.get("goal_text"),
                                 finish_date=finish_date
                                 )
            return redirect_home(request.user.username)
        else:
            return render(request, 'goal/new_goal.html')
    else:
        return HttpResponseRedirect("/login")
