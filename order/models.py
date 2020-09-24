from django.db import models
from client.models import Client
from article.models import Article
from django.contrib.postgres.fields import ArrayField


class Order(models.Model):
    order_number = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_supply = models.DateTimeField()
    urgent = models.BooleanField(default=False)
    warehouse = models.CharField(max_length=64, blank=True, null=True)
    reference = models.CharField(max_length=64, blank=True, null=True)
    office_code = models.IntegerField(blank=True, null=True)
    partner_code = models.IntegerField(blank=True, null=True)
    order_datails = ArrayField(
        models.CharField(max_length=128),
        default=None,
        null=True
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
