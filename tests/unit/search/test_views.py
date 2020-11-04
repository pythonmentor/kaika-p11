"""Tests for search module's views"""
from django.urls import reverse

from tests.test_pattern import TestPattern


class TestViews(TestPattern):
    """Test views"""

    def test_autocomplete(self):
        """Test autocomplete view"""
        response = self.client.get(reverse("product-autocomplete"))

        self.assertEqual(response.request["PATH_INFO"], "/search/product-autocomplete/")

        self.assertEqual(response.status_code, 200)
