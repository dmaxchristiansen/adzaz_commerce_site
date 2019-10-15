# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-15 05:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poorly_coded_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='poorly_coded_store.Order'),
            preserve_default=False,
        ),
    ]