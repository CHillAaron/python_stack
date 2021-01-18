from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
# Create your views here.




def new(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request,'new.html', context)

def newShow(request):
    errors = Show.objects.showvalidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new.html')

    show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], dates=request.POST['release'], desc=request.POST['desc'])
    # return redirect('/shows')
    return redirect(f'/showInfo/{show.id}')
    

def show(request):
    context = {
        'allshows': Show.objects.all()
    }

    return render(request, 'shows.html', context)

def showInfo(request, id):
    context = {
        'shows': Show.objects.all(),
        'thisShow': Show.objects.get(id=id)
    }

    return render(request, 'showsinfo.html', context)

def edit(request, id):
    context = {
        'shows': Show.objects.all(),
        'thisShow': Show.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def editShow(request, id):
    context = {
        'shows': Show.objects.all(),
        'thisShow': Show.objects.get(id=id)
    }
    print(request.POST)
    showUpdate = Show.objects.get(id=id)
    showUpdate.title = request.POST['title']
    showUpdate.network = request.POST['network']
    showUpdate.dates = request.POST['release']
    showUpdate.desc = request.POST['desc']
    errors = Show.objects.showvalidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/showInfo/{id}/edit')
    showUpdate.save()
    return redirect('/shows', context)

def delete(request, id):
    show_delete = Show.objects.get(id=id)
    show_delete.delete()
    return redirect('/shows')