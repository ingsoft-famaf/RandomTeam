from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User  
from goal.models import Goal

@python_2_unicode_compatible
class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    goal = models.ForeignKey(Goal, on_delete = models.CASCADE)
    comment_text = models.CharField(max_length=400)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
