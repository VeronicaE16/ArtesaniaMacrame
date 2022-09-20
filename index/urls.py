"""index URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from index.views import backup, creditos, index, inicio, ayuda
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', index, name="index"),
    path ('inicio/',login_required (inicio), name="inicio"),
    path ('creditos/', creditos, name="creditos"),
    path ('ayuda/',login_required (ayuda), name="ayuda"),
    path ('persona/', include('persona.urls')),
    path ('control/', include('control.urls')),
    path ('user/', include('users.urls')),
    path ('contabilidad/', include('contabilidad.urls')),
    path('copiaseguridad/<str:tipo>/', backup , name="backup"),
    # Logueo
    path('iniciarsesion/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='usuario-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='usuario-logout'),
    
    # Password
    path('password/reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',html_email_template_name='registration/password_reset_email.html'),
        name='password_reset'),
    path('password/reset/hecho/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    path('password/reset/confirmar/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password/reset/completo/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),
    path('password/reset/completo/',auth_views.PasswordResetCompleteView.as_view(template_name='usuarios/login.html'),
        name='password_reset_complete')
]+static(
    settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT)
