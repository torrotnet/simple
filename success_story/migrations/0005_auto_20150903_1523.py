# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0004_auto_20150901_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='StackSkills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('skill',),
            },
        ),
        migrations.RemoveField(
            model_name='successstory',
            name='story_stack',
        ),
        migrations.AddField(
            model_name='successstory',
            name='story_stack',
            field=models.ManyToManyField(to='success_story.StackSkills'),
        ),
    ]
