# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180215_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='replay',
            old_name='comment_id',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='replay',
            old_name='userid',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 15, 16, 49, 13, 937877)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 15, 16, 49, 13, 937171)),
        ),
        migrations.AlterField(
            model_name='replay',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 15, 16, 49, 13, 938596)),
        ),
    ]
