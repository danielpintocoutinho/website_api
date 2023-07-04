from django.db import models

from home.models import Category

class Post(models.Model):
    path = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    category = models.ManyToManyField(Category)