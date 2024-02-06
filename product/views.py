from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import Product
from product.form import Productform

# Create your views here.


def index(request):
    data=Product.objects.all()
        
    return render(request,'product_index.html',{'title': 'list product' ,'product':data})
    
        

def detail(request,id):
    response= f"parameter :{id}"
    return HttpResponse(response)

def calculator(request,bil1,bil2):
    hasil= bil1 + bil2
    response= f"hasil bil1 + bil2 :{hasil}"
    return HttpResponse(response)

def delete(request,id):
    Product.objects.filter(id=id).delete()
    return redirect('product.index')

def create(request):
    if request.method == 'POST':
        form = Productform(request.POST)
        if form.is_valid():
            nama      = form.cleaned_data['nama']
            deskripsi = form.cleaned_data['deskripsi']
            harga     = form.cleaned_data['harga']
            Product.objects.create(nama=nama,deskripsi=deskripsi,harga=harga)
            return redirect('product.index')
        else:
            return render(request,'product_create.html',{'form':form})
    else:
        form = Productform()
        return render(request, 'product_create.html',{'form':form})
    
def edit(request,id):
    product =  Product.objects.get(id=id)
    if request.method == 'POST':
        form = Productform(request.POST)
        if form.is_valid():
            product.nama     =form.cleaned_data['nama']
            product.deskripsi=form.cleaned_data['deskripsi']
            product.harga    =form.cleaned_data['harga']
            product.save()
            return redirect('product.index')
        else:
           return render(request,'product_create.html',{'form':form,'product':product})
    else:
       form = Productform(initial={'nama':product.nama,'deskripsi':product.deskripsi,'harga':product.harga})
       return render(request,'product_create.html',{'form':form,'product':product})
            
    
    
        
    
    
    
    