# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0012_auto_20150905_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='became',
            field=models.CharField(max_length=100, choices=[('Senior', 'Senior'), ('Trainee', 'Trainee')]),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='used_to',
            field=models.CharField(max_length=100, choices=[('Senior', 'Senior'), ('Trainee', 'Trainee')]),
        ),
    ]
