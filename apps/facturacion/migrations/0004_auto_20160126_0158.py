# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0003_auto_20160126_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloquepedido',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 1, 26, 1, 58, 54, 193000)),
        ),
        migrations.AlterField(
            model_name='bloqueventa',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 1, 26, 1, 58, 54, 191000)),
        ),
        migrations.AlterField(
            model_name='notapedido',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 1, 26, 1, 58, 54, 196000)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 1, 26, 1, 58, 54, 194000)),
        ),
    ]
