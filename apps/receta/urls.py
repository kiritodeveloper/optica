from django.conf.urls import patterns,  url, include
from .views import Index,EditarView,HistorialView,NuevoExamenView

urlpatterns = patterns('',
   url(r'^$',Index.as_view(),name="index"),
   url(r'^historialcliente$',HistorialView.as_view(),name="historial"),
   url(r'^nuevoexamen$',NuevoExamenView.as_view(),name="nuevoexamen"),
   url(r'^editar/(\d+)/$',EditarView.as_view(),name="editar"),
)