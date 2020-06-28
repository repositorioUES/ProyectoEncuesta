
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from ProTransApp.models import Usuario
from ProTransApp.forms import UsuarioForm
from django.views import generic

# Create your views here.

def home(request):
	return render(request, 'index.html')

def CrearUsuario(request):
	if request.method == 'POST':
		formulario = UsuarioForm(request.POST)
		if formulario.is_valid():
			formulario.save()
		return redirect('home')
	else:
		formulario = UsuarioForm()

	return render(request, 'CrearUsuario.html', {'formulario':formulario})