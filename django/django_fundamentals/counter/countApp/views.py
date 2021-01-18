from django.shortcuts import render, HttpResponse



def index(request):
    request.session['name'] = request.POST['name']
    request.session['counter'] = 100

    if 'key_name' in request.session:
        print('key exists!')
    else:
        print("key 'key_name' does NOT exist")
    return render(request, 'index.html')