from django.urls import path
from .views import AutoreDetail_SF, LibroList_SF 

app_name = 'libreria'

urlpatterns = [
    path('', LibroList_SF.as_view(), name='lista_libri'),
    path('autore/<int:pk>/', AutoreDetail_SF.as_view(), name='profilo_autore')
]