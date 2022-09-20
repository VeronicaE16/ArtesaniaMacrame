from django.template import loader
from django.shortcuts import redirect,render
from django.template import Template, Context
from django.http import HttpResponse
from contabilidad.models import DetalleVenta
from control.models import Producto
from index.models import Backup
from index.forms import BackupForm
from datetime import date
import os


def tablaProveedor (request):
    plt= loader.get_template("proveedor.html")
    doc=plt.render()
    return HttpResponse(doc)

def tablaProducto (request):
    plt= loader.get_template("producto.html")
    doc=plt.render()
    return HttpResponse(doc)

def tablaUsuario (request):
    plt= loader.get_template("usuario.html")
    doc=plt.render()
    return HttpResponse(doc)

def tablaVenta (request):
    plt= loader.get_template("venta.html")
    doc=plt.render()
    return HttpResponse(doc)


def inicio(request):
    
    titulo_pagina="Inicio"
    context={
       
        'titulo_pagina':titulo_pagina
    }
    return render(request,'inicio.html',context)

def creditos(request):
    
    titulo_pagina="Creditos"
    context={
       
        'titulo_pagina':titulo_pagina
    }
    return render(request,'creditos.html',context)
    
def index(request):
    
    titulo_pagina="Index"
    context={
       
        'titulo_pagina':titulo_pagina
    }
    return render(request,'INDEX.html',context)

def ayuda(request):
    action_txt="/inicio"
    titulo_pagina="Ayuda"
    context={
        'action_txt':action_txt,
        'titulo_pagina':titulo_pagina
    }
    return render(request,'ayuda.html',context)




def exportar_datos():
    fecha=date.today()
    os.system(f"mysqldump --add-drop-table --column-statistics=0 -u root --password=Johanasoler20* proyartmacrame> static/backup/BKP_{fecha}.sql")
   

def importar_datos(archivo):
    try:
        os.system(f"mysql -u root --password=Johanasoler20* proyartmacrame < {archivo[1:]}")
    except:
        print("Problemas al importar")





def backup(request,tipo):
    titulo_pagina="Copia de Seguridad"
    ejemplo_dir = 'static/backup/'
    with os.scandir(ejemplo_dir) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
    print(ficheros)
    filtrado=[]
    backups = Backup.objects.all()
    if request.method == 'POST' and tipo== "U":
        # Fetching the form data
        
        form = BackupForm(request.POST, request.FILES)
        if form.is_valid():
            nombre= request.POST['nombre']
            archivo = request.FILES['archivo']
            
            insert = Backup(nombre=nombre, archivo=archivo)
            insert.save()
            
            importar_datos(insert.archivo.url)
            
            insert = Backup(nombre=nombre, archivo=archivo)
            insert.save()
            
            return redirect('backup','A')
        else:
            print( "Error al procesar el formulario")
              
    elif request.method == 'POST' and tipo== "D":
        exportar_datos()
        return redirect('backup','A')
    
    else:
        form = BackupForm()
      
        
    context ={
        "titulo_pagina":titulo_pagina,
        "ficheros":ficheros,
        "form":form,
        "backups":backups
    }
    return render(request, 'backup.html',context) 
