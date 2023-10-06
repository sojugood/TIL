from django.db import models

# Create your models here.
class Movie(models.Model):
    subject = models.CharField(max_length=20)
    object = models.TextField()