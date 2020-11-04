"""Tests for ocrProjet8 views"""
from django.urls import reverse

from tests.test_pattern import TestPattern


class TestViews(TestPattern):
    """Tests on ocrProjet views."""

    def test_home(self):
        """Load home"""
        url = reverse("home")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        """Load contact"""
        url = reverse("contact")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_notice(self):
        """Load notice"""
        url = reverse("notice")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
