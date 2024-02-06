from django.shortcuts import render,redirect
from news.models import News,Category,Komentar,ReplayKomentar,Like
from home.forms import KomentarForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from home.forms_replay import ReplayForm
from .models import SosialMedia
from django.http import JsonResponse



# Create your views here.

def index_home(request):
    news =News.objects.order_by('-tanggal').all()
    category = Category.objects.all()   
    sosmed = SosialMedia.objects.all()
    return render(request,'home_index.html',{'news':news,'category' : category,'sosmed':sosmed})

def news_Detail(request,slug):
    news =  News.objects.order_by('-tanggal').all()
    news_Detail = News.objects.get(slug=slug)
    category = Category.objects.all()
    sosmed = SosialMedia.objects.all()
    news_Detail.total_views +=1
    news_Detail.save()
    
    # form komentar
    form = KomentarForm()
    formReplay = ReplayForm()
    return render(request,'news_detail.html',{'news':news,'category':category,'news_detail':news_Detail, 'form':form,'formReplay':formReplay,'sosmed':sosmed})
    
    

def news_Category(request,slug):
   news         =  News.objects.order_by('-tanggal').all()
   category     = Category.objects.all()
   news_category=News.objects.filter(category__category=category)
   return render(request,'news_category.html',{'news':news,'category':category,'news_category':news_category})
    
def tambah_komentar(request, slug,):
        
    form = KomentarForm(request.POST)
    if form.is_valid():
        Komentar.objects.create(
            posting = News.objects.get(slug=slug),
            penulis = request.user,
            teks = form.cleaned_data['teks'])
                   
    messages.success(request,'komen telah di kirim')
    return redirect('home.news_detail',slug=slug)



    
def replay_komentar(request,slug,id ):
        
    form = ReplayForm(request.POST)
    if form.is_valid():
        ReplayKomentar.objects.create(
            komentar = Komentar.objects.get(id=id),
            penulis = request.user,
            teks = form.cleaned_data['teks'])
                   
    messages.success(request,'komen telah di kirim')
    return redirect('home.news_detail',slug=slug)


def load_ajax(request):
    return render(request,'ajax.html')



def ajax_data(request):

    data = {
        'nama':"ihsan",
        
        'alamat':"solok",
        
        'club':[
           
            {
            "nama club":"semen padang",
            "tahun club":"1902"
            },
            {
             "nama club":"Persija",
            "tahun club":"1911"
                
            }
            
        ]
        
    }


    return JsonResponse(data)


           
def news_like(request,newsId):
    
    #ambil data news sesuai parameter newsId
    news=News.objects.get(id=newsId)
    
    #insert ke tabel like
    Like.objects.create(likes=news)
    
    #untuk menghitung total like sesuai news dengan menggunakan nama relasi "like"
    newsLikeCount = news.like.count()
    data= {
        "newsLikeCount":newsLikeCount
    }
    
    return JsonResponse(data)
 



    







 

