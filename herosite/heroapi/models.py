# models.py

from django.db import models


class Superpower(models.Model):
    name =  models.CharField(max_length=80)
    def __str__(self):
        return str(self.name)

class Publisher(models.Model):

    name = models.CharField(max_length=80)
    def __str__(self):
        return str(self.name)

class Hero(models.Model):
    name = models.CharField(max_length=80)
    alias = models.CharField(max_length=80)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default = None)
    superpowers = models.ManyToManyField(Superpower)
    def __str__(self):
        return str(self.name)
