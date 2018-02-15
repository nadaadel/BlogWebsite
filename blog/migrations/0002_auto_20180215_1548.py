# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ForeignKey(default=1, to='blog.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 15, 15, 48, 21, 441843)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 15, 15, 48, 21, 441120)),
        ),
        migrations.AlterField(
            model_name='replay',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 15, 15, 48, 21, 442467)),
        ),
    ]
