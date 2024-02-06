from django.shortcuts import render,redirect
from artikel.models import Artikel
from artikel.forms import  ArtikelForm

# Create your views here.

def index(request):
    data ={
        
        'data_artikel':Artikel.objects.all(),
    }
    
    
    return render(request,'artikel_index.html',data)

def delete(request,id):
    Artikel.objects.filter(id=id).delete()
    return redirect('artikel_index')



def create(request):
    if request.method == 'POST':
        form = ArtikelForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('artikel_index')
        else:
            return render(request,'artikel_form.html',{'form':form})
    else:
        form = ArtikelForm()
        return render(request, 'artikel_form.html',{'form':form})
    
    
def edit (request,id):
    artikel = Artikel.objects.get(id=id)
    if request.method == 'POST':
        form = ArtikelForm(request.POST, instance=artikel)
        if form.is_valid():
          form.save()
          return redirect('artikel_index')
        else:
            return render(request,'artikel_form.html',{'form':form})
    else:
        form = ArtikelForm(instance=artikel)
        return render(request, 'artikel_form.html',{'form':form})
    
    
    
    