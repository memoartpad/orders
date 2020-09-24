from django.db import models
from article.models import Article


class Vendor(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=128)
    articles = models.ManyToManyField(Article)
