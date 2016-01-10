# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('should_know', '0011_person_linked_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='twitter',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
