from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile
from .models import Review


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
    A view to render form and handle form submission.
    - Params:
        int: product_id
    """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to do that.')
        return redirect(reverse('account_login'))

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
    A view to render form and handle form submission.
    - Params:
        int: review_id
    """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to do that.')
        return redirect(reverse('account_login'))

    original_review = Review.objects.get(id=review_id)
    product = original_review.product
    user = UserProfile.objects.get(user=request.user)

    if request.user != original_review.user and not request.user.is_superuser:
        messages.error(request, 'Sorry, you can only edit your own reviews.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            form = ReviewForm(request.POST, instance=original_review)
            review = form.save()
            review.product = original_review.product
            review.user = original_review.user
            review.save()
            messages.success(request, "Product review updated successfully.")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Failed to update review.\
                            Please ensure the form is valid.")

    else:
        form = ReviewForm(instance=original_review)

    template = 'reviews/edit_review.html'
    context = {
        'review': original_review,
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    Delete a review
    - Params:
        int: review_id
    """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to do that.')
        return redirect(reverse('account_login'))

    review = Review.objects.get(id=review_id)
    product = review.product

    if request.user != review.user and not request.user.is_superuser:
        messages.error(request, 'Sorry, you can only delete your own reviews.')
        return redirect(reverse('home'))

    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('product_detail', args=[product.id]))
