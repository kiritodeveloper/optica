# -*- encoding: utf-8 -*-
from django.shortcuts import render,redirect, HttpResponse
from django.views.generic import View, ListView, DeleteView
from apps.cliente.models import Cliente
from apps.facturacion.models import Venta
from apps.receta.models import Receta
from .models import Producto,Proveedor
from .forms import ProductoForm,IngresoProductosForm
from django.contrib import messages
from apps.usuarios.views import LoginRequiredMixin
from decimal import Decimal
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class Index(LoginRequiredMixin,View):
    template_name = 'index.html'
    def get(self,request):
        # Calculando 6 meses anterior y sus totales
        import datetime
        # nombre_meses = { 1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Setiembre",10:"Octubre", 11:"Noviembre",12:"Diciembre" }
        # contador = [0,0,0,0,0,0]
        # totales = [Decimal(0),Decimal(0),Decimal(0),Decimal(0),Decimal(0),Decimal(0)]
        # receta = Receta.objects.all().order_by('-fecha')
        # lista = []
        # for item in receta:
        #     diff = (datetime.date.today() - item.fecha).days
        #     if(int(diff/30) >= 8):
        #         lista.append(item)
        # receta = lista
        # ventas = Venta.objects.all()
        # suma_mes = Decimal(0)
        # suma_dia = Decimal(0)
        # flag = False
        # meses = [[datetime.date.today().month,datetime.date.today().year],]
        # #Obtener los ultimos 6 meses
        # if (datetime.date.today().month - 1 >0 and flag == False):
        #     meses.append([datetime.date.today().month-1,datetime.date.today().year])
        # else:
        #     meses.append([12,datetime.date.today().year-1])
        #     flag = True
        # if (datetime.date.today().month - 2 >0  and flag == False):
        #     meses.append([datetime.date.today().month-2,datetime.date.today().year])
        # else:
        #     meses.append([11,datetime.date.today().year-1])
        #     flag = True
        # if (datetime.date.today().month - 3 >0  and flag == False):
        #     meses.append([datetime.date.today().month-3,datetime.date.today().year])
        # else:
        #     meses.append([10,datetime.date.today().year-1])
        #     flag = True
        # if (datetime.date.today().month - 4 >0  and flag == False):
        #     meses.append([datetime.date.today().month-4,datetime.date.today().year])
        # else:
        #     meses.append([9,datetime.date.today().year-1])
        #     flag = True
        # if (datetime.date.today().month - 5 >0  and flag == False):
        #     meses.append([datetime.date.today().month-5,datetime.date.today().year])
        # else:
        #     meses.append([8,datetime.date.today().year-1])
        #     flag = True
        #
        # for item in ventas:#Calcular totales del dia y del mes
        #     if item.fecha == datetime.date.today():
        #         suma_dia += Decimal(item.total or 0)
        #     if (item.fecha.month == datetime.date.today().month) and (item.fecha.year == datetime.date.today().year):
        #         suma_mes += Decimal(item.total or 0)
        #     #Cacular totales para los 6 meses
        #     if (item.fecha.month == meses[0][0]) and (item.fecha.year == meses[0][1]):
        #         totales[0] += Decimal(item.total or 0)
        #         contador[0] += 1
        #     if (item.fecha.month == meses[1][0]) and (item.fecha.year == meses[1][1]):
        #         totales[1] += Decimal(item.total or 0)
        #         contador[1] += 1
        #     if (item.fecha.month == meses[2][0]) and (item.fecha.year == meses[2][1]):
        #         totales[2] += Decimal(item.total or 0)
        #         contador[2] += 1
        #     if (item.fecha.month == meses[3][0]) and (item.fecha.year == meses[3][1]):
        #         totales[3] += Decimal(item.total or 0)
        #         contador[3] += 1
        #     if (item.fecha.month == meses[4][0]) and (item.fecha.year == meses[4][1]):
        #         totales[4] += Decimal(item.total or 0)
        #         contador[4] += 1
        #     if (item.fecha.month == meses[5][0]) and (item.fecha.year == meses[5][1]):
        #         totales[5] += Decimal(item.total or 0)
        #         contador[5] += 1
        #
        # #Renderizando datos a json
        # import json
        # index = 0
        # for item in meses:
        #     meses[index] = "%s - %s" %(str(nombre_meses[item[0]]),str(item[1]))
        #     index +=1
        # meses = json.dumps(meses)
        # contador = json.dumps(contador)
        # index = 0
        # for item in totales:
        #     totales[index] = float(totales[index])
        #     index+=1
        # totales = json.dumps(totales)
        # # Clientes de cumpleaños
        clientes = Cliente.objects.filter(fecha_nacimiento__month=datetime.date.today().month, fecha_nacimiento__day=datetime.date.today().day)
        return render(request,self.template_name,locals())

class Productos(LoginRequiredMixin,View):
    template_name = 'productos/index.html'
    def get(self,request):
        productos = Producto.objects.all()
        producto_form = ProductoForm()
        ingreso_form = IngresoProductosForm()
        return render(request,self.template_name,locals())
    def post(self,request):
        productos = Producto.objects.all()
        producto_form = ProductoForm(request.POST)
        ingreso_form = IngresoProductosForm(request.POST)
        if producto_form.is_valid():
            producto = producto_form.save()
            messages.success(request, unicode('El producto '+unicode(producto.descripcion)+' de código '+unicode(producto.codigo)+' fue registrado con exito'))
            productos = Producto.objects.all()
            producto_form = ProductoForm()
            ingreso_form = IngresoProductosForm()
            return render(request,self.template_name,locals())
        elif(ingreso_form.is_valid()):
            historial = ingreso_form.save()
            producto = Producto.objects.get(pk=historial.producto.id)
            producto.stock_actual += int(request.POST['cantidad'])
            producto.save()
            messages.success(request, 'Se ingresaron '+request.POST['cantidad']+' unidades de '+producto.descripcion)
            productos = Producto.objects.all()
            producto_form = ProductoForm()
            ingreso_form = IngresoProductosForm()
            return render(request,self.template_name,locals())
        else:
            messages.error(request, 'No se pudo registrar la operación, porfavor intente denuevo.')
            return render(request,self.template_name,locals())

import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ObtenerProducto(request,nro):
    item = Producto.objects.get(pk=nro)
    return HttpResponse(json.dumps({"precio":float(item.precio_sugerido),"max_value":item.stock_actual}),content_type='application/json')

