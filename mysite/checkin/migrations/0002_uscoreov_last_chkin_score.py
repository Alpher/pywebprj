# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uscoreov',
            name='last_chkin_score',
            field=models.IntegerField(default=0, verbose_name='\u4e0a\u6b21\u7b7e\u5230\u79ef\u5206'),
        ),
    ]