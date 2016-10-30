from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User  
from goal.models import AbstractGoal


def content_file_name(instance, filename):
    return '/'.join(['Archivo', str(instance.goal.id), filename])+'/'


class Archivo(models.Model):
    goal = models.ForeignKey(AbstractGoal, on_delete = models.CASCADE)
    owner = models.ForeignKey(User , on_delete = models.CASCADE, null=True)
    titulo = models.CharField(max_length=200)
    is_public = models.BooleanField(default=True)
    descripcion = models.TextField(null=True)
    upload = models.FileField(upload_to= content_file_name , blank=True, null=True) 
    url = models.CharField(max_length=500,  blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
  
    def is_user_allowed(self, user):
    	return self.users.filter(pk=owner.pk).exists()


    @models.permalink
    def get_absolute_url(self):
    	return (content_file_name, [self.pk], {})
# Create your models here.
