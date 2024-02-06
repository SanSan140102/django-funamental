from django import forms


class barangForm(forms.Form):
    nama_barang = forms.CharField(max_length=100)
    size_barang = forms.IntegerField()
    warna_barang =forms.CharField()
    