# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('should_know', '0008_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
