# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 17:16
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbbs',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='\u5185\u5bb9'),
        ),
    ]
