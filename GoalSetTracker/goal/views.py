from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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
                                 finish_date=finish_date,
                                 create_date=timezone.now(),
                                 priority = request.POST.get("priority"),
                                 state = request.POST.get("state")
                                 )
            return redirect_home(request.user.username)
        else:
            return render(request, 'goal/new_goal.html')
    else:
        return HttpResponseRedirect("/login")

#TODO: Sacar el "default" de goal_id
def new_sub_goal(request, goal_id=1):
    if request.user.is_authenticated:
        goal = get_object_or_404(Goal, pk=goal_id)
        if request.method == "POST":
            finish_date = request.POST.get("finish_date")
            if finish_date == '':
                finish_date = timezone.now()
            goal.subgoal_set.create(sub_goal_text=request.POST.get("sub_goal_text"))
            return redirect_goal(goal_id)
        else:
            return render(request, 'goal/new_sub_goal.html')
    else:
        return HttpResponseRedirect("/login")

#TODO: Comprobar que se accede a metas del usuario.
def detail_goal(request, goal_id):
    if request.user.is_authenticated:
        goal = get_object_or_404(Goal, pk=goal_id)
        return render(request, 'goal/detail.html', {'goal': goal})

def redirect_goal(id):
    return HttpResponseRedirect("/goal/{}".format(id))
