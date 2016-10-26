from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from login.views import redirect_home
from .models import Comment
from goal.models import AbstractGoal
from goal.views import redirect_goal

# redirect_subgoal(goal_id, subgoal_id)

def new_comment(request, goal_id, subgoal_id=None):
    if subgoal_id:
        supgoal_id = goal_id
        goal_id = subgoal_id
    goal = get_object_or_404(AbstractGoal, pk=goal_id)

    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
        except Exception as e:
            return HttpResponse("El usuario no existe")
        
        if request.method == "POST":
            if request.POST.get("comment_text"):
                comment = Comment(owner=user, goal=goal, text=request.POST.get("comment_text"))
            comment.save()

            if subgoal_id:
                return redirect_goal(supgoal_id, goal_id)
            else:
                return redirect_goal(goal_id)
        else:
            if subgoal_id:
                return render(request, 'commentary/new_subcomment.html', {'goal': goal, 'supgoal_id': supgoal_id})
            else:
                return render(request, 'commentary/new_comment.html', {'goal': goal})
    else:
        return HttpResponseRedirect("/login")

def modify_comment(request, goal_id, comment_id, subgoal_id=None):
    if subgoal_id:
        supgoal_id = goal_id
        goal_id = subgoal_id
    goal = get_object_or_404(AbstractGoal, pk=goal_id)
    
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST.get("comment_text"):
                comment.text = request.POST.get("comment_text")
            comment.save()

            if subgoal_id:
                return redirect_goal(supgoal_id, goal_id)
            else:
                return redirect_goal(goal_id)
        else:
            if subgoal_id:
                return render(request, 'commentary/modify_subcomment.html', {'goal': goal, 'comment': comment, 'supgoal_id': supgoal_id})
            else:
                return render(request, 'commentary/modify_comment.html', {'goal': goal, 'comment': comment })
    else:
        return HttpResponseRedirect("/login")

def delete_comment(request, goal_id, comment_id, subgoal_id=None):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user.is_authenticated:
        if request.method == "GET":
            comment.delete()
        if subgoal_id:
            return redirect_goal(goal_id, subgoal_id)
        else:
            return redirect_goal(goal_id)
    else:
        return HttpResponseRedirect("/login")


