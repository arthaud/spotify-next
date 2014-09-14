# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_vote_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='point',
            field=models.SmallIntegerField(default=1),
        ),
    ]
