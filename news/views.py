from django.shortcuts import render,redirect
from django.http import HttpResponse
from news.models import Category,Like
from news.form import categoryForms
from news.models import News
from news.form import newsForm
from django.http import JsonResponse




def index_category(request):
    data=Category.objects.all()
        
    return render(request,'category_index.html',{'title': 'list category' ,'category':data})
    
        

def detail_category(request,id):
    response= f"parameter :{id}"
    return HttpResponse(response)


def delete_category(request,id):
    Category.objects.filter(id=id).delete()
    return redirect('category.index')



def create_category(request):
    if request.method == 'POST':
        form = categoryForms(request.POST)
        if form.is_valid():
            category      = form.cleaned_data['category']
            Category.objects.create(category=category)
            return redirect('category.index')
        else:
            return render(request,'category_create.html',{'form':form})
    else:
        form = categoryForms()
        return render(request, 'category_create.html',{'form':form})
    
def edit_category(request,id):
    category_edit = Category.objects.get(id=id)
    if request.method == 'POST':
        form = categoryForms(request.POST)
        if form.is_valid():
            category_edit.category      = form.cleaned_data['category']
            category_edit.save()
            return redirect('category.index')
        else:
           return render(request,'category_create.html',{'form':form,})
    else:
       form = categoryForms(initial={'category':category_edit.category})
       return render(request,'category_create.html',{'form':form,})



# news

def index_news(request):
    data= News.objects.all()
        
    return render(request,'news_index.html',{'title': 'list news' ,'news':data})
    
        

def detail_news(request,id):
    response= f"parameter :{id}"
    return HttpResponse(response)


def delete_news(request,id):
    News.objects.filter(id=id).delete()
    return redirect('news.index')



def create_news(request):
    if request.method == 'POST':
        form = newsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # category      = form.cleaned_data['category']
            # title         = form.cleaned_data['title']
            # deskripsi     = form.cleaned_data['deskripsi']
            # image         = form.cleaned_data['image']
            # tanggal       = form.cleaned_data['tanggal']
            # News.objects.create(category=category,title=title,deskripsi=deskripsi,image=image,tanggal=tanggal)
            return redirect('news.index')
        else:
            return render(request,'news_create.html',{'form':form})
    else:
        form = newsForm()
        return render(request, 'news_create.html',{'form':form})
    
def edit_news(request,id):
    news =  News.objects.get(id=id)
    if request.method == 'POST':
        form = newsForm(request.POST, request.FILES)
        if form.is_valid():
            news.category     =form.cleaned_data['category']
            news.title        =form.cleaned_data['title']
            news.deskripsi    =form.cleaned_data['deskripsi']
            news.tanggal      =form.cleaned_data['tanggal']
            if request.FILES.get('image') is not None:
                news.image        =form.cleaned_data['image']
            news.save()
            return redirect('news.index')
        else:
           return render(request,'news_create.html',{'form':form,'news':news})
    else:
       form = newsForm(initial={'category':news.category,'title':news.title,'deskripsi':news.deskripsi,'image':news.image,'tanggal':news.tanggal})
       return render(request,'news_create.html',{'form':form,'news':news})
 
