from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactForm, ResponseForm
from .models import Contact, Response


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


@login_required
def send_response_email(request, contact, response):
    """
    Send the user a response email
    """
    cust_email = contact.email
    subject = render_to_string(
        'contact/confirmation_emails/response_email_subject.txt',
        {'contact': contact})
    body = render_to_string(
        'contact/confirmation_emails/response_email_body.txt',
        {'contact': contact, 'response': response,
         'contact_email': settings.DEFAULT_FROM_EMAIL})
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )


@login_required
def send_response(request, contact_id):
    """
    A view to render response form and handle form submission
    - Params:
        int: contact_id
    """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you do not have the required permissions.')
        return redirect(reverse('home'))

    contact = Contact.objects.filter(id=contact_id)
    if request.method == "POST":
        form = ResponseForm(request.POST)

        if form.is_valid():
            response = form.save(commit=False)
            response.save()
            # switch boolean field on contact to true
            contact.response_sent = True
            contact.save()
            messages.success(request, "Response sent to user successfully.")
            send_response_email(request, contact, response)
            return redirect(reverse('home'))
        else:
            messages.error(request, "Failed to send message.\
                            Please ensure the form is valid.")
    else:
        form = ResponseForm()

    template = 'contact/send_response.html'
    context = {
        'form': form,
        'contact': contact,
    }
    return render(request, template, context)
