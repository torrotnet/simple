# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('should_know', '0012_auto_20160110_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='linked_in',
            field=models.URLField(null=True, blank=True),
        ),
    ]
