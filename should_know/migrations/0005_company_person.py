# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('should_know', '0004_auto_20160109_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('logo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('link', models.URLField(null=True, blank=True)),
                ('location', models.CharField(max_length=100, null=True, blank=True)),
                ('price_min', models.IntegerField(null=True, blank=True)),
                ('price_max', models.IntegerField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product_direction', models.ManyToManyField(to='should_know.ProductDirection')),
                ('stack_technology', models.ManyToManyField(to='should_know.StackTechnology')),
            ],
            options={
                'ordering': ('updated',),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('skype', models.CharField(max_length=100, null=True, blank=True)),
                ('twitter', models.URLField(null=True, blank=True)),
                ('facebook', models.URLField(null=True, blank=True)),
                ('vk', models.URLField(null=True, blank=True)),
                ('tel', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('updated',),
            },
        ),
    ]
