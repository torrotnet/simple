# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='story_img_avatar',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='story_img_background',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
