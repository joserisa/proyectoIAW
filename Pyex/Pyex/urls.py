"""myPyex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Pyex_app.views import *
from Pyex_app import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, serializers, viewsets
from Pyex_app.api import router

urlpatterns = [
    #path('alta/', AltaListView.as_view()),
    #path('apuntado/', ApuntadoListView.as_view()),
    #path('polls/', include('polls.urls')),
    #path('apuntado/<int:pk>/', ApuntadoDetailView.as_view(), name='apuntado-detail'),
    #path('alta/<int:pk>/', AltaDetailView.as_view(), name='alta-detail'),

    path('', index, name='index'),
    
    path('admin/', admin.site.urls),
    path('gimnasio/', GimnasioListView.as_view(), name='gimnasio'),
    path('curso/', CursoListView.as_view(), name='curso'),
    path('usuario/', UserListView.as_view(), name='usuario'),
    path('unidad/', UnidadListView.as_view(), name='unidad'),
    path('maquina/', MaquinaListView.as_view(), name='maquina'),

    #VISTAS DE DETALLES
    path('gimnasio/<int:pk>/', GimnasioDetailView.as_view(), name='gimnasios-detail'),
    path('usuario/<int:pk>/', UserDetailView.as_view(), name='usuarios-detail'),
    path('curso/<int:pk>/', CursoDetailView.as_view(), name='cursos-detail'),
    path('unidad/<int:pk>/', UnidadDetailView.as_view(), name='unidades-detail'),
    path('maquina/<int:pk>/', MaquinaDetailView.as_view(), name='maquinas-detail'),

    #VISTAS AÑADIR, MODIFICAR Y BORRAR GIMNASIO
    path('gimnasio/add/', GimnasioCreateView.as_view(), name='gimnasio-add'),
    path('gimnasio/<int:pk>/edit/', GimnasioUpdateView.as_view(), name='gimnasio-update'),
    path('gimnasio/<int:pk>/delete/', GimnasioDeleteView.as_view(), name='gimnasio-delete'),

    #VISTAS AÑADIR, MODIFICAR Y BORRAR CURSO
    path('curso/add/', CursoCreateView.as_view(), name='curso-add'),
    path('curso/<int:pk>/edit/', CursoUpdateView.as_view(), name='curso-update'),
    path('curso/<int:pk>/delete/', CursoDeleteView.as_view(), name='curso-delete'),

    #VISTAS AÑADIR, MODIFICAR Y BORRAR MAQUINA
    path('maquina/add/', MaquinaCreateView.as_view(), name='maquina-add'),
    path('maquina/<int:pk>/edit/', MaquinaUpdateView.as_view(), name='maquina-update'),
    path('maquina/<int:pk>/delete/', MaquinaDeleteView.as_view(), name='maquina-delete'),

    #VISTAS AÑADIR, MODIFICAR Y BORRAR CURSO
    path('unidad/add/', UnidadCreateView.as_view(), name='unidad-add'),
    path('unidad/<int:pk>/edit/', UnidadUpdateView.as_view(), name='unidad-update'),
    path('unidad/<int:pk>/delete/', UnidadDeleteView.as_view(), name='unidad-delete'),

    #VISTAS AÑADIR, MODIFICAR Y BORRAR USUARIO
    path('register/', UserCreateView.as_view(), name='usuario-add'),
    path('usuario/<int:pk>/edit/', UserUpdateView.as_view(), name='usuario-update'),
    path('usuario/<int:pk>/delete/', UserDeleteView.as_view(), name='usuario-delete'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("register/", views.register_request, name="register"),
   
    #API
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #SEARCH
    path('gimnasio/search/', search.as_view(), name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

