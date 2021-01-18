from django.urls import path     
from . import views



urlpatterns = [
    path('', views.index),	
    path('addBook', views.addBook),  
    path('bookInfo/<int:id>/', views.bookInfo), 
    path('bookInfo/<int:id>/addAuthor', views.addAuthor),
]