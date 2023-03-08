from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import UserForm
from typing import List
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Gimnasio, User, Curso, Unidad, Maquina
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm, Ocupacion,Desocupacion
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail

"""def signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        user = User.objects.create_user(
            username = username,
            password = password,
            email = email
        )
        login(request,user)
        subject='Bienvenido a Pyex'
        message=f'Buenas {user.username}, gracias por tu registro en Pyex, te hemos añadido al grupo Bloggers.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.mail,]
        send_mail(subject,message, email_from, recipient_list)
        return redirect("/index")
    return render(request, "signup.html")"""

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
#Alta, Apuntado

def index(request):
    return render(request, "Pyex_app/index.html")

class search(ListView):
    model = Gimnasio
    template_name="search_results.html"
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list=Gimnasio.objects.filter(Q(nomGym__icontains=query))
        return object_list
#    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
#        try:
#            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
#        except:
#            return False

class UserListView(UserPassesTestMixin,ListView):
    model = User
    queryset = User.objects.all()
    context_object_name = 'usuario_list'
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return self.request.user.is_superuser
        except:
            return False

class GimnasioListView(ListView):
    model = Gimnasio
    queryset = Gimnasio.objects.all()
    context_object_name = 'gimnasio_list'
#    @method_decorator(login_required)
#    def dispatch(self, *args, **kwargs):
#        return super().dispatch(*args, **kwargs)
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

class MaquinaListView(ListView):
    model = Maquina
    queryset = Maquina.objects.all()
    context_object_name = 'maquina_list'
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
        context['unidad_list'] = Unidad.objects.all()
        context['curso_list'] = Curso.objects.all()
        return context
#    @method_decorator(login_required)
#    def dispatch(self, *args, **kwargs):
#        return super().dispatch(*args, **kwargs)
class UserDetailView(UserPassesTestMixin,DetailView):
    model = User
    context_object_name = 'usuario'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unidad_list'] = Unidad.objects.all()
        return context
    queryset = User.objects.all()
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk")) or self.request.user.is_superuser
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

class MaquinaDetailView(DetailView):
    model = Maquina
    context_object_name = 'maquina'
    queryset = Maquina.objects.all()
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UnidadDetailView(DetailView):
    model = Unidad
    context_object_name = 'unidad'
    queryset = Unidad.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estado']= Ocupacion(prefix="estado")
        context['desocupar']= Desocupacion(prefix="desocupar")
        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if "estado" in request.POST:

            form = Ocupacion(request.POST, prefix="estado")
            if "estado-ocupar" in form.data:
                pk=request.META["HTTP_REFERER"].split("/")[4]
                unidad=Unidad.objects.get(pk=int(pk))
                unidad.persona=request.user
                unidad.save()
        if "desocupar" in request.POST:

            form = Desocupacion(request.POST, prefix="desocupar")
            if "desocupar-desocupar" in form.data:
                pk=request.META["HTTP_REFERER"].split("/")[4]
                unidad=Unidad.objects.get(pk=int(pk))
                unidad.persona_id = None
                unidad.save()
            #Unidad.persona = request.user.username
        return self.render_to_response(context)


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
            #return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
            return self.request.user.is_superuser
        except:
            return False
class GimnasioUpdateView(UserPassesTestMixin, UpdateView):
    model = Gimnasio
    fields = ['nomGym','direccionGym','telefonoGym','correoGym','fotoGym']
    success_url = reverse_lazy('gimnasio')
    template_name = "./Pyex_app/gimnasio_update_form.html"
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return self.request.user.is_superuser
        except:
            return False
class GimnasioDeleteView(UserPassesTestMixin, DeleteView):
    model = Gimnasio
    success_url = reverse_lazy('gimnasio')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return self.request.user.is_superuser
        except:
            return False
#--------------------------------------------------
class CursoCreateView(UserPassesTestMixin, CreateView):
    model = Curso
    fields = ['nomCur','profesorCur','horarioIniCur','horarioFinCur','grupoCur','gimnasioCur','descCur','capCur','capMaxCur']
    success_url = reverse_lazy('curso')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return self.request.user.is_superuser
        except:
            return False
class CursoUpdateView(UserPassesTestMixin, UpdateView):
    model = Curso
    fields = ['nomCur','profesorCur','horarioIniCur','horarioFinCur','grupoCur','gimnasioCur','descCur','capCur','capMaxCur']
    success_url = reverse_lazy('curso')
    template_name = "./Pyex_app/curso_update_form.html"
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return self.request.user.is_superuser
        except:
            return False
class CursoDeleteView(UserPassesTestMixin, DeleteView):
    model = Curso
    success_url = reverse_lazy('curso')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return self.request.user.is_superuser
        except:
            return False
#---------------------------------------------------------------------------------------------------
class MaquinaCreateView(UserPassesTestMixin, CreateView):
    model = Maquina
    fields = ['nombreMa','DescMa']
    success_url = reverse_lazy('maquina')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return self.request.user.is_superuser
        except:
            return False
class MaquinaUpdateView(UpdateView):
    model = Unidad
    fields = ['nombreMa','DescMa']
    success_url = reverse_lazy('maquina')
    template_name = "./Pyex_app/maquina_update_form.html"
#   def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
#        try:
#            return self.request.user.is_superuser
#        except:
#            return False
class MaquinaDeleteView(UserPassesTestMixin, DeleteView):
    model = Maquina
    success_url = reverse_lazy('maquina')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return self.request.user.is_superuser
        except:
            return False
#-----------------------------------------------------------------------------------------------------

class UnidadCreateView(UserPassesTestMixin, CreateView):
    model = Unidad
    fields = ['unidadUn','gimnasioUn','maquinaUn','persona']
    success_url = reverse_lazy('unidad')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return self.request.user.is_superuser
        except:
            return False
class UnidadUpdateView(UpdateView):
    model = Unidad
    fields = ['unidadUn','gimnasioUn','maquinaUn','persona']
    success_url = reverse_lazy('unidad')
    template_name = "./Pyex_app/unidad_update_form.html"

class UnidadDeleteView(UserPassesTestMixin, DeleteView):
    model = Unidad
    success_url = reverse_lazy('unidad')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return self.request.user.is_superuser
        except:
            return False
#-----------------------------------------------------------------------------------------
class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('index')

class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = User
    fields = ('username','first_name','last_name','email','sexUs','fechanacUs','telefonoUs','fotoUs','apuntados')
    success_url = reverse_lazy('index')
    template_name = "./Pyex_app/user_update_form.html"
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = User
    success_url = reverse_lazy('index')
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
