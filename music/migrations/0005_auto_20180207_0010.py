# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-07 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_remove_album_album_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='album',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]