from django.shortcuts import render, redirect
from control.models import Producto,Produccion, Material
from control.forms import ProductoForm, ProduccionForm, MaterialForm, ProductoEditarForm, MaterialEditarForm, ProduccionEditarForm
from django.contrib import messages
from django.db.models import Max, Sum
from django.db import models

from persona.views import proveedor
#@login_required(login_url="usuario-login")

def producto(request):
    titulo_pagina="Producto"
    titulo_modal="Agregar producto"
    productos=Producto.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Correcto! tu registro ha sido guardado exitosamente.')
            return redirect('control-producto')
        else:
            messages.error(request, 'Error! tu registro no ha sido guardado, vuelve a intentarlo')
            return redirect ('control-producto')
    else:
        form = ProductoForm ()
        context={
            "titulo_pagina":titulo_pagina,
            "titulo_modal":titulo_modal,
            "productos":productos,
            "form":form
        }
    return render (request, "control/producto.html", context)

#----------------------produccion--------------------------

def produccion(request, pk):
    titulo_pagina="Producción"
    titulo_modal="Agregar producción"
    producciones=Produccion.objects.filter(producto_id=pk)
    producto_u=Producto.objects.get(id=pk)
    
    if (Produccion.objects.filter(producto_id=producto_u.id).values("producto").annotate(total_definitivo=Sum(('gastos'),output_field=models.IntegerField()))):
        gastos=Produccion.objects.filter(producto_id=producto_u.id).values("producto").annotate(total_definitivo=Sum(('gastos'),output_field=models.IntegerField()))[0]["total_definitivo"]
    
    if request.method == 'POST':
        form = ProduccionForm(request.POST)
        if form.is_valid():
            material=Material.objects.get(id=request.POST['material'])

            if (material.cantidad <= int(request.POST['cantidad_material'])):
                existe= Produccion.objects.filter(producto_id=producto_u.id, material=material)
                
                if len(existe)==0:
                    Produccion.objects.create(
                        cantidad_material=form.cleaned_data.get('cantidad_material'),
                        gastos=material.precio * form.cleaned_data.get('cantidad_detalle'),
                        producto=producto_u,
                        material=material
                    )
                
                    Material.objects.update(
                        cantidad=material.cantidad - form.cleaned_data.get('cantidad_material')
                    )

                    if (Produccion.objects.filter(producto_id=producto_u.id).values("producto").annotate(total_definitivo=Sum(('gastos'), output_field=models.IntegerField()))):
                        gastos=Produccion.objects.filter(producto_id=producto_u.id).values("producto").annotate(total_definitivo=Sum(('gastos'),output_field=models.IntegerField()))["total_definitivo"]
                        
                    else:
                        gastos=0
            
                #form.save()
                messages.success(request, 'Correcto! tu registro ha sido guardado exitosamente.')
                return redirect('control-produccion', pk)
            else:
                anterior=Produccion.objects.filter(producto_id=pk, material=material)

                Material.objects.update(
                    cantidad=material.cantidad - form.cleaned_data.get('cantidad_material')
                )
                if (Produccion.objects.filter(producto_id=producto_u.id).values("producto").annotate(total_definitivo=Sum(('gastos'), output_field=models.IntegerField()))):
                        gastos=Produccion.objects.filter(producto_id=producto_u.id).values("producto").annotate(total_definitivo=Sum(('gastos'),output_field=models.IntegerField()))[0]["total_definitivo"]
                        
                else:
                    gastos=0
        else:
            messages.error(request, 'Error! tu registro no ha sido guardado, vuelve a intentarlo')
            return redirect ('control-produccion', pk)
    else:
        form = ProduccionForm ()
    context={
        "titulo_pagina":titulo_pagina,
        "titulo_modal":titulo_modal,
        "producciones":producciones,
        "form":form,
        "gastos":gastos,
    }
    return render (request, "control/produccion.html", context)

# def ver_produccion(request, pk):
#     titulo_pagina="Produccion"
#     produccion= Produccion.objects.get(id=pk)
#     print(produccion)
#     context={
#         "titulo_pagina":titulo_pagina,
#         "produccion":produccion
#     }
#     return render (request, "control/verproduccion.html", context)

def produccion_editar(request,pk):
    titulo_pagina='producciones'
    producciones= Produccion.objects.all()
    produccion= Produccion.objects.get(id=pk)
    identificacion= produccion.id
    txt="producción"
    url_back= "/control/produccion/2/"
    if request.method == 'POST':
        form= ProduccionEditarForm(request.POST, instance=produccion)
        
        if form.is_valid():
            form.save()
            produccion_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'La producción {produccion_nombre} se editó correctamente!')
            return redirect('control-produccion',pk)
        else:
            usuario_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'Error al modificar la producción {produccion_nombre}')    
            
    else:
        form= ProduccionEditarForm(instance=produccion)
    
    context={
            "titulo_pagina": titulo_pagina,
            "producciones":producciones,
            "form": form,
            "identificacion":identificacion,
            "url_back": url_back,
            "txt":txt
    }
    return render(request, "control/produccion-editar.html", context)

def produccion_eliminar(request,pk):
    titulo_pagina='Producciones'
    producciones= Produccion.objects.all()
    produccion= Produccion.objects.get(id=pk)
    url_back= "/control/produccion"
    accion_txt= f"Proveedor {produccion.id}"
    if request.method == 'POST':
        
        Produccion.objects.filter(id=pk).update(
                    estado='Inactivo'
                )
        produccion_nombre= produccion.id
        messages.success(request,f'La producción {produccion_nombre} se eliminó correctamente!')
        return redirect('control-produccion', pk)
            
    
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "producciones":producciones,
            
            "url_back": url_back
    }
    return render(request, "control/produccion-eliminar.html", context)


def ver_producto(request, pk):
    titulo_pagina="Producto"
    producto= Producto.objects.get(id=pk)
    print(producto)
    context={
        "titulo_pagina":titulo_pagina,
        "producto":producto
    }
    return render (request, "control/verproducto.html", context)

def producto_editar(request,pk):
    titulo_pagina='Productos'
    productos= Producto.objects.all()
    producto= Producto.objects.get(id=pk)
    identificacion= producto.id
    txt="producto"
    url_back= "/control/producto"
    if request.method == 'POST':
        form= ProductoEditarForm(request.POST, instance=producto)
        
        if form.is_valid():
            form.save()
            producto= Producto.objects.get(id=pk)
            id= producto.id
            messages.success(request,f'El producto {id} se editó correctamente!')
            return redirect('control-producto')
        else:
            producto= Producto.objects.get(id=pk)
            id= producto.id
            messages.error(request,f'Error al modificar el producto {id}')    
            
    else:
        form= ProductoEditarForm(instance=producto)
    
    context={
            "titulo_pagina": titulo_pagina,
            "productos":productos,
            "form": form,
            "identificacion":identificacion,
            "url_back": url_back,
            "txt":txt
    }
    return render(request, "control/producto-editar.html", context)

def producto_eliminar(request,pk):
    titulo_pagina='Productos'
    productos= Producto.objects.all()
    producto= Producto.objects.get(id=pk)
    url_back= "/control/producto"
    accion_txt= f"Producto {producto.id}"
    if request.method == 'POST':
        
        Producto.objects.filter(id=pk).update(
                    estado='Inactivo'
                )
        producto_nombre= producto.id
        messages.success(request,f'El producto {producto_nombre} se eliminó correctamente!')
        return redirect('control-producto')
            
    
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "productos":productos,
            
            "url_back": url_back
    }
    return render(request, "control/producto-eliminar.html", context)

#---------------------------Material----------------------

def material(request):
    titulo_pagina="Material"
    titulo_modal="Agregar material"
    materiales=Material.objects.all()
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Correcto! tu registro ha sido guardado exitosamente.')
            return redirect('control-material')
        else:
            messages.error(request, 'Error! tu registro no ha sido guardado, vuelve a intentarlo')
            return redirect ('control-material')
    else:
        form = MaterialForm ()
        context={
            "titulo_pagina":titulo_pagina,
            "titulo_modal":titulo_modal,
            "materiales":materiales,
            "form":form
        }
    return render (request, "control/material.html", context)

def ver_material(request, pk):
    titulo_pagina="Material"
    material= Material.objects.get(id=pk)
    print(material)
    context={
        "titulo_pagina":titulo_pagina,
        "material":material
    }
    return render (request, "control/vermaterial.html", context)

def material_editar(request,pk):
    titulo_pagina='materiales'
    materiales= Material.objects.all()
    material= Material.objects.get(id=pk)
    identificacion= material.id
    txt="material"
    url_back= "/control/material"
    if request.method == 'POST':
        form= MaterialEditarForm(request.POST, instance=material)
        
        if form.is_valid():
            form.save()
            material_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El material {material_nombre} se editó correctamente!')
            return redirect('control-material')
        else:
            material_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'Error al modificar el material {material_nombre}')    
            
    else:
        form= MaterialEditarForm(instance=material)
    
    context={
            "titulo_pagina": titulo_pagina,
            "materiales":materiales,
            "form": form,
            "identificacion":identificacion,
            "url_back": url_back,
            "txt":txt
    }
    return render(request, "control/material-editar.html", context)

def material_eliminar(request,pk):
    titulo_pagina='Materiales'
    materiales= Material.objects.all()
    material= Material.objects.get(id=pk)
    url_back= "/control/material"
    accion_txt= f"Material {material.id}"
    if request.method == 'POST':
        
        Material.objects.filter(id=pk).update(
                    estado='Inactivo'
                )
        material_nombre= material.nombre
        messages.success(request,f'El material {material_nombre} se eliminó correctamente!')
        return redirect('control-material')
            
    
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "materiales":materiales,
            
            "url_back": url_back
    }
    return render(request, "control/material-eliminar.html", context)
# Create your views here.
