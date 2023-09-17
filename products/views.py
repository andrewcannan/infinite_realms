from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """
    A view to show all products, search queries and sorting
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
     A view to show individual product details.
    params:
    - int: product_id
     """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
