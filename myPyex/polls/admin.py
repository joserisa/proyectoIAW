from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from polls.models import *
#from .models import Apuntado
#from .models import Alta

admin.site.register(User)
admin.site.register(Gimnasio)
admin.site.register(Curso)
admin.site.register(Unidad)
#admin.site.register(Apuntado)
#admin.site.register(Alta)
# Register your models here.