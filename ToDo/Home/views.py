from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . forms import infoform
from django.urls import reverse
from . models import Information
# Create your views here.
def Index(request):
    if request.method == 'POST':
        form = infoform(request.POST)
        if form.is_valid():
            form.save()
            homeurl = reverse('home')
            return HttpResponseRedirect(homeurl)
    else:       
        form = infoform()
        
    
    return render(request,'base.html',{'form':form})

def show(request):
    form = Information.objects.all()
    return render(request,'show.html',{'form':form})

def edit(request,id):
    info = get_object_or_404(Information,id = id)
    if request.method == 'POST':
        form = infoform(request.POST,instance=info)
        if form.is_valid():
            info.save()
            homeurl = reverse('show')
            return HttpResponseRedirect(homeurl)
    else:        
        form = infoform(instance=info)
        return render(request,'edit.html',{'form':form})

def delete(request,id):
    form = Information.objects.get(id = id)
    form.delete()
    homeurl = reverse('show')
    return HttpResponseRedirect(homeurl)

def search(request):
    query = request.GET.get('query',None)
    task = Information.objects.filter(task__icontains = query)
    print(task)
    return render(request,'search.html',{'task':task})