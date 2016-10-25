# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-24 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0005_auto_20161017_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='emr_release',
            field=models.CharField(choices=[(b'5.0.0', b'5.0.0'), (b'4.5.0', b'4.5.0')], default=b'5.0.0', help_text=b'Different EMR versions have different versions of software like Hadoop, Spark, etc', max_length=50, verbose_name=b'EMR release version'),
        ),
    ]