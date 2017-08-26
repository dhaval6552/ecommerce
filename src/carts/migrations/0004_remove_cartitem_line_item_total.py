# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cartitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='line_item_total',
        ),
    ]
