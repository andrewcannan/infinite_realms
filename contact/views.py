from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactForm


@login_required
def send_confirmation_email(request, contact):
    """
    Send the user a confirmation email
    """
    user = request.user
    cust_email = user.email
    subject = render_to_string(
        'contact/confirmation_emails/confirmation_email_subject.txt',)
    body = render_to_string(
        'contact/confirmation_emails/confirmation_email_body.txt',
        {'contact': contact, 'contact_email': settings.DEFAULT_FROM_EMAIL})
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )


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
            messages.success(request, f"Contact message sent successfully. \
                             A confirmation email will be sent to\
                             {contact.email}.")
            send_confirmation_email(request, contact)
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
