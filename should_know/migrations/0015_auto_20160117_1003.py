# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('should_know', '0014_auto_20160117_0937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ('name_portfolio',)},
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='company',
            new_name='company_portfolio',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='description',
            new_name='description_portfolio',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='link',
            new_name='link_portfolio',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='name',
            new_name='name_portfolio',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='product_direction',
            new_name='product_direction_portfolio',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='stack_technology',
            new_name='stack_technology_portfolio',
        ),
    ]
