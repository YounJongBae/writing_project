# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-05-24 08:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20190524_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlehashashtag',
            name='article',
        ),
        migrations.RemoveField(
            model_name='articlehashashtag',
            name='hashtag',
        ),
        migrations.DeleteModel(
            name='ArticleHasHashtag',
        ),
    ]
