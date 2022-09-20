from pickle import TRUE
from django.db import models
from django.utils.translation import gettext_lazy as _

class Proveedor (models.Model):
    nombre=models.CharField(max_length=50, blank=False, verbose_name="Nombre")
    identificacion=models.IntegerField( unique=True, blank=False, verbose_name="# de identificación" )
    telefono=models.CharField(max_length=13, unique=True, blank=False, verbose_name="Teléfono")
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
    estado= models.CharField(max_length=8, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    def __str__ (self) -> str:
        return '%s' %(self.nombre)
    def clean(self):
        self.nombre= self.nombre.capitalize()

class Usuario (models.Model):
    identificacion=models.IntegerField( unique=True, blank=False, verbose_name="N° de documento" )
    nombre=models.CharField(max_length=50, blank=False, verbose_name="Nombre")
    apellido=models.CharField(max_length=50, blank=False, verbose_name="Apellido")
    correo=models.EmailField(max_length=50, blank=False, unique=True, verbose_name="Correo")
    telefono=models.CharField(max_length=13, unique=True, blank=False, verbose_name="Teléfono")
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
    estado=models.CharField(max_length=50, blank=False, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO) 
    def __str__ (self) -> str:
        return '%s %s'%(self.nombre, self.apellido)
    def clean(self):
        self.nombre= self.nombre.capitalize()
        self.apellido= self.apellido.capitalize()


class Cliente (models.Model):
    nombre=models.CharField(max_length=50, blank=False,  verbose_name="Nombre")
    identificacion=models.BigIntegerField (unique=True, blank=False, verbose_name="# de identificación" )
    telefono=models.CharField(max_length=13, unique=True, blank=False, verbose_name="Teléfono")
    def __str__ (self) -> str:
        return '%s' %(self.nombre)
    def clean(self):
        self.nombre= self.nombre.capitalize()
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
    estado=models.CharField(max_length=50, blank=False, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO) 
    def __str__ (self) -> str:
        return '%s' %(self.nombre)
    def clean(self):
        self.nombre= self.nombre.capitalize()
        
# Create your models here.
