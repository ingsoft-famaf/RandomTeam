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
            return HttpResponseRedirect(reverse("success_upload"))
    else:
        form = UploadFileForm()
    return render(request, "upload/index.html",{"form":form, "action": reverse("upload_img")})

def seccess_upload(request):
    return HttpResponse("funciono")