# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-19 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_photo',
            field=models.FileField(blank=True, upload_to='cover_photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.FileField(blank=True, upload_to='profile_photos/%Y/%m/%d/'),
        ),
    ]