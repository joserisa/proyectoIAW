from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Gimnasio(models.Model):
    codGym = models.IntegerField(primary_key=True)
    nomGym = models.CharField(max_length=50)
    direccionGym =models.CharField(max_length=200)
    telefonoGym = models.CharField(max_length=9)
    correoGym = models.EmailField(max_length=50)
    fotoGym = models.ImageField(height_field=None, width_field=None, max_length=100, upload_to ='uploads/')

class Unidad(models.Model):
    codUn = models.IntegerField(primary_key=True)
    nomUn = models.CharField(max_length=50)
    estadoUn = models.BooleanField()
    gimnasioUn = models.ForeignKey(Gimnasio, on_delete=models.CASCADE)

class Curso(models.Model):
    codCur = models.IntegerField(primary_key=True)
    nomCur = models.CharField(max_length=50)
    profesorCur = models.CharField(max_length=50)
    horarioIniCur = models.TimeField(max_length=50, default='20:00')
    horarioFinCur = models.TimeField(max_length=50, default='20:00')
    grupoCur = models.CharField(max_length=50)
    gimnasioCur = models.ForeignKey(Gimnasio, on_delete=models.CASCADE)
    descCur = models.CharField(max_length=200)
    capCur = models.IntegerField()
    capMaxCur = models.CharField(max_length=2)

class Usuario(models.Model):
    Hombre = 'H'
    Mujer = 'M'
    No_binario = 'NB'
    codUs = models.CharField(max_length=15, primary_key=True)
    sexos = [(Hombre, 'Hombre'),(Mujer, 'Mujer'),(No_binario, 'No binario'),]
    sexUs = models.CharField(max_length=3, choices=sexos)
    fechanacUs = models.DateField()
    telefonoUs= models.CharField(max_length = 9)
    fotoUs = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    pagoUs = models.BooleanField()
    tarjetaUs = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

class Apuntado(models.Model):
    cursoAp = models.ForeignKey(Curso, on_delete=models.CASCADE)
    usuarioAp = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Alta(models.Model):
    usuarioAl = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    gimnasioAl = models.ForeignKey(Gimnasio, on_delete=models.CASCADE)