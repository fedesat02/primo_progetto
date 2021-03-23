from django import forms
from django.forms import fields
from .models import Contatto

class FormContatto(forms.ModelForm):
    class Meta:
        model = Contatto
        fields = "__all__"
