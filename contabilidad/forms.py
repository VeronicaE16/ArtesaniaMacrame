from dataclasses import fields
from django import forms
from contabilidad.models import DetalleCompra, DetalleVenta, Compra, Venta

class CompraForm(forms.ModelForm):
    class Meta:
        model= Compra
        fields=['proveedor']

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model= DetalleVenta
        fields=['producto','cantidad_detalle', 'metodo']

class VentaForm(forms.ModelForm):
    class Meta:
        model= Venta
        fields=[ 'rol', 'cliente']


class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model= DetalleCompra
        fields=['material','cantidad_detalle', 'metodo']