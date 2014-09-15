# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20140914_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('up', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
