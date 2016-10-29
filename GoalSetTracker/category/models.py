# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from goal.models import AbstractGoal

# Create your models here.

class Category(models.Model):
    category_tipo = models.CharField(max_length=200)
    goal = models.ManyToManyField(AbstractGoal)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.category_tipo
