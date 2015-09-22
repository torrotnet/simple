# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0003_auto_20150922_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='successstory',
            name='became',
            field=models.ForeignKey(related_name='succ_became', default=1, to='success_story.Speciality'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='successstory',
            name='used_to',
            field=models.ForeignKey(related_name='succ_used_to', to='success_story.Speciality'),
        ),
    ]
