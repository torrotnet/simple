# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0009_auto_20150905_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='successstory',
            old_name='story_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='successstory',
            old_name='story_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='successstory',
            old_name='story_img_avatar',
            new_name='img_avatar',
        ),
        migrations.RenameField(
            model_name='successstory',
            old_name='story_img_background',
            new_name='img_background',
        ),
        migrations.RenameField(
            model_name='successstory',
            old_name='story_advice',
            new_name='advice',
        ),
        migrations.RenameField(
            model_name='successstory',
            old_name='story_stack',
            new_name='stack_skills',
        ),
        migrations.RenameField(
            model_name='successstory',
            old_name='story_used_to',
            new_name='used_to',
        ),
        migrations.RenameField(
            model_name='successstory',
            old_name='story_became',
            new_name='became',
        ),
        migrations.RenameField(
            model_name='successstory',
            old_name='story_timestamp_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='successstory',
            old_name='story_timestamp_updated',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='successstory',
            old_name='story_rate',
            new_name='rate',
        ),
    ]
