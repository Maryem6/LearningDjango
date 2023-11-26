from django.db import models

# Create your models here.
class Feature(models.Model):
    #id : int (we can remove it when adding models.Model)
    #name : str
    #details : str
    #is_true : bool
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)