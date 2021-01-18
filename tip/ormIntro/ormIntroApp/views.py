from django.shortcuts import render, HttpResponse, redirect
from .models import Product

# Create your views here.
def index(request):
    print("printing all the product from the views file now below")
    print(Product.objects.all())
    context = {
        'allProds': Product.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    print("*"*20)
    print(request.POST)
    print("*"*20)
    Product.objects.create(name = request.POST['prodname'] , price = request.POST['dollas'], description = request.POST['desc'])

    return redirect("/")