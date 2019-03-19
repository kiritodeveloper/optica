from django.conf.urls import patterns,  url, include
from .views import *

urlpatterns = patterns('',

    url(r'^$', IndexView.as_view(),name='index'),
    url(r'^reporte/(\d+)/$','apps.facturacion.views.reporte',name='reporte'),
    url(r'^historial/$',HistorialView.as_view(),name="historial"),
    url(r'^notas/$',NotaPedidoView.as_view(),name="nota"),
    url(r'^nota_pedido/(\d+)/$',NotaPedidoPayment.as_view(),name='cancelar_nota_pedido'),
    url(r'^get_nota_pedido$','apps.facturacion.views.get_nota_pedido',name='get_nota_pedido'),
    url(r'^get_venta','apps.facturacion.views.get_venta',name='get_venta'),
    url(r'^change_BloqueVenta','apps.facturacion.views.change_BloqueVenta',name='change_BloqueVenta'),
    url(r'^new_BloqueVenta','apps.facturacion.views.new_BloqueVenta',name='new_BloqueVenta'),
    url(r'^change_BloquePedido','apps.facturacion.views.change_BloquePedido',name='change_BloquePedido'),
    url(r'^new_BloquePedido','apps.facturacion.views.new_BloquePedido',name='new_BloquePedido'),
)
