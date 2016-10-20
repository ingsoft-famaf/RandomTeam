from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

#fs = FileSystemStorage(location='/home/upload')

class Archivo(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    upload = models.FileField(upload_to='static/files', blank=True, null=True)
    url = models.CharField(max_length=200,  blank=True, null=True)

# Create your models here.
