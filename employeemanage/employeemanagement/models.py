from django.db import models

class signupdatabase(models.Model):
    name=models.CharField(max_length=128,unique=True)
    email=models.CharField(max_length=128)
    password=models.CharField(max_length=128,unique=True,primary_key=True)
    code=models.CharField(max_length=128)
    
class department1 (models.Model):
    employeename=models.CharField(max_length=128)
    
class department2(models.Model):
    employeename=models.CharField(max_length=128)
    
class department3(models.Model):
    employeename=models.CharField(max_length=128)
    
class perfomancedb(models.Model):
    perfomance=models.CharField(max_length=128)
    perfomancedate=models.DateField()

class trainingdb(models.Model):
    training=models.CharField(max_length=128)
    trainingdate=models.DateField()
    
class imagedb(models.Model):
    image=models.ImageField(upload_to='photos/', blank=True, null=True)  