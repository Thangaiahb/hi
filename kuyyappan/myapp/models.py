from django.db import models

# Create your models here.

class feedback(models.Model):
    User_Name=models.CharField(max_length=50)
    Mobile=models.BigIntegerField()
    FeedBack=models.CharField(max_length=100)

class fiup(models.Model):
    f_name=models.CharField(max_length=100)
    file=models.FileField()