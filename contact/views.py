from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.email = request.user.email
            contact.save()
            messages.success(request, "Contact message sent successfully.")
            return redirect(reverse('home'))
        else:
            messages.error(request, "Failed to send message.\
                            Please ensure the form is valid.")
    else:
        form = ContactForm()

    template = 'contact/contact_us.html'
    context = {
        'form': form
    }
    return render(request, template, context)
