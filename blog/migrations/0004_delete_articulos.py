# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 19:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_articulos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Articulos',
        ),
    ]
