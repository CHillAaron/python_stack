from django.db import models

# Create your models(tables) here.
class Product(models.Model):
    #fields here
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

