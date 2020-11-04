"""Views for ocrProjet8"""
from django.contrib import messages
from django.core.mail import mail_admins
from django.shortcuts import redirect, render
from django.urls import reverse

from catalog.models import Product
from ocrProjet8.forms import ContactForm
from search.forms import SearchForm
from search.navbar_decorator import navbar_search_decorator


def home(request):
    """View for home page"""
    if request.method == "POST":
        form: SearchForm = SearchForm(request.POST)

        if form.is_valid():
            base_product: Product = form.cleaned_data["produit"]

            return redirect(
                reverse("catalog:results", kwargs={"base_product": base_product.id})
            )
    else:
        form: SearchForm = SearchForm()

    return render(request, "home.html", {"form": form})


@navbar_search_decorator
def legal_notice(request):
    """View for legal notice page"""
    return render(request, "notice.html")


@navbar_search_decorator
def contact(request):
    """View for contact page"""
    if request.method == "POST":
        form: ContactForm = ContactForm(request.POST)

        email = form.data.get("email")
        subject = " " + form.data.get("subject")
        message = email + "\r\n" + form.data.get("message")

        if form.is_valid():
            try:
                mail_admins(subject, message)
                messages.add_message(
                    request,
                    25,
                    "Merci de nous avoir sollicité, nous vous contacterons dans les "
                    "plus bref délais.",
                )
                return redirect(reverse("home"))

            except TimeoutError:
                messages.add_message(
                    request,
                    40,
                    "Votre message n'a pas été envoyé, si l'erreur se reproduit, "
                    "veuillez utilisez les informations de contact sur la page "
                    "d'accueil",
                )
    else:
        form: ContactForm = ContactForm()

    return render(request, "contact.html", {"form": form})
