# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0008_auto_20150905_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='successstory',
            old_name='story_title',
            new_name='title',
        ),
    ]
