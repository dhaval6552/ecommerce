# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20170622_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-title']},
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(max_digits=20, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=products.models.image_upload_to),
        ),
        migrations.AlterField(
            model_name='variation',
            name='inventory',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='price',
            field=models.DecimalField(max_digits=20, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='variation',
            name='sale_price',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
