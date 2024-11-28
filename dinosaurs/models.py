from django.db import models

# Create your models here.
class Dino(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField(max_length=200)  
    period = models.CharField(max_length=50)
    diet = models.CharField(max_length=20)
    size = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    habitat = models.CharField(max_length=200)
    characteristics = models.TextField() 