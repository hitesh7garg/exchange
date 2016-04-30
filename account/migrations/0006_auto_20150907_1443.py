# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20150907_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='sex',
            field=models.CharField(null=True, max_length=10),
        ),
    ]
