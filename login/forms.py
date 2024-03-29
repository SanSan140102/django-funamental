from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm


class LoginForm(AuthenticationForm):
    username =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    password =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    
class registerForm(UserCreationForm):
    username =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='password')
    password2 =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password Confirmation')


    