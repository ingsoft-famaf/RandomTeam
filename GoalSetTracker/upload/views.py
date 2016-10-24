from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
import models
from . import forms
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def index(request):
    form = forms.ArchivoForm()
    return render(request, "upload/index.html",{"form":form, "action": reverse("upload_img")})

@csrf_protect
def upload_img(request):
    if request.method == 'POST':
        form = forms.ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("listar"))
    else:
        form = forms.ArchivoForm()
    return render(request, "upload/index.html",{"form":form, "action": reverse("upload_img")})

def archivo_list(request):
    archivo = models.Archivo.objects.all().order_by('id')
    contexto = {'archivos':archivo}
    return render(request, 'upload/archivo_list.html', contexto)

def archivo_editar(request, id_archivo):
    archivo = models.Archivo.objects.get(id = id_archivo)
    if request.method == 'GET':
        form = forms.ArchivoForm(instance = archivo)
    else:
        form = forms.ArchivoForm(request.POST, instance = archivo)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('listar'))

    return render(request, 'upload/index.html', {'form':form, "action":""})

def archivo_eliminar(request, id_archivo):
    archivo = models.Archivo.objects.get(id = id_archivo)
    if request.method == 'POST':
        archivo.delete()
        return HttpResponseRedirect(reverse('listar'))
    return render(request, 'upload/archivo_delete.html', {'archivo':archivo }) 

