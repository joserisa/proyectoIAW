from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from typing import List
from django.views.generic import ListView, DetailView
from .models import Gimnasio, Usuario, Curso, Unidad
#Alta, Apuntado

class GimnasioListView(ListView):
    model = Gimnasio
    queryset = Gimnasio.objects.all()
    context_object_name = 'gimnasio_list'

class UsuarioListView(ListView):
    model = Usuario
    queryset = Usuario.objects.all()
    context_object_name = 'usuario_list'

class CursoListView(ListView):
    model = Curso
    queryset = Curso.objects.all()
    context_object_name = 'curso_list'

class UnidadListView(ListView):
    model = Unidad
    queryset = Unidad.objects.all()
    context_object_name = 'unidad_list'

"""class AltaListView(ListView):
    model = Alta
    queryset = Alta.objects.all()
    context_object_name = 'alta_list'

class ApuntadoListView(ListView):
    model = Apuntado
    queryset = Apuntado.objects.all()
    context_object_name = 'apuntado_list'
"""
#-----------------------------------
class GimnasioDetailView(DetailView):
    model = Gimnasio
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gimnasio_list'] = Gimnasio.objects.all()
        return context

class UsuarioDetailView(DetailView):
    model = Usuario
    context_object_name = 'usuario'
    queryset = Usuario.objects.all()

class CursoDetailView(DetailView):
    model = Curso
    context_object_name = 'curso'
    queryset = Curso.objects.all()

class UnidadDetailView(DetailView):
    model = Unidad
    context_object_name = 'unidad'
    queryset = Unidad.objects.all()

"""class AltaDetailView(DetailView):
    model = Alta
    context_object_name = 'alta'
    queryset = Alta.objects.all()

class ApuntadoDetailView(DetailView):
    model = Apuntado
    context_object_name = 'apuntado'
    queryset = Apuntado.objects.all()
"""
# Create your views here.
