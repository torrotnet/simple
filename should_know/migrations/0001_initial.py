# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('skype', models.CharField(max_length=100)),
                ('twitter', models.URLField()),
                ('facebook', models.URLField()),
                ('vk', models.URLField()),
                ('tel', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductDirection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direction', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('direction',),
            },
        ),
        migrations.CreateModel(
            name='StackTechnology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('technology', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('technology',),
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to=b'')),
                ('contact', models.OneToOneField(primary_key=True, serialize=False, to='should_know.Contact')),
                ('link', models.URLField()),
                ('location', models.CharField(max_length=100)),
                ('price_min', models.IntegerField()),
                ('price_max', models.IntegerField()),
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
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to=b'')),
                ('contact', models.OneToOneField(primary_key=True, serialize=False, to='should_know.Contact')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('updated',),
            },
        ),
        migrations.AddField(
            model_name='portfolio',
            name='product_direction',
            field=models.ManyToManyField(to='should_know.ProductDirection'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='stack_technology',
            field=models.ManyToManyField(to='should_know.StackTechnology'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='company',
            field=models.ForeignKey(to='should_know.Company'),
        ),
    ]
