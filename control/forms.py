from logging import PlaceHolder
from logging import PlaceHolder
from tkinter import Widget
from tkinter import Widget
from django import forms
from control.models import Producto, Produccion, Material

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['descripcion','precio','categoria']
     
class ProductoEditarForm(forms.ModelForm):
    class Meta:
        model= Producto
        fields= ['descripcion','precio','categoria','estado']
        

class ProduccionForm(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = ['material','producto','fechai','fechaf','cantidad_material']
        
        
        
class ProduccionEditarForm(forms.ModelForm):
    class Meta:
        model= Produccion
        fields= ['fechai','fechaf','cantidad_material','estado']
        

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nombre','categoria','cantidad','precio','metodo'] 
        
class MaterialEditarForm(forms.ModelForm):
    class Meta:
        model= Material
        fields= ['nombre','cantidad','precio','metodo', 'estado']
        