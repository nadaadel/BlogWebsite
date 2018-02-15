# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180215_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 15, 15, 50, 15, 99599)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 15, 15, 50, 15, 98855)),
        ),
        migrations.AlterField(
            model_name='replay',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 15, 15, 50, 15, 100304)),
        ),
    ]
