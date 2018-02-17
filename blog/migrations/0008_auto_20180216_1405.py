# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180216_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlike',
            old_name='dislike',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='userlike',
            name='like',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 16, 14, 5, 22, 732557)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 16, 14, 5, 22, 731825)),
        ),
        migrations.AlterField(
            model_name='replay',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 16, 14, 5, 22, 733168)),
        ),
    ]
