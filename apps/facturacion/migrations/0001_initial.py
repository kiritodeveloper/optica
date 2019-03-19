# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '__first__'),
        ('almacen', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloquePedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime(2016, 1, 26, 0, 37, 35, 535000))),
                ('current', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BloqueVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime(2016, 1, 26, 0, 37, 35, 535000))),
                ('current', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleLente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('complementos', models.ManyToManyField(to='almacen.Aditivos')),
                ('lente', models.ForeignKey(to='almacen.Lente')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('cantidad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='NotaPedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro', models.IntegerField()),
                ('fecha', models.DateField(default=datetime.datetime(2016, 1, 26, 0, 37, 35, 551000))),
                ('importe', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('saldo', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('bloque', models.ForeignKey(to='facturacion.BloquePedido')),
            ],
            options={
                'verbose_name': 'Nota de Pedido',
                'verbose_name_plural': 'Notas de Pedido',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro', models.IntegerField(null=True, blank=True)),
                ('fecha', models.DateField(default=datetime.datetime(2016, 1, 26, 0, 37, 35, 535000))),
                ('importe', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('saldo', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('total', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('cancelado', models.BooleanField(default=True)),
                ('observaciones', models.TextField(null=True, blank=True)),
                ('bloque', models.ForeignKey(blank=True, to='facturacion.BloqueVenta', null=True)),
                ('dni_cliente', models.ForeignKey(blank=True, to='cliente.Cliente', null=True)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.AddField(
            model_name='notapedido',
            name='venta',
            field=models.ForeignKey(to='facturacion.Venta'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='nro_venta',
            field=models.ForeignKey(to='facturacion.Venta', blank=True),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(blank=True, to='almacen.Producto', null=True),
        ),
        migrations.AddField(
            model_name='detallelente',
            name='nro_venta',
            field=models.ForeignKey(to='facturacion.Venta', blank=True),
        ),
    ]
