"""Decorator to use navbar search"""
from django.shortcuts import redirect
from django.urls import reverse

from catalog.models import Product
from search.forms import SearchForm


def navbar_search_decorator(function):
    """Decorator to add navbar_search form by decorator"""

    def wrapper(*args, **kwargs):
        if args[0].method == "POST":
            if args[0].POST.get("produit"):
                form: SearchForm = SearchForm(args[0].POST)

                if form.is_valid():
                    base_product: Product = form.cleaned_data["produit"]

                    return redirect(
                        reverse(
                            "catalog:results", kwargs={"base_product": base_product.id}
                        )
                    )

        return function(*args, **kwargs)

    return wrapper
