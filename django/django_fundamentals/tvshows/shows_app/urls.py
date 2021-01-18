from django.urls import path     
from . import views


urlpatterns = [
    path('', views.show),
    path('new.html', views.new),
    path('newShow', views.newShow),
    path('shows', views.show),
    path('showInfo/<int:id>', views.showInfo),
    path('showInfo/<int:id>/edit', views.edit),
    path('showInfo/<int:id>/editShow', views.editShow),
    path('showInfo/<int:id>/destroy', views.delete)
]