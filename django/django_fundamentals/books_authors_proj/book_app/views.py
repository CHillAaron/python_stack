from django.shortcuts import render, HttpResponse, redirect
from .models import *


def index(request):
    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all()
    }
    return render(request, "index.html", context)

def addBook(request):
    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all()
    }
    
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'] )
    return redirect('/', context)

def bookInfo(request, id):
    context = {
        'books': Book.objects.get(id=id),
        'authors': Author.objects.exclude(books = Book.objects.get(id=id) ),
        # 'author_book': Book.objects.get(id=id).authors.first_name
    }
    # ClassName.objects.exclude(field1="value for field1", etc.) - gets any records not matching the query provided
    return render(request, 'booksum.html', context)

def addAuthor(request, id):
    context = {
        'books': Book.objects.all(),
        'authors': Author.objects.all()
    }
    print("***"*10)
    print(request.POST)
    print("***"*10)
    # locate = DojoSai.objects.get(id=request.POST['location'])
    auth = Author.objects.get(id=request.POST['auth'])
    tablet = Book.objects.get(id=id)
    tablet.authors.add(auth)
    return redirect('/', context)