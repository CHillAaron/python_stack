# Create your views here.


from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

def root(request):
    return redirect("/blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def create(request):
    return redirect("/")

def show(request, num):
    return HttpResponse(f"placeholder to display blog number: {num}")

def edit(request, num):
    return HttpResponse(f"placeholder to edit blog number: {num}")

def destroy(request, num):
    return redirect("/blogs")

def jsonResponse(request):
    response = { }
    return JsonResponse({
        'title': 'My first blog' ,
        'key': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit.'
    })