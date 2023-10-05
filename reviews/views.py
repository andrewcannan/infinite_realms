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


@login_required
def edit_review(request, review_id):
    """
    A view to render form and handle form submission
    """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to do that.')
        return redirect(reverse('account_login'))

    review = Review.objects.get(id=review.id)
    product = Product.objects.filter(review=review)
    user = UserProfile.objects.get(user=request.user)

    if user != review.user and not request.user.is_superuser:
        messages.error(request, 'Sorry, you can only edit your own reviews.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save()
            review.save()
            messages.success(request, "Product review updated successfully.")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Failed to update review.\
                            Please ensure the form is valid.")

    else:
        form = ReviewForm(instance=review)

    template = 'reviews/edit_review.html'
    context = {
        'review': review,
        'form': form,
        'product': product,
    }
    return render(request, template, context)
