# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20151012_1022'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
