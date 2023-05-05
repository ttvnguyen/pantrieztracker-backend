from django.db import models

# Create your models here.
class Inventory(models.Model):
    qty = models.SmallIntegerField()
    image = models.CharField(max_length=255)
    item = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    expiry = models.DateField()