from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ProTransApp.models import Usuario

#Formulario para crear usuario
class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario

		fields = [
			'dui',
			'nombre',
			'apellidos',
			'edad',
			'sexo',
			'domicilio',
		]

		labels = {
			'dui':'DUI',
			'nombre':'Nombre',
			'apellido':'Apellido',
			'edad':'edad',
			'sexo':'sexo',
			'domicilio':'domicilio',
		}

		widgets = {
			'dui':forms.TextInput(attrs={'class':'form-control'}),
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellido':forms.TextInput(attrs={'class':'form-control'}),
			'edad':forms.TextInput(attrs={'class':'form-control'}),
			'sexo':forms.TextInput(attrs={'class':'form-control'}),
			'domicilo':forms.TextInput(attrs={'class':'form-control'}),
		}
