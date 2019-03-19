# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    productos = models.ManyToManyField("Producto")
    observaciones = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

class Producto(models.Model):
    codigo = models.CharField(max_length=10,blank=True, null=True)
    descripcion = models.CharField(max_length=30)
    marca = models.CharField(max_length=30, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    categoria = models.ForeignKey(Categoria)
    longitud = models.CharField(max_length=15, blank=True, null=True)
    precio_sugerido = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    stock_minimo = models.IntegerField(default=0)
    stock_actual = models.IntegerField(default=0)

    def __unicode__(self):
        return u'{a} ({b} {c} {d} {e})'.format(a=self.descripcion,b=self.codigo,c=self.marca,d=self.color,e=self.longitud )

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Aditivos(models.Model):
    componente = models.CharField(max_length=30)
    def __unicode__(self):
        return self.componente

    class Meta:
        verbose_name = 'Tratamiento'
        verbose_name_plural = 'Tratamientos'

class Lente(models.Model):
    tipo_lente = models.CharField(max_length=30)

    def __unicode__(self):
        return self.tipo_lente

    class Meta:
        verbose_name = 'Tipo de Lente'
        verbose_name_plural = 'Tipo de Lentes'

class IngresoProductos(models.Model):
    producto = models.ForeignKey(Producto)
    proveedor = models.ForeignKey(Proveedor,null=True,blank=True)
    fecha = models.DateField(default=timezone.now())
    cantidad = models.IntegerField()

    def __unicode__(self):
        return self.producto.descripcion

    class Meta:
        verbose_name = 'Ingreso de Producto'
        verbose_name_plural = 'Ingresos de Productos'