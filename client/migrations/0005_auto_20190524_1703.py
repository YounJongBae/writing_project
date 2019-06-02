# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-05-24 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20190524_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleHasHashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='hashtag',
            field=models.ManyToManyField(to='client.Hashtag'),
        ),
        migrations.AddField(
            model_name='articlehashashtag',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Article'),
        ),
        migrations.AddField(
            model_name='articlehashashtag',
            name='hashtag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Hashtag'),
        ),
    ]
