from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Model1(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, default='Male', blank=True)
    def __str__(self):
        return self.name

class Model2(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, default='Male', blank=True)
    def __str__(self):
        return self.name