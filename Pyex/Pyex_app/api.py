from django.urls import path, include
from django.contrib.auth.models import *
from rest_framework import routers, serializers, viewsets
from .models import *

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff','codUs','sexUs','fechanacUs']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Serializers define the API representation.
class GimnasioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gimnasio
        fields = ['nomGym','direccionGym','telefonoGym','correoGym','fotoGym']

# ViewSets define the view behavior.
class GimnasioViewSet(viewsets.ModelViewSet):
    queryset = Gimnasio.objects.all()
    serializer_class = GimnasioSerializer

# Serializers define the API representation.
class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = ['nomCur','profesorCur','horarioIniCur','horarioFinCur','grupoCur','gimnasioCur','descCur','capCur','capMaxCur']

# ViewSets define the view behavior.
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# Serializers define the API representation.
class UnidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unidad
        fields = ['nomUn','estadoUn','gimnasioUn','aforoUn','aforoMaxUn']

# ViewSets define the view behavior.
class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer

# Routers provide an easy way of automatically determining the URL conf.

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'gimnasios', GimnasioViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'unidad', UnidadViewSet)