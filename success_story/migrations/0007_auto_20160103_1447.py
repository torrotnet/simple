# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0006_auto_20160103_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='became',
            field=models.ForeignKey(related_name='succ_became', blank=True, to='success_story.Speciality', null=True),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='used_to',
            field=models.ForeignKey(related_name='succ_used_to', blank=True, to='success_story.Speciality', null=True),
        ),
    ]
