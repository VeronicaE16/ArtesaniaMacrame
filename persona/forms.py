from django import forms
from persona.models import Proveedor, Usuario, Cliente

class ProveedorForm(forms.ModelForm):
    class Meta:
        model= Proveedor
        fields=['nombre', 'identificacion', 'telefono']
        
class ProveedorEditarForm(forms.ModelForm):
    class Meta:
        model= Usuario
        fields= ['nombre','telefono','estado']
            

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        #fields='__all__'
        fields=['identificacion','nombre', 'apellido', 'correo', 'telefono']

class UsuarioEditarForm(forms.ModelForm):
    class Meta:
        model= Usuario
        fields= ['nombre','apellido','correo','telefono', 'estado']

class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        fields=['nombre','identificacion','telefono']       

class ClienteEditarForm(forms.ModelForm):
    class Meta:
        model= Usuario
        fields= ['nombre','telefono', 'estado']