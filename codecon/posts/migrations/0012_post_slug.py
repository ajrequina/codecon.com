# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(),
            preserve_default=False,
        ),
    ]
