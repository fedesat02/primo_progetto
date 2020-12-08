from django.urls import path
from .views import home, ArticoloDetailView

app_name = 'news'

urlpatterns = [
    path('', home, name="homeview"),
    path('articoli/<int:pk>', ArticoloDetailView.as_view(), name="articolo_detail"),
]