from logging import PlaceHolder
from django.db import models
from django.utils.translation import gettext_lazy as _


class Producto(models.Model):
    descripcion=models.TextField (max_length=100, verbose_name="Nombre")
    precio=models.FloatField (blank=False, verbose_name="Precio")
    class Categoria(models.TextChoices):
        LLAVEROS='Llaveros', _('Llaveros')
        ATRAPASUEÑOS='Atrapasueños', _('Atrapasueños')
        MASETAS='Masetas', _('Masetas')
        MANILLAS='Manillas', _('Manillas')
    categoria=models.CharField(max_length=50, blank=False, choices=Categoria.choices, verbose_name="Categoria")
    class Estado(models.TextChoices):
        EXISTENTE='Existente', _('Existente')
        AGOTADO='Agotado', _('Agotado')
    estado=models.CharField(max_length=50, blank=False, choices=Estado.choices, verbose_name="Estado", default=Estado.EXISTENTE)
    def __str__(self) -> str:
        return '%s '%(self.descripcion)
 
    
class Material(models.Model):
    nombre=models.CharField(max_length=50, blank=False, verbose_name="Nombre")
    precio=models.FloatField (blank=False, verbose_name="Precio")
    class Categoria(models.TextChoices):
        HILO='Hilo', _('Hilo')
        PEPITAS='Pepitas', _('Pepitas')
    categoria=models.CharField(max_length=50, blank=False, choices=Categoria.choices, verbose_name="Categoria")
    cantidad=models.IntegerField(verbose_name="Cantidad de material")
    class Metodo(models.TextChoices):
        EFECTIVO='Efectivo', _('Efectivo')
    metodo=models.CharField(max_length=50, blank=False, choices=Metodo.choices, verbose_name="Metodo de pago", default=Metodo.EFECTIVO)
    class Estado(models.TextChoices):
        EXISTENTE='Existente', _('Existente')
        AGOTADO='Agotado', _('Agotado')
    estado=models.CharField(max_length=50, blank=False, choices=Estado.choices, verbose_name="Estado", default=Estado.EXISTENTE)
    def __str__ (self) -> str:
        return '%s' %(self.nombre)
    def clean(self):
        self.nombre= self.nombre.capitalize() 
        
class Produccion(models.Model):
    material=models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, verbose_name="Material")
    producto=models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, verbose_name="Producto")
    fechai=models.DateField(verbose_name="Fecha de inicio")
    fechaf=models.DateField(verbose_name="Fecha final")
    cantidad_material=models.IntegerField(blank=False, verbose_name="Cantidad de material")
    gastos=models.IntegerField(default=0)
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
    estado=models.CharField(max_length=50,choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)
    
# Create your models here.  
