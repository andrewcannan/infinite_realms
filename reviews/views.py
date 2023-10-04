from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm
from products.models import Product


def reviews(request, product_id):
    """
    A view to show all reviews for product
    """
    product = get_object_or_404(Product, pk=product_id)

    reviews = Review.objects.filter(product=product)
    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
        'product': product,
    }

    return render(request, template, context)


@login_required
def add_review(request, product_id):
    """
    A view to render form and handle form submission
    """
    product = get_object_or_404(Product, pk=product_id)

    form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)
