# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-30 11:24
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20161127_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbbs',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u5185\u5bb9'),
        ),
    ]