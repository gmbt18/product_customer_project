from distutils.command.build_scripts import first_line_re
from email.headerregistry import Address
from itertools import product
from pickle import TRUE
from pyexpat import model
from tokenize import Name
from django.db import models

# Create your models here.
class ProductManager(models.Model):
    username = models.CharField(max_length=200,null=True)
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200, null=True)
    profilepicture=models.ImageField(null=True)

class Supplier(models.Model):
    name=models.CharField(max_length=200,null=TRUE)
    address=models.CharField(max_length=200,null=TRUE)
    email=models.CharField(max_length=30,null=TRUE)
    telephone=models.CharField(max_length=10,null=TRUE)
    contactperson=models.CharField(max_length=200, null=TRUE)
    isarchived=models.BooleanField()

    def __str__(self):
        return self.name

class Catalog(models.Model):
    details = models.TextField()

class Reviewer(models.Model):
    name=models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)
    profilepicture = models.ImageField(null=True)
    contact = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=200,null=True)
    description=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    rating = models.FloatField()
    reviews = models.TextField(blank=True,null=True)
    stocks = models.IntegerField(default=0)
    reorderlvl = models.IntegerField()
    sellingprice = models.FloatField()
    discount = models.FloatField()
    isarchived = models.BooleanField()

    def __str__(self):
        return self.name

class SupplierProduct(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    leadtime = models.IntegerField(null=True)
    supplierprice=models.FloatField()
    discount = models.FloatField()
    isarchived = models.BooleanField()

class ProductCatalog(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    catalog=models.ForeignKey(Catalog, on_delete=models.CASCADE)
    details=models.TextField(blank=True,null=True)
    joindate=models.DateTimeField(auto_now_add=True)

class ProductPhotos(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    filename=models.CharField(max_length=200,null=True)
    photo= models.ImageField(upload_to='images',null=True)

class ProductVideos(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    filename=models.CharField(max_length=200,null=True)
    media= models.FileField(upload_to='videos',null=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    details = models.TextField(blank=True, null=True)
    rating = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    photo= models.ImageField(upload_to='review_images',null=True)
    media= models.FileField(upload_to='review_videos',null=True)