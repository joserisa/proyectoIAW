from django.urls import path
from . import views
from .views import GimnasioListView

urlpatterns = [
    path('', views.index, name='index'),
    path('gimnasio/', GimnasioListView.as_view()),
]