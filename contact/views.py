from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from .forms import ContactForm


@login_required
def contact_us(request):
    """
    A view to render contact form and handle form submission
    """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to do that.')
        return redirect(reverse('account_login'))

    form = ContactForm()
    template = 'contact/contact_us.html'
    context = {
        'form': form
    }
    return render(request, template, context)
