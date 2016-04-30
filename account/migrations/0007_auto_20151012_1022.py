# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20150907_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='following',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='followers'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pics/', blank=True),
        ),
    ]
