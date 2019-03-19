# -*- encoding: utf-8 -*-
from django.db import models
from apps.cliente.models import *
from apps.almacen.models import Producto,Lente,Aditivos
from apps.receta.models import *
from django.utils import timezone
# Create your models here
class BloqueVenta(models.Model):
    fecha = models.DateField(default=timezone.now())
    current = models.BooleanField(default=True)
    def __unicode__(self):
        return str(self.id)

class BloquePedido(models.Model):
    fecha = models.DateField(default=timezone.now())
    current = models.BooleanField(default=True)
    def __unicode__(self):
        return str(self.id)

class Venta(models.Model):
    nro = models.IntegerField(blank=True,null=True)
    bloque = models.ForeignKey(BloqueVenta,blank=True,null=True)
    dni_cliente = models.ForeignKey(Cliente,blank=True, null=True)
    fecha = models.DateField(default = timezone.now())
    importe = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    saldo = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    total = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    cancelado = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "Venta nro. %s, talonario %s" %(self.nro or 'Venta Fallida',self.bloque or 'No tiene')

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

class DetalleVenta(models.Model):
    nro_venta = models.ForeignKey(Venta,blank=True)
    producto = models.ForeignKey(Producto,blank=True, null=True)
    precio = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    cantidad = models.IntegerField(default=0)
    def __unicode__(self):
        return "%s - %s" %(self.producto,self.cantidad)

class DetalleLente(models.Model):
    nro_venta = models.ForeignKey(Venta, blank=True)
    lente = models.ForeignKey(Lente)
    complementos = models.ManyToManyField(Aditivos)
    precio = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

class NotaPedido(models.Model):
    nro = models.IntegerField()
    bloque = models.ForeignKey(BloquePedido)
    venta = models.ForeignKey(Venta)
    fecha = models.DateField(default=timezone.now())
    importe = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    saldo = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

    def __unicode__(self):
        return "Nota de Pedido nro. %i" %(self.id)

    class Meta:
        verbose_name = 'Nota de Pedido'
        verbose_name_plural = 'Notas de Pedido'