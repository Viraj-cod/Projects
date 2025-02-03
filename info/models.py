from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class accesories_model(models.Model):
    name = models.CharField(max_length=20,null=True)
    qauntity = models.IntegerField(null=True,default=0)
    maintenance = models.DateField(null=True)

    def __str__(self):
        return self.name

class Trainers_model(models.Model):
    name = models.CharField(max_length=20,null=True)
    phone_no = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    payscale = models.IntegerField(null=True)
    join_date=models.DateField(null=True)

    def __str__(self):
        return self.name

class members_model(models.Model):
    name = models.CharField(max_length=20,null=True)
    phone_no = models.IntegerField(null=True,default=0)
    email = models.EmailField(null=True)
    duration = models.CharField(max_length=20,null=True)
    trainer = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name

class transactions_model(models.Model):
    description = models.CharField(max_length=30,null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.description


