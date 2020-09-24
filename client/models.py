from django.db import models


class Client(models.Model):
    TYPE_CHOICES = (
    ("NORMAL", "Normal"),
    ("PLATA", "Plata"),
    ("ORO", "Oro"),
    ("PLATINO", "Platino"),
)
    name = models.CharField(max_length=64, blank=False)
    code = models.CharField(max_length=64, blank=False)
    photo = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default="NORMAL")
