from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    model = Cliente
    list_display =  ('dni','nombre','apellido','telefono','email', 'edad','ocupacion','fotografia')
    search_fields = ('dni','nombre','apellido',)
