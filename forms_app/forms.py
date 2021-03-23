from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields, widgets
from .models import Contatto

class FormContatto(forms.ModelForm):
    class Meta:
        model = Contatto
        fields = "__all__"
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Compila questo campo', 'class': 'form-control'}),
            'cognome': forms.TextInput(attrs={'placeholder': 'Compila questo campo', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Compila questo campo', 'class': 'form-control'}),
            'contenuto': forms.Textarea(attrs={'placeholder': 'Area testuale scrivi pure', 'class': 'form-control'})
        }
    
    def clean_contenuto(self): #nome funzione: clean_nomecampodavalidare
        dati = self.cleaned_data["contenuto"]
        if "parola" in dati: #parola non è ammesso
            raise ValidationError("Il contenuto inserito viola le norme del sito!")
        if len(dati)<20:
            raise ValidationError("Il contenuto inserito è troppo breve")
        return dati
