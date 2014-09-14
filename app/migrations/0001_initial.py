# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('name', models.CharField(max_length=200, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('ip', models.GenericIPAddressField()),
                ('reverse', models.CharField(null=True, blank=True, max_length=200)),
                ('point', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
