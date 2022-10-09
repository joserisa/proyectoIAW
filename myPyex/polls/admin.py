from django.contrib import admin

from .models import Usuario
from .models import Gimnasio
from .models import Curso
from .models import Unidad
from .models import Apuntado
from .models import Alta

admin.site.register(Usuario)
admin.site.register(Gimnasio)
admin.site.register(Curso)
admin.site.register(Unidad)
admin.site.register(Apuntado)
admin.site.register(Alta)
# Register your models here.
