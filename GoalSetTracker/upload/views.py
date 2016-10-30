from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
import models
from django.contrib.auth.decorators import login_required
from . import forms
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import os
from os.path import join, basename, isfile
from GoalSetTracker.settings import MEDIA_ROOT
from goal.models import AbstractGoal
from goal.views import redirect_goal
from login.views import redirect_home
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User





@csrf_protect
def upload_img(request, goal_id):
    goal = get_object_or_404(AbstractGoal, pk=goal_id)
    if not os.path.exists(join(MEDIA_ROOT, 'Archivo/'+str(goal_id))):
        os.makedirs(join(MEDIA_ROOT, 'Archivo/'+str(goal_id)))
    error = None
    flag = True
    error2 = None
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
        except Exception as e:
            return HttpResponse("El usuario no existe")
        if request.method == 'POST':
            form = forms.ArchivoForm(request.POST, request.FILES)
            if form.is_valid():
                tiene_url = len(form.cleaned_data['url']) > 0
                tiene_file = len(request.FILES) > 0
                if ((not tiene_url) and (not tiene_file)) or (tiene_url and tiene_file):
                    error = "Debe tener url o archivo"
                else:
                
                    for file in os.listdir(join(MEDIA_ROOT, 'Archivo/'+str(goal_id))):
                        if file == form.cleaned_data['upload'].name:
                            error2 = "Este archivo ya se encuenta en esta meta"
                            flag = False
                    if flag:
                        form.save()
                        return redirect_goal(goal_id)
        else:
            form = forms.ArchivoForm(initial={'goal': goal_id, 'owner': user})
        form.fields['goal'].widget = forms.HiddenInput()
        form.fields['is_public'].widget = forms.HiddenInput()
        form.fields['owner'].widget = forms.HiddenInput()
        return render(request, "upload/index.html",{'goal': goal, "form":form, 
                                                 "mensaje_error": error,
                                                 "mensaje_error": error2})
                                                 #"action": reverse('add_file')})
    else:
        return HttpResponseRedirect("/login")


def protected_serve(request, path, file_root=None):
    try:
        archivo = models.Archivo.objects.get(owner=request.user.id)
        archivo_url = archivo.upload.url
        correct_archivo_url = archivo_url.replace("/media/", "")
        if correct_archivo_url == path:
            return serve(request, path, file_root)
    except ObjectDoesNotExist:
        return HttpResponse("Sorry you don't have permission to access this file")

    



@login_required
def archivo_list(request, goal_id):
    goal = get_object_or_404(AbstractGoal, pk=goal_id)
    archivos = models.Archivo.objects.all().filter(goal=goal.id)
    return render(request, 'upload/archivo_list.html', {'goal': goal, 'archivos': archivos.all()})
   

def archivo_editar(request, id_archivo, goal_id):
    goal = get_object_or_404(AbstractGoal, pk=goal_id)
    archivo = models.Archivo.objects.get(id = id_archivo)
    if request.method == 'GET':
        form = forms.ArchivoForm(instance = archivo)
    else:
        form = forms.ArchivoForm(request.POST, instance = archivo)
        if form.is_valid():
            form.save()
            return redirect_goal(goal_id)

    return render(request, 'upload/index.html', {'form':form, "action":""})

def archivo_eliminar(request, id_archivo, goal_id):
    goal = get_object_or_404(AbstractGoal, pk=goal_id)
    archivo = models.Archivo.objects.get(id = id_archivo)
    form = forms.ArchivoForm(instance = archivo)
    if request.method == 'POST':
        file_to_delete = join(MEDIA_ROOT, archivo.upload.name)
        if isfile(file_to_delete):
            os.remove(file_to_delete)
        archivo.delete()

        return redirect_goal(goal_id)
    return render(request, 'upload/archivo_delete.html', {'goal':goal })  

