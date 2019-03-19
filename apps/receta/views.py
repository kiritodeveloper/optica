# -*- encoding: utf-8 -*-
from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import RecetaForm
from .models import Receta
from apps.cliente.forms import ClienteForm
from apps.cliente.models import Cliente
from django.contrib import messages
from apps.usuarios.views import LoginRequiredMixin
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# Create your views here.
class Index(LoginRequiredMixin, View):
    template_name = 'receta/index.html'
    def get(self,request):
        form = RecetaForm()
        cliente_form = ClienteForm
        return render(self.request,self.template_name,locals())
    def post(self,request):
        try:
            cliente_instance = Cliente.objects.get(dni=request.POST['Cliente'])
            form = RecetaForm(request.POST,request.FILES)
            if form.is_valid():
                receta = form.save(commit=False)
                receta.cliente = cliente_instance
                receta.save()
                form.save_m2m()
                form = RecetaForm()
                cliente_form = ClienteForm()
                messages.success(request, 'La medición se registro con éxito.')
                return render(self.request,self.template_name,locals())
            else:
                print form.errors
                cliente_form = ClienteForm
                messages.error(request, 'No se pudo registrar, se produjeron algunos errores.')
                return render(self.request,self.template_name,locals())
        except Cliente.DoesNotExist:
            messages.error(request, 'No se pudo registrar, el cliente seleccionado no existe.')
            form = RecetaForm()
            cliente_form = ClienteForm
            return render(self.request,self.template_name,locals())

class HistorialView(View):
    template_name = 'receta/historial.html'
    def get(self,request):
        dni = str(request.GET['dni'])
        cliente = Cliente.objects.get(pk=dni)
        historial = Receta.objects.filter(cliente=cliente).order_by("-fecha")
        return render(request,self.template_name,locals())

class NuevoExamenView(View):
    template_name = 'receta/nuevo_examen.html'
    def get(self,request):
        nro = request.GET['dni']
        if int(nro) < 1:
            return redirect("/cliente/")
        else:
            cliente = Cliente.objects.get(pk=nro)
            form = RecetaForm()
            return render(request,self.template_name,locals())
    def post(self,request):
        print "registrado"
        try:
            cliente_instance = Cliente.objects.get(dni=request.POST['Cliente'])
            form = RecetaForm(request.POST,request.FILES)
            if form.is_valid():
                receta = form.save(commit=False)
                receta.cliente = cliente_instance
                receta.save()
                form.save_m2m()
                form = RecetaForm()
                cliente_form = ClienteForm()
                return redirect("/receta/historialcliente?dni="+str(cliente_instance.dni))
            else:
                print form.errors
                cliente_form = ClienteForm
                messages.error(request, 'No se pudo registrar, se produjeron algunos errores.')
                return render(self.request,self.template_name,locals())
        except Cliente.DoesNotExist:
            messages.error(request, 'No se pudo registrar, el cliente seleccionado no existe.')
            form = RecetaForm()
            cliente_form = ClienteForm
            return render(self.request,self.template_name,locals())

class EditarView(View):
    template_name = 'receta/editar.html'
    def get(self,request,nro):
        if int(nro) < 1:
            return redirect("/cliente/")
        else:
            receta = Receta.objects.get(pk=nro)
            form = RecetaForm(instance=receta)
            return render(request,self.template_name,locals())
    def post(self,request,nro):
        receta = Receta.objects.get(pk=nro)
        form = RecetaForm(request.POST,instance=receta)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            form.save_m2m()
            return redirect("/receta/historialcliente?dni="+str(item.cliente.dni))
        else:
            messages.error(request,"No se pudo registrar la medición, existen errores en el formulario.")
            return render(request,self.template_name,locals())