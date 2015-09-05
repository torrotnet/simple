# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0007_auto_20150905_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='successstory',
            old_name='title',
            new_name='story_title',
        ),
        migrations.AlterField(
            model_name='stackskills',
            name='skill',
            field=models.CharField(max_length=100),
        ),
    ]
