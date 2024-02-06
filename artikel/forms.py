from django import forms
from artikel.models import Artikel

class ArtikelForm(forms.ModelForm):
    
    class Meta:
        model = Artikel
        fields = ("title","body")
