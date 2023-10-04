from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile


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
    product = Product.objects.get(id=product_id)
    user = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save()
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Product review added successfully.")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Failed to add review.\
                            Please ensure the form is valid.")

    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)
