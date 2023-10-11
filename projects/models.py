from django.db import models

# Create your models here.
class Project(models.Model):
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
