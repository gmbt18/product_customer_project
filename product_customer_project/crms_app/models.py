from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ImageField
from django.contrib.auth.models import AbstractUser
from pcims_app.models import *
##modify Cutomer to AUTH_USER???
#Register them in admins.py


#User

class AuthUser(AbstractUser):
    USER_TYPE_CHOICES = {
        (1, 'Product Manager'),
        (2, 'Customer'),
        (3, 'Customer Manager')
    }
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True)




# Create your models here.
class CustomerInformation(models.Model):
    # blank: False = required
    customer = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    productCatalog = models.ForeignKey(ProductCatalog, on_delete=models.CASCADE, null=True, blank=True)
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


class ProductComplaint(models.Model):
    customer = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    complaint = models.CharField(max_length=200, null=True, blank=False)

class CustomerReview(models.Model):
    customer = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    rating = models.IntegerField(
        null=True,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    reviewDate = models.DateTimeField(auto_now_add=True, null=True)
    productReview = models.CharField(max_length=200, null=True, blank=False)