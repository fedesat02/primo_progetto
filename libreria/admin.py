from django.contrib import admin

# Register your models here.
from .models import Autore_SF, Libro_SF, Genere_SF

admin.site.register(Autore_SF)
admin.site.register(Libro_SF)
admin.site.register(Genere_SF)