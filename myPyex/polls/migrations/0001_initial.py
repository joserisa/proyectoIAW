# Generated by Django 4.1.2 on 2022-10-24 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCur', models.CharField(max_length=50)),
                ('profesorCur', models.CharField(max_length=50)),
                ('horarioIniCur', models.TimeField(default='20:00', max_length=50)),
                ('horarioFinCur', models.TimeField(default='20:00', max_length=50)),
                ('grupoCur', models.CharField(max_length=50)),
                ('descCur', models.CharField(max_length=200)),
                ('capCur', models.IntegerField()),
                ('capMaxCur', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Gimnasio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomGym', models.CharField(max_length=50)),
                ('direccionGym', models.CharField(max_length=200)),
                ('telefonoGym', models.CharField(max_length=9)),
                ('correoGym', models.EmailField(max_length=50)),
                ('fotoGym', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codUs', models.CharField(max_length=15)),
                ('sexUs', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('NB', 'No binario')], max_length=3)),
                ('fechanacUs', models.DateField()),
                ('telefonoUs', models.CharField(max_length=9)),
                ('fotoUs', models.ImageField(upload_to=None)),
                ('pagoUs', models.BooleanField()),
                ('tarjetaUs', models.ImageField(upload_to=None)),
                ('apuntados', models.ManyToManyField(to='polls.curso')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomUn', models.CharField(max_length=50)),
                ('estadoUn', models.BooleanField()),
                ('aforoUn', models.IntegerField()),
                ('aforoMaxUn', models.CharField(max_length=2)),
                ('gimnasioUn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.gimnasio')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='gimnasioCur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.gimnasio'),
        ),
    ]
