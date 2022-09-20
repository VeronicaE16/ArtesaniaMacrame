from django.db import models
from django.utils.translation import gettext_lazy as _
from control.models import Producto, Material
from persona.models import Proveedor, Cliente, Usuario


class Venta(models.Model):
    rol=models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, verbose_name="Vendedor")
    cliente=models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, verbose_name="Cliente")
    fecha=models.DateField(auto_now = True)
    neto_pagar=models.FloatField(default=0)
    class Estado(models.TextChoices):
        ABIERTA='Abierta', _('Abierta')
        CERRADA='Cerrada', _('Cerrada')
        ANULADA='Anulada', _('Anulada')
    estado=models.CharField(max_length=7, blank=False, choices=Estado.choices, verbose_name="Estado", default=Estado.ABIERTA)
    def __str__(self) -> str:
        return '%s''%s'%(self.fecha, self.estado)

class DetalleVenta(models.Model):
    producto=models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, verbose_name=u"Producto")
    venta=models.ForeignKey(Venta, on_delete=models.SET_NULL, null=True, verbose_name="Venta")
    cantidad_detalle=models.IntegerField(blank=False,  verbose_name="Cantidad")
    class Metodo(models.TextChoices):
        EFECTIVO='Efectivo', _('Efectivo')
    metodo=models.CharField(max_length=25, blank=False,  choices=Metodo.choices, verbose_name="Método de pago", default=Metodo.EFECTIVO)
    class Estado(models.TextChoices):
        ABIERTA='Abierta', _('Abierta')
        CERRADA='Cerrada', _('Cerrada')
        ANULADA='Anulada', _('Anulada')
    total=models.FloatField(default=0)
    estado=models.CharField(max_length=50, blank=False, choices=Estado.choices, verbose_name="Estado", default=Estado.ABIERTA)
    def __str__(self) -> str:
        return '%s'%(self.venta)
    
class Compra(models.Model):
    proveedor=models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, verbose_name="Proveedor")
    neto_pagar=models.FloatField(default=0)
    class Estado(models.TextChoices):
        ABIERTA='Abierta', _('Abierta')
        CERRADA='Cerrada', _('Cerrada')
        ANULADA='Anulada', _('Anulada')
    estado=models.CharField(max_length=50, blank=False, choices=Estado.choices, verbose_name="Estado", default=Estado.ABIERTA)
    fecha=models.DateTimeField(auto_now = True)

class DetalleCompra(models.Model):
    material=models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, verbose_name="Material")
    compra=models.ForeignKey(Compra, on_delete=models.SET_NULL, null=True, verbose_name="Compra")
    cantidad_detalle=models.IntegerField(blank=False,  verbose_name="Cantidad")
    class Metodo(models.TextChoices):
        EFECTIVO='Efectivo', _('Efectivo')
    total=models.FloatField(default=0)
    metodo=models.CharField(max_length=25, blank=False,  choices=Metodo.choices, verbose_name="Método de pago", default=Metodo.EFECTIVO)
    class Estado(models.TextChoices):
        ABIERTA='Abierta', _('Abierta')
        CERRADA='Cerrada', _('Cerrada')
        ANULADA='Anulada', _('Anulada')
    estado=models.CharField(max_length=50, blank=False, choices=Estado.choices, verbose_name="Estado", default=Estado.ABIERTA)
    def __str__ (self) -> str:
        return '%s' %(self.material)
# Create your models here.
