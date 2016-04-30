# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg'),
        ),
    ]
