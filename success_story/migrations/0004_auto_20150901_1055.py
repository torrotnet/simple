# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0003_auto_20150831_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='story_rate',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=1),
        ),
    ]
