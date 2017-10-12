# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0010_produto_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocao',
            name='data_fim',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='promocao',
            name='data_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='promocao',
            name='valor',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
