from django.db import models
from datetime import date
import re

today = date.today()


# Validations
class UserManager(models.Manager):

    def logInValidator(self, formInfo):
        errors = {}
        matchingEmail = User.objects.filter(email=formInfo['email'])
        print(matchingEmail)
        if len(formInfo['email']) < 1:
            errors['emailRequired'] = "Email is required to login"
        elif len(matchingEmail) == 0:
            errors['emailNotFound'] = "No email, not registered"
        else:
            #check password
            if matchingEmail[0].password != formInfo['password']:
                errors['incorrectpassword'] = 'Try again'
        
        return errors

    def userValidator(self, formInfo):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        matchingEmail = User.objects.filter(email = formInfo['email'])
        User.objects.filter(email = formInfo['email'])

        if len(formInfo['first']) < 2:
            errors['first'] = "Your first name is to short"
        if len(formInfo['last']) < 2:
            errors['lastError'] = "Your last name is to short"
        if len(formInfo['email']) < 1:
            errors['emailRequired'] = "What is your email"
        elif not EMAIL_REGEX.match(formInfo['email']):            
            errors['email'] = "Invalid email address!"
        elif len(matchingEmail) > 0:
            errors['matchingemail'] = "this email is taken"
        if  len(formInfo['password']) < 8:    
            errors['pwError'] = "password to Short"
        if formInfo['password'] != formInfo['confirm']:
            errors['matchError'] = "Passwords do not match"
        return errors

    def postValidator(self, formInfo):
        errors = {}
        if len(formInfo['body']) < 1:
            errors['bodyError'] = "Dont be short minded"
        return errors
    
    def replyValidator(self, formInfo):
        errors = {}
        if len(formInfo['reply']) < 1:
            errors['bodyError'] = "Dont be short minded"
        return errors


# Create your models here.

class User(models.Model):

    first = models.CharField(max_length = 255)
    last = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    objects = UserManager()

class Post(models.Model):
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name="liked_Post") 
    usersPost = models.ForeignKey(User, related_name="users_post", on_delete = models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class Comment(models.Model):
    reply = models.TextField()
    likes = models.ManyToManyField(User, related_name="likedComment") 
    usersComment = models.ForeignKey(User, related_name="users_comment", on_delete = models.CASCADE, null=True)
    postComment = models.ForeignKey(Post, related_name="posts_comment", on_delete = models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)