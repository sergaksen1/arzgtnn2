# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zip_locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loc_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Zip_nakl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_types', models.CharField(max_length=32)),
                ('zip_locations', models.CharField(max_length=32)),
                ('zip_systems', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Zip_params',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Par_name', models.CharField(max_length=32)),
                ('Par_desc', models.CharField(max_length=32)),
                ('Par_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zip_systems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sys_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Zip_types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipType_name', models.CharField(max_length=32)),
                ('zipType_desc', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ZIP_Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Zip_user_name', models.CharField(max_length=32)),
            ],
        ),
    ]
