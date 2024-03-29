# Generated by Django 4.1.3 on 2023-01-13 11:25

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCur', models.CharField(max_length=50, verbose_name='Nombre')),
                ('profesorCur', models.CharField(max_length=50, verbose_name='Profesor que imparte el curso')),
                ('horarioIniCur', models.TimeField(default='20:00', max_length=50, verbose_name='Horario de inicio')),
                ('horarioFinCur', models.TimeField(default='20:00', max_length=50, verbose_name='Horario de fin')),
                ('grupoCur', models.CharField(max_length=50, verbose_name='Grupo')),
                ('descCur', models.CharField(max_length=200, verbose_name='Descripción')),
                ('capCur', models.IntegerField(verbose_name='Aforo actual')),
                ('capMaxCur', models.CharField(max_length=2, verbose_name='Capacidad máxima')),
            ],
        ),
        migrations.CreateModel(
            name='Gimnasio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomGym', models.CharField(max_length=50, verbose_name='Nombre del gimnasio')),
                ('direccionGym', models.CharField(max_length=200, verbose_name='Dirección')),
                ('telefonoGym', models.CharField(max_length=9, verbose_name='Teléfono')),
                ('correoGym', models.EmailField(max_length=50, verbose_name='email')),
                ('fotoGym', models.ImageField(blank=True, upload_to='fotgym', verbose_name='Foto del Gimnasio')),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMa', models.CharField(blank=True, max_length=75)),
                ('DescMa', models.CharField(max_length=200, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('codUs', models.CharField(max_length=15, verbose_name='Codigo')),
                ('sexUs', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('NB', 'No binario')], max_length=3, verbose_name='Sexo')),
                ('fechanacUs', models.DateField(blank=True, null=True, verbose_name='Fecha nacimiento')),
                ('telefonoUs', models.CharField(blank=True, max_length=9, verbose_name='Telefono')),
                ('fotoUs', models.ImageField(upload_to='fotus', verbose_name='Foto de usuario')),
                ('pagoUs', models.BooleanField(blank=True, null=True, verbose_name='Pagado')),
                ('tarjetaUs', models.ImageField(upload_to='fotus', verbose_name='Tarjeta QR')),
                ('apuntados', models.ManyToManyField(blank=True, to='Pyex_app.curso')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gimnasioUn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pyex_app.gimnasio')),
                ('maquinaUn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pyex_app.maquina')),
                ('persona', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='gimnasioCur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pyex_app.gimnasio'),
        ),
    ]
