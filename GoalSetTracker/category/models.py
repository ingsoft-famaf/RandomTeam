# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from goal.models import Goal

# Create your models here.

class Category(models.Model):
    categoria_tipo = models.CharField(max_length=200)
    categoria_relacion = models.ManyToManyField(Goal)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.categoria_tipo
