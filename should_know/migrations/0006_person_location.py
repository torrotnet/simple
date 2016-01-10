# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('should_know', '0005_company_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='location',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
