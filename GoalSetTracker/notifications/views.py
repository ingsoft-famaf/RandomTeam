from django.shortcuts import render

from datetime import datetime, timedelta
from django.contrib.auth.models import User
from goal.models import Goal

def show_goals_near_deadline(request):
    # we pick 7 days as the number of days that a goal has to be near
    # to the deadline to classify it as 'near to deadline'
    how_many_days = 7
    if request.user.is_authenticated:
        goals = (Goal.objects.all().filter(owner=request.user)
        .filter(finish_date__lte=datetime.now()+timedelta(days=how_many_days)))

        return render(request, 'notifications/show_notifications.html',
                          {'goals': goals})
    return redirect_home(request.user)

# Create your views here.
