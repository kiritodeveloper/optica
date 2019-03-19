# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime
# Create your models here.
class Cliente(models.Model):
    dni = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    direccion = models.TextField(blank=True,null=True)
    telefono = models.CharField(max_length=15, blank=True,null=True )
    email = models.CharField(max_length=30, blank=True,null=True )
    fecha_nacimiento = models.DateField(null=True, blank=True)
    ocupacion = models.CharField(max_length=50, blank=True,null=True )
    foto = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/default_user.png',blank=True,null=True)

    def fotografia(self):
        if self.foto:
            return "<a href='%s' target='_blank'><img src='%s' width='100'></a>" %(self.foto.url,self.foto.url)
        else:
            return "<strong>No tiene foto</strong>"

    fotografia.allow_tags = True

    def nombre_completo(self):
        return "%s %s"  %(self.nombre,self.apellido)

    def edad(self):
        import datetime
        if(self.fecha_nacimiento):
           diff = (datetime.date.today() - self.fecha_nacimiento).days
           years = str(int(diff/365))
           return unicode(years)
        else:
            return "No especificado"

    def __unicode__(self):
        return "%s, %s" %(self.nombre,self.apellido)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'