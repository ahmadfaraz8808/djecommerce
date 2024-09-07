from django.urls import path
from .views import *

urlpatterns = [
    #category
    path('category/',category_list,name='category_list'),
    path('category/create/',category_create,name='category_create'),
    path('category/edit/<slug:slug>/',category_edit,name='category_edit'),  
    path('category/delete/<slug:slug>/',category_delete,name='category_delete'),

    #product
    path('products/', product_list, name='product_list'),
    path('product/create/', product_create,name='product_create'),
    path('product/edit/<slug:slug>', product_edit, name='product_edit'),
    path('product/delete/<slug:slug>', product_delete, name='product_delete'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('category/<slug:category_slug>/products/', category_product_list, name='product_list_by_category'),
    path('search/', search, name='search'),

    # wishlist
    path('wishlist/', product_wishlist, name='wishlist'),
    path('wishlist/add/<slug:slug>/', wishlist_add, name='wishlist_add'),
    path('wishlist/remove/<slug:slug>/', wishlist_remove, name='wishlist_remove'),

    #cart
    # path('cart/add/<slug:slug>/', add_product, name='add_product'),
    # path('cart/remove/<slug:slug>/', remove_product, name='remove_product'),
    # path('cart/clear/<slug:slug>/', empty_cart, name='clear_cart'),

    # path('cart/', view_cart, name='view_cart'),
    # path('cart/,<slug:slug>/increase/', increase_quantity, name='increase_quantity'),
    # path('cart/,<slug:slug>/decrease/', decrease_quantity, name='decrease_quantity'),

]