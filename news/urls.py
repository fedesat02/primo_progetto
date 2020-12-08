from django.urls import path
from .views import home, ArticoloDetailView, ArticoloListView

app_name = 'news'

urlpatterns = [
    path('', home, name="homeview"),
    path('articoli/', ArticoloListView.as_view(), name="articolo_list"),
    path('articoli/<int:pk>', ArticoloDetailView.as_view(), name="articolo_detail"),
]