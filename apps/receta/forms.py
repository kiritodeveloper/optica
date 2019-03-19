# -*- encoding: utf-8 -*-
from django import forms
from .models import Receta
from apps.almacen.models import *

class RecetaForm(forms.ModelForm):
    od_esf = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':"OD. ESF."}),required=False)
    oi_esf = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':"OI. ESF."}),required=False)
    od_cil = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':"OD. CIL."}),required=False)
    oi_cil = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':"OI. CIL."}),required=False)
    od_eje = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':"OD. EJE."}),required=False)
    oi_eje = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':"OI. EJE."}),required=False)
    od_dip = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':"OD. DIP."}),required=False)
    oi_dip = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':"OI. DIP."}),required=False)
    od_avsc = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':"OD. AV.SC."}),required=False)
    oi_avsc = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':"OI. AV.SC."}),required=False)
    od_avcc = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':"OD. AV.CC."}),required=False)
    oi_avcc = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':"OI. AV.CC."}),required=False)
    add = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Add'}),required=False)
    patologia = forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Patología'}),required=False)
    lente = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control chosen-select',}),
                                   label="Lente",queryset=Lente.objects.all(),empty_label="Seleccione el tipo de Lente",required=False)
    complementos = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'chosen-select chosen-container-multi',}),queryset=Aditivos.objects.all(),required=False)
    imagen = forms.ImageField(required=False)
    class Meta:
        model = Receta
        fields = ('od_esf','oi_esf','od_cil','oi_cil','od_eje','oi_eje','od_dip','oi_dip','od_avsc','oi_avsc','od_avcc','oi_avcc','add','patologia','lente','complementos','imagen',)