# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0005_auto_20151213_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='became',
            field=models.ForeignKey(related_name='succ_became', blank=True, to='success_story.Speciality'),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='used_to',
            field=models.ForeignKey(related_name='succ_used_to', blank=True, to='success_story.Speciality'),
        ),
    ]
