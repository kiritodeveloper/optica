from django.contrib import admin
from .forms import *
# Register your models here.

#@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
    list_display = ('nombre','descripcion',)
    search_fields = ('nombre',)
#@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    model = Proveedor
    list_display = ('nombre','telefono','observaciones')

#@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ('codigo','descripcion','marca','color','categoria','longitud','stock_actual')
    list_filter = ('categoria','marca','color',)
    search_fields = ('descripcion',)
    #exclude = ('stock_actual',)

@admin.register(Lente)
class LenteAdmin(admin.ModelAdmin):
    model=Lente
    list_display = ('id','tipo_lente',)

@admin.register(Aditivos)
class AditivoAdmin(admin.ModelAdmin):
    model=Aditivos
    list_display = ('componente',)
#@admin.register(IngresoProductos)
class IngresoProductosAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:
            print "editar"
            g = IngresoProductos.objects.get(pk=obj.id)
            dif =  obj.cantidad - g.cantidad
            product = Producto.objects.get(pk=obj.producto.id)
            product.stock_actual += dif
            product.save()
            obj.save()
        else:
            obj.save()
            product = Producto.objects.get(pk=obj.producto.id)
            product.stock_actual += obj.cantidad
            product.save()

    model = IngresoProductos
    list_display = ('fecha','producto','proveedor','cantidad')

