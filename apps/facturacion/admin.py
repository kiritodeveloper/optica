from django.contrib import admin
from .models import *
from apps.almacen.models import *
from decimal import Decimal
# Register your models here.

class AditivosAdmin(admin.ModelAdmin):
    model = Aditivos
    list_display =  ('componente',)

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1

class DetalleLenteInline(admin.TabularInline):
    model = DetalleLente
    extra = 1

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id','nro','dni_cliente','fecha','importe','total','cancelado','observaciones',)
    fieldsets = (
        ('Cliente', {'fields': ('dni_cliente',)}),
        ('Venta', {'fields': ('nro','importe','total','saldo','cancelado','observaciones' )}),
    )
    model = Venta
    inlines = [DetalleVentaInline,DetalleLenteInline,]
    # def save_model(self, request, obj, form, change):
    #     if change:
    #         productos = DetalleVenta.objects.filter(nro_venta=obj.nro)
    #         lentes = DetalleLente.objects.filter(nro_venta=obj.nro)
    #         print request.POST['importe']
    #         obj.save()
    #     else:
    #         obj.save()


class NotaPedidoAdmin(admin.ModelAdmin):
    model = NotaPedido
    list_display = ('id','nro','venta','fecha','importe','saldo',)
    search_fields = ('nro','venta','fecha',)
    # def save_model(self, request, obj, form, change):
    #     if change:
    #         productos = DetalleVenta.objects.filter(venta=obj.nro)
    #         print "detalles"
    #         print productos
    #         obj.save()
    #     else:
    #         obj.save()

#admin.site.register(Venta,VentaAdmin)
#admin.site.register(NotaPedido,NotaPedidoAdmin)


