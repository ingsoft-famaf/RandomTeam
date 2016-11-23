from django.shortcuts import render

from django.contrib.auth.models import User
from goal.models import Goal

def show_goals_near_deadline(request):
    if request.user.is_authenticated:
        goals = Goal.objects.all().filter(owner=request.user)
        
        return render(request, 'notifications/show_notifications.html',
                          {'goals': goals})
    return redirect_home(request.user)

# Create your views here.
