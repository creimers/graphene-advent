# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar', '0002_auto_20161114_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.IntegerField(choices=[(1, '_1_'), (2, '_2_'), (3, '_3_'), (4, '_4_'), (5, '_5_'), (6, '_6_'), (7, '_7_'), (8, '_8_'), (9, '_9_'), (10, '_10_'), (11, '_11_'), (12, '_12_'), (13, '_13_'), (14, '_14_'), (15, '_15_'), (16, '_16_'), (17, '_17_'), (18, '_18_'), (19, '_19_'), (20, '_20_'), (21, '_21_'), (22, '_22_'), (23, '_23_'), (24, '_24_')]),
        ),
    ]