from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)                 #the name of category
    logo = models.ImageField(upload_to='category/')         #logo of category
    slug = models.SlugField(max_length=225,unique=True)       #its(slug) the unique url for every category

    def __str__(self):                                                   #????
        return self.name

class Product(models.Model):
    title = models.CharField(max_length = 255)                  #title of product
    brand = models.CharField(max_length = 225,default="N/A")                #brand name of the product
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)     #category,which the product belong to
    price = models.DecimalField(max_digits=10,decimal_places=2)             #price 
    seller = models.ForeignKey(User, on_delete=models.CASCADE)          #if the seller is deleted,the product will also be deleted(CASCADE) i.e. the child(product) be deleted
    description = models.TextField()    
    image = models.ImageField(upload_to='product/')
    slug = models.SlugField(max_length = 255,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)       
    updated_at = models.DateTimeField(auto_now=True)             

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_images')
    image = models.ImageField(upload_to='product/')

class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product.title    
    
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
        


    
    
    
    
    
    
    
    