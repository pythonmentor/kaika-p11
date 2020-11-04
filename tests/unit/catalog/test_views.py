"""Test on catalog module's views"""
from django.contrib.auth.models import User
from django.urls import reverse

from catalog.models import Product
from scrapping import NUTELLA
from tests.test_pattern import TestPattern


class TestViews(TestPattern):
    """Test on catalog's views"""

    def setUp(self) -> None:
        """Tests configuration."""
        self.test_user = User.objects.create_user(
            "test_user", "test_user@test.com", "test_password"
        )
        self.client.login(username="test_user", password="test_password")
        self.product = Product(**NUTELLA)
        self.product.save()

    def test_aliment(self):
        """Load aliment"""
        url = reverse(
            "catalog:aliment", kwargs={"product_id": Product.objects.all()[0].id}
        )

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_favorites(self):
        """Load favorites"""
        url = reverse("catalog:favorites", kwargs={"user": self.test_user.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_results(self):
        """Load results"""
        url = reverse("catalog:results", kwargs={"base_product": str(self.product.id)})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
