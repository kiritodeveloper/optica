from django.conf.urls import patterns,  url, include
from .views import *


urlpatterns = patterns('',

    url(r'^productos$', Productos.as_view(),name='producto'),
    url(r'^obtener-producto/(\d+)/$', 'apps.almacen.views.ObtenerProducto',name='ObtenerProducto'),
)

