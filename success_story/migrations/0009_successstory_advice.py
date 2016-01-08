# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0008_auto_20160108_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='successstory',
            name='advice',
            field=models.CharField(default=b'', max_length=140, blank=True),
        ),
    ]
