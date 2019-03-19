# -*- encoding: utf-8 -*-
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View, ListView, DeleteView
from apps.cliente.forms import ClienteForm
from .forms import VentaForm,DetalleVentaForm,DetalleLenteForm,PagarNota,BloqueVentaForm,BloquePedidoForm

from .models import *
from django.contrib import messages
from apps.usuarios.views import LoginRequiredMixin
from decimal import Decimal
# Create your views here.

def BloqueVenta_last_id():
    try:
        nro = BloqueVenta.objects.get(current=True)
        return nro
    except BloqueVenta.DoesNotExist:
        nro = BloqueVenta.objects.create()
        nro.save()
        return nro

def BloquePedido_last_id():
    try:
        nro = BloquePedido.objects.get(current=True)
        return nro
    except BloquePedido.DoesNotExist:
        nro = BloquePedido.objects.create()
        nro.save()
        return nro

#Obtiene el ultimo numero de pedido
def get_nota_pedido():
    bloque = BloquePedido_last_id()

    try:
        ultima_venta = NotaPedido.objects.filter(bloque=bloque.id).order_by('-nro')[0]
        nro = ultima_venta.nro + 1
        return nro
        #return HttpResponse(json.dumps({"nro":nro}),content_type='application/json')
    #except NotaPedido.DoesNotExist:
    except IndexError:
        return 1
        #return HttpResponse(json.dumps({"nro":1}),content_type='application/json')

#Obtiene el ultimo numero de venta
def get_venta():
    bloque = BloqueVenta_last_id()

    try:
        ultima_venta = Venta.objects.filter(bloque=bloque.id).order_by('-nro')[0]
        nro = ultima_venta.nro + 1
        return nro
        #return HttpResponse(json.dumps({"nro":nro}),content_type='application/json')
    except IndexError:
        return 1
        #return HttpResponse(json.dumps({"nro":1}),content_type='application/json')

class IndexView(LoginRequiredMixin, View):
    template_name= "facturacion/index.html"
    def get(self,request):
        cliente_form = ClienteForm()
        venta_form = VentaForm()
        ProductoForm = DetalleVentaForm()
        LenteForm = DetalleLenteForm()
        nro_venta = get_venta()
        nro_pedido = get_nota_pedido()
        nro_bloque_venta  = BloqueVenta_last_id()
        nro_bloque_pedido = BloquePedido_last_id()
        return render(request,self.template_name,locals())

    def post(self,request):
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():
            venta = venta_form.save(commit=False)
            if request.POST['Cliente']: #El if verifica si existe un cliente
                cliente = Cliente.objects.get(pk=request.POST['Cliente'])
                if cliente:
                    venta.dni_cliente = cliente
            venta.save()
            total = Decimal(0) #variable para calcular el total

            nro_productos = int(request.POST['NumeroProductos']) + 1
            for i in range(1,nro_productos):
                producto_codigo = "producto-codigo-" + str(i)
                producto_precio = "producto-precio-" + str(i)
                producto_cantidad = "producto-cantidad-" + str(i)
                detalle = DetalleVenta()
                producto = Producto.objects.get(pk=request.POST[producto_codigo])
                producto.stock_actual = producto.stock_actual - int(request.POST[producto_cantidad])
                producto.save()
                detalle.producto = producto
                detalle.nro_venta = venta
                detalle.cantidad = int(request.POST[producto_cantidad])
                detalle.precio = Decimal(request.POST[producto_precio])
                detalle.save()
                total = total + Decimal(detalle.precio)*Decimal(detalle.cantidad)

            nro_lentes = int(request.POST['NumeroLentes']) + 1
            for i in range(1,nro_lentes): #Guardar Detalles Lentes
                lente_codigo = "lente-codigo-" + str(i)
                lente_complementos = "lente-complementos-" + str(i)
                lente_precio = "lente-precio-" + str(i)
                item = DetalleLente()
                item.nro_venta = venta
                item.lente = Lente.objects.get( pk=str(request.POST[lente_codigo]) )
                item.precio = Decimal(request.POST[lente_precio])
                item.save()
                id_detalle = item.id
                longitud = len(request.POST.getlist(lente_complementos))
                lista = request.POST.getlist(lente_complementos)
                item = DetalleLente.objects.get(pk=id_detalle)
                for i in range(0,longitud):
                    item.complementos.add(Aditivos.objects.get( pk = lista[i]))
                item.save()
                total = total + Decimal(item.precio)

            venta = Venta.objects.get(pk=venta.id) #Actualizar venta
            venta.nro = get_venta()
            venta.bloque = BloqueVenta_last_id()
            flag = str(request.POST['tipo_recibo'])
            if flag == "True": #Boleta de Venta
                venta.cancelado = True
                venta.importe = Decimal(request.POST['importe'])
                venta.total = Decimal(total)
                venta.saldo = total-venta.importe
                venta.save()
            else:   #Nota de Pedido
                nota = NotaPedido()
                nota.nro = get_nota_pedido()
                nota.bloque = BloquePedido_last_id()
                nota.venta = venta
                nota.importe = Decimal(request.POST['importe'])
                nota.saldo = total - Decimal(request.POST['importe'])
                nota.save()
                venta.cancelado = False
                venta.importe = Decimal(request.POST['importe'])
                venta.total = total
                venta.saldo = total - venta.importe
                venta.save()
            messages.success(request, 'La venta número '+ str(venta.nro) +' se registro con éxito')
            return  redirect('reporte/'+str(venta.id))
        else:
            messages.error(request, 'No se pudo registrar la venta, ocurrio un error en el formulario de venta.')
            cliente_form = ClienteForm()
            venta_form = VentaForm()
            ProductoForm = DetalleVentaForm()
            LenteForm = DetalleLenteForm()
            nro_venta = get_venta()
            nro_pedido = get_nota_pedido()
            nro_bloque_venta  = BloqueVenta_last_id()
            nro_bloque_pedido = BloquePedido_last_id()
            return render(request,self.template_name,locals())


class HistorialView(LoginRequiredMixin,View):
    template_name = 'facturacion/historial_ventas.html'
    def get(self,request):
        bloque_form = BloqueVentaForm()
        ventas = Venta.objects.all()
        bloque = BloqueVenta_last_id
        return render(request,self.template_name,locals())


class NotaPedidoView(LoginRequiredMixin,View):
    template_name = 'facturacion/historial_notas_pedido.html'
    def get(self,request):
        notas = NotaPedido.objects.all()

        bloque_form = BloquePedidoForm()
        bloque = BloquePedido_last_id()
        return render(request,self.template_name,locals())


class NotaPedidoPayment(View):
    template_name = 'facturacion/nota_pedido.html'
    def get(self,request,id):
        nota = NotaPedido.objects.get(pk=id)
        venta = Venta.objects.get(pk=nota.venta.id)
        detalles = DetalleVenta.objects.filter(nro_venta=nota.venta.id)
        lentes = DetalleLente.objects.filter(nro_venta=nota.venta.id)
        form = PagarNota()
        return render(request,self.template_name,locals())
    def post(self,request,id):
        nota = NotaPedido.objects.get(pk=id)
        nota.importe = nota.importe + nota.saldo
        nota.saldo = 0
        nota.save()
        venta = Venta.objects.get(pk=nota.venta.id)
        venta.importe = venta.total
        venta.saldo = 0
        venta.cancelado = True
        venta.save()
        return redirect('/facturacion/notas')


def reporte(request,id):
    template_name = 'facturacion/reporte.html'
    venta = Venta.objects.get(pk=id)
    detalles = DetalleVenta.objects.filter(nro_venta=id)
    lentes = DetalleLente.objects.filter(nro_venta=id)
    return render(request,template_name,locals())

def new_BloqueVenta(request):
    g = BloqueVenta.objects.get(current=True)
    g.current = False
    g.save()
    g = BloqueVenta.objects.create()
    g.save()
    return redirect('/facturacion/historial')

def change_BloqueVenta(request):
    g = BloqueVenta.objects.get(current=True)
    g.current = False
    g.save()
    g = BloqueVenta.objects.get(pk=request.POST['bloque'])
    g.current = True
    g.save()
    return redirect('/facturacion/historial')

def new_BloquePedido(request):
    bloqueActual = BloquePedido.objects.get(current=True)
    bloqueActual.current = False
    bloqueActual.save()
    nuevoBloque = BloquePedido.objects.create()
    nuevoBloque.save()
    return redirect('/facturacion/notas')

def change_BloquePedido(request):
    bloqueActual = BloquePedido.objects.get(current=True)
    bloqueActual.current = False
    bloqueActual.save()
    nuevoBloque = BloquePedido.objects.get(pk=request.POST['bloque'])
    nuevoBloque.current = True
    nuevoBloque.save()

    return redirect('/facturacion/notas')