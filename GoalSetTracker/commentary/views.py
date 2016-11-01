from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from login.views import redirect_home
from .models import Comment
from goal.models import Goal
from goal.views import redirect_goal

def new_comment(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
        except Exception as e:
            return HttpResponse("El usuario no existe")
        if request.method == "POST":
            if request.POST.get("comment_text"):
                comment = Comment(owner=user, goal=goal, text=request.POST.get("comment_text"))
            comment.save()
            return redirect_goal(goal_id)
        else:
            return render(request, 'commentary/new_comment.html', {'goal': goal })
    else:
        return HttpResponseRedirect("/login")

def modify_comment(request, goal_id, comment_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST.get("comment_text"):
                comment.text = request.POST.get("comment_text")
            comment.save()
            return redirect_goal(goal_id)
        else:
            return render(request, 'commentary/modify_comment.html', {'goal': goal, 'comment': comment })
    else:
        return HttpResponseRedirect("/login")

def delete_comment(request, goal_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user.is_authenticated:
        if request.method == "GET":
            comment.delete()
        return redirect_goal(goal_id)
    else:
        return HttpResponseRedirect("/login")
