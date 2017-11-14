from django.db import models
from datetime import datetime
from django.utils import timezone

class Autor(models.Model):
	idautor = models.AutoField(db_column='idAutor', primary_key=True)
	nombreart = models.CharField(db_column='nombreArt', unique=True, max_length=200)
	artpassword = models.CharField(db_column='artPassword', max_length=128)
	nombres = models.CharField(db_column='nombres',max_length=200)
	apellidos = models.CharField(db_column='apellidos', max_length=200)
	email = models.CharField(db_column='email',unique=True, max_length=200)
	class Meta:
		managed = True
		db_table = 'Autor'
		

class Estilo(models.Model):
	idestilo = models.AutoField(db_column='idEstilo', primary_key=True)
	estilo = models.CharField(db_column='estilo', unique=True, max_length=100)
	class Meta:
		managed = True
		db_table = 'Estilo'

class Obra(models.Model):
	idobra = models.AutoField(db_column='idObra', primary_key=True)
	idtipoobra = models.ForeignKey('TipoObra', models.DO_NOTHING, db_column='idtipoobra',related_name='obras_tipo')
	idestilo = models.ForeignKey('Estilo', models.DO_NOTHING, db_column='idestilo',related_name='obras_estilo')
	idautor = models.ForeignKey('Autor', models.DO_NOTHING, db_column='idautor',related_name='obras_autor')
	nombreobra = models.CharField(db_column='nombreObra', max_length=200)
	imgobra = models.ImageField(upload_to='photos')
	fechaobra = models.DateTimeField(db_column='fechaObra',default=timezone.now,blank=True)
	class Meta:
		managed = True
		db_table = 'Obra'

class TipoObra(models.Model):
	idtipoobra = models.AutoField(db_column='idTipoObra', primary_key=True)
	tipoobra = models.CharField(db_column='tipoObra', unique=True, max_length=200)
	class Meta:
		managed = True
		db_table = 'TipoObra'
