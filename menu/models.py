from django.db import models

# Create your models here.

class Pizza(models.Model):
    size = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
    border = models.BooleanField()
    border_flavor = models.CharField(max_length=100, blank=True)
    price = models.FloatField()
    sweet = models.BooleanField(default=False)

class Kalzone(models.Model):
    pasta = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
    