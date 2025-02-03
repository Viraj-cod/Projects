from django.shortcuts import render
from . forms import Register,Loginform
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

def registration(request):
    if request.user.is_authenticated:
        return render(request,'base.html')
    else:
        if request.method == 'POST':
            form = Register(request.POST)
            if form.is_valid():
                form.save()
                url = reverse('log')
                return HttpResponseRedirect(url)
        else:
            form = Register()
        return render(request,'account/register.html',{'form':form})

def loginview(request):
    if request.method == 'POST':
        form = Loginform(request=request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            #email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                homeurl = reverse('main')
                return HttpResponseRedirect(homeurl)
    else:
        form = Loginform()
    return render(request,'account/log.html',{'form':form})

def main(request):
    if request.user.is_authenticated:
        return render(request,'base.html')
    else:
        logurl = reverse('log')
        return HttpResponseRedirect(logurl)

def log_out(request):
    logout(request)
    logurl = reverse('log')
    return HttpResponseRedirect(logurl)

