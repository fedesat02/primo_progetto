from django.urls import path
from .views import contatti, registrazioneView 

app_name = 'forms_app'

urlpatterns = [
    path('contatto/', contatti, name = 'contatti'),
    path('registrazione', registrazioneView, name = 'registration_view'),
]
