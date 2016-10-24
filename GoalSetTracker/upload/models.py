from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

#fs = FileSystemStorage(location='/home/upload')

class Archivo(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    upload = models.FileField(upload_to='archivos/', blank=True, null=True) # Despues guardar con el nombre de la meta
    url = models.CharField(max_length=500,  blank=True, null=True)

# Create your models here.
