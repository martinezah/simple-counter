from django.db import models

class Counter(models.Model):
    value = models.IntegerField(default=0)
    step = models.IntegerField(default=1000)
