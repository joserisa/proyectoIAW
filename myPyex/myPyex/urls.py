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
from polls import views
from polls.views import index, GimnasioListView, CursoListView, UsuarioListView, UnidadListView, GimnasioDetailView, CursoDetailView, UsuarioDetailView, UnidadDetailView

urlpatterns = [
    path('', index),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('gimnasio/', GimnasioListView.as_view(), name='gimnasio'),
    path('curso/', CursoListView.as_view(), name='curso'),
    path('usuario/', UsuarioListView.as_view(), name='usuario'),
    path('unidad/', UnidadListView.as_view(), name='unidad'),
    #path('alta/', AltaListView.as_view()),
    #path('apuntado/', ApuntadoListView.as_view()),
    path('gimnasio/<int:pk>/', GimnasioDetailView.as_view(), name='gimnasio-detail'),
    path('usuario/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    path('curso/<int:pk>/', CursoDetailView.as_view(), name='curso-detail'),
    #path('apuntado/<int:pk>/', ApuntadoDetailView.as_view(), name='apuntado-detail'),
    path('unidad/<int:pk>/', UnidadDetailView.as_view(), name='unidad-detail'),
    #path('alta/<int:pk>/', AltaDetailView.as_view(), name='alta-detail'),
]

