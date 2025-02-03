from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import members_model,accesories_model,Trainers_model,transactions_model
from . forms import members_form,accesories_form,Trainers_form,transactions_form
from django.urls import reverse
from django.core.paginator import Paginator
from register import urls
# Create your views here.

def members(request):
    if request.user.is_authenticated:
        data = members_model.objects.all().order_by('-duration')
        paginator = Paginator(data,6)
        page_number = request.GET.get('p',1)
        page_obj = paginator.get_page(page_number)
        return render(request,'inf/members.html',{'data':page_obj})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)

def add_members(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = members_form(request.POST)
            if form.is_valid():
                form.save()
                url = reverse('mem')
                return HttpResponseRedirect(url)
        form = members_form()
        return render(request,'inf/add_mem.html',{'form':form})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)

def accesories(request):
    if request.user.is_authenticated:
        data = accesories_model.objects.all().order_by('-maintenance')
        paginator = Paginator(data,6)
        page_number = request.GET.get('p',1)
        page_obj = paginator.get_page(page_number)
        return render(request,'inf/acessories.html',{'data':page_obj})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)
    
def add_accesories(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = accesories_form(request.POST)
            if form.is_valid():
                form.save()
                url = reverse('ace')
                return HttpResponseRedirect(url)
        form = accesories_form()
        return render(request,'inf/add_ace.html',{'form':form})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)
    

def Trainers(request):
    if request.user.is_authenticated:
        data = Trainers_model.objects.all().order_by('-id')
        paginator = Paginator(data,6)
        page_number = request.GET.get('p',1)
        page_obj = paginator.get_page(page_number)
        return render(request,'inf/trainers.html',{'data':page_obj})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)
    
    

def add_trainers(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Trainers_form(request.POST)
            if form.is_valid():
                form.save()
                url = reverse('train')
                return HttpResponseRedirect(url)
        form = Trainers_form()
        return render(request,'inf/add_train.html',{'form':form})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)

def Transactions(request):
    if request.user.is_authenticated:
        data = transactions_model.objects.all().order_by('-id')
        paginator = Paginator(data,6)
        page_number = request.GET.get('p',1)
        page_obj = paginator.get_page(page_number)
        return render(request,'inf/transe.html',{'data':page_obj})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)

def add_Transactions(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = transactions_form(request.POST)
            if form.is_valid():
                form.save()
                url = reverse('transe')
                return HttpResponseRedirect(url)
        form = transactions_form()
        return render(request,'inf/add_transe.html',{'form':form})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)

def mem_delete(request,id):
    if request.user.is_authenticated:
        data = members_model.objects.get(id = id)
        data.delete()
        url = reverse('mem')
        return HttpResponseRedirect(url)
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)


def trainer_delete(request,id):
    if request.user.is_authenticated:
        data = Trainers_model.objects.get(id = id)
        data.delete()
        url = reverse('train')
        return HttpResponseRedirect(url)
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)
    
def accesories_delete(request,id):
    if request.user.is_authenticated:
        data = accesories_model.objects.get(id = id)
        data.delete()
        url = reverse('ace')
        return HttpResponseRedirect(url)
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)

def transaction_delete(request,id):
    if request.user.is_authenticated:
        data = transactions_model.objects.get(id = id)
        data.delete()
        url = reverse('transe')
        return HttpResponseRedirect(url)
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)

def search_mem(request):
    if request.user.is_authenticated:
        query = request.GET.get('query',None)
        data = members_model.objects.filter(name__icontains = query)
        return render(request,'inf/search_mem.html',{'data':data})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)
    
def search_transe(request):
    if request.user.is_authenticated:
        query = request.GET.get('query',None)
        data = transactions_model.objects.filter(description__icontains = query)
        return render(request,'inf/search_transe.html',{'data':data})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)
    
def search_train(request):
    if request.user.is_authenticated:
        query = request.GET.get('query',None)
        data = Trainers_model.objects.filter(name__icontains = query)
        return render(request,'inf/search_train.html',{'data':data})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)
    
def search_ace(request):
    if request.user.is_authenticated:
        query = request.GET.get('query',None)
        data = accesories_model.objects.filter(name__icontains = query)
        return render(request,'inf/search_ace.html',{'data':data})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)

def mem_rep(request):
    if request.user.is_authenticated:
        data = members_model.objects.all().order_by('-duration')[:30]

        return render(request,'inf/report.html',{'data':data})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)
    
def train_rep(request):
    if request.user.is_authenticated:
        data = Trainers_model.objects.all().order_by('-join_date')[:30]
        return render(request,'inf/rep_trainers.html',{'data':data})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)
    
def ace_rep(request):
    if request.user.is_authenticated:
        data = accesories_model.objects.all().order_by('-maintenance')[:30]
        return render(request,'inf/rep_ace.html',{'data':data})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)

def transe_rep(request):
    if request.user.is_authenticated:
        data = transactions_model.objects.all().order_by('-data')[:30]
        return render(request,'inf/rep_tran.html',{'data':data})
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)

def price(request):
    if request.user.is_authenticated:
        return render(request,'inf/pricing.html')
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)
    
def gallery(request):
    if request.user.is_authenticated:
        return render(request,'inf/gallery.html')
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)

def about(request):
    if request.user.is_authenticated:
        return render(request,'inf/about.html')
    else:
        home = reverse('log')
        return HttpResponseRedirect(home)

def under(request,name):
    print(name)
    data = members_model.objects.filter(trainer=name)
    print(data)
    return render(request,'inf/mem_under.html',{'data':data})

    