# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20150907_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='stars',
            field=models.IntegerField(null=True),
        ),
    ]
