# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-19 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('custom_key', '0004_auto_20170219_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email_send_data',
            old_name='email_connect',
            new_name='email_data',
        ),
        migrations.RemoveField(
            model_name='email_send_data',
            name='email_verify',
        ),
        migrations.AddField(
            model_name='email_send_data',
            name='key',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]
