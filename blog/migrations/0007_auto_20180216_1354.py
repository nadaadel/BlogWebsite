# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20180215_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userlike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like', models.IntegerField()),
                ('dislike', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='usersub',
            name='categoryid',
        ),
        migrations.RemoveField(
            model_name='usersub',
            name='userid',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 16, 13, 54, 2, 987385)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 16, 13, 54, 2, 986684)),
        ),
        migrations.AlterField(
            model_name='replay',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 16, 13, 54, 2, 987992)),
        ),
        migrations.DeleteModel(
            name='usersub',
        ),
        migrations.AddField(
            model_name='userlike',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
        migrations.AddField(
            model_name='userlike',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
