from django import forms
from .models import Cidades

class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidades
        fields = ['nome', 'estado'] 