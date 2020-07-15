
from django.urls import path
from django.views.generic.base import RedirectView
from django.conf.urls import include, url
from .views import Inicio,UsuarioCrear,Encuesta,loginT,logoutT


urlpatterns = [
  path('', Inicio.as_view(), name = 'inicio'),
  path('login/', loginT, name = 'login'),
  path('logout/', logoutT, name = 'logout'),
  path('CrearUsuario/', UsuarioCrear.as_view(), name= 'crear_usuario'),
  path('LlenarEncuesta/', Encuesta, name= 'llenar_e'),
  #path('CrearUs/', UsuarioC, name= 'usuario_crear'),
  #path('CrearUsuario/Seleccionar', SeleccionarTransporte.as_view(), name= 'seleccionar'),
 
    
]
