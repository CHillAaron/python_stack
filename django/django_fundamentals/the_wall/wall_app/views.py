from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse

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
        newAccount = User.objects.create(first=request.POST['first'], last=request.POST['last'], email=request.POST['email'], password=request.POST['password'])
        request.session ['loggedInId'] = newAccount.id



    return redirect('/wall',)

def logIn(request):
    errors = User.objects.logInValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        matchingEmail = User.objects.filter(email=request.POST['email'])
        request.session['loggedInId'] = matchingEmail[0].id

    return redirect('/wall')

def wall(request):
    if 'loggedInId' not in request.session:
        return redirect('/')
    context = {
        'loggedIn': User.objects.get(id=request.session ['loggedInId']),
        "users": User.objects.all(),
        "posts": Post.objects.all(),
        "reply": Comment.objects.all(),
        'new_post_form' : Post()
    }
    return render(request, 'wall.html', context)

def newPost(request):
    response = 'Form Submitted successfully'
    errors = User.objects.postValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    else:
        poster = User.objects.get(id=request.session['loggedInId'])
        Post.objects.create(body=request.POST['body'], usersPost = poster)
    return JsonResponse(response, safe=False)

def getPost(request):
    response = list(Post.objects.values())
    return JsonResponse(response, safe=False)

def deletePost(request, id):
    deleteMe = Post.objects.get(id=id)
    deleteMe.delete()
    print('***' *10)
    print('This is where the post gets deleted at')
    print('***' *10)
    response = "Delete successful"
    # return redirect('/wall')

    return JsonResponse(response, safe=False)

def reply(request):
    errors = User.objects.replyValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    else:
        poster = User.objects.get(id=request.session['loggedInId'])
        replyComment = Post.objects.get(id=request.POST['postId'])
        Comment.objects.create(reply=request.POST['reply'], usersComment = poster, postComment = replyComment)
    return redirect('/wall')

def logoutVal(request):
    request.session.clear()
    return redirect('/logout')
    
def logout(request):
    return redirect('/')