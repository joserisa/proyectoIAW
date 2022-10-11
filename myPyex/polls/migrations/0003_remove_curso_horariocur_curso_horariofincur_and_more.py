# Generated by Django 4.1.2 on 2022-10-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_curso_horariocur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='horarioCur',
        ),
        migrations.AddField(
            model_name='curso',
            name='horarioFinCur',
            field=models.TimeField(default='20:00', max_length=50),
        ),
        migrations.AddField(
            model_name='curso',
            name='horarioIniCur',
            field=models.TimeField(default='20:00', max_length=50),
        ),
        migrations.AlterField(
            model_name='gimnasio',
            name='correoGym',
            field=models.EmailField(max_length=50),
        ),
    ]
