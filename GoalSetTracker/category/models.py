# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from goal.models import Goal

# Create your models here.

class Category(models.Model):
    categoria_tipo = models.CharField(max_length=200)
    categoria_relacion = models.ManyToManyField(Goal)
