from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from django.views.decorators.http import require_http_methods
from .models import Product


def index(request):
    return render(request, 'products/index.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        form.save()
        return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'products/create.html', {'form': form})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product':product})

def delete_product_post(request, product_id):
    product_post = get_object_or_404(Product, id=product_id)
    product_post.delete()
    return redirect('products:product_list')