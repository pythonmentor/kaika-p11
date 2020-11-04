"""Functional tests on account module"""
from django.test import TestCase
from django.urls import reverse

from accounts.forms import SubscribeForm


class TestCreateUser(TestCase):
    """Functional tests"""

    def test_create_user(self):
        """It must be possible to create a user on the website"""
        response_1 = self.client.get(reverse("accounts:subscription"))

        assert isinstance(response_1.context["form"], SubscribeForm)

        data = {
            "login": "test_login",
            "last_name": "test_last_name",
            "first_name": "test_first_name",
            "email": "test@mail.com",
            "password": "test_password",
            "confirm_password": "test_password",
        }

        response_2 = self.client.post(reverse("accounts:subscription"), data)

        # User is redirected to login page after a successfull account creation
        self.assertEqual(response_2.status_code, 302)

        self.assertIn("login", response_2.url)
