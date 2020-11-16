from datetime import datetime

from django.db import models

# Create your models here.



class TestModel(models.Model):


    name=models.CharField(max_length=50)
    age= models.IntegerField()
    date=models.DateTimeField(auto_now=datetime.now(microsecend=0))
