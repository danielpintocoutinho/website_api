from django.db import models

from home.models import Category, Links


class Project(models.Model):
    cover = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    domains = models.ManyToManyField(Category, related_name='projects')
    links = models.ManyToManyField(Links, related_name='links')