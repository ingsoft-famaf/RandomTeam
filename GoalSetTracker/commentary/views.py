from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from login.views import redirect_home
from .models import Comment
from goal.models import Goal

def new_comment(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
        except Exception as e:
            return HttpResponse("El usuario no existe")
        if request.method == "POST":
            comment = Comment(owner=user, goal=goal, text=request.POST.get("comment_text"))
            comment.save()
            return redirect_home(request.user.username)
        else:
            return render(request, 'commentary/new_comment.html', {'goal': goal })
    else:
        return HttpResponseRedirect("/login")


#def modify_comment(request, comment_id):
#    comment = get_object_or_404(Goal, pk=comment_id)
#    if request.user.is_authenticated:
#        if request.method == "POST":
#            if request.POST.get("finish_date"):
#                goal.finish_date = request.POST.get("finish_date")
#            if request.POST.get("goal_text"):
#                goal.goal_text = request.POST.get("goal_text")
#            if request.POST.get("create_date"):
#                goal.create_date = request.POST.get("create_date")
#            if request.POST.get("priority"):
#                goal.priority = request.POST.get("priority")
#            if request.POST.get("state"):
#                goal.state = request.POST.get("state")
#            goal.save()
#            return redirect_goal(goal_id)
#        else:
#            return render(request, 'goal/modify_goal.html', {'goal': goal})

#def redirect_goal(id):
#    return HttpResponseRedirect("/goal/{}".format(id))
