# -*- encoding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import LoginForm

class LoginRequiredMixin(object):
    u"""Ensures that user must be authenticated in order to access view."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class Login(View):

    form_class = LoginForm
    template_name = 'login/index.html'
    user_check_failure_path = '/login'

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('/')
        form = self.form_class()
        return render(request, self.template_name, {'form':form })

    def post(self,request):
        form = self.form_class(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            if user.is_active:
                login(request, user)
                if request.GET:
                    return redirect(request.GET['next'])
                return redirect('/')
            return render(request, self.template_name, {'form': form, 'error': 'La cuenta esta deshabilitada'})
        else:
            return render(request, self.template_name, {'form': form, 'error': 'Verifique los datos ingresados'})


class Logout(View):
    def get(self,request):
            logout(request)
            return redirect('/login')