# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0004_auto_20150922_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='stack_skills',
            field=models.ManyToManyField(to='success_story.StackSkills', blank=True),
        ),
    ]
