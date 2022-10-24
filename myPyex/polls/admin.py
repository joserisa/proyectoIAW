from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from polls.models import Usuario

from .models import Usuario
from .models import Gimnasio
from .models import Curso
from .models import Unidad
#from .models import Apuntado
#from .models import Alta

admin.site.register(Usuario)
admin.site.register(Gimnasio)
admin.site.register(Curso)
admin.site.register(Unidad)
#admin.site.register(Apuntado)
#admin.site.register(Alta)
# Register your models here.
class UsuarioInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'usuario'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UsuarioInline,)
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)