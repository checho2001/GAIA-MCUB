from statistics import mode
from django.db import models

# Create your models here.

class Users(models.Model):
    UsersID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)
    mail = models.CharField(max_length=500)
    password = models.CharField(max_length=500)

