# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-07-08 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_models_for_mock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb4mockhttp',
            name='describe',
            field=models.TextField(db_column='describe', default='', verbose_name='详细描述'),
        ),
    ]
