from django.db import models
from django.conf import time




class myblogmodels(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    discription = models.TextField()

    def __str__(self):
        return self.title

