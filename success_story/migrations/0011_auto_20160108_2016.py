# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0010_auto_20160108_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='became',
            field=models.ForeignKey(related_name='succ_became', to='success_story.Speciality'),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='stack_skills',
            field=models.ManyToManyField(to='success_story.StackSkills'),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='used_to',
            field=models.ForeignKey(related_name='succ_used_to', to='success_story.Speciality'),
        ),
    ]
