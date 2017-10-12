# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 01:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0021_promocao_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supermarket.Marca'),
        ),
        migrations.AlterField(
            model_name='promocao',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supermarket.Marca'),
        ),
    ]
