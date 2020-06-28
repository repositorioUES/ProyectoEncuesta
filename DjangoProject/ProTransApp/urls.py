
from django.urls import path
from .views import home, CrearUsuario


urlpatterns = [
   path('', home, name='home'),
  
    
]
