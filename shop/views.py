from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Product, Category


def list_product(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/list_products.html',
                  {'category': category,
                   'categories': categories,
                   "products": products,
                   'cart_product_form':cart_product_form})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    return render(request, 'shop/product/productdetail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
