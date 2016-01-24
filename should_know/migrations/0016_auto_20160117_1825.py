# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('should_know', '0015_auto_20160117_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='company_portfolio',
            field=models.ForeignKey(to='should_know.Company', blank=True),
        ),
    ]
