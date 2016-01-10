# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('should_know', '0006_person_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='facebook',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='skype',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='tel',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AddField(
            model_name='company',
            name='twitter',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='vk',
            field=models.URLField(null=True, blank=True),
        ),
    ]
