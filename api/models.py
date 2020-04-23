from django.db import models

# Create your models here.

class Measurement(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    sensor = models.TextField("sensor")
    value = models.FloatField("value")
    tree_id = models.TextField("tree_id")
