from django import forms
from .models import Usuario
from .models import Respuesta

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = [
		'dui',
		'nombre',
		'apellidos',
		'edad',
		'domicilio',
		'sexo',
		'tipo_transporte',
		'departamento',
		'municipio'
		]

		labels = {
		'dui' : 'Documento de Identidad',
		'nombre' : 'Nombres',
		'apellidos' :'Apellidos',
		'edad' : 'Edad',
		'domicilio' : 'Domicilio',
		'sexo' : 'Sexo',
		'tipo_transporte' : 'Tipo de Transporte' ,
		'departamento' : 'Departamento',
		'municipio' : 'Municipio',
		}

		widgets = {
			'dui':forms.TextInput(attrs={'placeholder': "ingrese su número de DUI",'class':'form-control'}),
			'nombre':forms.TextInput(attrs={'placeholder': "ingrese sus nombres",'class':'form-control'}),
			'apellidos':forms.TextInput(attrs={'placeholder': "ingrese sus apellidos",'class':'form-control'}),
			'edad':forms.NumberInput(attrs={'placeholder': "ingrese su edad",'class':'form-control'}),
			'domicilio':forms.TextInput(attrs={'placeholder': "ingrese su dirección completa ",'class':'form-control'}),
			'sexo':forms.Select(attrs={'class':'form-control'}),
			'tipo_transporte':forms.Select(attrs={'class':'form-control'}),
			'departamento':forms.Select(attrs={'class':'form-control'}),
			'municipio':forms.Select(attrs={'class':'form-control'}),
		}
		

class RespuestaForm(forms.ModelForm):
	class Meta:
		model = Respuesta
		fields = [
		'dui',
		'idrespuesta',
		'numerodepregunta'
		]