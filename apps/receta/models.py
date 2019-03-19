# -*- encoding: utf-8 -*-
from django.db import models
from apps.cliente.models import Cliente
from apps.almacen.models import Lente,Aditivos
from django.utils import timezone
import datetime
# Create your models here.

class Receta(models.Model):
    cliente = models.ForeignKey(Cliente,blank=True, null=True)
    od_esf = models.CharField(max_length=15,blank=True,null=True)
    oi_esf= models.CharField(max_length=15,blank=True,null=True)
    od_cil = models.CharField(max_length=15,blank=True,null=True)
    oi_cil = models.CharField(max_length=15,blank=True,null=True)
    od_eje = models.CharField(max_length=15,blank=True,null=True)
    oi_eje = models.CharField(max_length=15,blank=True,null=True)
    od_dip = models.CharField(max_length=15,blank=True,null=True)
    oi_dip = models.CharField(max_length=15,blank=True,null=True)
    od_avsc = models.CharField(max_length=15,blank=True,null=True)
    oi_avsc = models.CharField(max_length=15,blank=True,null=True)
    od_avcc = models.CharField(max_length=15,blank=True,null=True)
    oi_avcc = models.CharField(max_length=15,blank=True,null=True)
    add = models.CharField(max_length=15,blank=True,null=True)
    patologia = models.CharField(max_length=25,blank=True,null=True)
    lente = models.ForeignKey(Lente,blank=True,null=True)
    complementos = models.ManyToManyField(Aditivos,blank=True,null=True)
    fecha = models.DateField(default=timezone.now())
    imagen = models.ImageField(upload_to = 'recetas/',default = 'recetas/default.jpg',blank=True,null=True)

    def __unicode__(self):
        return  "%s - %s" %(self.cliente,self.fecha)

    class Meta:
        verbose_name = 'Atención Médica'
        verbose_name_plural = 'Historias Clínicas'


class RecetaMananger(models.Manager):
    def recordar(self):
        lista = []
        recetas = Receta.objects.all()
        for item in recetas:
            diff = (datetime.date.today()-item.fecha).month
            if(int(diff) >= 8):
                lista.append(item)
        return lista