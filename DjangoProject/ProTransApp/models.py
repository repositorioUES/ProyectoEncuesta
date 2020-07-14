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
	tipo_transporte = models.ForeignKey('Tipo_transporte', models.DO_NOTHING, db_column='tipo_transporte')

	def __str__(self):
		return self.nombre

#Tabla Tipo_transporte
class Tipo_transporte (models.Model):
	tipo_transporte = models.AutoField(primary_key = True)
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

class Reclamo(models.Model):
    idreclamo = models.AutoField(primary_key=True)
    dui = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='dui')
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'reclamo'


class Respuesta(models.Model):
    idrespuesta = models.AutoField(primary_key=True)
    #idreclamo = models.ForeignKey(Reclamo, models.DO_NOTHING, db_column='idreclamo', blank=True, null=True)
    dui = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='dui')
    numerodepregunta = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'respuesta'

