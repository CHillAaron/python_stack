from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return redirect('/home')

def home(request):
    context = {
        'account': User.objects.all()
    }
    return render(request, "index.html", context)

def register(request):
    print(request.POST)
    errors = User.objects.userValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/home')
    else:
        newAccount = User.objects.create(first=request.POST['first'], last=request.POST['last'], email=request.POST['email'],bday=request.POST['bday'] , password=request.POST['password'])
        request.session ['loggedInId'] = newAccount.id



    return redirect('/quotes',)



def logIn(request):
    errors = User.objects.logInValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        matchingEmail = User.objects.filter(email=request.POST['email'])
        request.session['loggedInId'] = matchingEmail[0].id

    return redirect('/quotes')

def success(request):
    if 'loggedInId' not in request.session:
        return redirect('/')
    context = {
        'loggedIn': User.objects.get(id=request.session ['loggedInId'])
    }
    return render(request, 'success.html',context)

def logout(request):
    request.session.clear()
    return redirect('/')
