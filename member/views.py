from django.shortcuts import render,redirect
from django.http import HttpResponse
from member.models import Member
from member.form import MemberForm


# Create your views here.


def index(request):
    data=Member.objects.all()
        
    return render(request,'member_index.html',{'title': 'list product' ,'member':data})


def delete(request,id):
    Member.objects.filter(id=id).delete()
    return redirect('member.index')

def create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            nama                      = form.cleaned_data['nama']
            alamat                    = form.cleaned_data['alamat']
            no_telphon                = form.cleaned_data['no_telphon']
            jenis_kelamain             =form.cleaned_data['jenis_kelamain']
            pekerjaan                 =form.cleaned_data['pekerjaan']
        
            Member.objects.create(nama=nama,alamat=alamat,no_telphon=no_telphon,jenis_kelamain=jenis_kelamain,pekerjaan=pekerjaan)
            return redirect('member.index')
        else:
            return render(request,'member_create.html',{'form':form})
    else:
        form = MemberForm()
        return render(request, 'member_create.html',{'form':form})
    
def edit(request,id):
    member =  Member.objects.get(id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member.nama                      =form.cleaned_data['nama']
            member.alamat                    =form.cleaned_data['alamat']
            member.no_telphon                =form.cleaned_data['no_telphon']
            member.jenis_kelamain            =form.cleaned_data['jenis_kelamain']
            member.pekerjaan                 =form.cleaned_data['pekerjaan']
            member.save()
            
            return redirect('member.index')
        else:
           return render(request,'member_create.html',{'form':form,'member':member})
    else:
       form = MemberForm(initial={'nama':member.nama,'alamat':member.alamat,'no_telphon':member.no_telphon,'jenis_kelamain' :member.jenis_kelamain,'pekerjaan':member.pekerjaan})
       return render(request,'member_create.html',{'form':form,'member':member})
            
    
    
        
    
    
    
    
