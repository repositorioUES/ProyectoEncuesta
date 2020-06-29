from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,CreateView
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

class Inicio(TemplateView):
	template_name = 'index.html'


class UsuarioCrear(CreateView):
	model = Usuario
	form_class = UsuarioForm
	template_name = 'Usuario_Form.html'
	success_url = reverse_lazy('inicio')



