# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0017_auto_20171007_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='marca',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='supermarket.Marca'),
        ),
        migrations.AlterField(
            model_name='promocao',
            name='marca',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='supermarket.Marca'),
        ),
    ]
