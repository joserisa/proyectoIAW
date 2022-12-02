from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import UserForm
from typing import List
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Gimnasio, User, Curso, Unidad
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.contrib import messages
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
#Alta, Apuntado

def index(request):
    return render(request, "Pyex_app/index.html")

class UserListView(ListView):
    model = User
    queryset = User.objects.all()
    context_object_name = 'usuario_list'

class GimnasioListView(ListView):
    model = Gimnasio
    queryset = Gimnasio.objects.all()
    context_object_name = 'gimnasio_list'

"""class UsuarioListView(ListView):
    model = Usuario
    queryset = Usuario.objects.all()
    context_object_name = 'usuario_list'"""

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

class UserDetailView(DetailView):
    model = User
    context_object_name = 'usuario'
    queryset = User.objects.all()

"""class UsuarioDetailView(DetailView):
    model = Usuario
    context_object_name = 'usuario'
    queryset = Usuario.objects.all()"""

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

#--------------------------------------------------
class GimnasioCreateView(LoginRequiredMixin, CreateView):
    model = Gimnasio
    fields = ['nomGym','direccionGym','telefonoGym','correoGym','fotoGym']
    success_url = reverse_lazy('gimnasio')

class GimnasioUpdateView(LoginRequiredMixin, UpdateView):
    model = Gimnasio
    fields = ['nomGym','direccionGym','telefonoGym','correoGym','fotoGym']
    success_url = reverse_lazy('gimnasio')

class GimnasioDeleteView(LoginRequiredMixin, DeleteView):
    model = Gimnasio
    success_url = reverse_lazy('gimnasio')
#--------------------------------------------------
class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    fields = ['nomCur','profesorCur','horarioIniCur','horarioFinCur','grupoCur','gimnasioCur','descCur','capCur','capMaxCur']
    success_url = reverse_lazy('curso')

class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    fields = ['nomCur','profesorCur','horarioIniCur','horarioFinCur','grupoCur','gimnasioCur','descCur','capCur','capMaxCur']
    success_url = reverse_lazy('curso')

class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = reverse_lazy('curso')
#---------------------------------------------------------------------------------------------------
class UnidadCreateView(LoginRequiredMixin, CreateView):
    model = Unidad
    fields = ['nomUn','estadoUn','gimnasioUn','aforoUn','aforoMaxUn']
    success_url = reverse_lazy('unidad')

class UnidadUpdateView(LoginRequiredMixin, UpdateView):
    model = Unidad
    fields = ['nomUn','estadoUn','gimnasioUn','aforoUn','aforoMaxUn']
    success_url = reverse_lazy('unidad')

class UnidadDeleteView(LoginRequiredMixin, DeleteView):
    model = Unidad
    success_url = reverse_lazy('unidad')
#-----------------------------------------------------------------------------------------
class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('usuario')

class UserUpdateView(UpdateView):
    model = User
    fields = ('username','first_name','last_name','email','codUs','sexUs','fechanacUs','telefonoUs','fotoUs','pagoUs','tarjetaUs','apuntados')
    success_url = reverse_lazy('usuario')
    template_name = "./Pyex_app/user_update_form.html"

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('usuario')
#--------------------------------
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro completo." )
			return redirect("main:home")
		messages.error(request, "Registro no completo. Informacion invalida.")
	form = NewUserForm()
	return render (request=request, template_name="/register.html", context={"register_form":form})
# Create your views here.
