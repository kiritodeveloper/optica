from django import forms
from django.forms.formsets import formset_factory
from apps.almacen.models import Categoria
from .models import Venta,DetalleVenta,DetalleLente,Aditivos,Lente,NotaPedido,BloquePedido,BloqueVenta



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
# def get_nota_pedido():
#     bloque = BloquePedido_last_id()
#     print bloque.current
#     try:
#         ultima_venta = NotaPedido.objects.filter(bloque=bloque.id).order_by('-nro')[0]
#         nro = ultima_venta.nro + 1
#         return nro
#         #return HttpResponse(json.dumps({"nro":nro}),content_type='application/json')
#     #except NotaPedido.DoesNotExist:
#     except IndexError:
#         return 1
# def get_venta():
#     bloque = BloqueVenta_last_id()
#     print bloque.current
#     try:
#         ultima_venta = Venta.objects.filter(bloque=bloque.id).order_by('-nro')[0]
#         nro = ultima_venta.nro + 1
#         return nro
#         #return HttpResponse(json.dumps({"nro":nro}),content_type='application/json')
#     except IndexError:
#         return 1
class VentaForm(forms.ModelForm):
    tipo_pagos = (
        ('True','Boleta de Venta'),
        ('False','Nota de Pedido'),
    )
    importe = forms.DecimalField(label="Importe del Cliente",widget=forms.NumberInput(attrs={'class':'form-control','min':'0.1','required':'true','step': '0.1'}),)
    observaciones = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control','rows':'2'}),required=False,)
    tipo_recibo = forms.ChoiceField(label="Tipo de Pago",widget=forms.Select(attrs={'class':'form-control','required':'true',}),choices=tipo_pagos)
    class Meta:
        model = Venta
        fields = ('observaciones',)



def producto_as_choices():
    categories = []
    for category in Categoria.objects.all():
        new_category = []
        sub_categories = []
        for sub_category in category.producto_set.all():
            # _body = unicode(sub_category.descripcion)
            # _body += u" ( "
            # if(sub_category.codigo <> unicode("") ):
            #     _body +=  unicode(sub_category.codigo)
            # if(sub_category.marca):
            #     _body += u" Marca: " + unicode(sub_category.marca)
            # if(sub_category.color):
            #     _body += u" Color: " + unicode(sub_category.color)
            # if(sub_category.longitud):
            #     _body += u" Longitud:" + unicode(sub_category.longitud)
            # _body += u" )"
            _body = unicode(sub_category.descripcion) + " ( " +  unicode(sub_category.codigo) + " Marca: " + unicode(sub_category.marca) + " Color: " + unicode(sub_category.color) + " Longitud:" + unicode(sub_category.longitud) + u" )";
            sub_categories.append(
                    [sub_category.id, _body ])

        new_category = [category.nombre, sub_categories]
        categories.append(new_category)
    return categories


producto_widget = forms.Select(attrs={'class': 'prueba form-control chosen-select c-producto ', 'required': 'true',})

class DetalleVentaForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(DetalleVentaForm, self).__init__(*args,**kwargs)
        self.fields['producto'].choices = producto_as_choices
        self.fields['producto'].widget.attrs['class'] = 'form-control c-producto chosen-select'
        self.fields['producto'].empty_label = "Seleccione el tipo de Lente"

    #producto = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'prueba form-control chosen-select c-producto ','required':'true',}), label="Producto",empty_label="Seleccione un Producto",queryset=Producto.objects.all())
    precio = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control ','required':'true', 'placeholder':'Precio','min':'0','step': '0.1'}),label="Precio")
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','required':'true','placeholder':'Unidades','min':'0'}),label="Cantidad")
    class Meta:
        model = DetalleVenta
        fields = ('producto','precio','cantidad',)


#DetalleVentaFormSet =formset_factory(DetalleVentaForm, extra=2,can_delete=True)


class DetalleLenteForm(forms.ModelForm):
    lente = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control chosen-select','required':'true',}),
                                        label="Tipo de Lente",queryset=Lente.objects.all(),empty_label="Seleccione el tipo de Lente",)
    complementos = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'chosen-select chosen-container-multi','required':'true'}),queryset=Aditivos.objects.all(),)
    precio = forms.DecimalField(initial=0,widget=forms.NumberInput(attrs={'class':'form-control','required':'true', 'placeholder':'Precio','min':'0','step': '0.1'}),label="Precio",)
    class Meta:
        model = DetalleLente
        fields = ('lente','complementos','precio',)

#DetalleLenteFormSet =formset_factory(DetalleLenteForm, extra=1,can_delete=True)

class PagarNota(forms.Form):
    pago = forms.BooleanField(initial=False,widget=forms.CheckboxInput(attrs={'class':'form-control','required':'true',}),label="El cliente ha cancelado su deuda pendiente...")

class BloqueVentaForm(forms.Form):
    bloque = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control ','required':'true',}),
                                        label="Bloque",queryset=BloqueVenta.objects.all(),empty_label="Seleccione el Bloque",)

class BloquePedidoForm(forms.Form):
    bloque = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control chosen-select','required':'true',}),
                                        label="Bloque",queryset=BloquePedido.objects.all(),empty_label="Seleccione el Bloque",)