from django import forms
from .models import News, Category



class categoryForms (forms.Form):
    category = forms.CharField(max_length=100)


class newsForm(forms.ModelForm):
    category  = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label="pilih kategori",widget=forms.Select(attrs={'class' : 'form-control'}))
    tanggal   = forms.DateField(label='Tanggal Terbit',widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model=News
        fields= ['category','title','deskripsi','image','tanggal']
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #menyesuaikan widget atau menambahkan atribut lain jika perlu
        # self.fields[''].widget = forms.TextInput(attrs={'type':'deletetime-local','class':'form-control'})
        self.fields['deskripsi'].widget = forms.Textarea(attrs={'id':'summernote'})
        
        
