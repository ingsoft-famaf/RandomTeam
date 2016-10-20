from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Goal(models.Model):
    goal_text = models.CharField(max_length=200)
    finish_date = models.DateTimeField('date published')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @property
    def goals(self):
        return self.point_set.count()

    def __str__(self):
        return self.goal_text

    def is_active(self):
        return self.finish >= timezone.now()

@python_2_unicode_compatible
class SubGoal(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    sub_goal_text = models.CharField(max_length=200)

    def __str__(self):
        return self.sub_goal_text
