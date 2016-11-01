# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-12 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0026_load_intial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketForSignOff',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name': 'Market - To Sign Off',
                'verbose_name_plural': 'Markets - To Sign Off',
            },
            bases=('markets.market',),
        ),
        migrations.AddField(
            model_name='market',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]