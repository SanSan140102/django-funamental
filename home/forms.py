# forms.py

from django import forms


class KomentarForm(forms.Form):
    teks = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class' : 'form-control', 'name': 'comment'}),label='comment' )  
      
