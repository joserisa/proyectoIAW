from django.contrib.auth.models import Group
from Pyex_app.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import BadHeaderError, send_mail

@receiver(user_logged_in)
def log_user_loggin(sender, user, **kwargs):
    try:
        u = User.objects.get(username=user)
        g = Group.objects.get(name='Bloggers')
        c = User.objects.get(username=user).email
        if g in u.groups.all():
            print(f"{u.username} ya pertenece al grupo.")

        else:
            print(f"{u.username} no pertenece al grupo. Añadiendo...")
            u.groups.add(g)
            send_mail(
                'Grupo Bloggers',
                'Hola {u.username}. Te hemos añadido al grupo Bloggers, ahora puedes subir tus publicaciones, saludos.',
                'xemoso93@gmail.com',
                [c],
                fail_silently=False,
            )
    except:
        print("El usuario introducido no existe")