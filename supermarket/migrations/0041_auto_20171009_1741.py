# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0040_auto_20171009_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
