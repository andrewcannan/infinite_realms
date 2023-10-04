from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    """
    A view to render form and handle form submission
    """
    product = get_object_or_404(Product, pk=product_id)

    form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form
    }
    return render(request, template, context)
