# Generated by Django 2.1.1 on 2018-09-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_pagecontent_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='desc',
            field=models.CharField(default='Hey there!', max_length=400),
            preserve_default=False,
        ),
    ]
