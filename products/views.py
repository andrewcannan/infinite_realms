from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Sub_category


def all_products(request):
    """
    A view to show all products, search queries and sorting
    """

    products = Product.objects.all()
    query = None
    categories = None
    current_sub_categories = None
    all_sub_categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == "name":
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower("name"))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            all_sub_categories = Sub_category.objects.filter(
                category__in=categories)

        if 'category' and 'sub_category' in request.GET:
            categories = request.GET['category'].split(',')
            sub_categories = request.GET['sub_category'].split(',')
            products = products.filter(sub_category__name__in=sub_categories)
            categories = Category.objects.filter(name__in=categories)
            current_sub_categories = Sub_category.objects.filter(
                name__in=sub_categories)
            all_sub_categories = Sub_category.objects.filter(
                category__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sub_categories': current_sub_categories,
        'all_sub_categories': all_sub_categories,
        'current_sorting': current_sorting,
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
