from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
