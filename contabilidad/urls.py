from django.urls import path
from django.contrib.auth.decorators import login_required
from contabilidad.views import detalle_eliminar, detalle_venta, reporte_venta, reportes, venta, compra, detalle_compra, tdetalle, estado_detalle, ver_compra, estado_detallev, detallev_eliminar, tdetallev, ver_venta

urlpatterns = [
    path('venta/',login_required (venta), name= 'contabilidad-venta'),
    path('venta/detalle/<int:pk>/', detalle_venta, name='contabilidad-detalleventa'),
    
    path('venta/tabladetalle/<int:pk>/', tdetallev, name='contabilidad-tabladetalleventa'),
    
    path('venta/tabladetalle/<int:pk>/<str:estado>/', estado_detallev, name='contabilidad-estadoventa'),
    #path('tabladetalle/<int:pk>/', compra_cerrar, name='contabilidad-estadocompra'),
    
    #path('venta/tabladetalle/eliminar/<int:pk>/<str:estado>/', estado_detallev, name='contabilidad-eliminar-detalle'),
    path('venta/ver/<int:pk>/', ver_venta, name= 'contabilidad-verventa'),
    path('venta/eliminar-detalle/<int:pk>/', detallev_eliminar, name= 'detallev-eliminar'),
    path('venta/reporte/', reportes, name= 'contabilidad-reporte-venta'),


#-------------------------------COMPRA---------------------------

    path('compra/',login_required (compra), name= 'contabilidad-compra'),
    path('compra/detalle/<int:pk>/', detalle_compra, name='contabilidad-detallecompra'),
    
    path('compra/tabladetalle/<int:pk>/', tdetalle, name='contabilidad-tabladetalle'),
    
    path('compra/tabladetalle/<int:pk>/<str:estado>/', estado_detalle, name='contabilidad-estadocompra'),
    #path('tabladetalle/<int:pk>/', compra_cerrar, name='contabilidad-estadocompra'),
    
    #path('compra/tabladetalle/eliminar/<int:pk>/<str:estado>/', estado_detalle, name='contabilidad-eliminar-detalle'),
    path('compra/ver/<int:pk>/', ver_compra, name= 'contabilidad-vercompra'),
    path('compra/eliminar-detalle/<int:pk>/', detalle_eliminar, name= 'detalle-eliminar'),
]
