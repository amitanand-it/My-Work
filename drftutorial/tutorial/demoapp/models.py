from django.db import models

# Create your models here.
class Demo(models.Model):
    name = models.CharField(blank=False, max_length=20)
    age = models.IntegerField(blank=False)
    sex = models.BooleanField(blank=False)


