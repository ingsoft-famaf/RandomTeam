from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from goal.models import Goal

def show_goals_near_deadline(request):
    # we pick 7 days as the number of days that a goal has to be near
    # to the deadline to classify it as 'near to deadline'
    how_many_days = 7
    if request.user.is_authenticated:
        goals = (Goal.objects.all().filter(owner=request.user)
        .filter(finish_date__lte=timezone.now()+timedelta(days=how_many_days))
        .exclude(state="FINISH"))
        return render(request, 'notifications/show_notifications.html',
                          {'goals': goals})
    return HttpResponseRedirect("/login")

def goal_exist_near_deadline(request):
    how_many_days = 7
    if request.user.is_authenticated:
        g_near_deadline = (Goal.objects.all().filter(owner=request.user)
        .filter(finish_date__lte=timezone.now()+timedelta(days=how_many_days))
        .exclude(state="FINISH"))
        return HttpResponse((g_near_deadline.count() > 0))
    else:
        return HttpResponseRedirect("/login")
