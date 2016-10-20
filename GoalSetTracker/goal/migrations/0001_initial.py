# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 00:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_text', models.CharField(max_length=200)),
                ('finish_date', models.DateTimeField(verbose_name='date published')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_goal_text', models.CharField(max_length=200)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goal.Goal')),
            ],
        ),
    ]