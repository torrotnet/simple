# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0006_auto_20150903_1655'),
    ]

    operations = [
        migrations.RenameField('SuccessStory', 'story_title', 'title'),
    ]
