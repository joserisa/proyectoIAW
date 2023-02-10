from django.contrib.auth.models import Group
from Pyex_app.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def log_user_loggin(sender, user, **kwargs):
    try:
        u = User.objects.get(username=user)
        g = Group.objects.get(name='Bloggers')
        if g in u.groups.all():
            print(f"{u.username} ya pertenece al grupo.")

        else:
            print(f"{u.username} no pertenece al grupo. Añadiendo...")
            u.groups.add(g)
    except:
        print("El usuario introducido no existe")