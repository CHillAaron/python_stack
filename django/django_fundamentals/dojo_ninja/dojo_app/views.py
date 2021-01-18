from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
    	"dojo": DojoSai.objects.all(),
        "ninja": Ninja.objects.all()
    }
    return render(request, "index.html", context)

def dojoForm(request):
    print(request.POST)
    DojoSai.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'], desc=request.POST['desc'])
    return redirect("/")

def ninjaForm(request):
    context = {
        "dojos": DojoSai.objects.all(),
        "ninja": Ninja.objects.all()
    }
    locate = DojoSai.objects.get(id=request.POST['location'])
    Ninja.objects.create(first_name=request.POST['first'], last_name=request.POST['last'], dojos=locate)
    print("***"*10)
    print(request.POST)
    print("***"*10)
    return redirect("/", context)

def deleteDojo(request, id):
    deleteMe = DojoSai.objects.get(id=id)
    deleteMe.delete()
    return redirect("/")