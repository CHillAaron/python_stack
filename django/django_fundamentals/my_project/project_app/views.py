# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse


def index(request):
    return render(request, "index.html")

def signUp(request):
    return render(request, 'register.html')

def register(request):


    errors = User.objects.userValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/signUp')
    else:
        newAccount = User.objects.create(first=request.POST['first'], last=request.POST['last'], email=request.POST['email'] , password=request.POST['password'])
        request.session ['loggedInId'] = newAccount.id
    return redirect('/profile',)

def logIn(request):
    errors = User.objects.logInValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        matchingEmail = User.objects.filter(email=request.POST['email'])
        request.session['loggedInId'] = matchingEmail[0].id

    return redirect('/seeTheCrowd')

def getPost(request):
    response = list(Post.objects.values())
    return JsonResponse(response, safe=False)

def profile(request, id):
    if 'loggedInId' not in request.session:
        return redirect('/')
    context = {
        'loggedIn': User.objects.get(id=request.session ['loggedInId']),
        "users": User.objects.all(),
        "posts": Post.objects.all(),
        "reply": Comment.objects.all(),
        "usersProfile": User.objects.get(id=id)
    }
    return render (request, 'profile_page.html', context)

def profileView(request, id):
    return HttpResponse('Place holder for guest profile view')

def aboutme(request):
    return HttpResponse('Placeholder for about me')

def pictures(request):
    return HttpResponse('placeholder for the pictures page')

def friends(request):
    return HttpResponse('Place holder for your crowd mates')

def newPost(request):
    response = 'Form Submitted successfully'
    poster = User.objects.get(id=request.session['loggedInId'])
    Post.objects.create(body=request.POST['body'], usersPost = poster)
    # return redirect(f'/profile/{id}')
    return JsonResponse(response, safe=False)

def reply(request):
    errors = User.objects.replyValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/profile')
    else:
        poster = User.objects.get(id=request.session['loggedInId'])
        replyComment = Post.objects.get(id=request.POST['postId'])
        Comment.objects.create(reply=request.POST['reply'], usersComment = poster, postComment = replyComment)
    return redirect('/profile')

def newReply(request):
    # errors = User.objects.replyValidator(request.POST)
    # if len(errors) > 0:
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     return redirect('/profile')
    # else:
    poster = User.objects.get(id=request.session['loggedInId'])
    replyComment = Post.objects.get(id=request.POST['postId'])
    Comment.objects.create(reply=request.POST['reply'], usersComment = poster, postComment = replyComment)
    return redirect('/seeTheCrowd')

def DeleteProfilePost(request, id):
    loggedIn = request.session['loggedInId']
    deleteMe = Post.objects.get(id=id)
    deleteMe.delete()
    return redirect(f'/profile/{loggedIn}')

def DeleteProfileReply(request, id):
    deletereply = Comment.objects.get(id=id)
    deletereply.delete()
    return redirect('/profile')

def editPage(request, id):
    return render(request, 'editPage.html')

def updateAccount(request):
    context = {
        'account': User.objects.all(),
        'thisUser': User.objects.get(id=id)
    }
    userUpdate = User.objects.get(id=id)
    userUpdate.first = request.POST['first']
    userUpdate.last = request.POST['last']
    userUpdate.email = request.POST['email']
    errors = User.objects.updateValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{id}')
    userUpdate.save()
    return redirect('/edit', context)

def seeTheCrowd(request):
    if 'loggedInId' not in request.session:
        return redirect('/')
    context = {
        'loggedIn': User.objects.get(id=request.session ['loggedInId']),
        "users": User.objects.all(),
        # "users": list(User.objects.values()),
        "posts": Post.objects.all(),
        "reply": Comment.objects.all(),
        "usersProfile": User.objects.get(id=request.session['loggedInId'])
    }
    # return render (request, 'profile.html', context)
    return render (request, 'crowdPage.html', context)

def seeTheCrowd_json(request):
    if 'loggedInId' not in request.session:
        return redirect('/')
    users = User.objects.values()
    loggedIn = User.objects.filter(id=request.session ['loggedInId']).values()
    post = Post.objects.values()
    reply = Comment.objects.values()
    context = {
        'loggedIn': list(loggedIn),
        "users": list(users),
        "posts": list(post),
        # "reply": list(reply),
        # "usersProfile": User.objects.get(id=request.session['loggedInId'])
    }
    # return render (request, 'profile.html', context)
    return JsonResponse (context, safe=False)

def newCrowdPost(request, id):
    # errors = User.objects.postValidator(request.POST)
    # if len(errors) > 0:
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     return redirect('/profile')
    # else:
    poster = User.objects.get(id=request.session['loggedInId'])
    Post.objects.create(body=request.POST['body'], usersPost = poster)
    return redirect('/seeTheCrowd')

def deleteCrowdPost(request, id):
    loggedIn = request.session['loggedInId']
    deleteMe = Post.objects.get(id=id)
    deleteMe.delete()
    return redirect('/seeTheCrowd')

def deleteCrowdReply(request, id):
    deletereply = Comment.objects.get(id=id)
    deletereply.delete()
    return redirect('/seeTheCrowd')

def settings(request):
    return HttpResponse('Place holder for settings')

def logout(request):
    try:
        del request.session['loggedInId']
    except KeyError:
        pass
    return redirect('/')
