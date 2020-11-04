"""Test on account module's views"""
from django.urls import reverse

from tests.test_pattern import TestPattern


class TestViews(TestPattern):
    """Tests on ocrProjet views."""

    def test_login(self):
        """Load login"""
        url = reverse("accounts:login")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """Load logout"""
        url = reverse("accounts:logout")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_subscription(self):
        """Load subscription"""
        url = reverse("accounts:subscription")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_user_account(self):
        """Load user accounts"""
        url = reverse("accounts:user_account")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
