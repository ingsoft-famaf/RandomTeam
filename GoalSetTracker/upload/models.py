from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from goal.models import AbstractGoal
from django.core.validators import URLValidator


def content_file_name(instance, filename):
    return '/'.join(['Archivo', str(instance.goal.id), filename])+'/'


class Archivo(models.Model):
    goal = models.ForeignKey(AbstractGoal, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    upload = models.FileField(upload_to=content_file_name, blank=True,
                              null=True)
    url = models.TextField(validators=[URLValidator()],  blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
