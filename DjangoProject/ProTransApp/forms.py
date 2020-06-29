from django import forms
from .models import Usuario

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
		'dui' : 'Documento de Identidad',
		'nombre' : 'Nombres',
		'apellidos' :'Apellidos',
		'edad' : 'Edad',
		'sexo' : 'Sexo',
		'domicilio' : 'Domicilio',
		}

		widgets = {
			'dui':forms.TextInput(attrs={'placeholder': "ingrese su número de DUI",'class':'form-control'}),
			'nombre':forms.TextInput(attrs={'placeholder': "ingrese sus nombres",'class':'form-control'}),
			'apellidos':forms.TextInput(attrs={'placeholder': "ingrese sus apellidos",'class':'form-control'}),
			'edad':forms.NumberInput(attrs={'placeholder': "ingrese su edad",'class':'form-control'}),
			'sexo':forms.TextInput(attrs={'placeholder': "ingrese Femenino o Masculino",'class':'form-control'}),
			'domicilio':forms.TextInput(attrs={'placeholder': "ingrese su dirección completa ",'class':'form-control'}),
		}
		