from django.db import models


class Project(models.Model):
    cover = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    description = models.TextField()