# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20140914_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2014, 9, 14)),
            preserve_default=False,
        ),
    ]
