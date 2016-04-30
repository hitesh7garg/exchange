# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(null=True, blank=True, max_length=200)),
                ('stars', models.IntegerField()),
            ],
        ),
    ]
