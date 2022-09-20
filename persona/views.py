from django.shortcuts import render, redirect
from persona.forms import ProveedorForm, UsuarioForm, ClienteForm, UsuarioEditarForm, ProveedorEditarForm, ClienteEditarForm
from persona.models import Proveedor, Usuario, Cliente
from django.contrib import messages

def proveedor (request):
    titulo_pagina="Proveedor"
    titulo_modal="Agregar Proveedor"
    proveedores=Proveedor.objects.all()

    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Correcto! tu registro ha sido guardado exitosamente.')
            return redirect('persona-proveedor')
        else:
            messages.error(request, 'Error! tu registro no ha sido guardado, vuelve a intentarlo.')
            return redirect('persona-proveedor')
    else:
        form = ProveedorForm ()
        context={
            "titulo_pagina":titulo_pagina,
            "titulo_modal":titulo_modal,
            "proveedores":proveedores,
            "form":form
        }     
    return render (request, "persona/proveedor.html", context)


def ver_proveedor (request, pk):
    titulo_pagina="Proveedor"
    proveedor= Proveedor.objects.get(id=pk)
    print(proveedor)
    context={
        "titulo_pagina":titulo_pagina,
        "proveedor":proveedor,
        }     
        
    return render (request, "persona/verproveedor.html", context)

def proveedor_editar(request,pk):
    titulo_pagina='Proveedores'
    proveedores= Proveedor.objects.all()
    proveedor= Proveedor.objects.get(id=pk)
    identificacion= proveedor.identificacion
    txt="proveedor"
    url_back= "/persona/proveedor"
    if request.method == 'POST':
        form= ProveedorEditarForm(request.POST, instance=proveedor)
        
        if form.is_valid():
            form.save()
            proveedor_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El provedor {proveedor_nombre} se editó correctamente!')
            return redirect('persona-proveedor')
        else:
            proveedor_nombre= form.cleaned_data.get('nombre')                                
            messages.error(request,f'Error al modificar el proveedor {proveedor_nombre}')    
            
    else:
        form= ProveedorEditarForm(instance=proveedor)
    
    context={
            "titulo_pagina": titulo_pagina,
            "proveedores":proveedores,
            "form": form,
            "identificacion":identificacion,
            "url_back": url_back,
            "txt":txt
    }
    return render(request, "persona/proveedor-editar.html", context)


def proveedor_eliminar(request,pk):
    titulo_pagina='Proveedores'
    proveedores= Proveedor.objects.all()
    proveedor= Proveedor.objects.get(id=pk)
    url_back= "/persona/proveedor"
    accion_txt= f"Proveedor {proveedor.identificacion}"
    if request.method == 'POST':
        
        Proveedor.objects.filter(id=pk).update(
                    estado='Inactivo'
                )
        proveedor_nombre= proveedor.nombre
        messages.success(request,f'El proveedor {proveedor_nombre} se eliminó correctamente!')
        return redirect('persona-proveedor')
            
    
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "proveedores":proveedores,
            
            "url_back": url_back
    }
    return render(request, "persona/usuario-eliminar.html", context)


def usuario (request):
    titulo_pagina="Empleado"
    titulo_modal="Agregar empleado"
    usuarios=Usuario.objects.all()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Correcto! tu registro ha sido guardado exitosamente.')
            return redirect('persona-usuario')
        else:
            messages.error(request, 'Error! tu registro no ha sido guardado, vuelve a intentarlo')
            
    else:
        form = UsuarioForm ()
    context={
        "titulo_pagina":titulo_pagina,
        "titulo_modal":titulo_modal,
        "usuarios":usuarios,
        "form":form
    }     
        
    return render (request, "persona/usuario.html", context)

def ver_usuario (request, pk):
    titulo_pagina="Empleado"
    usuario= Usuario.objects.get(id=pk)
    print(usuario)
    context={
        "titulo_pagina":titulo_pagina,
        "usuario":usuario,
        }     
        
    return render (request, "persona/verusuario.html", context)

def usuario_editar(request,pk):
    titulo_pagina='Empleado'
    usuarios= Usuario.objects.all()
    usuario= Usuario.objects.get(id=pk)
    identificacion= usuario.identificacion
    txt="empleado"
    url_back= "/persona/usuario"
    if request.method == 'POST':
        form= UsuarioEditarForm(request.POST, instance=usuario)
        
        if form.is_valid():
            form.save()
            usuario_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El empleado {usuario_nombre} se editó correctamente!')
            return redirect('persona-usuario')
        else:
            usuario_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'Error al modificar el empleado {usuario_nombre}')    
            
    else:
        form= UsuarioEditarForm(instance=usuario)
    
    context={
            "titulo_pagina": titulo_pagina,
            "usuarios":usuarios,
            "form": form,
            "identificacion":identificacion,
            "url_back": url_back,
            "txt": txt
    }
    return render(request, "persona/usuario-editar.html", context)

def usuario_eliminar(request,pk):
    titulo_pagina='Empleado'
    usuarios= Usuario.objects.all()
    usuario= Usuario.objects.get(id=pk)
    url_back= "/persona/usuario"
    accion_txt= f"Empleado {usuario.identificacion}"
    if request.method == 'POST':
        
        Usuario.objects.filter(id=pk).update(
                    estado='Inactivo'
                )
        usuario_nombre= usuario.nombre
        messages.success(request,f'El empleado {usuario_nombre} se eliminó correctamente!')
        return redirect('persona-usuario')
            
    
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "usuarios":usuarios,
            
            "url_back": url_back
    }
    return render(request, "persona/usuario-eliminar.html", context)

def cliente (request):
    titulo_pagina="Cliente"
    titulo_modal="Agregar Cliente"
    clientes=Cliente.objects.all()
    #if padre 
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Correcto! tu registro ha sido guardado exitosamente.')
            return redirect('persona-cliente')
        else:
            messages.error(request, 'Error! tu registro no ha sido guardado, vuelve a intentarlo.')
            return redirect('persona-cliente')
    else:
        form = ClienteForm ()
        context={
            "titulo_pagina":titulo_pagina,
            "titulo_modal":titulo_modal,
            "clientes":clientes,
            "form":form
        }     
    return render (request, "persona/cliente.html", context)

def ver_cliente (request, pk):
    titulo_pagina="Cliente"
    cliente= Cliente.objects.get(id=pk)
    print(cliente)
    context={
        "titulo_pagina":titulo_pagina,
        "cliente":cliente,
        }     
        
    return render (request, "persona/vercliente.html", context)

def cliente_editar(request,pk):
    titulo_pagina='Clientes'
    clientes= Cliente.objects.all()
    cliente= Cliente.objects.get(id=pk)
    identificacion= cliente.identificacion
    txt="cliente"
    url_back= "/persona/cliente"
    if request.method == 'POST':
        form= ClienteEditarForm(request.POST, instance=cliente)
        
        if form.is_valid():
            form.save()
            cliente_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El cliente {cliente_nombre} se editó correctamente!')
            return redirect('persona-cliente')
        else:
            usuario_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'Error al modificar el usuario {cliente_nombre}')    
            
    else:
        form= ClienteEditarForm(instance=cliente)
    
    context={
            "titulo_pagina": titulo_pagina,
            "clientes":clientes,
            "form": form,
            "identificacion":identificacion,
            "url_back": url_back,
            "txt":txt
    }
    return render(request, "persona/cliente-editar.html", context)

def cliente_eliminar(request,pk):
    titulo_pagina='Clientes'
    clientes= Cliente.objects.all()
    cliente= Cliente.objects.get(id=pk)
    url_back= "/persona/cliente"
    accion_txt= f"Cliente {cliente.identificacion}"
    if request.method == 'POST':
        
        Cliente.objects.filter(id=pk).update(
                    estado='Inactivo'
                )
        cliente_nombre= cliente.nombre
        messages.success(request,f'El usuario {cliente_nombre} se eliminó correctamente!')
        return redirect('persona-cliente')
            
    
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "clientes":clientes,
            
            "url_back": url_back
    }
    return render(request, "persona/cliente-eliminar.html", context)
# Create your views here.
