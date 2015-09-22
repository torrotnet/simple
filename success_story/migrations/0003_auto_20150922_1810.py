# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0002_successstory_used_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='used_to',
            field=models.ForeignKey(related_name='spec_used_to', to='success_story.Speciality'),
        ),
    ]
