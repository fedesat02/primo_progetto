from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Articolo, Giornalista

# Create your views here.
def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    return render(request, 'homepage.html', context)

class ArticoloDetailView(DetailView):
    model = Articolo
    template_name = 'articolo_detail.html'

class ArticoloListView(ListView):
    model = Articolo
    template_name = 'lista_articoli.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articoli'] = Articolo.objects.all()
        return context