from django.db import models
from django.urls import reverse
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(blank=False,null=False,max_length=100)
    last_name = models.CharField(blank=False,null=False,max_length=100)
    email = models.EmailField(blank=False,null=False,max_length=100)
    date_of_birth = models.DateField()
    date_added = models.DateField(auto_now_add=True)

