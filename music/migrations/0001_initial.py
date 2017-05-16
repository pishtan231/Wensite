# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('artist', models.CharField(max_length=250)),
                ('album_title', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=100)),
                ('album_logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('file_type', models.CharField(max_length=10)),
                ('song_title', models.CharField(max_length=250)),
                ('album', models.ForeignKey(to='music.Album')),
            ],
        ),
    ]
