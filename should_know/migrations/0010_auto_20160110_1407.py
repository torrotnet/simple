# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('should_know', '0009_auto_20160110_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.CharField(max_length=140),
        ),
    ]
