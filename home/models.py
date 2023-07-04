from django.db import models


class Category(models.Model):
    label = models.CharField(primary_key=True, max_length=200)

class Links(models.Model):
    link = models.CharField(primary_key=True, max_length=200)