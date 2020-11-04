"""Functional tests for ocrProjet8"""
from django.test import TestCase
from django.urls import reverse

from search.forms import SearchForm


class TestFunctional(TestCase):
    """Functional tests"""

    def test_search_home_page(self):
        """Search must be accessible through home page"""
        response = self.client.get(reverse("home"))

        assert isinstance(response.context["form"], SearchForm)
