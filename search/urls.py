"""Urls for module search"""
from django.urls import path

from catalog.models import Product

from .views import ProductAutocomplete

urlpatterns = [
    path(
        "product-autocomplete/",
        ProductAutocomplete.as_view(model=Product),
        name="product-autocomplete",
    ),
]
