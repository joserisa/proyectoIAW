# Generated by Django 4.1.2 on 2022-10-31 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_user_fechanacus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pagoUs',
            field=models.BooleanField(null=True),
        ),
    ]
