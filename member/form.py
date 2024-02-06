from django import forms


class MemberForm(forms.Form):
    nama           = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    alamat         = forms.CharField(max_length=100,widget=forms.Textarea(attrs={'class':'form-control'}))
    no_telphon     =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    jenis_kelamain =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    pekerjaan      =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    