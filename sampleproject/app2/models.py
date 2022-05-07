from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from app1.models import *


# Create your models here.


class Model3(models.Model):
    model1 = models.ForeignKey(Model1, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, default='Male', blank=True)
    def __str__(self):
        return self.name