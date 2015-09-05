# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0005_auto_20150903_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stackskills',
            name='skill',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
