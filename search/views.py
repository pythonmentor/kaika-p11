"""Views for search module"""
from dal import autocomplete

from catalog.models import Product


class ProductAutocomplete(autocomplete.Select2QuerySetView):
    """Class to init search"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.q = None

    def get_queryset(self):
        """Get query set containing all products."""
        query_set = Product.objects.all()

        if self.q:
            query_set = query_set.filter(product_name_fr__istartswith=self.q)

        return query_set.order_by("product_name_fr")
