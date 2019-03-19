# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloquepedido',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 1, 26, 0, 40, 57, 610000)),
        ),
        migrations.AlterField(
            model_name='bloqueventa',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 1, 26, 0, 40, 57, 609000)),
        ),
        migrations.AlterField(
            model_name='notapedido',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 1, 26, 0, 40, 57, 619000)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 1, 26, 0, 40, 57, 612000)),
        ),
    ]
