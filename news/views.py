from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
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