from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User  
from goal.models import AbstractGoal

#fs = FileSystemStorage(location='/home/upload')

class Archivo(models.Model):
    goal = models.ForeignKey(AbstractGoal, on_delete = models.CASCADE)
    # owner = models.ForeignKey(User , on_delete = models.CASCADE, null=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    upload = models.FileField(upload_to='archivo/', blank=True, null=True) # Despues guardar con el nombre de la meta
    url = models.CharField(max_length=500,  blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
# Create your models here.
