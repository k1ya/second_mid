from django.db import models

# Create your models here.
class employee(models.Model):    
    name=models.CharField(max_length=100 )
    phone=models.CharField(max_length=13)
    salary=models.CharField(max_length=5)
    
class student(models.Model):
    
    name=models.CharField(max_length=100 )
    grade=models.CharField(max_length=2  )
    gender=models.CharField(max_length=1 )
    
class teacher(models.Model):
    
    name=models.CharField(max_length=100 )
    phone=models.CharField(max_length=13)
    salary=models.CharField(max_length=5)