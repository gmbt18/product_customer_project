from tkinter import Widget
from django import forms
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ImageField
from django.contrib.auth.models import AbstractUser
from pcims_app.models import ProductCatalog, Product
##modify Cutomer to AUTH_USER???
#Register them in admins.py


#User

class AuthUser(AbstractUser):
    USER_TYPE_CHOICES = {
        (1, 'Product Manager'),
        (2, 'Customer'),
        (3, 'Customer Manager'),
        (4, 'Reviewer'),
    }
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True)
    def __str__(self):
        return f"{self.username}"



# Create your models here.
class CustomerInformation(models.Model):
    # blank: False = required
    customer = models.ForeignKey(AuthUser, on_delete=models.CASCADE, null=True)
    productCatalog = models.ForeignKey("pcims_app.ProductCatalog", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    birthday = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, default='Male', blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    citizenship = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    isSubscribed = models.BooleanField(default=False, blank = True)
    presentAddress = models.CharField(max_length=100, null=True, blank=True)
    permanentAddress = models.CharField(max_length=100, null=True, blank=True)
    billingAddress = models.CharField(max_length=100, null=True, blank=True)
    shippingAddress = models.CharField(max_length=100, null=True, blank=True)
    officeAddress = models.CharField(max_length=100, null=True, blank=True)
    personalCPNumber = models.CharField(max_length=15, null=True, blank=True)
    officeCPNumber = models.CharField(max_length=15, null=True, blank=True)
    homeLandlineNumber = models.CharField(max_length=15, null=True, blank=True)
    officeLandlineNumber = models.CharField(max_length=15, null=True, blank=True)
    personalEmail = models.CharField(max_length=40, null=True, blank=True)
    officeEmail = models.CharField(max_length=40, null=True, blank=True)
    
    def __str__(self):
        return f"{self.customer}"


class ProductComplaint(models.Model):
    customer = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    product = models.ForeignKey("pcims_app.Product", on_delete=models.CASCADE,null=True)
    complaint = models.CharField(max_length=200, null=True, blank=False)
    def __str__(self):
        return f"{self.customer}-{self.product}"

class CustomerReview(models.Model):
    customer = models.ForeignKey(AuthUser, on_delete=models.CASCADE,null=True,)
    product = models.ForeignKey("pcims_app.Product", on_delete=models.CASCADE,null=True)
    picture = models.ImageField(null=True, blank=True)
    rating = models.IntegerField(
        null=False,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ],
        default=0,
    )
    reviewDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    productReview = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"{self.customer}-{self.product}"