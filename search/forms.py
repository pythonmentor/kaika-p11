"""Forms for search module"""
from dal import autocomplete
from django import forms

from catalog.models import Product


class SearchForm(forms.ModelForm):
    """Search form to retrieve products"""

    produit = forms.ModelChoiceField(
        empty_label="Produit",
        queryset=Product.objects.all(),
        widget=autocomplete.ModelSelect2(
            attrs={"id": "search-form-input"}, url="product-autocomplete"
        ),
    )

    class Meta:
        """Meta of SearchForm"""

        model = Product
        fields = ()
