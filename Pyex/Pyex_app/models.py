from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

class Gimnasio(models.Model):
    #codGym = models.IntegerField(primary_key=True)
    nomGym = models.CharField('Nombre del gimnasio', max_length=50)
    direccionGym =models.CharField('Dirección', max_length=200)
    telefonoGym = models.CharField('Teléfono', max_length=9)
    correoGym = models.EmailField('email', max_length=50)
    fotoGym = models.ImageField('Foto del Gimnasio', height_field=None, width_field=None, max_length=100, upload_to ='fotgym', blank=True)
    def __str__(self):
        return self.nomGym
    def get_absolute_url(self):
        return reverse('gimnasio-detail', kwargs={'pk': self.pk})

class Unidad(models.Model):
    #codUn = models.IntegerField(primary_key=True)
    nomUn = models.CharField('Unidad de ejercicio', max_length=50)
    estadoUn = models.BooleanField('Estado de la unidad')
    gimnasioUn = models.ForeignKey(Gimnasio, on_delete=models.CASCADE)
    aforoUn = models.IntegerField('Aforo actual')
    aforoMaxUn = models.CharField('Aforo máximo', max_length=2)
    def __str__(self):
        return self.nomUn
    def get_absolute_url(self):
        return reverse('unidad-detail', kwargs={'pk': self.pk})

class Curso(models.Model):
    #codCur = models.IntegerField(primary_key=True)
    nomCur = models.CharField('Nombre', max_length=50)
    profesorCur = models.CharField('Profesor que imparte el curso', max_length=50)
    horarioIniCur = models.TimeField('Horario de inicio', max_length=50, default='20:00')
    horarioFinCur = models.TimeField('Horario de fin', max_length=50, default='20:00')
    grupoCur = models.CharField('Grupo', max_length=50)
    gimnasioCur = models.ForeignKey(Gimnasio, on_delete=models.CASCADE)
    descCur = models.CharField('Descripción', max_length=200)
    capCur = models.IntegerField('Aforo actual')
    capMaxCur = models.CharField('Capacidad máxima', max_length=2)
    def __str__(self):
        return self.nomCur
    def get_absolute_url(self):
        return reverse('curso-detail', kwargs={'pk': self.pk})

"""class Usuario(models.Model):
    
    #idUs = models.IntegerField(primary_key=True) ESTE CAMPO ES INUTIL PORQUE DJANGO LO HACE POR MI, CON TODOS LOS ID Y COD IGUAL
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Hombre = 'H'
    Mujer = 'M'
    No_binario = 'NB'
    codUs = models.CharField(max_length=15)
    sexos = [(Hombre, 'Hombre'),(Mujer, 'Mujer'),(No_binario, 'No binario'),]
    sexUs = models.CharField(max_length=3, choices=sexos)
    fechanacUs = models.DateField()
    telefonoUs= models.CharField(max_length = 9)
    fotoUs = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    pagoUs = models.BooleanField()
    tarjetaUs = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    apuntados = models.ManyToManyField(Curso)
    def __str__(self):
        return self.codUs
    def get_absolute_url(self):
        return reverse('usuario-detail', kwargs={'pk': self.pk})"""

class User(AbstractUser):
    #idUs = models.IntegerField(primary_key=True) ESTE CAMPO ES INUTIL PORQUE DJANGO LO HACE POR MI, CON TODOS LOS ID Y COD IGUAL
    Hombre = 'H'
    Mujer = 'M'
    No_binario = 'NB'
    codUs = models.CharField('Codigo', max_length=15)
    sexos = [(Hombre, 'Hombre'),(Mujer, 'Mujer'),(No_binario, 'No binario'),]
    sexUs = models.CharField('Sexo', max_length=3, choices=sexos)
    fechanacUs = models.DateField('Fecha nacimiento', null=True, blank=True)
    telefonoUs= models.CharField('Telefono', max_length = 9, blank=True)
    fotoUs = models.ImageField('Foto de usuario', upload_to='fotus', height_field=None, width_field=None, max_length=100, blank=True)
    pagoUs = models.BooleanField('Pagado', null=True, blank=True)
    tarjetaUs = models.ImageField('Tarjeta QR', upload_to='fotus', height_field=None, width_field=None, max_length=100, blank=True)
    apuntados = models.ManyToManyField(Curso, blank=True)
    ocupados = models.ManyToManyField(Unidad, blank=True)
    def get_absolute_url(self):
        return reverse('usuario-detail', kwargs={'pk': self.pk})
