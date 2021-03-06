# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_miniurl_shortcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniurl',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='miniurl',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
