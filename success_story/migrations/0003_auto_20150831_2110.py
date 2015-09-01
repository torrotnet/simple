# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0002_auto_20150831_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='story_img_avatar',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='story_img_background',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='story_rate',
            field=models.DecimalField(max_digits=3, decimal_places=1, blank=True),
        ),
    ]
