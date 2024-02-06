from django.shortcuts import render,redirect
from django.http import HttpResponse
from sansan.models import barang
from sansan.form import barangForm

# Create your views here.


def index(request):
    data=barang.objects.all()
        
    return render(request,'barang_index.html',{'title': 'list barang' ,'barang':data})


def create(request):
    if request.method == 'POST':
        form = barangForm(request.POST)
        if form.is_valid():
            nama_barang     = form.cleaned_data['nama_barang']
            size_barang = form.cleaned_data['size_barang']
            warna_barang     = form.cleaned_data['warna_barang']
            barang.objects.create(nama_barang=nama_barang,size_barang=size_barang,warna_barang=warna_barang)
            return redirect('barang.index')
        else:
            return render(request,'barang_create.html',{'form':form})
    else:
        form = barangForm()
        return render(request, 'barang_create.html',{'form':form})
    
