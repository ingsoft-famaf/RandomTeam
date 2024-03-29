from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

TipePriority = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
)

TipeState = (
    ('PROGRESS', 'In Progress'),
    ('PROPOS', 'Proposed'),
    ('FINISH', 'Finished'),
)


@python_2_unicode_compatible
class AbstractGoal(models.Model):
    goal_text = models.CharField(max_length=200)
    finish_date = models.DateTimeField('finish date')
    create_date = models.DateTimeField('date published')
    priority = models.CharField(max_length=1, choices=TipePriority)
    state = models.CharField(max_length=1, choices=TipeState)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.goal_text

    def is_active(self):
        return (self.state != "FINISH")
    
    def time_until_deadline(self):
        return (self.finish_date - timezone.now())
    
    def near_deadline(self):       
        near_deadline_days = 7
        days = self.time_until_deadline().days
        return (days < near_deadline_days)


@python_2_unicode_compatible
class Goal(AbstractGoal):
    categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.categoria


@python_2_unicode_compatible
class SubGoal(AbstractGoal):
    sub_goal_text = models.CharField(max_length=200)
    goal_father = models.ForeignKey(Goal, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.sub_goal_text
