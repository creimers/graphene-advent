# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('uuid', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('1', '_1'), ('2', '_2'), ('3', '_3'), ('4', '_4'), ('5', '_5'), ('6', '_6'), ('7', '_7'), ('8', '_8'), ('9', '_9'), ('10', '_10'), ('11', '_11'), ('12', '_12'), ('13', '_13'), ('14', '_14'), ('15', '_15'), ('16', '_16'), ('17', '_17'), ('18', '_18'), ('19', '_19'), ('20', '_20'), ('21', '_21'), ('22', '_22'), ('23', '_23')], max_length=2)),
                ('image_source', models.URLField(blank=True)),
                ('image', models.ImageField(upload_to='')),
                ('image_small', image_cropping.fields.ImageRatioField('image', '250x250', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='image small')),
                ('image_large', image_cropping.fields.ImageRatioField('image', '250x250', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='image large')),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='calendar.Calendar')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='day',
            unique_together=set([('day', 'calendar')]),
        ),
    ]
