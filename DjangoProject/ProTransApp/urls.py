
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from django.conf.urls import include, url
from .views import Inicio,UsuarioCrear,Encuesta,loginT,logoutT,ListaUsuario,mantenerUsuario

#login_required()
urlpatterns = [
  path('', Inicio.as_view(), name = 'inicio'),
  path('accounts/login/', loginT, name = 'login'),
  path('logout/', logoutT, name = 'logout'),
  path('CrearUsuario/', UsuarioCrear.as_view(), name= 'crear_usuario'),
  path('encuestados/', ListaUsuario.as_view(), name= 'listado_usuario'),
  path('LlenarEncuesta/', Encuesta, name= 'llenar_e'),
  path('verUsuario/<iD>',mantenerUsuario , name= 'ver_usu'),
  #path('CrearUs/', UsuarioC, name= 'usuario_crear'),
  #path('CrearUsuario/Seleccionar', SeleccionarTransporte.as_view(), name= 'seleccionar'),
 
    
]
