from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from contabilidad.models import Venta, DetalleVenta, Compra, DetalleCompra
from contabilidad.forms import CompraForm, DetalleVentaForm, DetalleCompraForm, VentaForm
from control.models import Material, Producto
from django.db.models import Max, Sum
from django.db import models
from datetime import date, datetime
from persona.models import Usuario
#-------------------------------------REPORTES-------------------------------------


def reportes(request):

    # rol= Venta.objects.values('rol__categoria')
    # roles={"Vendedor":list()}
    venta= DetalleVenta.objects.filter(venta__estado="Cerrada").values('cantidad_detalle','producto_id','producto__descripcion','producto__categoria','venta__fecha')
    ventas={"Llaveros":list(),"Atrapasueños":list(),"Masetas":list(),"Manillas":list(), "total":list(), "VentasCategoria":list()}
    print(venta)
    # roles=["Vendedor"].append(rol.filter(rol__categoria="Vendedor"))
    for mes in range(12):
        ventas["Llaveros"].append(venta.filter(producto__categoria="LLaveros",venta__fecha__month=mes+1,venta__fecha__year=datetime.now().year).aggregate(Sum('cantidad_detalle'))['cantidad_detalle__sum'])
        ventas["Atrapasueños"].append(venta.filter(producto__categoria="Atrapasueños",venta__fecha__month=mes+1,venta__fecha__year=datetime.now().year).aggregate(Sum('cantidad_detalle'))['cantidad_detalle__sum'])
        ventas["Masetas"].append(venta.filter(producto__categoria="Masetas",venta__fecha__month=mes+1,venta__fecha__year=datetime.now().year).aggregate(Sum('cantidad_detalle'))['cantidad_detalle__sum'])
        ventas["Manillas"].append(venta.filter(producto__categoria="Manillas",venta__fecha__month=mes+1,venta__fecha__year=datetime.now().year).aggregate(Sum('cantidad_detalle'))['cantidad_detalle__sum'])
        ventas["total"].append(venta.filter(venta__fecha__month=mes+1,venta__fecha__year=datetime.now().year).aggregate(Sum('cantidad_detalle'))['cantidad_detalle__sum'])
        
        
        
        
        for i,item in enumerate(ventas["Llaveros"]):
            if item==None:
                ventas["Llaveros"][i]=0
            if ventas["Atrapasueños"][i]== None:
                ventas["Atrapasueños"][i]=0
            if ventas["Masetas"][i]== None:
                ventas["Masetas"][i]=0
            if ventas["Manillas"][i]== None:
                ventas["Manillas"][i]=0
            if ventas["total"][i]== None:
                ventas["total"][i]=0
            
    
    ventas["VentasCategoria"].append(venta.filter(producto__categoria="LLaveros",venta__fecha__year=datetime.now().year).aggregate(Sum('cantidad_detalle'))['cantidad_detalle__sum'])
    ventas["VentasCategoria"].append(venta.filter(producto__categoria="Atrapasueños",venta__fecha__year=datetime.now().year).aggregate(Sum('cantidad_detalle'))['cantidad_detalle__sum'])
    ventas["VentasCategoria"].append(venta.filter(producto__categoria="Masetas",venta__fecha__year=datetime.now().year).aggregate(Sum('cantidad_detalle'))['cantidad_detalle__sum'])
    ventas["VentasCategoria"].append(venta.filter(producto__categoria="Manillas",venta__fecha__year=datetime.now().year).aggregate(Sum('cantidad_detalle'))['cantidad_detalle__sum'])
    for i,item in enumerate(ventas["VentasCategoria"]):
        if item==None:
            ventas["VentasCategoria"][i]=0
            
    # for mes in meses:
    #     calzado[mes]=[venta.filter(producto__categoria="Calzado",factura__fecha__month=contador,factura__fecha__year=2022).aggregate(Sum('cantidad_detalle'))['cantidad_detalle__sum']]
    #     tejidos[mes]=[venta.filter(producto__categoria="tejidos",factura__fecha__month=contador,factura__fecha__year=2022).aggregate(Sum('cantidad_detalle'))['cantidad_detalle__sum']]
    #     ropa[mes]=[venta.filter(producto__categoria="ropa",factura__fecha__month=contador,factura__fecha__year=2022).aggregate(Sum('cantidad_detalle'))['cantidad_detalle__sum']]
    #     contador+=1

    
    print(ventas)
    titulo_pagina="Reporte de ventas"
    context={
        'titulo_pagina':titulo_pagina,
        'ventas':ventas,
        # 'roles':roles,
    }
    return render(request,'contabilidad/reportes-venta.html',context)


#-------------------------------------COMPRA-------------------------------------
def compra (request):
    titulo_pagina="Compra"
    compras=Compra.objects.all()
    if request.method == 'POST':
        form = CompraForm (request.POST)
        if form.is_valid():
            aux=form.save()
            messages.success(request, 'Correcto! tu registro ha sido guardado exitosamente.')
            return redirect('contabilidad-detallecompra',aux.id)
     
    
    form = CompraForm ()
    context={
        "titulo_pagina":titulo_pagina,
        "compras":compras,
        "form":form
    }     
    return render (request, "contabilidad/compra.html", context)

def detalle_compra(request, pk):
    titulo_pagina="Compra"
    titulo_modal="Agregar detalle compra"
    detalles=DetalleCompra.objects.filter(compra_id=pk)
    compra_u=Compra.objects.get(id=pk)
    
    if (DetalleCompra.objects.filter(compra_id=compra_u.id).values("compra").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))):
        total=DetalleCompra.objects.filter(compra_id=compra_u.id).values("compra").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))[0]["total_definitivo"]
    else:
        total=0
    
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST)
        if form.is_valid():
            material= Material.objects.get(id=request.POST['material'])
            existe= DetalleCompra.objects.filter(compra=pk, material=material)
            if len (existe)==0:
                DetalleCompra.objects.create(
                    cantidad_detalle=form.cleaned_data.get('cantidad_detalle'),
                    total= material.precio * form.cleaned_data.get('cantidad_detalle'),
                    compra=compra_u,
                    material = material,
                )
                
                Material.objects.filter(id=material.id).update(
                    cantidad=material.cantidad + form.cleaned_data.get('cantidad_detalle')
                )
                
                if (DetalleCompra.objects.filter(compra_id=compra_u.id).values("compra").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))):
                    total=DetalleCompra.objects.filter(compra_id=compra_u.id).values("compra").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))[0]["total_definitivo"]
                    Compra.objects.filter(id=pk).update(
                        neto_pagar=total
                    )
                else: 
                    total=0
                
                detalle_id = form.cleaned_data.get('id')
                messages.success(request, f'Correcto! el registro detalle de compra {detalle_id} ha sido guardado exitosamente.')
                return redirect('contabilidad-tabladetalle', pk)
            else:
                anterior=DetalleCompra.objects.filter(compra_id=pk,material=request.POST['material'])
                
                DetalleCompra.objects.filter(compra_id=pk,material=request.POST['material']).update(
                    cantidad_detalle=anterior[0].cantidad_detalle + form.cleaned_data.get('cantidad_detalle'),
                    total=anterior[0].total + material.precio * form.cleaned_data.get('cantidad_detalle'),
                )
                Material.objects.filter(id=material.id).update(
                        cantidad=material.cantidad + form.cleaned_data.get('cantidad_detalle')
                )
                
                if (DetalleCompra.objects.filter(compra_id=compra_u.id).values("compra").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))):
                    total=DetalleCompra.objects.filter(compra_id=compra_u.id).values("compra").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))[0]["total_definitivo"]
                    Compra.objects.filter(id=pk).update(
                        neto_pagar=total
                    )
                else:
                    total=0
                
    else:
        form = DetalleCompraForm ()
    context={
        "titulo_pagina":titulo_pagina,
        "titulo_modal":titulo_modal,
        "detalles":detalles,
        "form":form,
        "compra":compra_u,
        "total":total
    }
    return render (request, "contabilidad/detallecompra.html", context)

def tdetalle(request, pk):
    titulo_pagina="Compra"
    detalles=DetalleCompra.objects.filter(compra_id=pk)
    compra_u=Compra.objects.get(id=pk)
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST)
        if form.is_valid():
            
            compra=DetalleCompra.objects.create(
                material=form.cleaned_data.get('material'),
                cantidad=form.cleaned_data.get('cantidad'),
                metodo=form.cleaned_data.get('metodo'),
                compra=compra_u,
            )
            detalle_id = form.cleaned_data.get('id')
            messages.success(request, f'Correcto! el registro detalle de venta {detalle_id} ha sido guardado exitosamente.')
            
    else:
        form = DetalleCompraForm ()
    context={
        "titulo_pagina":titulo_pagina,
        "detalles":detalles,
        "form":form,
        "compra":compra_u
    }
    return render (request, "contabilidad/tabladetalle.html", context)

def detalle_eliminar (request, pk):
    titulo_pagina='Compra'
    u_detalles= DetalleCompra.objects.get(id=pk)
    compra_u= u_detalles.compra
    detalles=DetalleCompra.objects.filter(compra_id=compra_u.id)
    accion_txt= f"¿Está seguro de eliminar el detalle de compra {u_detalles.id}?"

    if request.method == 'POST':
        form= DetalleCompraForm(request.POST)
        u_detalles.delete()
        messages.success(request, f'El detalle de compra se eliminó correctamente!')
        return redirect ('contabilidad-tabladetalle', compra_u.id)
    
    else:
        form=DetalleCompraForm
    context={
        "titulo_pagina":titulo_pagina,
        "accion_txt":accion_txt,
        "detalles":detalles,
        "compra":compra_u,
        "form":form,
    }
    return render (request, "contabilidad/detalle-eliminar.html", context)
    

def estado_detalle(request, pk, estado):
    titulo_pagina="Compra"
    tcompras = Compra.objects.all()
    tcompra = Compra.objects.get(id=pk)
    eliminacion=DetalleCompra.objects.filter(compra=tcompra)
    estado_msj=""
    estado_txt=""
    if estado == "Abierta":
        if not eliminacion.exists():
            
            estado_msj= "Sí"
            estado_txt= f"¿Está seguro de eliminar la compra {tcompra.id}?"
            if request.method =='POST':
                form = DetalleCompraForm(request.POST)
                
                tcompra.delete()
                messages.success(request,f'Compra {pk} se eliminó correctamente!')
                return redirect('contabilidad-compra')
            else:
                form=DetalleCompraForm()
        else:
            messages.error(request,f'Compra {pk} no se eliminó correctamente!')
            return redirect('contabilidad-compra')
    elif estado=="Cerrada":
        titulo_modal="Anular compra"
        estado_msj="Sí"
        estado_txt=f"¿Está seguro de anular la compra {tcompra.id}?"
        if request.method == 'POST':
            form = DetalleCompraForm (request.POST)
            Compra.objects.filter(id=pk).update(
                        estado='Anulada'
                    )
            messages.success(request,f'Compra {tcompra.id} se anuló correctamente!')
            return redirect('contabilidad-compra')
        else:
            form=DetalleCompraForm()
    else:
        titulo_modal="Cerrar compra"
        estado_msj="Sí"
        estado_txt=f"¿Está seguro de cerrar la compra {tcompra.id}?"
        if request.method == 'POST':
            form = DetalleCompraForm (request.POST)
            Compra.objects.filter(id=pk).update(
                        estado='Cerrada'
                    )
            messages.success(request,f'Compra {tcompra.id} se cerró correctamente!')
            return redirect('contabilidad-compra')
        else:
            form=DetalleCompraForm()
    context={
        "titulo_pagina":titulo_pagina,
        "tcompras":tcompras,
        "estado_msj":estado_msj,
        "estado_txt":estado_txt,
        "titulo_modal":titulo_modal
    }
    return render(request, "contabilidad/estadocompra.html", context)


def ver_compra (request, pk):
    titulo_pagina="Compra"
    compra=Compra.objects.get(id=pk)
    detalles= DetalleCompra.objects.filter(compra_id=pk)
    print(detalles)
    context={
        "titulo_pagina":titulo_pagina,
        "compra":compra,
        "detalles":detalles
        }     
        
    return render (request, "contabilidad/vercompra.html", context)

#-------------------------------------VENTA-------------------------------------


def venta(request):
    titulo_pagina="Venta"
    titulo_modal="Agregar venta"
    ventas=Venta.objects.all()
    if request.method == 'POST':
        form= VentaForm(request.POST)
        aux=form.save()
        
        messages.success(request, 'Correcto! tu registro ha sido guardado exitosamente.')
        return redirect('contabilidad-detalleventa', aux.id)
    else:
        form= VentaForm()
        
    context={
        'form':form,
        "titulo_pagina":titulo_pagina,
        "titulo_modal":titulo_modal,
        "ventas":ventas,
    }
    return render (request, "contabilidad/venta.html", context)

def reporte_venta(request):
    titulo_pagina="Reporte de ventas"
    ventas=Venta.objects.all()
    
    context={
        "titulo_pagina":titulo_pagina,
        "ventas":ventas,
    }
    return render (request, "contabilidad/reportes-venta.html", context)

def detalle_venta(request, pk):
    titulo_pagina="Venta"
    titulo_modal="Agregar detalle venta"
    detalles=DetalleVenta.objects.filter(venta_id=pk)
    venta_u= Venta.objects.get(id=pk)
    
    if (DetalleVenta.objects.filter(venta_id=venta_u.id).values("venta").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))):
        total=DetalleVenta.objects.filter(venta_id=venta_u.id).values("venta").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))[0]["total_definitivo"]
    else:
        total=0
        
    if request.method == 'POST':
        form =DetalleVentaForm(request.POST)
        if form.is_valid():
            producto= Producto.objects.get(id=request.POST['producto'])
            existe= DetalleVenta.objects.filter(venta=pk,producto=producto)
            if len(existe) == 0:
                venta=DetalleVenta.objects.create(
                    producto=form.cleaned_data.get('producto'),
                    cantidad_detalle=form.cleaned_data.get('cantidad_detalle'),
                    total=producto.precio * form.cleaned_data.get('cantidad_detalle'),
                    metodo=form.cleaned_data.get('metodo'),
                    venta=venta_u,
                )
                
                if (DetalleVenta.objects.filter(venta_id=venta_u.id).values("venta").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))):
                    total=DetalleVenta.objects.filter(venta_id=venta_u.id).values("venta").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))[0]["total_definitivo"]
                    Venta.objects.filter(id=pk).update(
                        neto_pagar=total
                    )
                else:
                    total=0
                
                detalle_id = form.cleaned_data.get('id')
                messages.success(request, f'Correcto! el registro detalle de venta {detalle_id} ha sido guardado exitosamente.', pk)
                return redirect('contabilidad-tabladetalleventa', pk)
            else:
                anterior=DetalleVenta.objects.filter(venta_id=pk,producto=producto.POST['producto'])
                
                DetalleVenta.objects.filter(venta_id=pk,producto=request.POST['producto']).update(
                    cantidad_detalle=anterior[0].cantidad_detalle + form.cleaned_data.get('cantidad_detalle'),
                    total=anterior[0].total + producto.precio * form.cleaned_data.get('cantidad_detalle'),
                )
                
                if (DetalleVenta.objects.filter(venta_id=venta_u.id).values("venta").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))):
                    total=DetalleVenta.objects.filter(venta_id=venta_u.id).values("venta").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))[0]["total_definitivo"]
                    Venta.objects.filter(id=pk).update(
                        neto_pagar=total
                    )
                else:
                    total=0
                
                
    else:
        form = DetalleVentaForm ()
    context={
        "titulo_pagina":titulo_pagina,
        "titulo_modal":titulo_modal,
        "detalles":detalles,
        "form":form,
        "venta":venta_u,
        "total": total
    }
    return render (request, "contabilidad/detalleventa.html", context)


# def detalle_venta(request, pk):
#     titulo_pagina="Venta"
#     detalles=DetalleVenta.objects.filter(venta_id=pk)
#     venta_u= Venta.objects.get(id=pk)
    
#     if (DetalleVenta.objects.filter(venta_id=venta_u.id).values("venta").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))):
#         total=DetalleVenta.objects.filter(venta_id=venta_u.id).values("venta").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))[0]["total_definitivo"]
#     else:
#         total=0
        
#     if request.method == 'POST':
#         form =DetalleVentaForm(request.POST)
#         if form.is_valid():
#             producto= Producto.objects.get(id=request.POST['producto'])
#             existe= DetalleVenta.objects.filter(venta=pk,producto=producto)
#             if len(existe) == 0:
#                 venta=DetalleVenta.objects.create(
#                     producto=form.cleaned_data.get('producto'),
#                     cantidad_detalle=form.cleaned_data.get('cantidad_detalle'),
#                     metodo=form.cleaned_data.get('metodo'),
#                     venta=venta_u,
#                 )
                
#                 if (DetalleVenta.objects.filter(venta_id=venta_u.id).values("venta").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))):
#                     total=DetalleVenta.objects.filter(venta_id=venta_u.id).values("venta").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))[0]["total_definitivo"]
#                     Venta.objects.filter(id=pk).update(
#                         neto_pagar=total
#                     )
#                 else:
#                     total=0
                
#                 detalle_id = form.cleaned_data.get('id')
#                 messages.success(request, f'Correcto! el registro detalle de venta {detalle_id} ha sido guardado exitosamente.', pk)
#                 return redirect('contabilidad-tabladetalleventa', pk)
#             else:
#                 anterior=DetalleVenta.objects.filter(venta_id=pk,producto=producto.POST['producto'])
                
#                 DetalleVenta.objects.filter(venta_id=pk,producto=request.POST['producto']).update(
#                     cantidad_detalle=anterior[0].cantidad_detalle + form.cleaned_data.get('cantidad_detalle'),
#                     total=anterior[0].total + producto.precio * form.cleaned_data.get('cantidad_detalle'),
#                 )
                
#                 if (DetalleVenta.objects.filter(venta_id=venta_u.id).values("venta").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))):
#                     total=DetalleVenta.objects.filter(venta_id=venta_u.id).values("venta").annotate(total_definitivo=Sum(('total'),output_field=models.IntegerField()))[0]["total_definitivo"]
#                     Venta.objects.filter(id=pk).update(
#                         neto_pagar=total
#                     )
#                 else:
#                     total=0
                
                
#     else:
#         form = DetalleVentaForm ()
#     context={
#         "titulo_pagina":titulo_pagina,
#         "detalles":detalles,
#         "form":form,
#         "venta":venta_u,
#         "total": total
#     }
#     return render (request, "contabilidad/detalleventa.html", context)

def tdetallev(request, pk):
    titulo_pagina="Venta"
    detalles=DetalleVenta.objects.filter(venta_id=pk)
    venta_u=Venta.objects.get(id=pk)
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            
            venta=DetalleVenta.objects.create(
                producto=form.cleaned_data.get('producto'),
                cantidad=form.cleaned_data.get('cantidad'),
                metodo=form.cleaned_data.get('metodo'),
                venta_u=venta_u,
            )
            detalle_id = form.cleaned_data.get('id')
            messages.success(request, f'Correcto! el registro detalle de venta {detalle_id} ha sido guardado exitosamente.')
            
    else:
        form = DetalleVentaForm ()
    context={
        "titulo_pagina":titulo_pagina,
        "detalles":detalles,
        "form":form,
        "venta":venta_u,
    }
    return render (request, "contabilidad/tabladetalleventa.html", context)

def detallev_eliminar (request, pk):
    titulo_pagina='Venta'
    u_detalles= DetalleVenta.objects.get(id=pk)
    venta_u= u_detalles.venta
    detalles=DetalleVenta.objects.filter(venta_id=venta_u.id)
    accion_txt= f"¿Está seguro de eliminar el detalle de venta {u_detalles.id}?"
    
    if request.method == 'POST':
        form= DetalleVentaForm(request.POST)
        u_detalles.delete()
        messages.success(request, f'El detalle de venta se eliminó correctamente!')
        return redirect ('contabilidad-tabladetalleventa', venta_u.id)
    else:
        form=DetalleVentaForm ()
        
    context={
        "titulo_pagina":titulo_pagina,
        "accion_txt":accion_txt,
        "detalles":detalles,
        "venta":venta_u,
        "form":form
    }
    return render (request, "contabilidad/detalle-eliminarventa.html", context)


def estado_detallev(request, pk, estado):
    titulo_pagina="Compra"
    tventas = Venta.objects.all()
    tventa = Venta.objects.get(id=pk)
    eliminacion=DetalleVenta.objects.filter(venta=tventa)
    estado_msj=""
    estado_txt=""
    if estado == "Abierta":
        if not eliminacion.exists():
            estado_txt= "Sí"
            estado_msj= f"¿Está seguro de eliminar la venta {tventa.id}?"
            if request.method =='POST':
                form = DetalleVentaForm(request.POST)
                
                tventa.delete()
                messages.success(request,f'Venta {pk} se eliminó correctamente!')
                return redirect('contabilidad-venta')
            else:
                form=DetalleVentaForm()
        else:
            messages.error(request,f'Venta {pk} no se eliminó correctamente!')
            return redirect('contabilidad-venta')
    elif estado=="Cerrada":
        titulo_modal="Anular venta"
        
        estado_txt="Sí"
        estado_msj=f"¿Está seguro de anular la venta {tventa.id}?"
        if request.method == 'POST':
            form = DetalleVentaForm (request.POST)
            Venta.objects.filter(id=pk).update(
                        estado='Anulada'
                    )
            messages.success(request,f'Venta {tventa.id} se anuló correctamente!')
            return redirect('contabilidad-venta')
        else:
            form=DetalleVentaForm()
    else:
        titulo_modal="Cerrar venta"
        estado_txt="Sí"
        estado_msj=f"¿Está seguro de cerrar la venta {tventa.id}?"
        if request.method == 'POST':
            form = DetalleVentaForm (request.POST)
            Venta.objects.filter(id=pk).update(
                        estado='Cerrada'
                    )
            messages.success(request,f'Venta {tventa.id} se cerró correctamente!')
            return redirect('contabilidad-venta')
        else:
            form=DetalleVentaForm()
    context={
        "titulo_pagina":titulo_pagina,
        "tcompras":tventas,
        "estado_msj":estado_msj,
        "estado_txt":estado_txt,
        "form":form,
        "titulo_modal":titulo_modal
    }
    return render(request, "contabilidad/estadoventa.html", context)


def ver_venta (request, pk):
    titulo_pagina="Venta"
    venta=Venta.objects.get(id=pk)
    detalles= DetalleVenta.objects.filter(venta_id=pk)
    print(detalles)
    context={
        "titulo_pagina":titulo_pagina,
        "venta":venta,
        "detalles": detalles
        }     
        
    return render (request, "contabilidad/verventa.html", context)

