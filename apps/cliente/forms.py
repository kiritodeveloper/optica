from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    dni = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'DNI','required':'true',}),label="DNI")
    nombre = forms.CharField(max_length=45,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','required':'true',}),label="Nombre")
    apellido = forms.CharField(max_length=45,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido','required':'true',}),label="Apellido")
    direccion = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control','rows':2,}),required=False,)
    telefono = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}),label="Telefono",required=False,)
    email = forms.EmailField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Correo Electronico'}),label="Email",required=False,)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'yyyy-mm-dd'}),label="Fecha de Nacimiento",required=False,)
    ocupacion = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ocupacion'}),label="Ocupacion",required=False,)
    foto = forms.ImageField(required=False,)

    class Meta:
        model = Cliente
        fields = ('dni','nombre','apellido','direccion','telefono','email','fecha_nacimiento','ocupacion','foto')