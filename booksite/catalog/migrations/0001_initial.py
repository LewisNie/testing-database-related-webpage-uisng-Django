# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('pub_id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('pub_name', models.CharField(unique=True, max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('title_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=20)),
                ('price', models.FloatField(null=True, blank=True)),
                ('pub_id', models.ForeignKey(to='catalog.Publisher')),
            ],
        ),
    ]
