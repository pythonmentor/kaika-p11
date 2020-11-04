"""Tests on ocrProjet8 context processors"""
from django.urls import reverse

from tests.test_pattern import TestPattern


class TestContextProcessord(TestPattern):
    """Tests on ocrProjet context processors."""

    def test_toolbar_form(self):
        """Load contact and verify presence of toolbar_form"""
        url = reverse("contact")

        response = self.client.get(url)

        assert response.context["toolbar_form"]
