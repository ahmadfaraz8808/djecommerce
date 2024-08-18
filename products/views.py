from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from .forms import*
from django.contrib import messages

# Create your views here.
def category_list(request):
    return render(
        request,
        'products/category_list.html',
        {
        'categories':Category.objects.all(),
        'form': CategoryForm()
        }
    )

def category_create(request):
    form=CategoryForm(request.POST,request.FILES)
    if form.is_valid():
        messages.success(request,'Category created succesfully')
        form.save()
    else:
        messages.error(request,'Error creating category')
    return redirect('creating_list')

def category_edit(request, slug):
    pass 
def category_delete(request, slug):
    pass 
def product_list(request, slug):
    pass 
def product_create(request, slug):
    pass 
def product_edit(request, slug):
    pass 
def product_delete(request, slug):
    pass 
def product_detail(request, slug):
    pass 
def category_product_list(request, category_slug):
    pass 
def search(request):
    pass
        