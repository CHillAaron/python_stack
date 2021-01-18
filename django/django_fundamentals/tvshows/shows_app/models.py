from django.db import models
from datetime import date

today = date.today()



# Create Validation models here

class ShowManager(models.Manager):
    def showvalidator(self, formInfo):
        errors = {}
        if len(formInfo['title']) < 2:
            errors['titleError'] = "What is the Title"
        if len(formInfo['network']) < 3:
            errors['networkError'] = "What is the Network"
        if formInfo['release'] > str(today):
            errors['futureError'] = "No time travelers aloud"
        if  len(formInfo['desc']) > 0 and len(formInfo['desc']) < 10:    
            errors['networkError'] = "Be more Descriptive"
        return errors


# Create your models here.

class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    dates = models.DateField(null=True)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    objects = ShowManager()
   