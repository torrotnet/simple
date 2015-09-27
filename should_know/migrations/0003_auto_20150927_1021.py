# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('should_know', '0002_auto_20150927_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='price_max',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='price_min',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='link',
            field=models.URLField(null=True, blank=True),
        ),
    ]
