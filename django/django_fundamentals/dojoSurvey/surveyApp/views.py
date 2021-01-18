from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')

def result(request):
    print("we just submitted the form and are in the 'results' function")
    print(request.POST)
    context = {
        'formInfo': request.POST
    }
    return render(request, "result.html", context)