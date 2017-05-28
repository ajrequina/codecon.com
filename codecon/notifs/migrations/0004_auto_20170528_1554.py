# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-28 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifs', '0003_auto_20170526_1510'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-create_date']},
        ),
        migrations.RemoveField(
            model_name='notification',
            name='target_pk',
        ),
        migrations.AddField(
            model_name='notification',
            name='target_link',
            field=models.CharField(default='', max_length=100),
        ),
    ]
