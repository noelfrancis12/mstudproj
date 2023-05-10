from django.db import models

# Create your models here.
class course(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    duration=models.IntegerField()
class students(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    courses=models.CharField(max_length=255)    