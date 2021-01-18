from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),	
    path('signUp', views.signUp),
    path('register', views.register),
    path('logIn', views.logIn),
    path('profile/<int:id>', views.profile), 
    path('aboutMe', views.aboutme), 
    path('pictures', views.pictures),
    path('friends', views.friends),
    path('profile/<int:id>/newPost', views.newPost),
    path('deletePost/<int:id>', views.DeleteProfilePost),
    path('deleteReply/<int:id>', views.DeleteProfileReply),
    path('edit/<int:id>', views.editPage),
    path('seeTheCrowd', views.seeTheCrowd), 
    path('newPost',views.newPost),
    path('getPost', views.getPost),
    path('newReply', views.newReply),
    path('deleteCrowdPost/<int:id>', views.deleteCrowdPost),
    path('deleteCrowdReply/<int:id>', views.deleteCrowdReply),
    path('profile/<int:id>', views.profileView),
    path('settings', views.settings),
    path('logout', views.logout),
    path('seeTheCrowdJson', views.seeTheCrowd_json)
]