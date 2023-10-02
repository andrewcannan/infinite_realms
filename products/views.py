from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.http import JsonResponse

from .models import Product, Category, Sub_category
from .forms import ProductForm


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
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'sub_category':
                sortkey = 'sub_category__name'
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

    current_sorting = f'{sort}-{direction}'

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


@login_required
def add_product(request):
    """
    Render product form and handle form submission to add a product.
    """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you do not have the required permissions.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Render product form and handle form submission to edit a product.
    - Params:
        int: product_id
    """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you do not have the required permissions.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    A view to delete a product.
    - Params:
        int: product_id
    """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you do not have the required permissions.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def get_sub_categories(request, category_id):
    """
    A view to handle ajax request for list of sub_categories
    """
    sub_categories = Sub_category.objects.filter(category_id=category_id)

    data = [sub_category.friendly_name for sub_category in sub_categories]

    return JsonResponse(data, safe=False)
