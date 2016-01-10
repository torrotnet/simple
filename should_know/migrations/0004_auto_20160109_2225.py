# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('should_know', '0003_auto_20150927_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='company',
            name='product_direction',
        ),
        migrations.RemoveField(
            model_name='company',
            name='stack_technology',
        ),
        migrations.RemoveField(
            model_name='person',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='company',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='product_direction',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='stack_technology',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]
