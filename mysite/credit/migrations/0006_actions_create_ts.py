# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-21 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0005_lotterylog_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='actions',
            name='create_ts',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4'),
            preserve_default=False,
        ),
    ]