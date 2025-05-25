from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Contact
from django.urls import reverse
# Create your views here.

def check(request):
    return render(request,'show/main.html')

def gal(request):
    return render(request,'gal.html')

def abt(request):
    return render(request,'abt.html')

def price(request):
    return render(request,'service.html')

def cnt(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        Contact.objects.create(name=name,email=email,subject=subject,message=message)
        url = reverse('contact')
        return HttpResponseRedirect(url)
    return render(request,'cnt.html')