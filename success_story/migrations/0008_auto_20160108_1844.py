# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0007_auto_20160103_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advice',
            name='success_story',
        ),
        migrations.DeleteModel(
            name='Advice',
        ),
    ]
