from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
import models
from . import forms
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import os
from os.path import join, basename, isfile
from GoalSetTracker.settings import MEDIA_ROOT
from goal.models import Goal
from goal.views import redirect_goal
from login.views import redirect_home


@csrf_protect
def upload_img(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    if not os.path.exists(join(MEDIA_ROOT, 'Archivo/'+str(goal_id))):
        os.makedirs(join(MEDIA_ROOT, 'Archivo/'+str(goal_id)))
    error = None
    flag = True
    error2 = None
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
                #initial_path = form.cleaned_data['upload'].name
                #new_path = os.path.join(str(goal.id), initial_path)
                #os.rename(initial_path, new_path) 
                    form.save()
                    return redirect_goal(goal_id)
    else:
        form = forms.ArchivoForm(initial={'goal': goal_id})
    form.fields['goal'].widget = forms.HiddenInput()
    return render(request, "upload/index.html",{'goal': goal, "form":form, 
                                                 "mensaje_error": error,
                                                 "mensaje_error": error2})
                                                 #"action": reverse('add_file')})

def archivo_list(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    archivos = models.Archivo.objects.all().filter(goal=goal.id)

    #archivo.fields['field'].widget.attrs['readonly'] = True
    return render(request, 'upload/archivo_list.html', {'goal': goal, 'archivos': archivos.all()})

def archivo_editar(request, id_archivo, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
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
    goal = get_object_or_404(Goal, pk=goal_id)
    archivo = models.Archivo.objects.get(id = id_archivo)
    form = forms.ArchivoForm(instance = archivo)
    if request.method == 'POST':
        file_to_delete = join(MEDIA_ROOT, archivo.upload.name)
        if isfile(file_to_delete):
            os.remove(file_to_delete)
        archivo.delete()

        return redirect_goal(goal_id)
    return render(request, 'upload/archivo_delete.html', {'goal':goal })  

