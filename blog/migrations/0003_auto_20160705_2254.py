# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-05 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160115_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, help_text='one word for title alias.', unique=True, verbose_name='SLUG'),
        ),
    ]
