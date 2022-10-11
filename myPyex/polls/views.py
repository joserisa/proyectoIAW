from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from typing import List
from django.views.generic import ListView
from .models import Gimnasio

class GimnasioListView(ListView):
    model = Gimnasio

# Create your views here.
