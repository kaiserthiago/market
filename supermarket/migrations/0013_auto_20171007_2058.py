# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 00:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0012_auto_20171007_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocao',
            name='marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supermarket.Marca'),
        ),
    ]
