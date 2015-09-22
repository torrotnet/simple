# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='successstory',
            name='used_to',
            field=models.ForeignKey(related_name='+', default=1, to='success_story.Speciality'),
            preserve_default=False,
        ),
    ]
