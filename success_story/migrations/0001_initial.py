# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spec_title', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ('spec_title',),
            },
        ),
        migrations.CreateModel(
            name='StackSkills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('skill',),
            },
        ),
        migrations.CreateModel(
            name='SuccessStory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('img_avatar', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('img_background', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rate', models.DecimalField(default=0, max_digits=3, decimal_places=1)),
                ('stack_skills', models.ManyToManyField(to='success_story.StackSkills')),
            ],
        ),
        migrations.AddField(
            model_name='advice',
            name='success_story',
            field=models.ForeignKey(to='success_story.SuccessStory'),
        ),
    ]
