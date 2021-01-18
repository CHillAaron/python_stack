from django.shortcuts import render, HttpResponse, redirect
from .models import User


def index(request):
    context = {
    	"accounts": User.objects.all()
    }
    return render(request, "index.html", context)

def accounts(request):
    print('***'*10)
    print(request.POST)
    print('***'*10)
    User.objects.create(first_name = request.POST['first'], last_name = request.POST['last'], email_address = request.POST['email'], age = request.POST['age'])
    return redirect('/')