from django.db import models

# Create your models here.
class contact (models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField()
    addres=models.CharField(default=0)
    message = models.TextField()
    

def __str__(self):
    return self.name



class feedback(models.Model):
    name=models.CharField(max_length=100)