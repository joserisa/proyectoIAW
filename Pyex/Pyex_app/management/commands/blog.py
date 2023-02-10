from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from django.contrib.auth.signals import user_logged_in
from Pyex_app.models import User

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('usuario', type=str, help='Introduce el usuario a meter en Bloggers')

    def handle(self, *args, **kwargs):
        try:
            nombre = kwargs['usuario']
            u = User.objects.get(username=nombre)
            g = Group.objects.get(name='Bloggers')
            if g in u.groups.all():
                print(f"{u.username} ya pertenece al grupo.")

            else:
                print(f"{u.username} no pertenece al grupo. Añadiendo...")
                u.groups.add(g)
        except:
            print("El usuario introducido no existe")