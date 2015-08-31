# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import success_story.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuccessStory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('story_title', models.CharField(max_length=100)),
                ('story_text', models.TextField()),
                ('story_author', models.CharField(max_length=100)),
                ('story_img_avatar', models.ImageField(upload_to=b'')),
                ('story_img_background', models.ImageField(upload_to=b'')),
                ('story_advice', models.CharField(max_length=120)),
                ('story_stack', success_story.models.ListField()),
                ('story_used_to', models.CharField(max_length=100)),
                ('story_became', models.CharField(max_length=100)),
                ('story_timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('story_timestamp_updated', models.DateTimeField(auto_now=True)),
                ('story_rate', models.DecimalField(max_digits=3, decimal_places=1)),
            ],
        ),
    ]
