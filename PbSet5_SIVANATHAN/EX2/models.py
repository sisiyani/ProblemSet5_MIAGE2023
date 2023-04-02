from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(primary_key=True,max_length=255)

class Quotes(models.Model):
    content=models.CharField(max_length=2058)
    author= models.ForeignKey(Person, on_delete=models.CASCADE, related_name='quotes')
