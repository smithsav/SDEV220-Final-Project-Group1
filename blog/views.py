from django.shortcuts import render , redirect
from .products import Products
from .forms import ProductForm
from .models import Product
from .inventory import Inventory 

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_products.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def view_inventory(request):
    products = Product.objects.all()  
    return render(request, 'view_inventory.html', {'products': products})

def record_sale(request):
    return render(request, 'blog/record_sale.html', {})

def customer(request):
    return render(request, 'blog/customer.html', {})
