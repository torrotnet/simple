# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('should_know', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='facebook',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='skype',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tel',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='twitter',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='vk',
            field=models.URLField(null=True, blank=True),
        ),
    ]
