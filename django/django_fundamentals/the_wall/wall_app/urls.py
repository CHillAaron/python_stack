from django.urls import path     
from . import views



urlpatterns = [
    path('', views.index),
    path('home', views.home),	 
    path('register', views.register), 
    path('logIn', views.logIn),
    path('wall', views.wall, name='wall'),
    path('newPost',views.newPost),
    # path('newPost', views.newPost, name='posts'),
    path('getPost', views.getPost),
    path('deletePost/<int:id>', views.deletePost),
    path('reply', views.reply),
    path('logout', views.logout),
    path('logoutVal', views.logoutVal)
]