# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20151027_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='about',
            field=models.TextField(max_length=10000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.IntegerField(max_length=100000000000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='sex',
            field=models.CharField(max_length=10, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='stars',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
