# -*- encoding: utf-8 -*-
"""optica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from apps.usuarios.views import Login, Logout
from apps.almacen.views import Index
from optica import settings

admin.site.site_header = "Sistema de Información para Ópticas"
admin.site.site_title = "Panel de Administración"

urlpatterns = [
    url(r'^$',Index.as_view(),name='index'),
    url(r'^login/$',Login.as_view(),name="login"),
    url(r'^logout/$',Logout.as_view(),name="logout"),
    url(r'^almacen/',include('apps.almacen.urls',namespace='almacen')),
    url(r'^admin/', include(admin.site.urls),name="admin"),
    url(r'^cliente/',include('apps.cliente.urls',namespace='cliente')),
    url(r'^facturacion/',include('apps.facturacion.urls',namespace='facturacion')),
    url(r'^receta/',include('apps.receta.urls',namespace='receta')),
]

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )