# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20151027_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='following',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
