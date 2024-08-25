from django import forms
from .models import*

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields ='__all__'    #display all fields

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['title','brand','category','price','description','image']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields=['image']

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields=['rating','review']