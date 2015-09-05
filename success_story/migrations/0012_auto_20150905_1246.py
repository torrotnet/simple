# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0011_speciality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='title',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='became',
            field=models.CharField(max_length=100, choices=[(2, 'Senior'), (1, 'Trainee')]),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='used_to',
            field=models.CharField(max_length=100, choices=[(2, 'Senior'), (1, 'Trainee')]),
        ),
    ]
