from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from login.views import redirect_home
from .models import Goal, SubGoal

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

def new_sub_goal(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    if request.user.is_authenticated:
        if request.method == "POST":
            finish_date = request.POST.get("finish_date")
            if finish_date == '':
                finish_date = timezone.now()
            goal.subgoal_set.create(goal_text=request.POST.get("goal_text"),
                                     finish_date=finish_date,
                                     create_date=timezone.now(),
                                     priority = request.POST.get("priority"),
                                     state = request.POST.get("state")
                                     )
            return redirect_goal(goal_id)
        else:
            return render(request, 'goal/new_sub_goal.html', {'goal': goal})
    else:
        return HttpResponseRedirect("/login")

def delete_goal(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    if request.user.is_authenticated:
        if request.method == "POST":
            goal.delete()
            return redirect_home(request.user.username)
        else:
            return render(request, 'goal/delete.html', {'goal': goal})
    else:
        return HttpResponseRedirect("/login")

def detail_goal(request, goal_id):
    if request.user.is_authenticated:
        goal = get_object_or_404(Goal, pk=goal_id)
        if request.user == goal.owner:
            return render(request, 'goal/detail.html', {'goal': goal})
    return redirect_home(request.user)

def detail_sub_goal(request, goal_id, subgoal_id):
    if request.user.is_authenticated:
        goal = get_object_or_404(Goal, pk=goal_id)
        if request.user == goal.owner:
            subgoal = get_object_or_404(SubGoal, pk=subgoal_id)
            return render(request, 'goal/detail_sub_goal.html', {'subgoal': subgoal})
    return redirect_home(request.user)

def modify_goal(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST.get("finish_date"):
                goal.finish_date = request.POST.get("finish_date")
            if request.POST.get("goal_text"):
                goal.goal_text = request.POST.get("goal_text")
            if request.POST.get("create_date"):
                goal.create_date = request.POST.get("create_date")
            if request.POST.get("priority"):
                goal.priority = request.POST.get("priority")
            if request.POST.get("state"):
                goal.state = request.POST.get("state")
            goal.save()
            return redirect_goal(goal_id)
        else:
            return render(request, 'goal/modify_goal.html', {'goal': goal})

def redirect_goal(id):
    return HttpResponseRedirect("/goal/{}".format(id))
