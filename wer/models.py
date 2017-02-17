from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=20)
    res = models.IntegerField(max_length=10)
    names = models.CharField(max_length=20)
