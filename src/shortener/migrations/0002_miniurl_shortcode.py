# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniurl',
            name='shortcode',
            field=models.CharField(default='cfedefaultshortcode', max_length=15, unique=True),
            preserve_default=False,
        ),
    ]