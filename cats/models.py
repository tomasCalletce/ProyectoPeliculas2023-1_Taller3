from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

