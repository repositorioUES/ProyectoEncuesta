
from django.urls import path
from .views import Inicio,UsuarioCrear

urlpatterns = [
  path('', Inicio.as_view(), name = 'inicio'),
  path('CrearUsuario/', UsuarioCrear.as_view(), name= 'crear_usuario'),
  #path('CrearUsuario/Seleccionar', SeleccionarTransporte.as_view(), name= 'seleccionar'),
    
]
