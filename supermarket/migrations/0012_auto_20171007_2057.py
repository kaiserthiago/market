# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 00:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0011_auto_20171007_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='marca',
        ),
        migrations.AddField(
            model_name='promocao',
            name='marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supermarket.Marca'),
        ),
    ]
