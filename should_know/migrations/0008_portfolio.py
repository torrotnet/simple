# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('should_know', '0007_auto_20160110_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField(null=True, blank=True)),
                ('description', models.TextField()),
                ('company', models.ForeignKey(to='should_know.Company')),
                ('product_direction', models.ManyToManyField(to='should_know.ProductDirection')),
                ('stack_technology', models.ManyToManyField(to='should_know.StackTechnology')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
