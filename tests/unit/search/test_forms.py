"""Tests for search's module forms"""
from catalog.models import Product
from scrapping import NUTELLA
from search.forms import SearchForm
from tests.test_pattern import TestPattern


class TestForms(TestPattern):
    """Test module's forms"""

    def test_search_form(self):
        """Test SearchForm"""
        form = SearchForm(data={"produit": Product(**NUTELLA)})

        assert form.is_valid()
        self.assertEqual(form.data["produit"].id, NUTELLA["id"])
