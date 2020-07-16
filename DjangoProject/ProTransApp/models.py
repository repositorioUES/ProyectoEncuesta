from django.db import models

# Create your models here.

#Tabla Usuario
class Usuario(models.Model):
	dui = models.CharField(primary_key = True, max_length = 10)
	nombre = models.CharField(max_length = 30)
	apellidos = models.CharField(max_length = 30)
	edad = models.IntegerField()
	domicilio = models.CharField(max_length = 50)
	sexos = (('F','Femenino'),('M', 'Masculino'))
	sexo = models.CharField(max_length = 1,choices=sexos)
	tipo_transporte = models.ForeignKey('Tipo_transporte', models.DO_NOTHING)
	departamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='departamento')
	municipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='municipio')

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
	nombreMunicipio = models.CharField(max_length = 50)
	departamentoMun = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='departamentoMun')
	nombreMunicipio = models.CharField(max_length = 20)
	departamento = models.ForeignKey(Departamento, models.DO_NOTHING)

	def __str__(self):
		return self.nombreMunicipio

	class Meta:
		ordering = ["nombreMunicipio"]

class Reclamo(models.Model):
    idreclamo = models.ForeignKey('Usuario', on_delete = models.CASCADE, db_column='dui',primary_key = True)
    realizado = models.BooleanField(null = False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null = False)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'reclamo'


class Respuesta(models.Model):
    idrespuesta = models.AutoField(primary_key=True)
    dui = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='dui')
    numerodepregunta = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'respuesta'


	
