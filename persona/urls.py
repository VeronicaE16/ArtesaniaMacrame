from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from persona.views import proveedor, usuario, cliente, usuario_editar, usuario_eliminar, proveedor_editar, proveedor_eliminar, cliente_editar, cliente_eliminar, ver_usuario, ver_cliente, ver_proveedor

urlpatterns = [
    path('proveedor/', login_required(proveedor), name= 'persona-proveedor'),
    path('proveedor/ver/<int:pk>/', ver_proveedor, name= 'persona-verproveedor'),
    path('proveedor/editar/<int:pk>/', proveedor_editar, name='persona-proveedor-editar'),
    path('proveedor/eliminar/<int:pk>/', proveedor_eliminar, name='persona-proveedor-eliminar'),
    path('usuario/', login_required(usuario), name= 'persona-usuario'),
    path('usuario/ver/<int:pk>/', ver_usuario, name= 'persona-verusuario'),
    path('usuario/editar/<int:pk>/', usuario_editar, name='persona-usuario-editar'),
    path('usuario/eliminar/<int:pk>/', usuario_eliminar, name='persona-usuario-eliminar'),
    path('cliente/', login_required(cliente), name= 'persona-cliente'),
    path('cliente/ver/<int:pk>/', ver_cliente, name= 'persona-vercliente'),
    path('cliente/editar/<int:pk>/', cliente_editar, name='persona-cliente-editar'),
    path('cliente/eliminar/<int:pk>/', cliente_eliminar, name='persona-cliente-eliminar'),

    # Logueo
    path('iniciosesion/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='usuario-login'),
]
