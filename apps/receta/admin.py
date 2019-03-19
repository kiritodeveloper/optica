from django.contrib import admin
from .models import Receta
# Register your models here.
class RecetaAdmin(admin.ModelAdmin):
    model = Receta
    list_display = ('id','cliente','fecha')
    search_fields = ('cliente__nombre','cliente__apellido')

admin.site.register(Receta,RecetaAdmin)