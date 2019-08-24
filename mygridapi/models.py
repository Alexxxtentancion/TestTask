from django.db import models
class Person(models.Model):
    first_name = models.CharField(blank=True,null=False,max_length=100)
    last_name = models.CharField(blank=True,null=False,max_length=100)
    email = models.EmailField(blank=True,null=False,max_length=100)
    date_of_birth = models.DateField()
    date_added = models.DateField(auto_now_add=True)

