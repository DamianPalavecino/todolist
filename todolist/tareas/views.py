from django.shortcuts import render
from django.views.generic import ListView
from . models import Tarea


class TareasListView(ListView):
    model = Tarea
    template_name = "listado.html"
    context_object_name = 'listado'

