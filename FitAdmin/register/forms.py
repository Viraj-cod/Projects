from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class Register(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=20,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=20,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        #exclude = ['password2']
        fields = ['username','lastname','email','password1','password2']
    
        labels = {
            'username':'Name',
            'lastname' : 'Last Name',
            'email':'Email',
            'password1':'password'
            }
        widgets = {
            'password2':forms.PasswordInput(attrs={'class':'form-control'})
        }

class Loginform(AuthenticationForm):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    #email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    

        