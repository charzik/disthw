from django.db import models

class Item(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=32)

