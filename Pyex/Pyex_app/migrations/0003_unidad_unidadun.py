# Generated by Django 4.1.3 on 2023-01-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pyex_app', '0002_alter_unidad_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidad',
            name='unidadUn',
            field=models.CharField(blank=True, max_length=75),
        ),
    ]
