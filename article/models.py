from django.db import models


class Article(models.Model):
    code = models.IntegerField()
    description = models.CharField(max_length=256)
