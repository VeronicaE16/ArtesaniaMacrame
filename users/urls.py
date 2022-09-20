from django.urls import path
from users.views import registrar
from .import views


urlpatterns = [
    path('registrarse/', registrar, name='users-registrar')
]