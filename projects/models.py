from django.db import models

# Create your models here.
class Project(models.Model):
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    links = models.URLField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=100)
