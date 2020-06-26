from django.db import models

# Create your models here.

#Tabla Usuario
class Usuario(models.Model):
	dui = models.CharField(primary_key = True, max_length = 10)
	nombre = models.CharField(max_length = 30)
	apellidos = models.CharField(max_length = 30)
	edad = models.IntegerField()
	sexo = models.CharField(max_length = 10)
	domicilio = models.CharField(max_length = 50)

	def __str__(self):
		return self.nombre

#Tabla Tipo_transporte
class Tipo_transporte (models.Model):
	id = models.AutoField(primary_key = True)
	tipoTransporte = models.CharField(max_length = 20)

	def __str__(self):
		return self.tipoTransporte

#Tabla Departamento
class Departamento(models.Model):
	idDepartamento = models.AutoField(primary_key = True)
	nombreDepartamento = models.CharField(max_length = 20)

	def __str__(self):
		return self.nombreDepartamento

#Tabla Municipio
class Municipio(models.Model):
	idMunicipio = models.AutoField(primary_key = True)
	nombreMunicipio = models.CharField(max_length = 20)
	departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)

	def __str__(self):
		return self.nombreMunicipio

	

	
