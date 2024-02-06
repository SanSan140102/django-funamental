
from django import forms


class ReplayForm(forms.Form):
    teks = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class' : 'form-control', 'name': 'comment'}),label='' )  
      
