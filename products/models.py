from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)
    logo = models.ImageField(upload_to='category/')
    slug=models.SlugField(max_length=225,unique=True)

def __str__(self):
    return self.name

class Product(models.Model):
    title = models.CharField(max_length = 255)
    brand = models.CharField(max_length = 225,default="N/A")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='product/')
    slug = models.SlugField(max_length = 255,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_images')
    image = models.ImageField(upload_to='product/')
    
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
        


    
    
    
    
    
    
    
    