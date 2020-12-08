from django.urls import path
from .views import home, ArticoloDetailView, ArticoloListView, GiornalistaDetailView, GiornalistaListView

app_name = 'news'

urlpatterns = [
    path('', home, name="homeview"),
    path('articoli/', ArticoloListView.as_view(), name="articoli_list"),
    path('articoli/<int:pk>', ArticoloDetailView.as_view(), name="articolo_detail"),
    path('giornalisti/', GiornalistaListView.as_view(), name="giornalisti_list"),
    path('giornalisti/<int:pk>', GiornalistaDetailView.as_view(), name="giornalista_detail"),
]