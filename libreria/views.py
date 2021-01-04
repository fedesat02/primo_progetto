from libreria.models import Autore_SF, Libro_SF
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.

class LibroList_SF(ListView):
    model = Libro_SF
    template_name = 'lista_libri.html'
    context_object_name = 'libri'

class AutoreDetail_SF(DetailView):
    model = Autore_SF
    template_name = 'autore.html'
    context_object_name = 'autore'