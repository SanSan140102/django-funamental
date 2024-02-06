from django.shortcuts import render,redirect
from login.forms import LoginForm,registerForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def index (request):
    if request.method =='POST':
        form=LoginForm(request,request.POST)
        if form.is_valid():
            user = authenticate(request,username=form.cleaned_data['username'],password = form.cleaned_data [ 'password'])
           
            if user:
                login(request,user)
                return redirect ('product.index')  
        else:
            messages.error(request,'valid username or password.please try again')
            return redirect('login.index')
            
            
    else:
        form = LoginForm()
        return render (request,'login_index.html',{'form':form})
        
def logout_user (request):
    logout(request)
    return redirect('home_index')

def register_user(request):
    if request.method =='POST':
        form=registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.index')
        else:
            return render(request, 'register.html', {'form': form})
                 
    else:
        form = registerForm()
        return render (request,'register.html',{'form':form})
        
            