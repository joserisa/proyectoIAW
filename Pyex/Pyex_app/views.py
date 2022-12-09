from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import UserForm
from typing import List
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Gimnasio, User, Curso, Unidad
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
#Alta, Apuntado

def index(request):
    return render(request, "Pyex_app/index.html")

class UserListView(ListView):
    model = User
    queryset = User.objects.all()
    context_object_name = 'usuario_list'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class GimnasioListView(ListView):
    model = Gimnasio
    queryset = Gimnasio.objects.all()
    context_object_name = 'gimnasio_list'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
"""class UsuarioListView(ListView):
    model = Usuario
    queryset = Usuario.objects.all()
    context_object_name = 'usuario_list'"""

class CursoListView(ListView):
    model = Curso
    queryset = Curso.objects.all()
    context_object_name = 'curso_list'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
class UnidadListView(ListView):
    model = Unidad
    queryset = Unidad.objects.all()
    context_object_name = 'unidad_list'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
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
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
class UserDetailView(UserPassesTestMixin,DetailView):
    model = User
    context_object_name = 'usuario'
    queryset = User.objects.all()
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

"""class UsuarioDetailView(DetailView):
    model = Usuario
    context_object_name = 'usuario'
    queryset = Usuario.objects.all()"""

class CursoDetailView(DetailView):
    model = Curso
    context_object_name = 'curso'
    queryset = Curso.objects.all()
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class UnidadDetailView(DetailView):
    model = Unidad
    context_object_name = 'unidad'
    queryset = Unidad.objects.all()
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
class GimnasioCreateView(UserPassesTestMixin, CreateView):
    model = Gimnasio
    fields = ['nomGym','direccionGym','telefonoGym','correoGym','fotoGym']
    success_url = reverse_lazy('gimnasio')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
class GimnasioUpdateView(UserPassesTestMixin, UpdateView):
    model = Gimnasio
    fields = ['nomGym','direccionGym','telefonoGym','correoGym','fotoGym']
    success_url = reverse_lazy('gimnasio')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
class GimnasioDeleteView(UserPassesTestMixin, DeleteView):
    model = Gimnasio
    success_url = reverse_lazy('gimnasio')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
#--------------------------------------------------
class CursoCreateView(UserPassesTestMixin, CreateView):
    model = Curso
    fields = ['nomCur','profesorCur','horarioIniCur','horarioFinCur','grupoCur','gimnasioCur','descCur','capCur','capMaxCur']
    success_url = reverse_lazy('curso')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
class CursoUpdateView(UserPassesTestMixin, UpdateView):
    model = Curso
    fields = ['nomCur','profesorCur','horarioIniCur','horarioFinCur','grupoCur','gimnasioCur','descCur','capCur','capMaxCur']
    success_url = reverse_lazy('curso')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
class CursoDeleteView(UserPassesTestMixin, DeleteView):
    model = Curso
    success_url = reverse_lazy('curso')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
#---------------------------------------------------------------------------------------------------
class UnidadCreateView(UserPassesTestMixin, CreateView):
    model = Unidad
    fields = ['nomUn','estadoUn','gimnasioUn','aforoUn','aforoMaxUn']
    success_url = reverse_lazy('unidad')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
class UnidadUpdateView(UserPassesTestMixin, UpdateView):
    model = Unidad
    fields = ['nomUn','estadoUn','gimnasioUn','aforoUn','aforoMaxUn']
    success_url = reverse_lazy('unidad')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
class UnidadDeleteView(UserPassesTestMixin, DeleteView):
    model = Unidad
    success_url = reverse_lazy('unidad')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
#-----------------------------------------------------------------------------------------
class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('usuario')

class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = User
    fields = ('username','first_name','last_name','email','codUs','sexUs','fechanacUs','telefonoUs','fotoUs','pagoUs','tarjetaUs','apuntados')
    success_url = reverse_lazy('usuario')
    template_name = "./Pyex_app/user_update_form.html"
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = User
    success_url = reverse_lazy('usuario')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
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
