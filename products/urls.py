from django.urls import path
from .views import *

urlpatterns = [
    #category
    path('category/',category_list,name='category_list'),
    path('category/create/',category_create,name='category_create'),
    path('category/edit/<slug:slug>/',category_edit,name='category_edit'),  
    path('category/delete/<slug:slug>/',category_delete,name='category_delete'),

    #product
    path('products/',product_list,name='product_list'),
    path('product/create/',product_create,name='product_create'),
    path('product/edit/<slug:slug>',product_edit,name='product_edit'),
    path('product/delete/<slug:slug>',product_delete,name='product_delete'),
    path('product/<slug:slug>/',product_detail,name='product_detail'),
    path('<slug:category_slug>/products',category_product_list,name='product_list_by_category'),
    path('search/',search,name='search'),
]